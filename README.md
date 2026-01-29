# servicenow-incident-pack

A Python CLI tool that standardizes host-side troubleshooting evidence into:
- **JSON** (machine-readable evidence bundle)
- **Markdown** (ticket-ready report to paste into ServiceNow)

This repository is a **public-safe portfolio template**: no proprietary endpoints, no ServiceNow API keys, no internal environment assumptions.

## Problem
Enterprise tickets often arrive with little/no diagnostic context. The first 30–60 minutes becomes repetitive back-and-forth (IP/gateway/DNS/reachability/what changed), and shift handoffs re-triage the same basics.

`servicenow-incident-pack` standardizes the *first 10 minutes* of evidence so every incident starts with a consistent baseline.

## What it collects (Phase 1 — completed)
High-signal L1–L4 evidence:
- Reachability: `ping`
- Path: `traceroute` / `tracert`
- DNS proof: Python `socket.getaddrinfo`
- TCP port reachability: Python `socket.create_connection`
- Local state: interface/IP, routes, ARP/neighbors

Outputs:
- `incident_pack_<host>_<timestamp>.json`
- `incident_pack_<host>_<timestamp>.md`

## Planned (Phase 2 — roadmap)
Device-side evidence via SSH/APIs (template plan):
- Cisco: BGP/OSPF/interfaces/trunks/STP/ARP
- Palo Alto: traffic/session/routing lookup
- Meraki/Aruba: client state + SSID/VLAN mapping
- Optional ServiceNow API integration (auto-create/update ticket)

## Usage

### Requirements
- Python 3.10+ (stdlib only)

### Run (live)
```bash
python3 incident_pack.py --target 10.20.30.40 --dns-name app.example.com --ports 443 80 22
