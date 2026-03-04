#!/usr/bin/env python3
"""
incident_pack.py
Standardized host-side evidence collection -> JSON + Markdown (ServiceNow-ready).

Public-safe template:
- No ServiceNow integration
- No company-specific endpoints
- Optional --mock to generate deterministic sample output (for GitHub)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import platform
import re
import socket
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence


SUPPORTED_OS = {"windows", "macos", "linux"}
DEFAULT_CMD_TIMEOUT = 15
DEFAULT_TCP_TIMEOUT = 3.0
DEFAULT_MD_MAX_LINES = 40
MOCK_TIMESTAMP_UTC = "2026-01-29T06:07:27+00:00"
MOCK_OS = "linux"


def now_utc_iso() -> str:
    """Return current UTC timestamp in ISO format."""
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sanitize_filename_component(value: str, default: str = "host") -> str:
    """Return a filesystem-safe filename component."""
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", (value or "").strip())
    cleaned = cleaned.strip(".-_")
    return cleaned or default


def normalize_ports(ports: Sequence[int]) -> List[int]:
    """Deduplicate ports while preserving order."""
    seen = set()
    out: List[int] = []
    for port in ports:
        if port not in seen:
            out.append(port)
            seen.add(port)
    return out


def validate_ports(ports: Sequence[int]) -> None:
    """Validate all TCP ports are in the valid range."""
    invalid = [p for p in ports if p < 1 or p > 65535]
    if invalid:
        joined = ", ".join(str(p) for p in invalid)
        raise ValueError(f"Invalid port(s): {joined}. Valid range is 1-65535.")


def validate_md_max_lines(value: int) -> None:
    """Validate Markdown output truncation settings."""
    if value < 1:
        raise ValueError("--md-max-lines must be at least 1.")


def run(cmd: Sequence[str], timeout: int = DEFAULT_CMD_TIMEOUT) -> Dict[str, Any]:
    """
    Run a command and capture stdout/stderr/rc as evidence.
    Requirement: never crash the run; failures become evidence.
    """
    try:
        p = subprocess.run(list(cmd), capture_output=True, text=True, timeout=timeout, check=False)
        return {
            "cmd": " ".join(cmd),
            "rc": p.returncode,
            "stdout": (p.stdout or "").strip(),
            "stderr": (p.stderr or "").strip(),
        }
    except Exception as e:
        return {
            "cmd": " ".join(cmd),
            "rc": None,
            "stdout": "",
            "stderr": f"{type(e).__name__}: {e}",
        }


def resolve(name: str) -> Dict[str, Any]:
    """
    DNS resolution proof using socket.getaddrinfo().
    Returns dict with 'answers' list or 'error' string.
    """
    out: Dict[str, Any] = {"name": name, "answers": [], "error": ""}
    try:
        infos = socket.getaddrinfo(name, None)
        addrs = sorted({i[4][0] for i in infos})
        out["answers"] = addrs
    except Exception as e:
        out["error"] = f"{type(e).__name__}: {e}"
    return out


def tcp_check(host: str, port: int, timeout: float = DEFAULT_TCP_TIMEOUT) -> Dict[str, Any]:
    """
    Layer 4 TCP connect test.
    Returns dict with 'ok' bool and 'error' string if failed.
    """
    result: Dict[str, Any] = {"host": host, "port": port, "ok": False, "error": ""}
    try:
        with socket.create_connection((host, port), timeout=timeout):
            result["ok"] = True
    except Exception as e:
        result["error"] = f"{type(e).__name__}: {e}"
    return result


def detect_os() -> str:
    """
    Detect operating system for platform-specific commands.
    Returns: 'windows', 'macos', or 'linux'
    """
    system_name = platform.system().lower()
    if "windows" in system_name:
        os_name = "windows"
    elif "darwin" in system_name:
        os_name = "macos"
    else:
        os_name = "linux"
    return os_name if os_name in SUPPORTED_OS else "linux"


def os_commands(target: str) -> List[List[str]]:
    """
    Baseline host-side commands (best-effort).
    Keep it simple and high-signal; avoid privileged commands.
    """
    os_name = detect_os()

    if os_name == "windows":
        return [
            ["ipconfig", "/all"],
            ["route", "print"],
            ["arp", "-a"],
            ["ping", "-n", "4", target],
            ["tracert", "-d", target],
            ["netstat", "-ano"],
        ]

    if os_name == "macos":
        return [
            ["ifconfig"],
            ["netstat", "-rn"],
            ["arp", "-an"],
            ["ping", "-c", "4", target],
            ["traceroute", "-n", target],
            ["netstat", "-anv"],
        ]

    return [
        ["ip", "addr"],
        ["ip", "route"],
        ["ip", "neigh"],
        ["ping", "-c", "4", target],
        ["traceroute", "-n", target],
        ["ss", "-tulpn"],
    ]


def prompt_context(non_interactive: bool) -> Dict[str, str]:
    """
    Prompt user for incident context (impact, symptoms, changes, etc.).
    If non_interactive=True, returns empty dict.
    """
    fields = [
        ("impact", "Impact (who/what is affected?)"),
        ("symptoms", "Symptoms (what is failing?)"),
        ("scope", "Scope (one user/site/many?)"),
        ("recent_changes", "Recent changes (deploy/patch/network change?)"),
        ("actions_taken", "Actions already taken"),
    ]
    out: Dict[str, str] = {}
    if non_interactive:
        for key, _ in fields:
            out[key] = ""
        return out

    print("\nEnter incident context (press Enter to skip any field):\n")
    for key, label in fields:
        try:
            out[key] = input(f"{label}: ").strip()
        except EOFError:
            out[key] = ""
    return out


def build_markdown(evidence: Dict[str, Any], md_max_lines: int = DEFAULT_MD_MAX_LINES) -> str:
    """Convert evidence dict to Markdown format (ServiceNow-ready)."""
    meta = evidence["meta"]
    ctx = evidence["context"]
    dns = evidence.get("dns", {})
    tcp = evidence.get("tcp", [])
    cmds = evidence.get("commands", [])

    lines: List[str] = []
    lines.append("# Incident Evidence Pack")
    lines.append("")
    lines.append("## Metadata")
    lines.append(f"- Timestamp (UTC): `{meta.get('timestamp_utc')}`")
    lines.append(f"- Host: `{meta.get('host')}`")
    lines.append(f"- OS: `{meta.get('os')}`")
    lines.append(f"- Target: `{meta.get('target')}`")
    if meta.get("dns_name"):
        lines.append(f"- DNS Name: `{meta.get('dns_name')}`")
    if meta.get("ports"):
        lines.append(f"- Ports: `{', '.join(map(str, meta.get('ports', [])))}`")
    if meta.get("mode"):
        lines.append(f"- Mode: `{meta.get('mode')}`")
    lines.append("")

    lines.append("## Context")
    for key in ["impact", "symptoms", "scope", "recent_changes", "actions_taken"]:
        value = (ctx.get(key) or "").strip()
        lines.append(f"- **{key.replace('_', ' ').title()}**: {value}")
    lines.append("")

    lines.append("## Key Results")
    if dns:
        if dns.get("error"):
            lines.append(f"- DNS: ❌ `{dns.get('name')}` -> `{dns.get('error')}`")
        else:
            answers = ", ".join(dns.get("answers", [])) or "none"
            lines.append(f"- DNS: ✅ `{dns.get('name')}` -> {answers}")
    if tcp:
        for test in tcp:
            if test.get("ok"):
                lines.append(f"- TCP {test['host']}:{test['port']}: ✅ connect ok")
            else:
                lines.append(f"- TCP {test['host']}:{test['port']}: ❌ {test.get('error')}")
    lines.append("")

    lines.append("## Raw Command Outputs")
    for command_result in cmds:
        lines.append(f"### `{command_result.get('cmd')}`")
        lines.append("")
        lines.append("```text")

        stdout = (command_result.get("stdout") or "").strip()
        stderr = (command_result.get("stderr") or "").strip()

        combined = ""
        if stdout:
            combined += stdout
        if stderr:
            combined += ("\n\n" if combined else "") + "[stderr]\n" + stderr
        combined = combined.strip()

        if combined:
            out_lines = combined.splitlines()
            if len(out_lines) > md_max_lines:
                lines.extend(out_lines[:md_max_lines])
                lines.append(
                    f"... (truncated; full output preserved in JSON) [{len(out_lines)} lines total]"
                )
            else:
                lines.append(combined)
        else:
            lines.append("(no output)")

        lines.append("```")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def mock_evidence(target: str, dns_name: Optional[str], ports: List[int]) -> Dict[str, Any]:
    """Generate deterministic mock evidence for GitHub demos."""
    evidence: Dict[str, Any] = {
        "meta": {
            "timestamp_utc": MOCK_TIMESTAMP_UTC,
            "host": "demo-host",
            "os": MOCK_OS,
            "target": target,
            "dns_name": dns_name or "",
            "ports": ports,
            "mode": "mock",
        },
        "context": {
            "impact": "",
            "symptoms": "",
            "scope": "",
            "recent_changes": "",
            "actions_taken": "",
        },
        "dns": {
            "name": dns_name or "",
            "answers": ["93.184.216.34"],
            "error": "",
        }
        if dns_name
        else {},
        "tcp": [
            {"host": target, "port": port, "ok": (port in (80, 443)), "error": "Connection refused"}
            for port in ports
        ],
        "commands": [
            {"cmd": "ping ...", "rc": 0, "stdout": "PING output (mock)", "stderr": ""},
            {"cmd": "traceroute ...", "rc": 0, "stdout": "TRACEROUTE output (mock)", "stderr": ""},
            {"cmd": "ip/ifconfig ...", "rc": 0, "stdout": "Interface output (mock)", "stderr": ""},
        ],
    }
    for test in evidence["tcp"]:
        if test["ok"]:
            test["error"] = ""
    return evidence


def collect_live_evidence(
    target: str,
    dns_name: Optional[str],
    ports: List[int],
    timeout: int,
    non_interactive: bool,
) -> Dict[str, Any]:
    """Collect live host-side evidence."""
    host = platform.node() or "unknown-host"
    os_name = detect_os()

    evidence: Dict[str, Any] = {
        "meta": {
            "timestamp_utc": now_utc_iso(),
            "host": host,
            "os": os_name,
            "target": target,
            "dns_name": dns_name or "",
            "ports": ports,
            "mode": "live",
        },
        "context": prompt_context(non_interactive),
        "dns": resolve(dns_name) if dns_name else {},
        "tcp": [tcp_check(target, port) for port in ports],
        "commands": [],
    }

    for command in os_commands(target):
        evidence["commands"].append(run(command, timeout=timeout))

    return evidence


def choose_output_base(out_dir: str, host: str, timestamp: Optional[str] = None) -> str:
    """Return a unique output base path, adding a numeric suffix if needed."""
    stamp = timestamp or dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_host = sanitize_filename_component(host)
    directory = Path(out_dir)
    directory.mkdir(parents=True, exist_ok=True)

    base_name = f"incident_pack_{safe_host}_{stamp}"
    candidate = directory / base_name
    suffix = 1
    while candidate.with_suffix(".json").exists() or candidate.with_suffix(".md").exists():
        candidate = directory / f"{base_name}_{suffix:02d}"
        suffix += 1
    return str(candidate)


def write_outputs(evidence: Dict[str, Any], out_dir: str, md_max_lines: int) -> Dict[str, str]:
    """Write JSON and Markdown outputs to disk."""
    base = choose_output_base(out_dir, evidence["meta"].get("host", "host"))
    json_path = f"{base}.json"
    md_path = f"{base}.md"

    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(evidence, handle, indent=2, sort_keys=False)

    with open(md_path, "w", encoding="utf-8") as handle:
        handle.write(build_markdown(evidence, md_max_lines=md_max_lines))

    return {"json": json_path, "md": md_path}


def build_arg_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate a standardized incident evidence pack (JSON + Markdown)."
    )
    parser.add_argument("--target", required=True, help="IP or hostname to test (e.g., 10.0.0.10)")
    parser.add_argument(
        "--dns-name", default="", help="Optional DNS name to resolve (e.g., app.example.com)"
    )
    parser.add_argument("--ports", nargs="*", type=int, default=[], help="Ports to test (e.g., 443 80 22)")
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_CMD_TIMEOUT,
        help=f"Command timeout seconds (default: {DEFAULT_CMD_TIMEOUT})",
    )
    parser.add_argument(
        "--non-interactive", action="store_true", help="Skip prompts (empty context fields)"
    )
    parser.add_argument(
        "--mock", action="store_true", help="Generate deterministic sample outputs (for GitHub demos)"
    )
    parser.add_argument("--out-dir", default=".", help="Output directory (default: current)")
    parser.add_argument(
        "--md-max-lines",
        type=int,
        default=DEFAULT_MD_MAX_LINES,
        help=f"Max lines per command in Markdown (default: {DEFAULT_MD_MAX_LINES})",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """
    Main entry point: parse args, collect evidence, write outputs.
    Returns 0 on success.
    """
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    try:
        ports = normalize_ports(args.ports or [])
        validate_ports(ports)
        validate_md_max_lines(args.md_max_lines)
    except ValueError as error:
        parser.error(str(error))

    target = args.target.strip()
    if not target:
        parser.error("--target cannot be empty.")
    dns_name = args.dns_name.strip() or None

    if args.mock:
        evidence = mock_evidence(target, dns_name, ports)
    else:
        evidence = collect_live_evidence(
            target=target,
            dns_name=dns_name,
            ports=ports,
            timeout=args.timeout,
            non_interactive=args.non_interactive,
        )

    output_paths = write_outputs(evidence, out_dir=args.out_dir, md_max_lines=args.md_max_lines)
    print(f"Wrote:\n- {output_paths['json']}\n- {output_paths['md']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
