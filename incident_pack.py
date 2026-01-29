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
import socket
import subprocess
import sys
from typing import Any, Dict, List, Optional


def now_utc_iso() -> str:
    """Return current UTC timestamp in ISO format."""
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def run(cmd: List[str], timeout: int = 15) -> Dict[str, Any]:
    """
    Run a command and capture stdout/stderr/rc as evidence.
    Requirement: never crash the run; failures become evidence.
    """
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
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


def tcp_check(host: str, port: int, timeout: float = 3.0) -> Dict[str, Any]:
    """
    Layer 4 TCP connect test.
    Returns dict with 'ok' bool and 'error' string if failed.
    """
    r: Dict[str, Any] = {"host": host, "port": port, "ok": False, "error": ""}
    try:
        with socket.create_connection((host, port), timeout=timeout):
            r["ok"] = True
    except Exception as e:
        r["error"] = f"{type(e).__name__}: {e}"
    return r


def detect_os() -> str:
    """
    Detect operating system for platform-specific commands.
    Returns: 'windows', 'macos', or 'linux'
    """
    s = platform.system().lower()
    if "windows" in s:
        return "windows"
    if "darwin" in s:
        return "macos"
    return "linux"


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

    # linux
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
        for k, _ in fields:
            out[k] = ""
        return out

    print("\nEnter incident context (press Enter to skip any field):\n")
    for k, label in fields:
        out[k] = input(f"{label}: ").strip()
    return out


def build_markdown(e: Dict[str, Any]) -> str:
    """
    Convert evidence dict to Markdown format (ServiceNow-ready).
    """
    meta = e["meta"]
    ctx = e["context"]
    dns = e.get("dns", {})
    tcp = e.get("tcp", [])
    cmds = e.get("commands", [])

    lines: List[str] = []
    lines.append(f"# Incident Evidence Pack")
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
    lines.append("")

    lines.append("## Context")
    for k in ["impact", "symptoms", "scope", "recent_changes", "actions_taken"]:
        v = (ctx.get(k) or "").strip()
        lines.append(f"- **{k.replace('_',' ').title()}**: {v if v else '_n/a_'}")
    lines.append("")

    lines.append("## Key Results")
    if dns:
        if dns.get("error"):
            lines.append(f"- DNS: ❌ `{dns.get('name')}` -> `{dns.get('error')}`")
        else:
            answers = ", ".join(dns.get("answers", [])) or "none"
            lines.append(f"- DNS: ✅ `{dns.get('name')}` -> {answers}")
    if tcp:
        for t in tcp:
            if t.get("ok"):
                lines.append(f"- TCP {t['host']}:{t['port']}: ✅ connect ok")
            else:
                lines.append(f"- TCP {t['host']}:{t['port']}: ❌ {t.get('error')}")
    lines.append("")

    lines.append("## Raw Command Outputs")
    for c in cmds:
        lines.append(f"### `{c.get('cmd')}`")
        lines.append("")
        lines.append("```text")
        out = c.get("stdout") or ""
        err = c.get("stderr") or ""
        if out:
            lines.append(out)
        if err:
            lines.append("")
            lines.append("[stderr]")
            lines.append(err)
        if not out and not err:
            lines.append("(no output)")
        lines.append("```")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def mock_evidence(target: str, dns_name: Optional[str], ports: List[int]) -> Dict[str, Any]:
    """
    Generate deterministic mock evidence for GitHub demos.
    """
    host = platform.node() or "mock-host"
    os_name = detect_os()
    e: Dict[str, Any] = {
        "meta": {
            "timestamp_utc": now_utc_iso(),
            "host": host,
            "os": os_name,
            "target": target,
            "dns_name": dns_name or "",
            "ports": ports,
            "mode": "mock",
        },
        "context": {
            "impact": "Template run (public-safe).",
            "symptoms": "Simulated evidence output.",
            "scope": "n/a",
            "recent_changes": "n/a",
            "actions_taken": "n/a",
        },
        "dns": {"name": dns_name or "", "answers": ["93.184.216.34"], "error": ""} if dns_name else {},
        "tcp": [{"host": target, "port": p, "ok": (p in (80, 443)), "error": "Connection refused"} for p in ports],
        "commands": [
            {"cmd": "ping ...", "rc": 0, "stdout": "PING output (mock)", "stderr": ""},
            {"cmd": "traceroute ...", "rc": 0, "stdout": "TRACEROUTE output (mock)", "stderr": ""},
            {"cmd": "ip/ifconfig ...", "rc": 0, "stdout": "Interface output (mock)", "stderr": ""},
        ],
    }
    # Fix errors for ports that are ok
    for t in e["tcp"]:
        if t["ok"]:
            t["error"] = ""
    return e


def main() -> int:
    """
    Main entry point: parse args, collect evidence, write outputs.
    Returns 0 on success.
    """
    ap = argparse.ArgumentParser(description="Generate a standardized incident evidence pack (JSON + Markdown).")
    ap.add_argument("--target", required=True, help="IP or hostname to test (e.g., 10.0.0.10)")
    ap.add_argument("--dns-name", default="", help="Optional DNS name to resolve (e.g., app.example.com)")
    ap.add_argument("--ports", nargs="*", type=int, default=[], help="Ports to test (e.g., 443 80 22)")
    ap.add_argument("--timeout", type=int, default=15, help="Command timeout seconds (default: 15)")
    ap.add_argument("--non-interactive", action="store_true", help="Skip prompts (empty context fields)")
    ap.add_argument("--mock", action="store_true", help="Generate deterministic sample outputs (for GitHub demos)")
    ap.add_argument("--out-dir", default=".", help="Output directory (default: current)")
    args = ap.parse_args()

    target = args.target
    dns_name = args.dns_name.strip() or None
    ports = args.ports or []
    out_dir = args.out_dir

    if args.mock:
        evidence = mock_evidence(target, dns_name, ports)
    else:
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
            "context": prompt_context(args.non_interactive),
            "dns": resolve(dns_name) if dns_name else {},
            "tcp": [tcp_check(target, p) for p in ports],
            "commands": [],
        }

        for cmd in os_commands(target):
            evidence["commands"].append(run(cmd, timeout=args.timeout))

    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    host = evidence["meta"].get("host", "host")
    base = f"incident_pack_{host}_{ts}"
    os.makedirs(out_dir, exist_ok=True)
    json_path = os.path.join(out_dir, f"{base}.json")
    md_path = os.path.join(out_dir, f"{base}.md")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(evidence, f, indent=2, sort_keys=False)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(build_markdown(evidence))

    print(f"Wrote:\n- {json_path}\n- {md_path}")
    return 0


if __name__ == "__main__":
    # Entry point when run as script (not when imported as module)
    raise SystemExit(main())
