# Incident Evidence Pack

## Metadata
- Timestamp (UTC): `2026-01-29T04:03:26+00:00`
- Host: `Js-MBP-2.lan`
- OS: `macos`
- Target: `10.20.30.40`
- DNS Name: `app.example.com`
- Ports: `443, 80, 22`

## Context
- **Impact**: Template run (public-safe).
- **Symptoms**: Simulated evidence output.
- **Scope**: n/a
- **Recent Changes**: n/a
- **Actions Taken**: n/a

## Key Results
- DNS: ✅ `app.example.com` -> 93.184.216.34
- TCP 10.20.30.40:443: ✅ connect ok
- TCP 10.20.30.40:80: ✅ connect ok
- TCP 10.20.30.40:22: ❌ Connection refused

## Raw Command Outputs
### `ping ...`

```text
PING output (mock)
```

### `traceroute ...`

```text
TRACEROUTE output (mock)
```

### `ip/ifconfig ...`

```text
Interface output (mock)
```
