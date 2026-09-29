## Section Transport Layer (ACtE0504)

## 📖 1. Introduction
The Transport Layer, layer 4 in the OSI model and layer 3 in the TCP/IP suite, is responsible for the logical communication between application processes running on different hosts. For the NEC exam, understanding the transport layer is crucial because it bridges the network layer (which provides host-to-host communication) and the application layer.

## 💡 2. Basic Concept
The primary role of the transport layer is to provide **process-to-process delivery**. While the network layer (IP) gets the data to the correct computer (host), the transport layer ensures it reaches the correct application program (process) on that computer using port numbers.

> [!NOTE] Definition
> **Process-to-Process Delivery**: The delivery of a packet, part of a message, from one process to another. A process is an application program running on a host.

Think of the network layer as delivering a letter to a specific house (the host), and the transport layer as delivering that letter to a specific person living inside the house (the process).

## 3. Transport Layer Services
The transport layer can offer several services to applications:

1.  **Process-to-Process Communication**: Using port numbers.
2.  **Addressing**: Multiplexing and demultiplexing.
3.  **Encapsulation and Decapsulation**: Adding transport headers (TCP/UDP).
4.  **Reliability**: Connection establishment, error control, flow control, and congestion control (provided by TCP, not UDP).

### 3.1 Port Numbers
To identify processes, transport layer protocols use port numbers. A port number is a 16-bit integer (ranging from 0 to 65535).
*   **Well-known ports (0-1023)**: Assigned and controlled by ICANN (e.g., HTTP=80, FTP=21, SSH=22).
*   **Registered ports (1024-49151)**: Not controlled by ICANN, but registered to prevent duplication.
*   **Dynamic/Private ports (49152-65535)**: Used as ephemeral (temporary) ports for clients.

## 4. UDP: User Datagram Protocol
UDP is a connectionless, unreliable transport protocol. It provides a bare-bones transport service.

*   **Characteristics**: Connectionless, unreliable, stateless, low overhead.
*   **Header Size**: 8 bytes.
*   **Fields**: Source Port (16 bits), Destination Port (16 bits), Length (16 bits), Checksum (16 bits).
*   **Use Cases**: DNS, SNMP, multimedia applications (VoIP, streaming), where speed is more critical than reliability.

> [!IMPORTANT]
> The UDP length field includes both the UDP header and the UDP data. Minimum value is 8 (header only).

## 5. TCP: Transmission Control Protocol
TCP is a connection-oriented, reliable, and in-order byte-stream service.

*   **Characteristics**: Connection-oriented, reliable, flow control, congestion control, full-duplex.
*   **Header Size**: 20 bytes (minimum) to 60 bytes (maximum with options).

### 5.1 Three-Way Handshake
TCP uses a 3-way handshake to establish a connection before data transfer.
1.  **SYN**: Client sends a SYN segment with an initial sequence number (ISN).
2.  **SYN-ACK**: Server receives SYN, allocates buffers/variables, and replies with SYN-ACK, acknowledging the client's ISN and providing its own ISN.
3.  **ACK**: Client acknowledges the server's ISN. Data can be piggybacked here.

### 5.2 Flow Control
Flow control prevents a fast sender from overwhelming a slow receiver. TCP uses a **sliding window** mechanism.
*   **Receive Window (rwnd)**: The receiver advertises its available buffer space in every ACK segment.
*   The sender must ensure: $LastByteSent - LastByteAcked \le rwnd$

### 5.3 Congestion Control
Congestion control prevents the sender from overwhelming the network. TCP uses a congestion window (**cwnd**) maintained by the sender.
TCP congestion control phases:
1.  **Slow Start**: `cwnd` grows exponentially (doubles every RTT) until it reaches `ssthresh` (slow start threshold).
2.  **Congestion Avoidance**: `cwnd` grows linearly (adds 1 MSS per RTT) when `cwnd >= ssthresh`.
3.  **Congestion Detection**:
    *   *Timeout*: Severe congestion. `ssthresh` = $cwnd/2$, `cwnd` = 1 MSS. Back to Slow Start.
    *   *3 Duplicate ACKs*: Moderate congestion. `ssthresh` = $cwnd/2$, `cwnd` = `ssthresh` + 3 (Fast Recovery).

### 5.4 Error Control
TCP provides reliability through:
*   **Checksum**: Detects corrupted segments.
*   **Acknowledgments (ACKs)**: Cumulative ACKs confirm receipt of bytes.
*   **Retransmission**: If a timer expires (Timeout) or 3 duplicate ACKs are received, the unacknowledged segment is retransmitted.

### Comparison: TCP vs. UDP

| Feature | TCP | UDP |
| :--- | :--- | :--- |
| **Connection** | Connection-oriented | Connectionless |
| **Reliability** | Reliable | Unreliable |
| **Overhead** | High (20+ bytes) | Low (8 bytes) |
| **Ordering** | In-order delivery | Out-of-order possible |
| **Flow/Congestion Control** | Yes | No |
| **Examples** | HTTP, FTP, SMTP | DNS, DHCP, VoIP |

## 6. Quality of Service (QoS)
QoS is an internetworking issue that discusses how to define and guarantee a certain level of performance for a data flow.

### 6.1 Flow Characteristics
*   **Reliability**: Lack of dropped packets.
*   **Delay**: Time from source to destination.
*   **Jitter**: Variation in delay for packets belonging to the same flow. Crucial for real-time audio/video.
*   **Bandwidth**: Required data rate.

### 6.2 Techniques to Improve QoS
1.  **Scheduling**: FIFO, Priority Queuing, Weighted Fair Queuing (WFQ).
2.  **Traffic Shaping**: Controlling the rate of data leaving a node.
    *   **Leaky Bucket**: Smooths out bursty traffic into a steady stream. Constant output rate.
    *   **Token Bucket**: Allows bursty traffic up to a maximum size. Tokens are generated at a constant rate $r$, bucket capacity is $b$.
3.  **Admission Control**: Rejecting a flow if the network cannot guarantee the requested QoS.

### 6.3 Integrated and Differentiated Services
*   **Integrated Services (IntServ)**: Flow-based QoS. Resources are explicitly reserved for each flow (e.g., using RSVP - Resource Reservation Protocol). Hard to scale for the core internet.
*   **Differentiated Services (DiffServ)**: Class-based QoS. Packets are marked in the IP header (DSCP field). Routers apply per-hop behaviors (PHBs) based on the class. Highly scalable.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not confuse Flow Control (receiver-side limitation) with Congestion Control (network-side limitation). The actual window size used by TCP is $W = \min(rwnd, cwnd)$.

> [!TIP]
> Memorize the UDP header size (8 bytes) and the minimum TCP header size (20 bytes). They are frequently asked in MCQs.
> Remember that Leaky Bucket regulates the *average* rate and eliminates bursts, whereas Token Bucket regulates the *average* rate but *allows* bursts.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - TCP Window Size: $W = \min(\text{rwnd}, \text{cwnd})$
> - UDP Length = UDP Header (8) + Data
> - Token Bucket Maximum Burst Size: $S = b + r \cdot t$ (where $b$ = bucket capacity, $r$ = token rate, $t$ = burst duration)
> - Subnet mask / Port mapping: Standard well-known ports (e.g., 80, 443, 22).

## ✏️ Practice Problems

1.  **A TCP connection is transferring a file of 5000 bytes. The first byte is numbered 10001. What are the sequence numbers for each segment if data is sent in five segments, each carrying 1000 bytes?**
    *Answer:*
    Segment 1: Seq 10001 (Bytes 10001-11000)
    Segment 2: Seq 11001 (Bytes 11001-12000)
    Segment 3: Seq 12001 (Bytes 12001-13000)
    Segment 4: Seq 13001 (Bytes 13001-14000)
    Segment 5: Seq 14001 (Bytes 14001-15000)

2.  **In a TCP connection, the congestion window is set to 16 MSS. A timeout occurs. What will be the value of the congestion window and ssthresh immediately after the timeout?**
    *Answer:* `ssthresh` becomes half of current `cwnd`, so $16/2 = 8$ MSS. The `cwnd` drops to 1 MSS.

3.  **Explain the primary difference between IntServ and DiffServ architectures in QoS.**
    *Answer:* IntServ provides per-flow resource reservation signaling (RSVP) requiring routers to maintain state for every flow (not scalable). DiffServ categorizes traffic into classes and marks packets; routers handle packets based on their class without maintaining flow states (highly scalable).
</Section 5.4: Transport Layer (ACtE0504)>
