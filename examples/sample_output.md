# Incident Evidence Pack

## Metadata
- Timestamp (UTC): `2026-01-29T05:46:39+00:00`
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
	options=60<TSO4,TSO6>
	ether d2:00:12:4d:79:a0 
	media: autoselect <full-duplex>
	status: inactive
fw0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 4078
	lladdr 28:0b:5c:ff:fe:24:d7:9a 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect <full-duplex>
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether d2:00:12:4d:79:a0 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 11 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::ea1d:3097:d6f5:d27d%utun0 prefixlen 64 scopeid 0xe 
	nd6 options=201<PERFORMNUD,DAD>
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::ab45:b3fd:5520:a1a4%utun1 prefixlen 64 scopeid 0xf 
	nd6 options=201<PERFORMNUD,DAD>
utun2: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::32cd:8f84:68ff:a68c%utun2 prefixlen 64 scopeid 0x10 
	nd6 options=201<PERFORMNUD,DAD>
```

### `netstat -rn`

```text
Routing tables

Internet:
Destination        Gateway            Flags        Refs      Use   Netif Expire
default            192.168.1.1        UGSc           75        0     en1
127                127.0.0.1          UCS             0        0     lo0
127.0.0.1          127.0.0.1          UH              2    30382     lo0
169.254            link#8             UCS             0        0     en1
192.168.1          link#8             UCS             8        0     en1
192.168.1.1/32     link#8             UCS             1        0     en1
192.168.1.1        74:37:5f:96:ab:30  UHLWIir        27     2390     en1   1174
192.168.1.14       82:fd:9d:fc:70:24  UHLWI           0      136     en1    434
192.168.1.42       c4:29:96:63:c9:3d  UHLWI           0      906     en1   1146
192.168.1.77       4c:57:39:3a:3a:10  UHLWI           0       11     en1   1146
192.168.1.87       1c:86:9a:4a:5a:c8  UHLWI           0       10     en1   1146
192.168.1.98/32    link#8             UCS             1        0     en1
192.168.1.98       90:fd:61:eb:4f:4   UHLWI           0        1     lo0
192.168.1.161      88:a2:9e:3:73:3d   UHLWI           0      404     en1   1188
192.168.1.178      d0:3:df:b4:55:bc   UHLWI           0        9     en1    906
192.168.1.210      5c:e4:2a:fa:35:11  UHLWI           0        0     en1    741
192.168.1.226      fc:8c:11:bd:89:f   UHLWI           0       39     en1   1146
224.0.0/4          link#8             UmCS            2        0     en1
224.0.0.251        1:0:5e:0:0:fb      UHmLWI          0        0     en1
239.255.255.250    1:0:5e:7f:ff:fa    UHmLWI          0      249     en1
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
2603:6010:7c00:4328:6d73:7756:449d:ef44 90:fd:61:eb:4f:4                UHL             lo0
fd00:7437:5f96:ab30::/64                link#8                          UC              en1
fd00:7437:5f96:ab30:875:d974:fe52:baba  82:fd:9d:fc:70:24               UHLWI           en1
fd00:7437:5f96:ab30:1c37:5c46:ae31:64ce 90:fd:61:eb:4f:4                UHL             lo0
fd00:7437:5f96:ab30:592f:e2b6:9959:d8d  90:fd:61:eb:4f:4                UHL             lo0
fe80::%lo0/64                           fe80::1%lo0                     UcI             lo0
fe80::1%lo0                             link#1                          UHLI            lo0
fe80::%en1/64                           link#8                          UCI             en1
fe80::48c:9d60:dab4:6131%en1            90:fd:61:eb:4f:4                UHLI            lo0
fe80::18cb:685d:f9b8:681%en1            82:fd:9d:fc:70:24               UHLWI           en1
fe80::7637:5fff:fe96:ab30%en1           74:37:5f:96:ab:30               UHLWIir         en1
fe80::%awdl0/64                         link#10                         UCI           awdl0
fe80::ecc7:e9ff:fefe:390d%awdl0         ee:c7:e9:fe:39:d                UHLI            lo0
fe80::%utun0/64                         fe80::ea1d:3097:d6f5:d27d%utun0 UcI           utun0
fe80::ea1d:3097:d6f5:d27d%utun0         link#14                         UHLI            lo0
fe80::%utun1/64                         fe80::ab45:b3fd:5520:a1a4%utun1 UcI           utun1
fe80::ab45:b3fd:5520:a1a4%utun1         link#15                         UHLI            lo0
fe80::%utun2/64                         fe80::32cd:8f84:68ff:a68c%utun2 UcI           utun2
fe80::32cd:8f84:68ff:a68c%utun2         link#16                         UHLI            lo0
ff01::%lo0/32                           ::1                             UmCI            lo0
ff01::%en1/32                           link#8                          UmCI            en1
ff01::%awdl0/32                         link#10                         UmCI          awdl0
ff01::%utun0/32                         fe80::ea1d:3097:d6f5:d27d%utun0 UmCI          utun0
ff01::%utun1/32                         fe80::ab45:b3fd:5520:a1a4%utun1 UmCI          utun1
ff01::%utun2/32                         fe80::32cd:8f84:68ff:a68c%utun2 UmCI          utun2
ff02::%lo0/32                           ::1                             UmCI            lo0
ff02::%en1/32                           link#8                          UmCI            en1
ff02::%awdl0/32                         link#10                         UmCI          awdl0
ff02::%utun0/32                         fe80::ea1d:3097:d6f5:d27d%utun0 UmCI          utun0
ff02::%utun1/32                         fe80::ab45:b3fd:5520:a1a4%utun1 UmCI          utun1
ff02::%utun2/32                         fe80::32cd:8f84:68ff:a68c%utun2 UmCI          utun2
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
64 bytes from 1.1.1.1: icmp_seq=0 ttl=55 time=26.990 ms
64 bytes from 1.1.1.1: icmp_seq=1 ttl=55 time=25.710 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=55 time=26.347 ms
64 bytes from 1.1.1.1: icmp_seq=3 ttl=55 time=28.886 ms

--- 1.1.1.1 ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 25.710/26.983/28.886/1.188 ms
```

### `traceroute -n 1.1.1.1`

```text
1  192.168.1.1  2.819 ms  1.918 ms  1.149 ms
 2  142.254.144.25  6.760 ms  10.823 ms  7.776 ms
 3  65.29.26.254  15.293 ms  10.759 ms  11.654 ms
 4  65.29.39.71  13.988 ms  8.559 ms  8.969 ms
 5  65.29.31.26  10.558 ms  8.790 ms  10.400 ms
 6  65.189.140.162  26.771 ms  24.984 ms  26.660 ms
 7  65.29.33.229  22.933 ms  22.330 ms  23.092 ms
 8  172.69.174.2  25.172 ms  26.361 ms  25.174 ms
 9  172.68.168.9  25.779 ms
    172.69.174.1  38.192 ms  33.632 ms
10  1.1.1.1  30.027 ms  34.393 ms  29.540 ms

[stderr]
traceroute to 1.1.1.1 (1.1.1.1), 64 hops max, 52 byte packets
```

### `netstat -anv`

```text
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)     rhiwat shiwat    pid   epid
tcp4       0      0  192.168.1.98.51741     140.82.112.22.443      ESTABLISHED 131072 132432    704      0
tcp4       0      0  192.168.1.98.51740     130.211.26.229.443     ESTABLISHED 131072 131600    704      0
tcp4       0      0  192.168.1.98.51739     162.247.243.29.443     ESTABLISHED 131072 131480    704      0
tcp4       0      0  192.168.1.98.51738     140.82.114.26.443      ESTABLISHED 131072 132432    704      0
tcp6       0      0  2603:6010:7c00:4.51737 2606:50c0:8003::.443   ESTABLISHED 131072 132308    704      0
tcp4       0      0  192.168.1.98.51736     185.199.110.154.443    ESTABLISHED 131072 131480    704      0
tcp4       0      0  192.168.1.98.51735     185.199.110.154.443    ESTABLISHED 131072 131480    704      0
tcp4       0      0  192.168.1.98.51715     162.247.243.29.443     ESTABLISHED 131072 131480    704      0
tcp6       0      0  2603:6010:7c00:4.51529 2a06:98c1:3108::.443   ESTABLISHED 131072 132104    704      0
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
tcp6       0      0  2603:6010:7c00:4.51744 2603:1036:2403:1.443   TIME_WAIT   131072 131860   6906      0
tcp4       0      0  192.168.1.98.51745     1.1.1.1.443            TIME_WAIT   131768 131768  28786      0
tcp4       0      0  192.168.1.98.51746     1.1.1.1.53             TIME_WAIT   131768 131768  28786      0
udp6       0      0  2603:6010:7c00:4.50386 2a06:98c1:3100::.443               1048576  29040    704      0
udp6       0      0  2603:6010:7c00:4.56112 2a06:98c1:3100::.443               1048576  29040    704      0
udp4       0      0  *.65115                *.*                                196724   9216     56      0
udp6       0      0  *.58852                *.*                                196724   9216    187      0
udp4       0      0  *.58852                *.*                                196724   9216    187      0
udp6       0      0  *.60502                *.*                                196724   9216    187      0
udp4       0      0  *.60502                *.*                                196724   9216    187      0
udp6       0      0  *.49868                *.*                                196724   9216    187      0
udp4       0      0  *.49868                *.*                                196724   9216    187      0
udp6       0      0  *.64184                *.*                                196724   9216    187      0
udp4       0      0  *.64184                *.*                                196724   9216    187      0
udp6       0      0  *.62431                *.*                                196724   9216    187      0
udp4       0      0  *.62431                *.*                                196724   9216    187      0
udp6       0      0  *.55934                *.*                                196724   9216    187      0
udp4       0      0  *.55934                *.*                                196724   9216    187      0
udp4       0      0  *.*                    *.*                                196724   9216    401      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp4       0      0  *.5353                 *.*                                196724   9216    704      0
udp4       0      0  *.*                    *.*                                196724   9216    335      0
udp4       0      0  *.*                    *.*                                196724   9216    341      0
udp4       0      0  *.*                    *.*                                196724   9216    110      0
udp4       0      0  *.*                    *.*                                196724   9216    965      0
udp4       0      0  *.*                    *.*                                196724   9216    363      0
udp4       0      0  *.*                    *.*                                196724   9216    209      0
udp4       0      0  *.*                    *.*                                196724   9216    685      0
udp4       0      0  *.*                    *.*                                196724   9216    781      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp46      0      0  *.5353                 *.*                                196724   9216    704      0
udp4       0      0  *.5353                 *.*                                196724   9216    704      0
udp4       0      0  *.*                    *.*                                196724   9216    367      0
udp4       0      0  *.*                    *.*                                196724   9216    360      0
udp4       0      0  *.*                    *.*                                196724   9216    341      0
udp4       0      0  *.50903                *.*                                196724   9216    341      0
udp4       0      0  *.*                    *.*                                196724   9216    341      0
udp4       0      0  *.*                    *.*                                196724   9216    341      0
udp4       0      0  *.*                    *.*                                196724   9216    117      0
udp4       0      0  *.*                    *.*                                196724   9216    367      0
udp4       0      0  *.*                    *.*                                196724   9216    367      0
udp4       0      0  *.*                    *.*                                196724   9216    367      0
udp4       0      0  *.*                    *.*                                196724   9216    367      0
udp4       0      0  *.*                    *.*                                196724   9216    357      0
udp4       0      0  *.*                    *.*                                196724   9216    326      0
udp4       0      0  *.*                    *.*                                196724   9216     69      0
udp4       0      0  *.*                    *.*                                196724   9216     69      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.88                   *.*                                196724   9216    106      0
udp6       0      0  *.88                   *.*                                196724   9216    106      0
udp4       0      0  *.*                    *.*                                196724   9216    100      0
udp4       0      0  *.*                    *.*                                196724   9216    149      0
udp46      0      0  *.*                    *.*                                196724   9216    149      0
udp4       0      0  *.*                    *.*                                196724   9216     66      0
udp6       0      0  *.5353                 *.*                                196724   9216    187      0
udp4       0      0  *.5353                 *.*                                196724   9216    187      0
udp4       0      0  *.*                    *.*                                196724   9216     69      0
udp4       0      0  *.*                    *.*                                196724   9216     69      0
udp4       0      0  *.*                    *.*                                196724   9216    117      0
udp4       0      0  *.138                  *.*                                196724   9216  25259      0
udp4       0      0  *.137                  *.*                                196724   9216  25259      0
Active Multipath Internet connections
Proto/ID  Flags      Local Address          Foreign Address        (state)    
Active LOCAL (UNIX) domain sockets
Address          Type   Recv-Q Send-Q            Inode             Conn             Refs          Nextref Addr
e9eaa142ca4aa99f stream      0      0                0 e9eaa142ca4ac1d7                0                0 /var/run/mDNSResponder
e9eaa142ca4ac1d7 stream      0      0                0 e9eaa142ca4aa99f                0                0
e9eaa142c6970237 stream      0      0                0 e9eaa142c696f297                0                0 /var/run/mDNSResponder
e9eaa142c696f297 stream      0      0                0 e9eaa142c6970237                0                0
e9eaa142c6971a6f stream      0      0                0 e9eaa142c696f1cf                0                0 /var/run/mDNSResponder
e9eaa142c696f1cf stream      0      0                0 e9eaa142c6971a6f                0                0
e9eaa142c696ede7 stream      0      0                0 e9eaa142c6971687                0                0 /var/run/mDNSResponder
e9eaa142c6971687 stream      0      0                0 e9eaa142c696ede7                0                0
e9eaa142e473f107 stream      0      0                0 e9eaa142e474061f                0                0 /var/run/mDNSResponder
e9eaa142e474061f stream      0      0                0 e9eaa142e473f107                0                0
e9eaa142e474110f stream      0      0                0 e9eaa142e4740f7f                0                0 /var/run/mDNSResponder
e9eaa142e4740f7f stream      0      0                0 e9eaa142e474110f                0                0
e9eaa142e473f5b7 stream      0      0                0 e9eaa142e4740c5f                0                0 /var/run/mDNSResponder
e9eaa142e4740c5f stream      0      0                0 e9eaa142e473f5b7                0                0
e9eaa142e4740eb7 stream      0      0                0 e9eaa142e473f99f                0                0 /var/run/mDNSResponder
e9eaa142e473f99f stream      0      0                0 e9eaa142e4740eb7                0                0
e9eaa142e4740d27 stream      0      0                0                0                0                0
e9eaa142c696f5b7 stream      0      0                0 e9eaa142c696f67f                0                0 /var/run/mDNSResponder
e9eaa142c696f67f stream      0      0                0 e9eaa142c696f5b7                0                0
e9eaa142c696f99f stream      0      0                0 e9eaa142c697129f                0                0 /var/run/mDNSResponder
e9eaa142c697129f stream      0      0                0 e9eaa142c696f99f                0                0
e9eaa142c696fb2f stream      0      0                0 e9eaa142c697110f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c697110f stream      0      0                0 e9eaa142c696fb2f                0                0
e9eaa142c696fbf7 stream      0      0                0 e9eaa142c696fcbf                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c696fcbf stream      0      0                0 e9eaa142c696fbf7                0                0
e9eaa142c696ff17 stream      0      0                0 e9eaa142c696ffdf                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c696ffdf stream      0      0                0 e9eaa142c696ff17                0                0
e9eaa142c69700a7 stream      0      0                0 e9eaa142c6970f7f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c6970f7f stream      0      0                0 e9eaa142c69700a7                0                0
e9eaa142c6970eb7 stream      0      0                0 e9eaa142c6970d27                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c6970d27 stream      0      0                0 e9eaa142c6970eb7                0                0
e9eaa142c69702ff stream      0      0                0 e9eaa142c6970acf                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c6970acf stream      0      0                0 e9eaa142c69702ff                0                0
e9eaa142c69706e7 stream      0      0                0 e9eaa142c697048f                0                0 /var/run/usbmuxd
e9eaa142c697048f stream      0      0                0 e9eaa142c69706e7                0                0
e9eaa142c696ef77 stream      0      0                0 e9eaa142c696eeaf                0                0 /var/run/usbmuxd
e9eaa142c696eeaf stream      0      0                0 e9eaa142c696ef77                0                0
e9eaa142c185d5bf stream      0      0                0 e9eaa142c185d42f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c185d42f stream      0      0                0 e9eaa142c185d5bf                0                0
e9eaa142c697993f stream      0      0                0 e9eaa142c6979237                0                0 /var/run/mDNSResponder
e9eaa142c6979237 stream      0      0                0 e9eaa142c697993f                0                0
e9eaa142c185d10f stream      0      0                0 e9eaa142c185db37                0                0 /var/run/usbmuxd
e9eaa142c185db37 stream      0      0                0 e9eaa142c185d10f                0                0
e9eaa142c697916f stream      0      0                0 e9eaa142c6979b97                0                0 /var/run/usbmuxd
e9eaa142c6979b97 stream      0      0                0 e9eaa142c697916f                0                0
e9eaa142c6979a07 stream      0      0                0 e9eaa142c697948f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c697948f stream      0      0                0 e9eaa142c6979a07                0                0
e9eaa142c69792ff stream      0      0                0 e9eaa142c69793c7                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c69793c7 stream      0      0                0 e9eaa142c69792ff                0                0
e9eaa142c69797af stream      0      0                0 e9eaa142c69796e7                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c69796e7 stream      0      0                0 e9eaa142c69797af                0                0
e9eaa142c6979557 stream      0      0                0 e9eaa142c697961f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c697961f stream      0      0                0 e9eaa142c6979557                0                0
e9eaa142c185ade7 stream      0      0                0 e9eaa142c185ad1f                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c185ad1f stream      0      0                0 e9eaa142c185ade7                0                0
e9eaa142c185af77 stream      0      0                0 e9eaa142c185b107                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c185b107 stream      0      0                0 e9eaa142c185af77                0                0
e9eaa142c185da6f stream      0      0                0 e9eaa142c185d9a7                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c185d9a7 stream      0      0                0 e9eaa142c185da6f                0                0
e9eaa142c185b03f stream      0      0                0 e9eaa142c185d817                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c185d817 stream      0      0                0 e9eaa142c185b03f                0                0
e9eaa142c185aeaf stream      0      0                0 e9eaa142c185d8df                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c185d8df stream      0      0                0 e9eaa142c185aeaf                0                0
e9eaa142c185b1cf stream      0      0 e9eaa142d3353557                0                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-djinfamousone
e9eaa142c185b35f stream      0      0                0 e9eaa142c185d74f                0                0 /var/run/mDNSResponder
e9eaa142c185d74f stream      0      0                0 e9eaa142c185b35f                0                0
e9eaa142c185bb2f stream      0      0                0 e9eaa142ca4a9d1f                0                0 /var/run/mDNSResponder
e9eaa142ca4a9d1f stream      0      0                0 e9eaa142c185bb2f                0                0
e9eaa142ca4a9de7 stream      0      0                0 e9eaa142ca4a9eaf                0                0 /var/run/mDNSResponder
e9eaa142ca4a9eaf stream      0      0                0 e9eaa142ca4a9de7                0                0
e9eaa142ca4acbff stream      0      0                0 e9eaa142ca4a9f77                0                0 /var/run/mDNSResponder
e9eaa142ca4a9f77 stream      0      0                0 e9eaa142ca4acbff                0                0
e9eaa142ca4acb37 stream      0      0                0 e9eaa142ca4aa03f                0                0 /var/run/mDNSResponder
e9eaa142ca4aa03f stream      0      0                0 e9eaa142ca4acb37                0                0
e9eaa142ca4aa107 stream      0      0                0 e9eaa142ca4aa1cf                0                0 /var/run/mDNSResponder
e9eaa142ca4aa1cf stream      0      0                0 e9eaa142ca4aa107                0                0
e9eaa142ca4aa297 stream      0      0                0 e9eaa142ca4aa35f                0                0 /var/run/mDNSResponder
e9eaa142ca4aa35f stream      0      0                0 e9eaa142ca4aa297                0                0
e9eaa142ca4aa427 stream      0      0                0 e9eaa142ca4aacbf                0                0 /var/run/mDNSResponder
e9eaa142ca4aca6f stream      0      0                0 e9eaa142ca4aa80f                0                0 /var/run/mDNSResponder
e9eaa142ca4aacbf stream      0      0                0 e9eaa142ca4aa427                0                0
e9eaa142ca4aa80f stream      0      0                0 e9eaa142ca4aca6f                0                0
e9eaa142ca4aab2f stream      0      0                0 e9eaa142ca4ac687                0                0 /var/run/mDNSResponder
e9eaa142ca4ac687 stream      0      0                0 e9eaa142ca4aab2f                0                0
e9eaa142ca4aafdf stream      0      0                0 e9eaa142ca4ac5bf                0                0 /var/run/mDNSResponder
e9eaa142ca4ac5bf stream      0      0                0 e9eaa142ca4aafdf                0                0
e9eaa142ca4ac367 stream      0      0                0 e9eaa142ca4ab237                0                0 /var/run/mDNSResponder
e9eaa142ca4ab237 stream      0      0                0 e9eaa142ca4ac367                0                0
e9eaa142ca4ab16f stream      0      0 e9eaa142cc90a367                0                0                0 /var/folders/2h/2sdhtx6d6nzc_dw1t79xjd6w0000gn/T/.com.google.Chrome.7fBeOG/SingletonSocket
e9eaa142ca4ab2ff stream      0      0                0 e9eaa142ca4ab3c7                0                0 /var/run/mDNSResponder
e9eaa142ca4ab3c7 stream      0      0                0 e9eaa142ca4ab2ff                0                0
e9eaa142ca4ac10f stream      0      0                0 e9eaa142ca4ab61f                0                0 /var/run/mDNSResponder
e9eaa142ca4ab61f stream      0      0                0 e9eaa142ca4ac10f                0                0
e9eaa142ca4ab7af stream      0      0                0 e9eaa142ca4ab877                0                0
e9eaa142ca4ab877 stream      0      0                0 e9eaa142ca4ab7af                0                0
e9eaa142ca4ab93f stream      0      0                0 e9eaa142ca4abacf                0                0
e9eaa142ca4abacf stream      0      0                0 e9eaa142ca4ab93f                0                0
e9eaa142ca4abb97 stream      0      0                0 e9eaa142ca4aba07                0                0
e9eaa142ca4aba07 stream      0      0                0 e9eaa142ca4abb97                0                0
e9eaa142ca4abf7f stream      0      0                0 e9eaa142ca4abeb7                0                0
e9eaa142ca4abeb7 stream      0      0                0 e9eaa142ca4abf7f                0                0
e9eaa142ca4abd27 stream      0      0                0 e9eaa142ca4abc5f                0                0 /var/run/mDNSResponder
e9eaa142ca4abc5f stream      0      0                0 e9eaa142ca4abd27                0                0
e9eaa142c697a4f7 stream      0      0                0 e9eaa142c6978107                0                0 /var/run/mDNSResponder
e9eaa142c6978107 stream      0      0                0 e9eaa142c697a4f7                0                0
e9eaa142c697abff stream      0      0                0 e9eaa142c697ab37                0                0 /var/run/mDNSResponder
e9eaa142c697ab37 stream      0      0                0 e9eaa142c697abff                0                0
e9eaa142c6977d1f stream      0      0                0 e9eaa142c69785b7                0                0 /var/run/mDNSResponder
e9eaa142c69785b7 stream      0      0                0 e9eaa142c6977d1f                0                0
e9eaa142c6977de7 stream      0      0                0 e9eaa142c6978747                0                0 /var/run/mDNSResponder
e9eaa142c6978747 stream      0      0                0 e9eaa142c6977de7                0                0
e9eaa142c697880f stream      0      0                0 e9eaa142c697a367                0                0 /var/run/mDNSResponder
e9eaa142c697a367 stream      0      0                0 e9eaa142c697880f                0                0
e9eaa142c697a817 stream      0      0 e9eaa142c9eb32ef                0                0                0 /private/tmp/com.apple.launchd.fTBqLFQd2M/Listeners
e9eaa142c697867f stream      0      0 e9eaa142c9eb445f                0                0                0 /private/tmp/com.apple.launchd.FAxBDpfXrv/Render
e9eaa142c6979f7f stream      0      0 e9eaa142c8d96177                0                0                0 /var/tmp/filesystemui.socket
e9eaa142c697a10f stream      0      0                0 e9eaa142c69784ef                0                0 /var/run/mDNSResponder
e9eaa142c69784ef stream      0      0                0 e9eaa142c697a10f                0                0
e9eaa142c6978bf7 stream      0      0                0 e9eaa142c6978cbf                0                0 /var/run/mDNSResponder
e9eaa142c6978cbf stream      0      0                0 e9eaa142c6978bf7                0                0
e9eaa142c6979def stream      0      0                0 e9eaa142c6978d87                0                0 /var/run/mDNSResponder
e9eaa142c6978d87 stream      0      0                0 e9eaa142c6979def                0                0
e9eaa142c185b5b7 stream      0      0                0 e9eaa142c185d687                0                0 /var/run/mDNSResponder
e9eaa142c185d687 stream      0      0                0 e9eaa142c185b5b7                0                0
e9eaa142c185b747 stream      0      0                0 e9eaa142c185d4f7                0                0
e9eaa142c185d4f7 stream      0      0                0 e9eaa142c185b747                0                0
e9eaa142c185ba67 stream      0      0                0 e9eaa142c185d1d7                0                0 /var/run/mDNSResponder
e9eaa142c185d1d7 stream      0      0                0 e9eaa142c185ba67                0                0
e9eaa142c185d047 stream      0      0 e9eaa142c50aad97                0                0                0 /var/run/displaypolicyd/state
e9eaa142c185ceb7 stream      0      0 e9eaa142c4d73c9f                0                0                0 /var/run/pppconfd
e9eaa142c185be4f stream      0      0 e9eaa142c3b72e8f                0                0                0 /private/var/run/cupsd
e9eaa142c185cacf stream      0      0 e9eaa142c3b5b747                0                0                0 /var/run/usbmuxd
e9eaa142c185bf17 stream      0      0 e9eaa142c3b4cf0f                0                0                0 /var/run/systemkeychaincheck.socket
e9eaa142c185bfdf stream      0      0 e9eaa142c3b411f7                0                0                0 /var/run/portmap.socket
e9eaa142c185ca07 stream      0      0 e9eaa142c3b4207f                0                0                0 /var/run/vpncontrol.sock
e9eaa142c185c93f stream      0      0 e9eaa142c3b33d97                0                0                0 /var/rpc/ncalrpc/srvsvc
e9eaa142c185c0a7 stream      0      0 e9eaa142c3b33c9f                0                0                0 /var/rpc/ncacn_np/srvsvc
e9eaa142c185c16f stream      0      0 e9eaa142c3b21c1f                0                0                0 /var/rpc/ncalrpc/wkssvc
e9eaa142c185c877 stream      0      0 e9eaa142c3b21a2f                0                0                0 /var/rpc/ncacn_np/wkssvc
e9eaa142c185c7af stream      0      0 e9eaa142c3b21747                0                0                0 /var/rpc/ncalrpc/NETLOGON
e9eaa142c185c6e7 stream      0      0 e9eaa142c3b2164f                0                0                0 /var/rpc/ncacn_np/mdssvc
e9eaa142c185c61f stream      0      0 e9eaa142c3b200ff                0                0                0 /var/rpc/ncalrpc/lsarpc
e9eaa142c185c237 stream      0      0 e9eaa142c3b21557                0                0                0 /var/rpc/ncacn_np/lsarpc
e9eaa142c185c557 stream      0      0 e9eaa142c3b207c7                0                0                0 /var/run/mDNSResponder
e9eaa142c185c48f stream      0      0 e9eaa142c3aeb64f                0                0                0 /private/var/run/.sim_diagnosticd_socket
e9eaa142e473fcbf dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c69715bf
e9eaa142c69715bf dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c697142f
e9eaa142c697142f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142e473f427
e9eaa142e473fd87 dgram       0      0                0 e9eaa142e473f03f e9eaa142e473f03f                0
e9eaa142e473f03f dgram       0      0                0 e9eaa142e473fd87 e9eaa142e473fd87                0
e9eaa142e473f427 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142e47414f7
e9eaa142e47414f7 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142e474016f
e9eaa142e474016f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142e473f80f
e9eaa142e473f80f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142e4740557
e9eaa142e4740557 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142e473ff17
e9eaa142e473ff17 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c69714f7
e9eaa142c696f4ef dgram       0      0                0 e9eaa142c6971367 e9eaa142c6971367                0
e9eaa142c6971367 dgram       0      0                0 e9eaa142c696f4ef e9eaa142c696f4ef                0
e9eaa142c696f8d7 dgram       0      0                0 e9eaa142c696f747 e9eaa142c696f747                0
e9eaa142c696f747 dgram       0      0                0 e9eaa142c696f8d7 e9eaa142c696f8d7                0
e9eaa142c69714f7 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c696fe4f
e9eaa142c69711d7 dgram       0      0                0 e9eaa142c696fa67 e9eaa142c696fa67                0
e9eaa142c696fa67 dgram       0      0                0 e9eaa142c69711d7 e9eaa142c69711d7                0
e9eaa142c6971047 dgram       0      0                0 e9eaa142c696fd87 e9eaa142c696fd87                0
e9eaa142c696fd87 dgram       0      0                0 e9eaa142c6971047 e9eaa142c6971047                0
e9eaa142c696fe4f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c697016f
e9eaa142c697016f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6970c5f
e9eaa142c6970c5f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6979877
e9eaa142c697061f dgram       0      0                0 e9eaa142c69707af e9eaa142c69707af                0
e9eaa142c69707af dgram       0      0                0 e9eaa142c697061f e9eaa142c697061f                0
e9eaa142c6970877 dgram       0      0                0 e9eaa142c69703c7 e9eaa142c69703c7                0
e9eaa142c69703c7 dgram       0      0                0 e9eaa142c6970877 e9eaa142c6970877                0
e9eaa142c185dbff dgram       0      0                0 e9eaa142c69790a7 e9eaa142c69790a7                0
e9eaa142c69790a7 dgram       0      0                0 e9eaa142c185dbff e9eaa142c185dbff                0
e9eaa142c6979877 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6978a67
e9eaa142c6978a67 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c185b297
e9eaa142c185b297 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4aa4ef
e9eaa142ca4aa4ef dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4ac74f
e9eaa142ca4ac74f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4aa67f
e9eaa142ca4aa67f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4ac9a7
e9eaa142ca4ac9a7 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4aa747
e9eaa142ca4ac8df dgram       0      0                0 e9eaa142ca4aa5b7 e9eaa142ca4aa5b7                0
e9eaa142ca4aa5b7 dgram       0      0                0 e9eaa142ca4ac8df e9eaa142ca4ac8df                0
e9eaa142ca4aa747 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4aabf7
e9eaa142ca4aad87 dgram       0      0                0 e9eaa142ca4aae4f e9eaa142ca4aae4f                0
e9eaa142ca4aae4f dgram       0      0                0 e9eaa142ca4aad87 e9eaa142ca4aad87                0
e9eaa142ca4aabf7 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4aaf17
e9eaa142ca4aaf17 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4ac047
e9eaa142ca4ab48f dgram       0      0                0 e9eaa142ca4ac29f e9eaa142ca4ac29f                0
e9eaa142ca4ac29f dgram       0      0                0 e9eaa142ca4ab48f e9eaa142ca4ab48f                0
e9eaa142ca4ac047 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4ab557
e9eaa142ca4ab557 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4ab6e7
e9eaa142ca4ab6e7 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142ca4abdef
e9eaa142ca4abdef dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c697a047
e9eaa142c697a047 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c697a8df
e9eaa142c697a9a7 dgram       0      0                0 e9eaa142c697aa6f e9eaa142c697aa6f                0
e9eaa142c697aa6f dgram       0      0                0 e9eaa142c697a9a7 e9eaa142c697a9a7                0
e9eaa142c697a8df dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6978fdf
e9eaa142c6978fdf dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6979d27
e9eaa142c6979d27 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6978297
e9eaa142c697a42f dgram       0      0                0 e9eaa142c69781cf e9eaa142c69781cf                0
e9eaa142c69781cf dgram       0      0                0 e9eaa142c697a42f e9eaa142c697a42f                0
e9eaa142c6978297 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c697835f
e9eaa142c697835f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c697a1d7
e9eaa142c697a1d7 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6979eb7
e9eaa142c6979eb7 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6978e4f
e9eaa142c6977eaf dgram       0      0                0 e9eaa142c6978f17 e9eaa142c6978f17                0
e9eaa142c6978f17 dgram       0      0                0 e9eaa142c6977eaf e9eaa142c6977eaf                0
e9eaa142c6978e4f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c697803f
e9eaa142c697a5bf dgram       0      0                0 e9eaa142c6977f77 e9eaa142c6977f77                0
e9eaa142c6977f77 dgram       0      0                0 e9eaa142c697a5bf e9eaa142c697a5bf                0
e9eaa142c697a74f dgram       0      0                0 e9eaa142c697a687 e9eaa142c697a687                0
e9eaa142c697a687 dgram       0      0                0 e9eaa142c697a74f e9eaa142c697a74f                0
e9eaa142c697803f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c697a29f
e9eaa142c697a29f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c6978b2f
e9eaa142c6978b2f dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c185b8d7
e9eaa142c185b4ef dgram       0      0                0 e9eaa142c185b427 e9eaa142c185b427                0
e9eaa142c185b427 dgram       0      0                0 e9eaa142c185b4ef e9eaa142c185b4ef                0
e9eaa142c185b80f dgram       0      0                0 e9eaa142c185b67f e9eaa142c185b67f                0
e9eaa142c185b67f dgram       0      0                0 e9eaa142c185b80f e9eaa142c185b80f                0
e9eaa142c185b8d7 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c185bcbf
e9eaa142c185d29f dgram       0      0                0 e9eaa142c185cdef e9eaa142c185cdef                0
e9eaa142c185cdef dgram       0      0                0 e9eaa142c185d29f e9eaa142c185d29f                0
e9eaa142c185b99f dgram       0      0                0 e9eaa142c185d367 e9eaa142c185d367                0
e9eaa142c185d367 dgram       0      0                0 e9eaa142c185b99f e9eaa142c185b99f                0
e9eaa142c185bbf7 dgram       0      0                0 e9eaa142c185cf7f e9eaa142c185cf7f                0
e9eaa142c185cf7f dgram       0      0                0 e9eaa142c185bbf7 e9eaa142c185bbf7                0
e9eaa142c185bcbf dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c185cd27
e9eaa142c185cd27 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c185bd87
e9eaa142c185bd87 dgram       0      0                0 e9eaa142c185c3c7                0 e9eaa142c185c2ff
e9eaa142c185cc5f dgram       0      0                0 e9eaa142c185cb97 e9eaa142c185cb97                0
e9eaa142c185cb97 dgram       0      0                0 e9eaa142c185cc5f e9eaa142c185cc5f                0
e9eaa142c185c2ff dgram       0      0                0 e9eaa142c185c3c7                0                0
e9eaa142c185c3c7 dgram       0      0 e9eaa142c18400ff                0 e9eaa142e473fcbf                0 /private//var/run/syslog
Registered kernel control modules
id       flags    pcbcount rcvbuf   sndbuf   name 
       1        9        0   131072   131072 com.apple.flow-divert 
       2        1        1    16384     2048 com.apple.nke.sockwall 
       3        9        0   524288   524288 com.apple.content-filter 
       4        1        0    65536    65536 com.apple.net.necp_control 
       5        1       12    65536    65536 com.apple.net.netagent 
       6        9        3   524288   524288 com.apple.net.utun_control 
       7        1        0    65536    65536 com.apple.net.ipsec_control 
       8        0       52     8192     2048 com.apple.netsrc 
       9       18        4     8192     2048 com.apple.network.statistics 
       a        5        0     8192     2048 com.apple.network.tcp_ccdebug 
       b        1        0     8192     2048 com.apple.network.advisory 
Active kernel event sockets
Proto Recv-Q Send-Q vendor  class subclarhiwat shiwat    pid   epid
kevt       0      0      1      6      1 32768   4096    965      0
kevt       0      0      1      1      2 32768   4096    117      0
kevt       0      0      1      6      1 32768   4096    117      0
kevt       0      0      1      6      1 32768   4096    367      0
kevt       0      0      1      1     11 32768   4096    330      0
kevt       0      0      1      6      1 32768   4096    326      0
kevt       0      0      1      6      1 32768   4096     69      0
kevt       0      0      1      6      1 32768   4096     69      0
kevt       0      0      1      6      1 32768   4096    149      0
kevt       0      0      1      6      1 32768   4096    149      0
kevt       0      0      1      6      1 32768   4096    149      0
kevt       0      0      1      6      1 32768   4096    149      0
kevt       0      0      1      6      1 32768   4096    149      0
kevt       0      0      1      1      7 32768   4096    209      0
kevt       0      0      1      1      1 32768   4096    209      0
kevt       0      0      1      1     10 32768   4096    198      0
kevt       0      0   1000      5     11 32768   4096    198      0
kevt       0      0      1      6      1 32768   4096    100      0
kevt       0      0      1      1      2 32768   4096    149      0
kevt       0      0      1      1      2 32768   4096    187      0
kevt       0      0      1      3      3 32768   4096     57      0
kevt       0      0      1      6      1 32768   4096     69      0
kevt       0      0      1      1      0 32768   4096     69      0
Active kernel control sockets
Proto Recv-Q Send-Q rhiwat shiwat    pid   epid   unit     id name
kctl       0      0  16384   2048    198      0      1      2 com.apple.nke.sockwall
kctl       0      0  65536  65536     69      0      1      5 com.apple.net.netagent
kctl       0      0  65536  65536     69      0      2      5 com.apple.net.netagent
kctl       0      0  65536  65536     69      0      3      5 com.apple.net.netagent
kctl       0      0  65536  65536     69      0      4      5 com.apple.net.netagent
kctl       0      0  65536  65536     69      0      5      5 com.apple.net.netagent
kctl       0      0  65536  65536     69      0      6      5 com.apple.net.netagent
kctl       0      0  65536  65536     69      0      7      5 com.apple.net.netagent
kctl       0      0  65536  65536     69      0      8      5 com.apple.net.netagent
kctl       0      0  65536  65536    330      0      9      5 com.apple.net.netagent
kctl       0      0  65536  65536    330      0     10      5 com.apple.net.netagent
kctl       0      0  65536  65536    330      0     11      5 com.apple.net.netagent
kctl       0      0  65536  65536    360      0     12      5 com.apple.net.netagent
kctl       0      0 524288 524288    360      0      1      6 com.apple.net.utun_control
kctl       0      0 524288 524288    150      0      2      6 com.apple.net.utun_control
kctl       0      0 524288 524288    150      0      3      6 com.apple.net.utun_control
kctl       0      0 131072   2048      1      0      1      8 com.apple.netsrc
kctl       0      0 131072   2048    187      0      2      8 com.apple.netsrc
kctl       0      0 131072   2048     57      0      3      8 com.apple.netsrc
kctl       0      0 131072   2048    346      0      4      8 com.apple.netsrc
kctl       0      0 131072   2048    196      0      5      8 com.apple.netsrc
kctl       0      0 131072   2048     94      0      6      8 com.apple.netsrc
kctl       0      0 131072   2048    297      0      7      8 com.apple.netsrc
kctl       0      0 131072   2048    195      0      8      8 com.apple.netsrc
kctl       0      0 131072   2048     95      0      9      8 com.apple.netsrc
kctl       0      0 131072   2048    189      0     10      8 com.apple.netsrc
kctl       0      0 131072   2048    868      0     11      8 com.apple.netsrc
kctl       0      0 131072   2048    149      0     12      8 com.apple.netsrc
kctl       0      0 131072   2048    148      0     13      8 com.apple.netsrc
kctl       0      0 131072   2048    341      0     14      8 com.apple.netsrc
kctl       0      0 131072   2048    326      0     15      8 com.apple.netsrc
kctl       0      0 131072   2048    683      0     16      8 com.apple.netsrc
kctl       0      0 131072   2048   6906      0     17      8 com.apple.netsrc
kctl       0      0 131072   2048    387      0     18      8 com.apple.netsrc
kctl       0      0 131072   2048    690      0     19      8 com.apple.netsrc
kctl       0      0 131072   2048    709      0     20      8 com.apple.netsrc
kctl       0      0 131072   2048    704      0     21      8 com.apple.netsrc
kctl       0      0 131072   2048    367      0     22      8 com.apple.netsrc
kctl       0      0 131072   2048    371      0     23      8 com.apple.netsrc
kctl       0      0 131072   2048    695      0     24      8 com.apple.netsrc
kctl       0      0 131072   2048    332      0     25      8 com.apple.netsrc
kctl       0      0 131072   2048    372      0     26      8 com.apple.netsrc
kctl       0      0 131072   2048    345      0     27      8 com.apple.netsrc
kctl       0      0 131072   2048    362      0     28      8 com.apple.netsrc
kctl       0      0 131072   2048    360      0     29      8 com.apple.netsrc
kctl       0      0 131072   2048    400      0     30      8 com.apple.netsrc
kctl       0      0 131072   2048    370      0     31      8 com.apple.netsrc
kctl       0      0 131072   2048    379      0     32      8 com.apple.netsrc
kctl       0      0 131072   2048   1337      0     33      8 com.apple.netsrc
kctl       0      0 131072   2048    781      0     34      8 com.apple.netsrc
kctl       0      0 131072   2048    791      0     35      8 com.apple.netsrc
kctl       0      0 131072   2048    798      0     36      8 com.apple.netsrc
kctl       0      0 131072   2048    368      0     37      8 com.apple.netsrc
kctl       0      0 131072   2048    904      0     38      8 com.apple.netsrc
kctl       0      0 131072   2048    848      0     39      8 com.apple.netsrc
kctl       0      0 131072   2048    680      0     40      8 com.apple.netsrc
kctl       0      0 131072   2048    829      0     41      8 com.apple.netsrc
kctl       0      0 131072   2048    840      0     42      8 com.apple.netsrc
kctl       0      0 131072   2048    782      0     43      8 com.apple.netsrc
kctl       0      0 131072   2048    918      0     44      8 com.apple.netsrc
kctl       0      0 131072   2048    877      0     45      8 com.apple.netsrc
kctl       0      0 131072   2048    890      0     46      8 com.apple.netsrc
kctl       0      0 131072   2048    771      0     47      8 com.apple.netsrc
kctl       0      0 131072   2048    939      0     48      8 com.apple.netsrc
kctl       0      0 131072   2048    363      0     49      8 com.apple.netsrc
kctl       0      0 131072   2048    906      0     50      8 com.apple.netsrc
kctl       0      0 131072   2048    799      0     51      8 com.apple.netsrc
kctl       0      0 131072   2048  28786      0     52      8 com.apple.netsrc
kctl       0      0 131072   2048    209      0      1      9 com.apple.network.statistics
kctl       0      0 131072   2048    209      0      2      9 com.apple.network.statistics
kctl       0      0 131072   2048    209      0      3      9 com.apple.network.statistics
kctl       0      0 131072   2048    209      0      4      9 com.apple.network.statistics
```
