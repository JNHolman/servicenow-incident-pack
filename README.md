# servicenow-incident-pack

A Python CLI tool that standardizes host-side troubleshooting evidence into:
- **JSON** (machine-readable evidence bundle)
- **Markdown** (ticket-ready report to paste into ServiceNow)

This repo is a **public-safe portfolio template** (no proprietary endpoints, no ServiceNow API keys).

## Problem
Support tickets from non-technical users often arrive with little/no diagnostic context. Engineers spend 30–60 minutes collecting the same basics (IP/gateway/DNS/reachability/what changed), and shift handoffs re-triage the same steps.

## Solution
`incident_pack.py` collects a consistent baseline “evidence pack” so every ticket starts with the same high-signal L1–L4 data.

## What it collects (Phase 1 — completed)
- Reachability: `ping`
- Path: `traceroute` / `tracert`
- DNS proof: `socket.getaddrinfo`
- TCP port reachability: `socket.create_connection`
- Local state: interface/IP, routes, ARP/neighbors (OS-aware)

## Outputs
- `incident_pack_<host>_<timestamp>.json`
- `incident_pack_<host>_<timestamp>.md`

Example outputs:
- `examples/sample_output.json`
- `examples/sample_output.md`

## Usage

### Requirements
- Python 3.10+ (stdlib only)

### Live run
```bash
python3 incident_pack.py --target 10.20.30.40 --dns-name app.example.com --ports 443 80 22
