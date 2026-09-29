# Section 2.5: Microprocessor System (AExE0205)

## 📖 1. Introduction

Welcome to **Section 2.5** of the NEC Registration Exam syllabus. Having covered digital logic and the core architecture of the 8085 microprocessor in earlier sections, this chapter bridges the gap between the CPU and the outside world. A microprocessor by itself cannot achieve much; it needs memory to store programs and data, and it requires I/O devices to interact with the environment. 

This section covers the memory hierarchy, methods for interfacing memory and I/O to the microprocessor, and the standard peripheral chips—such as the 8255 Programmable Peripheral Interface (PPI) and DMA controllers—that facilitate efficient data transfer.

---

## 🏷️ 2. Memory Device Classification and Hierarchy

### 2.1 The Memory Hierarchy

> **Definition:** The **Memory Hierarchy** is an architectural design that organizes memory components based on response time, capacity, and cost to optimize overall system performance.

As you move up the hierarchy (towards the CPU), memory becomes faster, smaller in capacity, and more expensive per byte.

```text
               /\
              /  \
             /    \     <- Registers (In CPU, fastest, smallest)
            /------\
           /        \   <- Cache Memory (SRAM, very fast)
          /----------\
         /            \ <- Main Memory (DRAM, moderately fast, larger)
        /--------------\
       /                \ <- Secondary Storage (HDD/SSD, slowest, largest)
      /__________________\
```

### 2.2 Memory Device Classification

Memory devices are broadly classified into **Volatile** (loses data when power is removed) and **Non-Volatile** (retains data without power).

#### Random Access Memory (RAM) - Volatile
RAM allows data to be read and written in roughly the same amount of time, regardless of its physical location.

| Feature | Static RAM (SRAM) | Dynamic RAM (DRAM) |
| :--- | :--- | :--- |
| **Storage Element** | Flip-flops (typically 6 transistors/cell) | Capacitors (1 transistor + 1 capacitor) |
| **Density/Size** | Low density, physically larger | High density, smaller |
| **Speed** | Very fast (used in cache) | Slower than SRAM (used in main memory) |
| **Refreshing** | Not required | Required periodically (to recharge capacitors) |
| **Cost** | Expensive | Cheaper |
| **Power** | High power consumption | Low power consumption |

#### Read-Only Memory (ROM) - Non-Volatile
ROM primarily stores fixed programs (like BIOS) and lookup tables.

- **Mask ROM:** Data is permanently programmed during manufacturing.
- **PROM (Programmable ROM):** One-time programmable by the user using a PROM programmer. Blows internal fuses.
- **EPROM (Erasable PROM):** Erasable by exposing it to Ultraviolet (UV) light for 15-20 minutes. Reprogrammable.
- **EEPROM (Electrically Erasable PROM):** Erasable and reprogrammable electrically, byte by byte. Slower write time.
- **Flash Memory:** A type of EEPROM that is erased and rewritten in blocks rather than byte by byte. High density, widely used in modern SSDs and pen drives.

### 2.3 Memory Organization and Capacity Calculation

A memory chip has an organization defined as $2^n \times m$ bits, where:
- $n$ = number of address lines
- $m$ = number of data lines (bits per word)

> [!TIP]
> To find the number of address lines needed for a memory capacity, use the formula $C = 2^n \times m$. For example, a 4 KB memory block has $4 \times 1024 = 4096$ bytes $= 2^{12}$ bytes. So, $n = 12$ address lines are needed.

The 8085 microprocessor has a 16-bit address bus ($A_0 - A_{15}$). 
Total addressable memory $= 2^{16} = 65,536$ bytes $= 64$ KB.

---

## 3. Interfacing I/O and Memory

To connect external memory and I/O devices to the microprocessor, we use specific interfacing techniques. The microprocessor uses its address bus to select the device, the data bus to transfer data, and the control bus to determine the direction of transfer (Read or Write).

### 3.1 I/O Interfacing Techniques

There are two primary ways to interface I/O devices:

| Feature | Memory-Mapped I/O | I/O-Mapped I/O (Isolated I/O) |
| :--- | :--- | :--- |
| **Address Space** | Shares the 64 KB memory space (e.g., 8085) | Has a separate 256-byte space (in 8085 using 8-bit port address) |
| **Address Bus Used** | 16-bit ($A_0 - A_{15}$) | 8-bit ($A_0 - A_7$ mirrored on $A_8 - A_{15}$) |
| **Instructions Used** | `LDA`, `STA`, `MOV`, etc. | `IN`, `OUT` |
| **Control Signals** | $\overline{MEMR}$, $\overline{MEMW}$ | $\overline{IOR}$, $\overline{IOW}$ |
| **Max Devices** | Limited only by memory mapping | 256 input and 256 output devices |
| **Decoding** | Complex (16-bit decoding) | Simpler (8-bit decoding) |

### 3.2 Address Decoding Techniques

To activate a specific memory chip or I/O device, its Chip Select ($\overline{CS}$) pin must be asserted (usually active low). This is done using address decoding.

- **Full (Absolute) Decoding:** All higher-order address lines not used by the memory chip are used to generate the $\overline{CS}$ signal. The device has a unique, single address range.
- **Partial (Linear) Decoding:** Only a subset of higher-order lines is used. This is cheaper (requires fewer logic gates) but causes **foldback** or **shadowing**, where the same device appears at multiple address ranges.

### 3.3 Worked Example: Memory Interfacing

**Problem:** Interface a 4 KB EPROM to an 8085 microprocessor such that its starting address is `8000H`. Use a 3-to-8 decoder (74LS138) for full decoding.

**Step 1: Determine address lines for the chip.**
4 KB = $4 \times 1024$ bytes = $2^{12}$ bytes.
Therefore, 12 address lines ($A_{11} - A_0$) connect directly to the EPROM.

**Step 2: Determine decoding logic for $\overline{CS}$.**
The remaining lines ($A_{15} - A_{12}$) must be decoded to select this specific 4 KB block.
Starting address: `8000H` = `1000 0000 0000 0000` in binary.
Ending address: `8000H` + `0FFFH` (since $2^{12} - 1 = \text{0FFFH}$) = `8FFFH` = `1000 1111 1111 1111`.

Observe the upper 4 bits for the range `8000H` to `8FFFH`:
$A_{15} = 1$, $A_{14} = 0$, $A_{13} = 0$, $A_{12} = 0$.

**Step 3: Connect the 74LS138 Decoder.**
Connect $A_{12}, A_{13}, A_{14}$ to the select inputs C, B, A of the decoder.
Enable pins: $G_1 = A_{15}$ (active high), $\overline{G_{2A}} = \text{GND}$, $\overline{G_{2B}} = \text{GND}$ (or $\overline{IO/M}$ if ensuring memory space only).
Since C=0, B=0, A=0, the $Y_0$ output of the decoder will go LOW. Connect $Y_0$ to the $\overline{CS}$ pin of the EPROM.

---

## 4. Parallel Interface - Programmable Peripheral Interface (PPI) 8255

The Intel 8255 is a widely used programmable parallel I/O device. It provides 24 I/O pins, organized as three 8-bit ports.

### 4.1 Block Diagram and Ports

```text
                 +-------------------+
  Data Bus (D0-D7) |                   | Port A (PA0-PA7)
 <---------------->|    8255 PPI     |<---------------->
                   |                   |
  Read/Write Ctrl  |                 | Port B (PB0-PB7)
 <---------------->|                 |<---------------->
 (RD, WR, RESET,   |                   |
  CS, A0, A1)      |                 | Port C (PC0-PC7)
                   |                   |<---------------->
                 +-------------------+
```

- **Port A:** One 8-bit output latch/buffer and one 8-bit input latch.
- **Port B:** One 8-bit data I/O latch/buffer and one 8-bit input buffer.
- **Port C:** One 8-bit unlatched input buffer and one 8-bit output latch/buffer. Often split into Port C Upper (PC7-PC4) and Port C Lower (PC3-PC0) for control signals.

### 4.2 Operating Modes

The 8255 operates in two main configurations, selected by bit $D_7$ of the Control Word Register (CWR).

1. **BSR (Bit Set/Reset) Mode ($D_7 = 0$):** Used strictly to set or reset individual pins of **Port C**.
2. **I/O Mode ($D_7 = 1$):** Used for parallel data transfer. It has three sub-modes:
   - **Mode 0 (Simple I/O):** Ports A, B, and C can be programmed as simple input or output ports without handshaking.
   - **Mode 1 (Strobed I/O):** Ports A and B can be input or output ports with handshaking. Port C pins are used for handshaking signals (like STB, IBF, ACK, OBF).
   - **Mode 2 (Bi-directional I/O):** Port A is bi-directional with 5-bit handshaking via Port C. Port B can be Mode 0 or Mode 1.

### 4.3 Control Word Format for I/O Mode ($D_7 = 1$)

$$
\begin{array}{|c|c|c|c|c|c|c|c|}
\hline
D_7 & D_6 & D_5 & D_4 & D_3 & D_2 & D_1 & D_0 \\
\hline
1 & \text{Mode A} & \text{Mode A} & \text{Port A} & \text{Port C (U)} & \text{Mode B} & \text{Port B} & \text{Port C (L)} \\
\hline
\text{I/O} & (00=M0, & 01=M1, & 1=\text{In} & 1=\text{In} & 0=M0, & 1=\text{In} & 1=\text{In} \\
\text{Mode} & 1X=M2) & & 0=\text{Out} & 0=\text{Out} & 1=M1 & 0=\text{Out} & 0=\text{Out} \\
\hline
\end{array}
$$

> [!IMPORTANT]
> The internal addresses of 8255 registers are selected by $A_1$ and $A_0$:
> $00 \rightarrow$ Port A, $01 \rightarrow$ Port B, $10 \rightarrow$ Port C, $11 \rightarrow$ Control Word Register.

### 4.4 Worked Example: 8255 Configuration

**Problem:** Find the control word and write the 8085 assembly instructions to configure an 8255 such that Port A is an input port, Port B is an output port, Port C upper is an input port, and Port C lower is an output port. Use Mode 0 for all ports. Assume the CWR address is `83H`.

**Solution:**
Using the Control Word format ($D_7$ to $D_0$):
- $D_7 = 1$ (I/O mode)
- $D_6, D_5 = 0, 0$ (Port A Mode 0)
- $D_4 = 1$ (Port A Input)
- $D_3 = 1$ (Port C Upper Input)
- $D_2 = 0$ (Port B Mode 0)
- $D_1 = 0$ (Port B Output)
- $D_0 = 0$ (Port C Lower Output)

Binary Control Word: `1001 1000` = `98H`.

Assembly Code:
```assembly
MVI A, 98H  ; Load control word into accumulator
OUT 83H     ; Send to Control Word Register
```

---

## 5. Serial Interface

When distances are long, parallel transmission (sending 8 bits at a time over 8 wires) becomes expensive and prone to crosstalk. Serial transmission sends data one bit at a time over a single wire.

### 5.1 Synchronous vs Asynchronous Transmission

| Feature | Asynchronous Transmission | Synchronous Transmission |
| :--- | :--- | :--- |
| **Clock Signal** | No shared clock line | Transmitter and receiver share a clock |
| **Data Framing** | Start and stop bits added to each character | Data sent as a continuous block/frame |
| **Speed** | Slower (overhead of start/stop bits) | Faster (less overhead) |
| **Efficiency** | Low (~80% data, 20% overhead) | High |
| **Examples** | RS-232, Modems, Keyboards | HDLC, SDLC, Ethernet |

#### Asynchronous Frame Format
A typical asynchronous character frame includes:
- **Start Bit (1 bit):** Always LOW (0), indicates the start of a character.
- **Data Bits (5 to 8 bits):** The actual character data (LSB first).
- **Parity Bit (0 or 1 bit):** Optional for error checking (Even/Odd).
- **Stop Bit(s) (1, 1.5, or 2 bits):** Always HIGH (1), indicates the end of the frame.

> [!NOTE]
> **Baud Rate** is the number of signal changes per second. **Bit Rate** is the number of bits transmitted per second. In binary digital systems (like RS-232), Baud Rate = Bit Rate.

### 5.2 Serial Interface Standards

**1. RS-232 (EIA-232):**
- **Voltage Levels:** Uses bipolar signaling. Logic 1 (Mark) is $-3V$ to $-15V$, Logic 0 (Space) is $+3V$ to $+15V$.
- **Distance & Speed:** Short distance (~15m), low speed (up to 20 kbps).
- **Topology:** Point-to-Point, Single-ended (unbalanced).
- **Connector:** Typically DB-9 or DB-25. Key pins: TXD (Transmit), RXD (Receive), GND, RTS, CTS.

**2. RS-422 and RS-485:**
To overcome noise over long distances, these standards use **differential signaling** (sending signals over two wires inverted from each other).
- **RS-422:** Point-to-multipoint (1 driver, up to 10 receivers). Up to 1200m at 100 kbps, or up to 10 Mbps at short distances.
- **RS-485:** Multipoint (up to 32 drivers and 32 receivers on the same bus). True multi-drop network standard widely used in industrial automation.

### 5.3 8251 USART
The Intel 8251 is a Universal Synchronous/Asynchronous Receiver/Transmitter. It handles parallel-to-serial conversion for transmission and serial-to-parallel conversion for reception, offloading this task from the CPU.

---

## 6. Direct Memory Access (DMA)

### 6.1 Introduction to DMA
Normally, the CPU handles all data transfers between I/O and Memory (Programmed I/O or Interrupt I/O). However, for bulk data transfers (e.g., loading a program from a disk to RAM), CPU intervention for every single byte is a massive bottleneck.

> **Definition:** **Direct Memory Access (DMA)** is a hardware-driven mechanism allowing I/O devices to transfer data directly to or from the main memory without CPU involvement, dramatically speeding up bulk transfers.

### 6.2 DMA Transfer Process
1. I/O device asserts a DMA request to the DMA Controller (DMAC).
2. The DMAC sends a **HOLD** signal to the microprocessor.
3. The microprocessor finishes its current machine cycle, places its address, data, and control buses in a high-impedance state (floats them), and asserts the **HLDA** (Hold Acknowledge) signal to the DMAC.
4. The DMAC takes mastership of the system bus and generates the necessary addresses and control signals (e.g., $\overline{IOR}$ and $\overline{MEMW}$) to transfer data directly between I/O and Memory.
5. Once the transfer is complete, the DMAC drops the HOLD signal, and the CPU regains bus mastership.

### 6.3 Types of DMA Transfers

- **Burst Mode (Block Transfer):** The DMAC takes the bus and transfers an entire block of data before returning control. CPU is fully blocked.
- **Cycle Stealing Mode:** The DMAC transfers one byte/word, then releases the bus back to the CPU for one cycle, then requests it again. CPU execution slows down but doesn't stop completely.
- **Transparent (Hidden) Mode:** The DMAC transfers data only during states when the CPU is internally executing an instruction and not using the system bus. No CPU delay, but requires complex timing.

### 6.4 The 8257 DMA Controller
The Intel 8257 is a 4-channel DMA controller, meaning it can service up to 4 different I/O devices (Channels 0 to 3). Each channel has a 16-bit Address Register and a 16-bit Terminal Count Register (which holds the number of bytes to transfer).

```text
      CPU (8085)                          DMAC (8257)                       I/O Device
   +-------------+       HOLD          +---------------+      DRQ         +------------+
   |             |<--------------------|               |<-----------------|            |
   |             |       HLDA          |               |      DACK        |            |
   |             |-------------------->|               |----------------->|            |
   |             |                     |               |                  |            |
   |    Bus      |                     |               |                  |            |
   |             |---(Address, Data,---|               |---(Data Bus)---->|            |
   +-------------+    Control Buses)   +---------------+                  +------------+
         |                                     |
         V                                     V
   +---------------------------------------------------+
   |                    Memory                         |
   +---------------------------------------------------+
```

### 6.5 Comparison of I/O Transfer Techniques

| Feature | Programmed I/O | Interrupt-Driven I/O | DMA |
| :--- | :--- | :--- | :--- |
| **CPU Involvement** | Very High (Polling loop) | Medium (ISR overhead) | Very Low (Setup only) |
| **Speed of Transfer**| Slow | Moderate | Very Fast |
| **Hardware cost** | Lowest | Moderate | Highest (Needs DMAC) |
| **Best suited for** | Slow, simple devices | Intermittent, async events | Bulk data (Disk, Video) |

---

## 📝 7. Key Formulas Summary

| Metric | Formula/Rule |
| :--- | :--- |
| **Memory Address Lines ($n$)** | $2^n = \text{Total number of memory locations}$ |
| **Memory Capacity** | $2^n \times m$ (where $m$ is data bits per location) |
| **Baud Rate (Async)** | Baud Rate = $\frac{1}{\text{Bit Duration}}$ |
| **Transfer Time (Async)** | $T = \frac{\text{Total Bits (Data + Overhead)}}{\text{Baud Rate}}$ |
| **DMA Block Transfer Time**| $T = \text{Number of bytes} \times \text{Clock period of DMA cycle}$ |

---

## 💡 8. Common Mistakes / Exam Tips

> [!WARNING]
> **Pitfalls to Avoid in the Exam:**
> 1. **Address decoding:** Don't forget that hexadecimal addresses represent 4 bits per digit. `8000H` means $A_{15}=1$, others are 0.
> 2. **Active-low signals:** Pay attention to the bar over signals like $\overline{CS}$, $\overline{RD}$, $\overline{WR}$. A 0 enables them, a 1 disables them.
> 3. **8255 BSR vs I/O Mode:** Remember that BSR mode ($D_7=0$) only affects Port C bits. It cannot be used for Ports A or B.
> 4. **Baud Rate vs Bit Rate:** They are only equivalent in binary signaling (2 symbols). If a problem mentions 4-level signaling, Bit Rate = 2 × Baud Rate.
> 5. **Hold / Hold Acknowledge:** Remember the direction: DMAC sends HOLD to CPU; CPU sends HLDA to DMAC.

---

## ✏️ 9. Practice Problems

**Q1.** Calculate the number of address lines required to interface a $16 \text{ KB} \times 8$ memory chip.
**Answer:** $16 \text{ KB} = 16 \times 1024 = 2^4 \times 2^{10} = 2^{14}$ bytes. It requires **14 address lines** ($A_0 - A_{13}$).

**Q2.** Identify the control word for the 8255 to set Port A in Mode 1 (output), Port B in Mode 0 (input), and Port C upper as output.
**Answer:** 
$D_7=1$ (I/O). $D_6,D_5=01$ (Port A M1). $D_4=0$ (Port A out). $D_3=0$ (Port C upper out). $D_2=0$ (Port B M0). $D_1=1$ (Port B in). $D_0=X$ (used for M1 handshaking, assume 0).
Binary: `1 01 0 0 0 1 0` = `A2H`.

**Q3.** An asynchronous serial transmission uses 1 start bit, 8 data bits, 1 parity bit, and 1 stop bit. If the baud rate is 9600, what is the maximum number of data characters that can be transmitted per second?
**Answer:** 
Total bits per frame = $1 + 8 + 1 + 1 = 11$ bits.
Characters per second = $\frac{9600 \text{ bits/sec}}{11 \text{ bits/char}} \approx 872.72$ characters.

**Q4.** Differentiate between cycle stealing and burst mode in DMA.
**Answer:** In Burst Mode, the DMAC monopolizes the bus until the whole block of data is transferred. In Cycle Stealing, the DMAC transfers a single byte, returns bus control to the CPU, and requests it again, interleaving with CPU operations.

**Q5.** Which RS standard supports true multi-drop (multipoint) networking?
**Answer:** **RS-485** supports up to 32 drivers and 32 receivers on a single 2-wire bus, making it true multi-drop, unlike RS-232 (point-to-point) or RS-422 (point-to-multipoint).
