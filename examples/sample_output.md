# Incident Evidence Pack

## Metadata
- Timestamp (UTC): `2026-01-29T05:26:54+00:00`
- Host: `Js-MBP-2.lan`
- OS: `macos`
- Target: `10.20.30.40`
- DNS Name: `app.example.com`
- Ports: `443, 80, 22`

## Prompt Inputs

Enter incident context (press Enter to skip any field):

- Impact (who/what is affected?):
- Symptoms (what is failing?):
- Scope (one user/site/many?):
- Recent changes (deploy/patch/network change?):
- Actions already taken:

## Context
- **Impact**: 
- **Symptoms**: 
- **Scope**: 
- **Recent Changes**: 
- **Actions Taken**: 

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
