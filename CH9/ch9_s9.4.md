## Section Data Communication Switching Techniques (AEiE0904)

## 📖 1. Introduction
Data Communication Switching Techniques form the backbone of modern telecommunication networks. In any network connecting multiple devices, it is impractical to have dedicated point-to-point links between every pair of devices. Switching provides a mechanism to establish temporary connections between devices to facilitate data transfer. This section covers the taxonomy of switched networks, various switching techniques, ISDN services, and multiple access techniques. For the NEC exam, understanding the differences between circuit switching and packet switching, as well as multiple access methods, is highly critical.

## 2. Taxonomy of Switched Networks
A switched network consists of a series of interconnected nodes called switches. Switches are hardware and/or software devices capable of creating temporary connections between two or more devices linked to the switch.

Switched networks can be broadly categorized into three types:
1. Circuit-Switched Networks
2. Packet-Switched Networks
3. Message-Switched Networks

Packet-switched networks are further divided into:
- Datagram Networks
- Virtual-Circuit Networks

> [!NOTE] Definition
> **Switching**: The process of directing a signal or data packet from a source to a destination through intermediate nodes in a network.

```text
Taxonomy of Switched Networks:
                      Switched Network
                             |
       ---------------------------------------------
       |                     |                     |
Circuit-Switched      Packet-Switched       Message-Switched
   Network               Network               Network
                             |
                  -----------------------
                  |                     |
              Datagram           Virtual-Circuit
              Network               Network
```

## 3. Circuit Switch Network
In a circuit-switched network, a dedicated communication path is established between two stations through the nodes of the network. This path is a connected sequence of physical links between nodes. On each link, a logical channel is dedicated to the connection.

### Transmission Phases
The communication in a circuit-switched network occurs in three distinct phases:
1. **Setup Phase**: Before any signal can be transmitted, an end-to-end (source to destination) circuit must be established.
2. **Data Transfer Phase**: Once the circuit is established, data (analog or digital) is transmitted. The connection remains dedicated for the entire duration of the data transfer.
3. **Teardown Phase**: After data transfer is complete, the circuit is disconnected, and the dedicated resources (channels/bandwidth) are released.

> [!TIP]
> **Exam Tip**: Remember that circuit switching is connection-oriented and offers guaranteed bandwidth, making it ideal for real-time services like voice calls (PSTN).

**Efficiency and Delay**:
Circuit switching is generally less efficient than packet switching because channel capacity is dedicated for the entire duration of a connection, even if no data is being sent. However, delay is minimal (only propagation delay) once the connection is established.

Total Delay ($T_D$) in Circuit Switching:
$$T_D = T_{setup} + T_{transmission} + T_{propagation}$$

## 4. Datagram Network (Packet Switching)
In packet switching, data is transmitted in discrete blocks called packets. A datagram network is a packet-switched network in which each packet is treated independently, with no reference to packets that have gone before.

### Characteristics
- Connectionless service: No setup phase.
- Packets are called datagrams.
- Datagrams may follow different routes to the destination.
- Datagrams may arrive out of order.

### Routing Table and Destination Address
Each switch (or router) in a datagram network uses a routing table that is based on the destination address. The destination address in the header of a packet remains the same during the entire journey of the packet.

When a switch receives a packet, it examines the destination address, looks up its routing table to find the corresponding output port, and forwards the packet.

> [!WARNING]
> A common mistake is assuming datagram networks guarantee delivery in order. They do not; upper-layer protocols (like TCP) must handle reordering.

## 5. Virtual Circuit Network
A virtual circuit (VC) network is a cross between a circuit-switched network and a datagram network. It has some characteristics of both.

- Like circuit switching, it has setup and teardown phases.
- Like datagram networks, data is packetized.
- All packets belonging to the same source and destination travel the same path.
- Packets arrive in order.

A virtual circuit is identified by a Virtual Circuit Identifier (VCI). The VCI is a small number that has only switch scope; it is used by a frame between two switches. When a frame arrives at a switch, it has a VCI; when it leaves, it has a different VCI.

### Comparison of Switching Techniques

| Feature | Circuit Switching | Datagram Packet Switching | Virtual-Circuit Packet Switching |
| :--- | :--- | :--- | :--- |
| **Dedicated Path** | Yes | No | No (Logical path) |
| **Setup Phase** | Required | Not required | Required |
| **Bandwidth** | Dedicated | Dynamic | Dynamic |
| **Routing** | Once during setup | Per packet | Once during setup |
| **Packet Order** | In order | Out of order | In order |
| **Example** | PSTN | IP networks | Frame Relay, ATM |

## 6. ISDN Services
Integrated Services Digital Network (ISDN) is a set of communication standards for simultaneous digital transmission of voice, video, data, and other network services over the traditional circuits of the public switched telephone network.

### ISDN Channels
- **B Channel (Bearer)**: 64 kbps, used for voice, video, or data.
- **D Channel (Delta)**: 16 kbps or 64 kbps, used for signaling and control.
- **H Channel**: Higher data rates (384 kbps, 1536 kbps, 1920 kbps).

### ISDN Interfaces
1. **Basic Rate Interface (BRI)**: 2B + 1D (144 kbps total payload).
2. **Primary Rate Interface (PRI)**: 
   - T1 standard (North America): 23B + 1D (1.544 Mbps).
   - E1 standard (Europe/Nepal): 30B + 1D + 1 Synchronization channel (2.048 Mbps).

## 7. Spread Spectrum Modulation
Spread spectrum techniques spread the bandwidth needed to transmit data over a wider bandwidth. This is done to prevent eavesdropping, reduce interference, and allow multiple users to share the same frequency band.

### Types of Spread Spectrum
1. **Frequency Hopping Spread Spectrum (FHSS)**: The signal is broadcast over a seemingly random series of radio frequencies, hopping from frequency to frequency at fixed intervals.
2. **Direct Sequence Spread Spectrum (DSSS)**: Each bit in the original signal is represented by multiple bits in the transmitted signal, using a spreading code (chipping code).

**Processing Gain ($G_p$)**:
$$G_p = \frac{B_s}{B_m} = \frac{\text{Spread Bandwidth}}{\text{Message Bandwidth}}$$
$$G_p (dB) = 10 \log_{10} \left( \frac{B_s}{B_m} \right)$$

## 💡 8. Multiple Access Techniques
Multiple access schemes allow multiple users to share a common communication medium.

1. **FDMA (Frequency Division Multiple Access)**: The available frequency spectrum is divided into non-overlapping frequency bands, and each user is assigned a specific band for the duration of the communication.
2. **TDMA (Time Division Multiple Access)**: The entire frequency band is allocated to users in non-overlapping time slots. Each user transmits only during its assigned time slot.
3. **CDMA (Code Division Multiple Access)**: All users share the same frequency band simultaneously. Each user is assigned a unique pseudo-random code (spreading code) to distinguish their signal from others.

> [!IMPORTANT]
> **CDMA Capacity**: Unlike FDMA and TDMA which have a hard limit on the number of users, CDMA is interference-limited, meaning its capacity degrades gracefully as more users are added.

## 💡 Common Mistakes / Exam Tips
- **Confusion between VCI and IP address**: VCI is local to a link between switches, while an IP address is a global end-to-end address.
- **ISDN PRI rates**: For Nepal, the E1 standard applies, so PRI is 30B+D (2.048 Mbps), not the T1 standard.
- **Spread Spectrum**: Remember that spreading the spectrum decreases the power spectral density, making the signal look like noise to unauthorized receivers.

## 📝 Quick Reference / Formula Summary
- Total delay in circuit switching = Setup + Transmission + Propagation
- $BRI = 2B + D = 2(64) + 16 = 144$ kbps
- $PRI (E1) = 30B + 1D = 30(64) + 64 = 1984$ kbps (plus framing to make 2048 kbps)
- Processing Gain: $G_p = B_s / B_m$

## ✏️ Practice Problems

**Problem 1**: Consider a circuit-switched network where the setup time is $200$ ms, data transmission rate is $1$ Mbps, and the total propagation delay is $50$ ms. Calculate the total time required to transmit a $500$ KB file.
**Solution Sketch**:
- File size = $500 \times 1024 \times 8$ bits = $4,096,000$ bits.
- Transmission time ($T_{tx}$) = $\frac{4,096,000 \text{ bits}}{1,000,000 \text{ bps}} = 4.096$ s.
- Total time = $T_{setup} + T_{tx} + T_{prop} = 0.2 + 4.096 + 0.05 = 4.346$ seconds.

**Problem 2**: What is the processing gain in dB of a DSSS system if the message bandwidth is $10$ kHz and the spread bandwidth is $1$ MHz?
**Solution Sketch**:
- $G_p = \frac{B_s}{B_m} = \frac{1,000,000}{10,000} = 100$.
- $G_p (dB) = 10 \log_{10}(100) = 20$ dB.

**Problem 3**: Differentiate between datagram and virtual-circuit packet switching.
**Answer Sketch**: Mention connectionless vs. connection-oriented, per-packet routing vs. setup phase routing, out-of-order vs. in-order delivery.
</Section 9.4: Data Communication Switching Techniques (AEiE0904)>
