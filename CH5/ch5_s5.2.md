## Section Data Link Layer (ACtE0502)


## 📖 1. Introduction
The Data Link Layer (DLL) operates at layer 2 of the OSI model. While the Physical Layer simply transmits raw bits over a medium, the DLL is responsible for creating a reliable node-to-node link. It packages bits into frames, detects and potentially corrects transmission errors, and manages flow and access control.

## 💡 2. Basic Concept
The DLL ensures that data transferred from node A to node B over a direct physical link is error-free. It is subdivided into two sub-layers by the IEEE 802 standard:
- **Logical Link Control (LLC)**: Handles framing, flow control, and error control.
- **Media Access Control (MAC)**: Handles access to the shared medium and physical addressing.

> [!NOTE] Definition
> **MAC Address**: A 48-bit physical address embedded in the network interface card (NIC), typically represented in hexadecimal format (e.g., `00:1A:2B:3C:4D:5E`).

## 3. Data Link Layer Design Issues

### Framing
Framing breaks the bit stream into discrete, manageable blocks called frames. Techniques include:
- **Byte/Character Count**: A field in the header specifies the number of characters in the frame.
- **Flag Bytes with Byte Stuffing**: Uses special flag bytes at the start and end of frames. If the flag byte pattern appears in the payload, an escape character (stuffing) is inserted.
- **Starting/Ending Flags with Bit Stuffing**: Uses a specific bit pattern (e.g., `01111110`) as flags. In the payload, a `0` is stuffed after every five consecutive `1`s to avoid accidental flags.

### Error Detection and Correction
Noise can alter bits during transmission.

**1. Parity Check**: Adds a single parity bit so the total number of 1s is either even (Even Parity) or odd (Odd Parity). Can only detect single-bit errors.

**2. Checksum**: Data is divided into segments, added together (using 1's complement arithmetic), and the complement of the sum is sent.

**3. Cyclic Redundancy Check (CRC)**:
Uses polynomial division. The sender divides the data by a generator polynomial and appends the remainder (CRC checksum). The receiver performs the same division; if the remainder is zero, the data is error-free.
- E.g., if generator $G(x) = x^3 + x + 1$, it maps to bit sequence `1011`.

**4. Hamming Code (Error Correction)**:
Inserts redundant bits to not only detect but also locate and correct single-bit errors.
Formula for number of redundant bits $r$ given $m$ data bits:
$$2^r \ge m + r + 1$$

## 4. Flow Control
Ensures a fast sender does not overwhelm a slow receiver.

- **Stop-and-Wait**: Sender sends one frame and waits for an ACK before sending the next.
  - Link Utilization: $U = \frac{T_{\text{frame}}}{T_{\text{frame}} + 2 \times T_{\text{prop}}}$
- **Go-Back-N (Sliding Window)**: Sender can transmit up to $N$ frames without waiting. If frame $i$ is lost, the receiver discards all subsequent frames. The sender must retransmit frame $i$ and all frames sent after it.
- **Selective Repeat (Sliding Window)**: Only the specific lost frame is retransmitted. Requires a window size $W \le 2^{m-1}$ (where $m$ is the sequence number bit length).

## 5. Access Control and Protocols (MAC)
When multiple devices share a medium, they need rules to avoid collisions.

- **ALOHA**:
  - *Pure ALOHA*: Transmit whenever data is ready. Max efficiency $\approx 18.4\%$.
  - *Slotted ALOHA*: Time is divided into slots; transmission only starts at slot boundaries. Max efficiency $\approx 36.8\%$.
- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**: Used in traditional Ethernet. Devices listen before transmitting. If a collision is detected, they stop, send a jam signal, and wait a random time (Binary Exponential Backoff) before retrying.
- **CSMA/CA (Collision Avoidance)**: Used in Wireless LANs where collision detection is difficult. Uses RTS/CTS (Request to Send/Clear to Send) to reserve the medium.

## 6. Standard LAN Protocols

### Point-to-Point Protocol (PPP)
Used over point-to-point links (like leased lines or dial-up). It provides framing, authentication (PAP, CHAP), and network-layer protocol multiplexing.

### Ethernet (IEEE 802.3)
The most common wired LAN standard. Uses CSMA/CD.
- Minimum frame size: 64 bytes.
- Maximum frame size: 1518 bytes.
- Header contains Dest MAC, Src MAC, EtherType.

### Token Ring (IEEE 802.5)
Nodes are connected in a logical ring. A special frame called a "token" circulates. Only the node holding the token can transmit data. It guarantees deterministic access and prevents collisions.

### Wireless LANs (IEEE 802.11)
Wi-Fi standard. Uses CSMA/CA.
- Defines Infrastructure mode (using an Access Point) and Ad-hoc mode.
- Uses techniques like Direct Sequence Spread Spectrum (DSSS) and Orthogonal Frequency Division Multiplexing (OFDM).

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not confuse Go-Back-N with Selective Repeat. Go-Back-N resends the lost frame *and all subsequent frames*. Selective Repeat resends *only* the lost frame.

> [!TIP]
> Memorize the IEEE standards: 802.3 is Ethernet, 802.5 is Token Ring, 802.11 is Wi-Fi, 802.15 is Bluetooth.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - **Hamming Redundant Bits Rule**: $2^r \ge m + r + 1$
> - **Pure ALOHA Max Efficiency**: $S = \frac{1}{2e} \approx 18.4\%$
> - **Slotted ALOHA Max Efficiency**: $S = \frac{1}{e} \approx 36.8\%$

## ✏️ Practice Problems

1. **Problem**: Determine the number of redundant bits $r$ needed for $m=7$ data bits using Hamming code.
   *Answer Sketch*: Check $2^r \ge 7 + r + 1$. For $r=3$, $8 \ge 11$ (False). For $r=4$, $16 \ge 12$ (True). Therefore, $r=4$.

2. **Problem**: In a Stop-and-Wait protocol, the frame transmission time is $1 \text{ ms}$ and propagation delay is $10 \text{ ms}$. Calculate the channel utilization.
   *Answer Sketch*: $U = \frac{T_{\text{frame}}}{T_{\text{frame}} + 2 \times T_{\text{prop}}} = \frac{1}{1 + 2(10)} = \frac{1}{21} \approx 4.76\%$.

3. **Problem**: Which IEEE standard specifies the Wireless LAN (Wi-Fi)?
   *Answer Sketch*: IEEE 802.11.

</Section 5.2: Data Link Layer (ACtE0502)>
