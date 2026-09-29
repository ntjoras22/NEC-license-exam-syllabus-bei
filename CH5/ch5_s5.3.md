## Section Network Layer (ACtE0503)


## 📖 1. Introduction
The Network Layer (OSI Layer 3) is responsible for host-to-host delivery of packets across multiple networks. While the Data Link Layer handles node-to-node delivery on the same local network, the Network Layer provides the logical addressing and routing mechanisms necessary to traverse complex internetworks.

## 💡 2. Basic Concept
The core function of the network layer is routing—determining the optimal path for a packet to travel from a source to a destination. The primary protocol functioning at this layer is the Internet Protocol (IP).

> [!NOTE] Definition
> **Datagram**: A self-contained, independent entity of data carrying sufficient information to be routed from the source to the destination computer without reliance on earlier exchanges.

## 3. Network Layer Services
- **Packetizing**: Encapsulating payload data into network-layer packets.
- **Routing**: Choosing the best path for packet delivery.
- **Forwarding**: Moving incoming packets to the appropriate outgoing interface.

### Packet Switching and Datagram Approach
The Internet primarily uses the **Datagram Approach** (connectionless packet switching). Each packet is treated independently. Route decisions are made per-packet based on routing tables, meaning packets from the same flow might take different paths and arrive out of order.

## 4. IPv4 Addressing and Subnetting
An IPv4 address is a 32-bit logical address, typically written in dotted-decimal notation (e.g., `192.168.1.10`).

### Classful Addressing
Historically, IPv4 addresses were divided into classes based on leading bits:
- **Class A**: 0... (1.0.0.0 to 126.255.255.255), Subnet mask `/8`
- **Class B**: 10... (128.0.0.0 to 191.255.255.255), Subnet mask `/16`
- **Class C**: 110... (192.0.0.0 to 223.255.255.255), Subnet mask `/24`
- **Class D**: 1110... (224.0.0.0 to 239.255.255.255) - Multicast
- **Class E**: 1111... (240.0.0.0 to 255.255.255.255) - Experimental

### Subnetting and CIDR (Classless Inter-Domain Routing)
Subnetting divides a large network block into smaller sub-networks by borrowing bits from the host portion. CIDR allows arbitrary length subnet masks, denoted by `/n` (e.g., `/26` means 26 bits for the network ID, 6 bits for the host ID).

- **Number of Hosts per Subnet**: $2^h - 2$ (where $h$ is the number of host bits). The `- 2` accounts for the network address (all 0s) and broadcast address (all 1s).
- **Number of Subnets**: $2^n$ (where $n$ is the number of borrowed bits).

**Example**:
Given block `192.168.1.0/24`, if we subnet to `/26`:
- We borrow 2 bits ($26 - 24 = 2$).
- Number of subnets = $2^2 = 4$.
- Number of host bits $h = 32 - 26 = 6$.
- Usable hosts per subnet = $2^6 - 2 = 64 - 2 = 62$.

## 5. Protocols at the Network Layer

### IP (Internet Protocol)
The core connectionless protocol responsible for logical addressing and routing.
- **Header length**: Minimum 20 bytes.
- Key fields include Source IP, Destination IP, Time to Live (TTL), and Protocol.

### ARP (Address Resolution Protocol)
Resolves a logical IPv4 address to a physical MAC address.
- When a host needs to send an IP packet on the LAN, it broadcasts an ARP Request: "Who has IP 192.168.1.5?" The target replies with its MAC address.

### ICMP (Internet Control Message Protocol)
Used for diagnostics and error reporting (e.g., `ping` uses ICMP Echo Request/Reply).
- It reports issues like "Destination Unreachable" or "Time Exceeded" (when TTL hits zero).

### IGMP (Internet Group Management Protocol)
Manages IPv4 multicast group memberships. Used by routers to learn which LAN hosts belong to which multicast groups.

## 6. Unicast, Multicast, and Routing Protocols

### Routing Concepts
- **Unicast**: One-to-one communication.
- **Multicast**: One-to-many communication (specifically to a subscribed group).
- **Broadcast**: One-to-all communication on a network segment.

### Interior vs. Exterior Routing Protocols
- **IGP (Interior Gateway Protocols)**: Route within an Autonomous System (AS).
  - **RIP (Routing Information Protocol)**: Distance-vector protocol. Uses hop count as the metric. Max hop count is 15. Slow convergence.
  - **OSPF (Open Shortest Path First)**: Link-state protocol. Uses Dijkstra's algorithm. Metric is based on bandwidth. Faster convergence and scalable.
- **EGP (Exterior Gateway Protocols)**: Route between Autonomous Systems.
  - **BGP (Border Gateway Protocol)**: Path-vector protocol. The core routing protocol of the global Internet. Determines paths based on network policies and AS paths.

| Feature | RIP | OSPF | BGP |
|---|---|---|---|
| Type | Distance Vector | Link State | Path Vector |
| Metric | Hop Count | Bandwidth (Cost) | Path Attributes |
| Scope | Small LANs / IGP | Large Enterprise / IGP | Global Internet / EGP |

## 7. IPv6
Designed to overcome the address exhaustion of IPv4.
- **Address Space**: 128 bits long, represented as 8 groups of 4 hexadecimal digits separated by colons (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
- **Header**: Fixed at 40 bytes. Removes checksum for faster processing.
- IPsec support is built-in.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not forget to subtract 2 when calculating the number of *usable hosts* per subnet ($2^h - 2$). However, do *not* subtract 2 when calculating the number of *subnets*.

> [!TIP]
> RIP uses hop count. OSPF uses link state / cost based on bandwidth. Memorize these metrics, as they are frequently tested!

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - **Usable hosts per subnet**: $2^{(32 - \text{prefix})} - 2$
> - **IPv4 address size**: 32 bits. **IPv6 address size**: 128 bits.
> - **ARP**: IP $\rightarrow$ MAC.

## ✏️ Practice Problems

1. **Problem**: An organization is assigned the block `172.16.0.0/16`. They want to create 100 subnets. What should the new subnet mask be?
   *Answer Sketch*: Find $n$ where $2^n \ge 100$. $2^7 = 128$. Borrow 7 bits. Old prefix was `/16`. New prefix is $16 + 7 = /23$. The subnet mask for `/23` is `255.255.254.0`.

2. **Problem**: Which protocol maps a logical IP address to a physical MAC address?
   *Answer Sketch*: Address Resolution Protocol (ARP).

3. **Problem**: Why is the TTL (Time to Live) field important in an IP packet?
   *Answer Sketch*: It prevents packets from looping endlessly in the network if there is a routing loop. It is decremented by 1 at each router hop.

</Section 5.3: Network Layer (ACtE0503)>
