## Section IP Switching (AEiE0905)

## 📖 1. Introduction
IP Switching represents a significant evolution in networking, aiming to combine the speed and predictability of ATM (Asynchronous Transfer Mode) switching with the ubiquity and flexibility of IP routing. Traditional routers examine every IP packet header to make routing decisions, which can be slow and computationally intensive. IP Switching techniques identify flows of packets and switch them directly at the hardware layer, bypassing the slower routing software. This section covers Ipsilon IP switching, flow classification, IP service models, and the structure of IP protocols.

## 2. Ipsilon IP Switching
Ipsilon Networks originally pioneered IP switching. The core concept of Ipsilon IP switching is to identify long-lasting flows of IP packets and dynamically establish a switched path (originally over ATM hardware) for these flows, while routing short-lived packets normally.

### Operation Principles
1. **Default Routing**: All packets are initially handled by a standard IP router running routing protocols (like OSPF or BGP).
2. **Flow Identification**: The IP switch monitors the traffic to identify "flows" — sequences of packets sharing the same source/destination addresses, ports, and protocol.
3. **Cut-Through Switching**: Once a flow is recognized as long-lasting or high-volume (e.g., FTP, Video streaming), the switch dynamically establishes a direct hardware path (a Virtual Channel) for subsequent packets in that flow.
4. **Bypassing the Router**: Subsequent packets belonging to the flow bypass the router's software processing and are switched directly by the hardware, significantly reducing latency and increasing throughput.

> [!NOTE] Definition
> **Flow**: A sequence of packets sent from a particular source to a particular destination that are related and require similar treatment by the network.

## 🏷️ 3. Flow Classification
Flow classification is the process of categorizing network traffic into different flows based on certain criteria. It is essential for QoS (Quality of Service) and IP switching.

### Criteria for Classification
Flows are typically classified using a combination of header fields, often referred to as a "5-tuple":
1. Source IP Address
2. Destination IP Address
3. Source Port Number
4. Destination Port Number
5. Protocol ID (e.g., TCP, UDP)

### Types of Flows
- **Short-lived flows (Mice)**: Web requests, DNS queries. These are typically routed hop-by-hop.
- **Long-lived flows (Elephants)**: File transfers, video streams. These are candidates for IP switching (cut-through switching).

## 4. IP Service Model
The Internet Protocol (IP) provides a specific service model to upper layers:
1. **Connectionless**: No setup is required before sending data.
2. **Best-Effort Delivery**: The network tries its best to deliver packets, but provides no guarantees against loss, delay, or out-of-order delivery.
3. **Datagram Service**: Each packet is treated independently.

This simple service model is a key reason for the Internet's scalability, but it shifts the burden of reliability and sequencing to higher-layer protocols like TCP.

## 5. Layering in the IP Protocols
The TCP/IP protocol suite follows a layered architecture, typically represented in four layers:

1. **Application Layer**: User-facing protocols (HTTP, FTP, SMTP).
2. **Transport Layer**: End-to-end communication and reliability (TCP, UDP).
3. **Internet Layer (IP)**: Logical addressing and routing (IP, ICMP).
4. **Network Access Layer**: Physical transmission over specific media (Ethernet, Wi-Fi).

```text
TCP/IP Layering Model:
+---------------------+
|  Application Layer  |
+---------------------+
|   Transport Layer   |
+---------------------+
|    Internet Layer   |
+---------------------+
| Network Access Layer|
+---------------------+
```

## 6. IP Packet Structure and Header
An IP datagram consists of a header and a data payload. The header contains all the necessary information for routing the packet.

### IPv4 Header Format
The standard IPv4 header is 20 bytes long (without options).

```text
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |         Header Checksum       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### Key Header Fields Explained
- **Version (4 bits)**: Indicates the IP version (4 for IPv4).
- **IHL (Internet Header Length) (4 bits)**: Length of the header in 32-bit words. Minimum value is 5 (5 x 4 = 20 bytes).
- **Type of Service (TOS) (8 bits)**: Used for QoS, indicates priority and desired treatment.
- **Total Length (16 bits)**: Total length of the IP datagram (header + data) in bytes. Max is $2^{16}-1 = 65,535$ bytes.
- **Identification, Flags, Fragment Offset**: Used for fragmentation and reassembly of packets.
- **TTL (Time to Live) (8 bits)**: Decremented by each router. If it reaches 0, the packet is discarded (prevents infinite loops).
- **Protocol (8 bits)**: Indicates the upper-layer protocol (e.g., TCP=6, UDP=17, ICMP=1).
- **Header Checksum (16 bits)**: Error-checking for the header only.
- **Source & Destination Addresses (32 bits each)**: Logical IP addresses.

> [!TIP]
> **Exam Tip**: Memorize the sizes of key fields. TTL is 8 bits, Total Length is 16 bits, and IP addresses are 32 bits. Also, remember that the Header Checksum only checks the header, not the data payload.

## 💡 Common Mistakes / Exam Tips
- **Confusing IP switching with standard routing**: Standard routing processes every packet header in software; IP switching dynamically establishes a hardware path for a sequence of related packets (a flow).
- **IHL value**: The IHL field represents the length in 32-bit words. If the header is 20 bytes, IHL = 5. Do not write 20.
- **Fragmentation**: IP fragmentation happens at routers when the packet size exceeds the MTU of the outgoing link, but reassembly only happens at the final destination, not at intermediate routers.

## 📝 Quick Reference / Formula Summary
- Header size without options = 20 bytes.
- Max IPv4 packet size = $65,535$ bytes.
- Payload Length = Total Length - (IHL $\times$ 4)
- Flow 5-tuple: Protocol, Src IP, Dst IP, Src Port, Dst Port.

## ✏️ Practice Problems

**Problem 1**: An IPv4 packet arrives with the first 8 bits as `01000101` in binary. What is the version and the header length in bytes?
**Solution Sketch**:
- The first 4 bits represent the Version: `0100` = 4 (IPv4).
- The next 4 bits represent the IHL: `0101` = 5.
- Header length in bytes = IHL $\times$ 4 = $5 \times 4 = 20$ bytes.

**Problem 2**: A packet has a Total Length field value of $1500$ and an IHL field value of $5$. What is the size of the data payload being carried by the IP packet?
**Solution Sketch**:
- Header length = $5 \times 4 = 20$ bytes.
- Total length = $1500$ bytes.
- Payload = Total Length - Header Length = $1500 - 20 = 1480$ bytes.

**Problem 3**: Explain the concept of "cut-through" in Ipsilon IP switching.
**Answer Sketch**: Cut-through refers to bypassing the traditional software-based routing engine. Once a flow of packets is identified, the switch maps the IP flow to an underlying hardware path (like ATM VC), allowing subsequent packets of that flow to be switched at wire-speed hardware rather than being individually routed.
</Section 9.5: IP Switching (AEiE0905)>
