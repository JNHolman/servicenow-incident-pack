# Incident Evidence Pack

## Metadata
- Timestamp (UTC): `2026-01-29T06:03:09+00:00`
- Host: `Js-MBP-2.lan`
- OS: `macos`
- Target: `1.1.1.1`
- DNS Name: `example.com`
- Ports: `443, 53`

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
- DNS: ✅ `example.com` -> 104.18.26.120, 104.18.27.120, 2606:4700::6812:1a78, 2606:4700::6812:1b78
- TCP 1.1.1.1:443: ✅ connect ok
- TCP 1.1.1.1:53: ✅ connect ok

## Raw Command Outputs
### `ifconfig`

```text
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
EHC29: flags=0<> mtu 0
EHC26: flags=0<> mtu 0
XHC20: flags=0<> mtu 0
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 0c:4d:e9:d0:0c:2f 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (none)
	status: inactive
en1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 90:fd:61:eb:4f:04 
	inet6 fe80::48c:9d60:dab4:6131%en1 prefixlen 64 secured scopeid 0x8 
	inet 192.168.1.98 netmask 0xffffff00 broadcast 192.168.1.255
	inet6 2603:6010:7c00:4328:c75:f76a:f8f6:369e prefixlen 64 autoconf secured 
	inet6 2603:6010:7c00:4328:6d73:7756:449d:ef44 prefixlen 64 autoconf temporary 
	inet6 fd00:7437:5f96:ab30:1c37:5c46:ae31:64ce prefixlen 64 autoconf secured 
	inet6 fd00:7437:5f96:ab30:592f:e2b6:9959:d8d prefixlen 64 autoconf temporary 
	inet6 2603:6010:7c00:4328::1d63 prefixlen 64 dynamic 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether 02:fd:61:eb:4f:04 
	media: autoselect
	status: inactive
awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether ee:c7:e9:fe:39:0d 
	inet6 fe80::ecc7:e9ff:fefe:390d%awdl0 prefixlen 64 scopeid 0xa 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
... (truncated; full output preserved in JSON) [71 lines total]
```

### `netstat -rn`

```text
Routing tables

Internet:
Destination        Gateway            Flags        Refs      Use   Netif Expire
default            192.168.1.1        UGSc           61        0     en1
127                127.0.0.1          UCS             0        0     lo0
127.0.0.1          127.0.0.1          UH              2    30652     lo0
169.254            link#8             UCS             0        0     en1
192.168.1          link#8             UCS             8        0     en1
192.168.1.1/32     link#8             UCS             1        0     en1
192.168.1.1        74:37:5f:96:ab:30  UHLWIir        13     2649     en1   1192
192.168.1.14       82:fd:9d:fc:70:24  UHLWI           0      173     en1    535
192.168.1.42       c4:29:96:63:c9:3d  UHLWI           0     1002     en1   1114
192.168.1.77       4c:57:39:3a:3a:10  UHLWI           0       11     en1   1114
192.168.1.87       1c:86:9a:4a:5a:c8  UHLWI           0       10     en1    994
192.168.1.98/32    link#8             UCS             1        0     en1
192.168.1.98       90:fd:61:eb:4f:4   UHLWI           0        1     lo0
192.168.1.161      88:a2:9e:3:73:3d   UHLWI           0      429     en1   1139
192.168.1.178      d0:3:df:b4:55:bc   UHLWI           0        9     en1    994
192.168.1.210      5c:e4:2a:fa:35:11  UHLWI           0        0     en1    418
192.168.1.226      fc:8c:11:bd:89:f   UHLWI           0       39     en1   1114
224.0.0/4          link#8             UmCS            2        0     en1
224.0.0.251        1:0:5e:0:0:fb      UHmLWI          0        0     en1
239.255.255.250    1:0:5e:7f:ff:fa    UHmLWI          0      281     en1
255.255.255.255/32 link#8             UCS             0        0     en1

Internet6:
Destination                             Gateway                         Flags         Netif Expire
default                                 fe80::7637:5fff:fe96:ab30%en1   UGc             en1
default                                 fe80::%utun0                    UGcI          utun0
default                                 fe80::%utun1                    UGcI          utun1
default                                 fe80::%utun2                    UGcI          utun2
::1                                     ::1                             UHL             lo0
2603:6010:7c00:4328::/64                link#8                          UC              en1
2603:6010:7c00:4328::1                  74:37:5f:96:ab:30               UHLWI           en1
2603:6010:7c00:4328::1253               82:fd:9d:fc:70:24               UHLWI           en1
2603:6010:7c00:4328::1d63               90:fd:61:eb:4f:4                UHL             lo0
2603:6010:7c00:4328:477:55e2:6f41:8b04  82:fd:9d:fc:70:24               UHLWI           en1
2603:6010:7c00:4328:c75:f76a:f8f6:369e  90:fd:61:eb:4f:4                UHL             lo0
2603:6010:7c00:4328:40df:da9:3b5c:1099  82:fd:9d:fc:70:24               UHLWI           en1
... (truncated; full output preserved in JSON) [71 lines total]
```

### `arp -an`

```text
? (192.168.1.1) at 74:37:5f:96:ab:30 on en1 ifscope [ethernet]
? (192.168.1.14) at 82:fd:9d:fc:70:24 on en1 ifscope [ethernet]
? (192.168.1.42) at c4:29:96:63:c9:3d on en1 ifscope [ethernet]
? (192.168.1.77) at 4c:57:39:3a:3a:10 on en1 ifscope [ethernet]
? (192.168.1.87) at 1c:86:9a:4a:5a:c8 on en1 ifscope [ethernet]
? (192.168.1.98) at 90:fd:61:eb:4f:4 on en1 ifscope permanent [ethernet]
? (192.168.1.161) at 88:a2:9e:3:73:3d on en1 ifscope [ethernet]
? (192.168.1.178) at d0:3:df:b4:55:bc on en1 ifscope [ethernet]
? (192.168.1.210) at 5c:e4:2a:fa:35:11 on en1 ifscope [ethernet]
? (192.168.1.226) at fc:8c:11:bd:89:f on en1 ifscope [ethernet]
? (224.0.0.251) at 1:0:5e:0:0:fb on en1 ifscope permanent [ethernet]
? (239.255.255.250) at 1:0:5e:7f:ff:fa on en1 ifscope permanent [ethernet]
```

### `ping -c 4 1.1.1.1`

```text
PING 1.1.1.1 (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: icmp_seq=0 ttl=55 time=26.915 ms
64 bytes from 1.1.1.1: icmp_seq=1 ttl=55 time=23.779 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=55 time=25.914 ms
64 bytes from 1.1.1.1: icmp_seq=3 ttl=55 time=26.248 ms

--- 1.1.1.1 ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 23.779/25.714/26.915/1.174 ms
```

### `traceroute -n 1.1.1.1`

```text
1  192.168.1.1  3.287 ms  1.102 ms  1.853 ms
 2  142.254.144.25  8.791 ms  8.768 ms  9.678 ms
 3  65.29.26.254  14.587 ms  8.780 ms  8.551 ms
 4  65.29.39.71  8.246 ms  10.575 ms  8.929 ms
 5  65.29.31.26  9.325 ms  10.148 ms  9.582 ms
 6  65.189.140.162  24.831 ms  26.180 ms  25.010 ms
 7  65.29.33.229  24.055 ms  23.314 ms  22.646 ms
 8  172.69.174.2  22.823 ms
    172.68.168.2  36.227 ms
    172.69.174.2  23.308 ms
 9  172.69.174.1  22.417 ms
    172.68.168.9  27.968 ms  26.891 ms
10  1.1.1.1  29.733 ms  22.709 ms  23.902 ms

[stderr]
traceroute to 1.1.1.1 (1.1.1.1), 64 hops max, 52 byte packets
```

### `netstat -anv`

```text
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)     rhiwat shiwat    pid   epid
tcp4       0      0  192.168.1.98.51937     162.247.243.29.443     ESTABLISHED 131072 131480    704      0
tcp4       0      0  192.168.1.98.51920     185.199.108.154.443    ESTABLISHED 299920 131072    704      0
tcp4       0      0  192.168.1.98.51919     185.199.108.154.443    ESTABLISHED 476752 131072    704      0
tcp6       0      0  2603:6010:7c00:4.51910 2606:50c0:8000::.443   ESTABLISHED 131072 132308    704      0
tcp4       0      0  192.168.1.98.51906     162.247.243.29.443     ESTABLISHED 131072 131480    704      0
tcp6       0      0  2603:6010:7c00:4.51904 2a06:98c1:3108::.443   ESTABLISHED 131072 131072    704      0
tcp4       0      0  192.168.1.98.51767     140.82.112.25.443      ESTABLISHED 131072 131072    704      0
tcp6       0      0  2603:6010:7c00:4.51388 2606:4700::6810:.443   ESTABLISHED 131072 131072    704      0
tcp6       0      0  *.50539                *.*                    LISTEN      131072 131072    634      0
tcp4       0      0  *.50539                *.*                    LISTEN      131072 131072    634      0
tcp4       0      0  192.168.1.98.50537     17.57.144.42.5223      ESTABLISHED 131072 131768     94      0
tcp6       0      0  2603:6010:7c00:4.50530 2607:f8b0:4001:c.5228  ESTABLISHED 131072 131376    704      0
tcp4       0      0  127.0.0.1.49399        *.*                    LISTEN      131072 131072    848      0
tcp4       0      0  127.0.0.1.45623        *.*                    LISTEN      131072 131072    848      0
tcp4       0      0  127.0.0.1.49308        *.*                    LISTEN      131072 131072    848      0
tcp4       0      0  127.0.0.1.49307        *.*                    LISTEN      131072 131072    848      0
tcp4       0      0  127.0.0.1.15292        *.*                    LISTEN      131072 131072    829      0
tcp6       0      0  fe80::ab45:b3fd:.1025  fe80::cdac:d366:.1026  ESTABLISHED 131072 131072    360      0
tcp6       0      0  fe80::ab45:b3fd:.1024  fe80::cdac:d366:.1024  ESTABLISHED 131088 131072    360      0
tcp4       0      0  *.631                  *.*                    LISTEN      131072 131072    196      0
tcp6       0      0  *.631                  *.*                    LISTEN      131072 131072    196      0
tcp4       0      0  *.88                   *.*                    LISTEN      131072 131072    106      0
tcp6       0      0  *.88                   *.*                    LISTEN      131072 131072    106      0
tcp4       0      0  *.548                  *.*                    LISTEN      131072 131072      1      0
tcp6       0      0  *.548                  *.*                    LISTEN      131072 131072      1      0
tcp4       0      0  192.168.1.98.51941     1.1.1.1.443            TIME_WAIT   131768 131768  29137      0
tcp4       0      0  192.168.1.98.51942     1.1.1.1.53             TIME_WAIT   131768 131768  29137      0
udp6       0      0  2603:6010:7c00:4.51816 2600:1901:0:47fc.443               1048576  29040    704      0
udp6       0      0  2603:6010:7c00:4.51806 2a06:98c1:3100::.443               1048576  29040    704      0
udp6       0      0  2603:6010:7c00:4.59088 2a06:98c1:310b::.443               1048576  29040    704      0
udp4       0      0  *.65115                *.*                                196724   9216     56      0
udp6       0      0  *.58852                *.*                                196724   9216    187      0
udp4       0      0  *.58852                *.*                                196724   9216    187      0
udp6       0      0  *.60502                *.*                                196724   9216    187      0
udp4       0      0  *.60502                *.*                                196724   9216    187      0
udp6       0      0  *.49868                *.*                                196724   9216    187      0
udp4       0      0  *.49868                *.*                                196724   9216    187      0
udp6       0      0  *.64184                *.*                                196724   9216    187      0
... (truncated; full output preserved in JSON) [452 lines total]
```
