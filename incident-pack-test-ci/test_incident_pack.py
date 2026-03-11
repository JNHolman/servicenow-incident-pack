"""
Basic smoke tests for incident_pack.py mock mode.
Validates that mock output generates valid JSON and Markdown
with the expected evidence structure.
"""

import json
import os
import subprocess
import sys
import tempfile


def run_mock(tmp_dir):
    """Run incident_pack.py in mock mode and return the output directory."""
    cmd = [
        sys.executable, "incident_pack.py",
        "--target", "10.20.30.40",
        "--dns-name", "app.example.com",
        "--ports", "443", "80", "22",
        "--mock",
        "--out-dir", tmp_dir,
        "--non-interactive",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0, f"Mock run failed: {result.stderr}"
    return tmp_dir


def find_output(tmp_dir, ext):
    """Find the first file with the given extension in the output directory."""
    for f in os.listdir(tmp_dir):
        if f.endswith(ext):
            return os.path.join(tmp_dir, f)
    return None


def test_mock_generates_json():
    with tempfile.TemporaryDirectory() as tmp:
        run_mock(tmp)
        path = find_output(tmp, ".json")
        assert path is not None, "No JSON output generated"

        with open(path) as f:
            data = json.load(f)

        # Verify expected top-level keys
        assert "target" in data, "Missing 'target' in JSON"
        assert "evidence" in data or "checks" in data, "Missing evidence data in JSON"


def test_mock_generates_markdown():
    with tempfile.TemporaryDirectory() as tmp:
        run_mock(tmp)
        path = find_output(tmp, ".md")
        assert path is not None, "No Markdown output generated"

        with open(path) as f:
            content = f.read()

        assert len(content) > 100, "Markdown output is suspiciously short"
        assert "10.20.30.40" in content, "Target not found in Markdown output"


def test_mock_is_deterministic():
    """Two mock runs with the same input should produce identical JSON."""
    with tempfile.TemporaryDirectory() as tmp1, tempfile.TemporaryDirectory() as tmp2:
        run_mock(tmp1)
        run_mock(tmp2)

        json1 = find_output(tmp1, ".json")
        json2 = find_output(tmp2, ".json")

        assert json1 and json2, "Missing JSON output in one or both runs"

        with open(json1) as f1, open(json2) as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

        # Remove timestamps before comparing
        for d in [data1, data2]:
            d.pop("timestamp", None)
            d.pop("generated_at", None)

        assert data1 == data2, "Mock mode is not deterministic"


if __name__ == "__main__":
    test_mock_generates_json()
    print("PASS: test_mock_generates_json")

    test_mock_generates_markdown()
    print("PASS: test_mock_generates_markdown")

    test_mock_is_deterministic()
    print("PASS: test_mock_is_deterministic")

    print("\nAll tests passed.")
