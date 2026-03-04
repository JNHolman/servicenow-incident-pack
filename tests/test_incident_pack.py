import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import incident_pack


class IncidentPackTests(unittest.TestCase):
    def test_sanitize_filename_component(self):
        self.assertEqual(incident_pack.sanitize_filename_component("Js MBP/2.lan"), "Js-MBP-2.lan")
        self.assertEqual(incident_pack.sanitize_filename_component("***", default="demo"), "demo")

    def test_normalize_ports_deduplicates_preserves_order(self):
        self.assertEqual(incident_pack.normalize_ports([443, 80, 443, 22, 80]), [443, 80, 22])

    def test_validate_ports_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            incident_pack.validate_ports([0, 443, 70000])

    def test_validate_md_max_lines_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            incident_pack.validate_md_max_lines(0)

    def test_build_markdown_includes_mode(self):
        evidence = incident_pack.mock_evidence("1.1.1.1", "example.com", [443, 53])
        markdown = incident_pack.build_markdown(evidence, md_max_lines=10)
        self.assertIn("- Mode: `mock`", markdown)
        self.assertIn("TCP 1.1.1.1:443: ✅ connect ok", markdown)

    def test_build_markdown_truncates_long_output(self):
        evidence = incident_pack.mock_evidence("1.1.1.1", "example.com", [443])
        evidence["commands"] = [
            {
                "cmd": "demo",
                "rc": 0,
                "stdout": "\n".join(f"line-{i}" for i in range(6)),
                "stderr": "",
            }
        ]
        markdown = incident_pack.build_markdown(evidence, md_max_lines=3)
        self.assertIn("line-0", markdown)
        self.assertIn("line-2", markdown)
        self.assertIn("truncated; full output preserved in JSON", markdown)
        self.assertNotIn("line-5", markdown)

    def test_mock_evidence_is_deterministic_and_demo_safe(self):
        evidence = incident_pack.mock_evidence("1.1.1.1", "example.com", [443, 53])
        self.assertEqual(evidence["meta"]["host"], "demo-host")
        self.assertEqual(evidence["meta"]["timestamp_utc"], incident_pack.MOCK_TIMESTAMP_UTC)
        self.assertEqual(evidence["meta"]["os"], incident_pack.MOCK_OS)

    def test_resolve_captures_dns_failure(self):
        with mock.patch("incident_pack.socket.getaddrinfo", side_effect=OSError("dns failed")):
            result = incident_pack.resolve("bad.example")
        self.assertEqual(result["answers"], [])
        self.assertIn("dns failed", result["error"])

    def test_run_captures_command_failure(self):
        with mock.patch("incident_pack.subprocess.run", side_effect=TimeoutError("slow command")):
            result = incident_pack.run(["ping", "example.com"])
        self.assertIsNone(result["rc"])
        self.assertIn("TimeoutError", result["stderr"])

    def test_os_commands_linux(self):
        with mock.patch("incident_pack.detect_os", return_value="linux"):
            commands = incident_pack.os_commands("example.com")
        self.assertEqual(commands[0], ["ip", "addr"])
        self.assertIn(["ss", "-tulpn"], commands)

    def test_os_commands_macos(self):
        with mock.patch("incident_pack.detect_os", return_value="macos"):
            commands = incident_pack.os_commands("example.com")
        self.assertEqual(commands[0], ["ifconfig"])
        self.assertIn(["traceroute", "-n", "example.com"], commands)

    def test_os_commands_windows(self):
        with mock.patch("incident_pack.detect_os", return_value="windows"):
            commands = incident_pack.os_commands("example.com")
        self.assertEqual(commands[0], ["ipconfig", "/all"])
        self.assertIn(["tracert", "-d", "example.com"], commands)

    def test_prompt_context_handles_non_interactive(self):
        result = incident_pack.prompt_context(non_interactive=True)
        self.assertTrue(all(value == "" for value in result.values()))
        self.assertEqual(
            set(result),
            {"impact", "symptoms", "scope", "recent_changes", "actions_taken"},
        )

    def test_prompt_context_handles_eof(self):
        with contextlib.redirect_stdout(io.StringIO()):
            with mock.patch("builtins.input", side_effect=EOFError):
                result = incident_pack.prompt_context(non_interactive=False)
        self.assertTrue(all(value == "" for value in result.values()))

    def test_main_rejects_invalid_ports(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as ctx:
                incident_pack.main(["--target", "1.1.1.1", "--ports", "0"])
        self.assertEqual(ctx.exception.code, 2)

    def test_main_rejects_invalid_md_max_lines(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as ctx:
                incident_pack.main(["--target", "1.1.1.1", "--md-max-lines", "0"])
        self.assertEqual(ctx.exception.code, 2)

    def test_main_rejects_blank_target(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as ctx:
                incident_pack.main(["--target", "   "])
        self.assertEqual(ctx.exception.code, 2)

    def test_collect_live_evidence_uses_injected_helpers(self):
        with (
            mock.patch("incident_pack.platform.node", return_value="lab-host"),
            mock.patch("incident_pack.detect_os", return_value="linux"),
            mock.patch(
                "incident_pack.prompt_context",
                return_value={
                    "impact": "",
                    "symptoms": "",
                    "scope": "",
                    "recent_changes": "",
                    "actions_taken": "",
                },
            ),
            mock.patch(
                "incident_pack.resolve",
                return_value={"name": "app.example.com", "answers": ["1.1.1.1"], "error": ""},
            ),
            mock.patch(
                "incident_pack.tcp_check",
                return_value={"host": "1.1.1.1", "port": 443, "ok": True, "error": ""},
            ),
            mock.patch("incident_pack.os_commands", return_value=[["ping", "1.1.1.1"]]),
            mock.patch(
                "incident_pack.run",
                return_value={"cmd": "ping 1.1.1.1", "rc": 0, "stdout": "ok", "stderr": ""},
            ),
        ):
            evidence = incident_pack.collect_live_evidence(
                target="1.1.1.1",
                dns_name="app.example.com",
                ports=[443],
                timeout=5,
                non_interactive=True,
            )
        self.assertEqual(evidence["meta"]["host"], "lab-host")
        self.assertEqual(evidence["meta"]["mode"], "live")
        self.assertEqual(evidence["dns"]["answers"], ["1.1.1.1"])
        self.assertEqual(evidence["commands"][0]["rc"], 0)

    def test_choose_output_base_adds_suffix_on_collision(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            first_base = incident_pack.choose_output_base(tmpdir, "demo-host", timestamp="20260303_120000")
            Path(f"{first_base}.json").write_text("{}", encoding="utf-8")
            second_base = incident_pack.choose_output_base(tmpdir, "demo-host", timestamp="20260303_120000")
        self.assertTrue(second_base.endswith("_01"))

    def test_write_outputs_creates_json_and_markdown(self):
        evidence = incident_pack.mock_evidence("1.1.1.1", "example.com", [443])
        with tempfile.TemporaryDirectory() as tmpdir:
            paths = incident_pack.write_outputs(evidence, tmpdir, md_max_lines=10)
            json_path = Path(paths["json"])
            md_path = Path(paths["md"])
            self.assertTrue(json_path.exists())
            self.assertTrue(md_path.exists())
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["meta"]["host"], "demo-host")


if __name__ == "__main__":
    unittest.main()
