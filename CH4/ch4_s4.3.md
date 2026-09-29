# Section 4.3: Input-Output Organization and Multiprocessor (ACtE0403)

## 📖 1. Introduction

The **Input-Output (I/O) organization** of a computer is one of the most critical aspects of computer architecture, responsible for bridging the gap between the high-speed CPU/Memory subsystem and the relatively slow, diverse external world. Without a well-designed I/O subsystem, the CPU would spend most of its time waiting for external devices, severely degrading system performance. Furthermore, as computational demands increase, a single processor often falls short, leading to the development of **multiprocessor systems** where multiple CPUs cooperate to execute tasks faster.

## 💡 2. Basic Concept

> [!NOTE]
> **Definition**: **I/O Organization** refers to the architecture, interfaces, and protocols that facilitate data transfer between the central processing unit (CPU), main memory, and external peripheral devices.

Think of the CPU as the CEO of a company (fast, makes decisions) and peripherals as external contractors (slower, specialized tasks). The **I/O Module** acts as the project manager, translating the CEO's high-level commands into specific instructions for the contractors and reporting back when the job is done. 

## 3. Peripheral Devices

Peripherals are external devices connected to the computer to provide input, output, or storage capabilities. They operate asynchronously and typically have different data formats and transfer speeds compared to the CPU and memory.

### Categories of Peripherals
1.  **Input Devices**: Convert physical/user input into digital signals.
    *   *Examples*: Keyboard, Mouse, Scanner, Microphone, Sensors.
2.  **Output Devices**: Convert digital signals into human-readable or physical actions.
    *   *Examples*: Monitor, Printer, Speaker, Actuators.
3.  **Storage Devices**: Provide non-volatile data storage.
    *   *Examples*: Hard Disk Drives (HDD), Solid State Drives (SSD), Magnetic Tapes, Optical Disks.

## 4. I/O Modules

An **I/O Module** (or I/O Controller) is the hardware component that interfaces the CPU and Memory with one or more peripheral devices. 

### Functions of an I/O Module
1.  **Control and Timing**: Coordinates the flow of traffic between internal resources and external devices.
2.  **CPU Communication**: Decodes commands from the CPU, exchanges data, and reports status.
3.  **Device Communication**: Issues commands, receives status, and transfers data to/from the peripheral.
4.  **Data Buffering**: Temporarily holds data being transferred to manage speed mismatches between the fast CPU/Memory and slow peripherals.
5.  **Error Detection**: Detects mechanical and electrical errors reported by the device (e.g., paper out, parity error).

### Block Diagram of an I/O Module

```text
                     I/O Module
                +-------------------+
                |                   |      +------------+
  Data Bus <===>| Data Registers    |<====>|            |
                |                   |      | Peripheral |
  Address Bus ->| I/O Logic         |      | Device     |
                |                   |      | Interface  |
  Control Bus ->| Status/Control    |<====>|            |
                | Registers         |      +------------+
                |                   |
                +-------------------+
```

## 5. Input-Output Interface

The I/O interface provides a standardized method for connecting peripherals to the CPU/Memory via a system bus. 

### Components of I/O Interface
*   **I/O Bus**: A dedicated bus consisting of data, address, and control lines used exclusively for I/O operations (though it may share physical lines with the memory bus in some architectures).
*   **Interface Circuits**: Logic that decodes address and control signals to select a specific device and determine the type of operation (Read/Write).
*   **I/O Port**: An addressable location (register) in the I/O module where data is written to or read from. 

### I/O Addressing Methods
*   **Memory-Mapped I/O**: I/O ports are mapped into the memory address space. The CPU uses standard memory instructions (e.g., `LOAD`, `STORE`) to access them.
*   **Isolated I/O (I/O-Mapped I/O)**: I/O ports have a separate address space. The CPU uses special instructions (e.g., `IN`, `OUT` in x86) to access them.

## 6. Modes of Transfer

Data transfer between the computer and peripherals can be managed in three primary ways:

### 6.1 Programmed I/O (Polling)
In Programmed I/O, the CPU is entirely responsible for the data transfer operation. 
*   **Concept**: The CPU executes a program that continuously checks (polls) the status register of the I/O module until the device is ready. Once ready, the CPU transfers a single word of data and repeats the process.
*   **Advantages**: Simple hardware design; easy to implement in software.
*   **Disadvantages**: Extremely inefficient. The CPU wastes vast amounts of clock cycles waiting in a busy-wait loop, heavily degrading overall system performance.

### 6.2 Interrupt-Driven I/O
To overcome CPU idling, interrupts are used.
*   **Concept**: The CPU issues an I/O command and then proceeds to execute other useful work. When the I/O module is ready to exchange data, it asserts an interrupt request line. The CPU stops its current task, saves its state, jumps to an Interrupt Service Routine (ISR) to handle the data transfer, and then resumes the original task.
*   **Advantages**: Eliminates CPU busy-waiting; CPU can perform other tasks concurrently.
*   **Disadvantages**: Context switching (saving/restoring state) overhead consumes time. High data rates can cause "interrupt storms," overwhelming the CPU.

### 6.3 Direct Memory Access (DMA)
For large blocks of data, involving the CPU in every single word transfer is inefficient.
*   **Concept**: A dedicated hardware controller (DMA Controller) takes over the system bus to transfer data directly between the I/O module and memory, bypassing the CPU completely. The CPU initiates the transfer by giving the DMAC the starting address, word count, and direction (Read/Write). The DMAC interrupts the CPU only when the entire block transfer is complete.
*   **DMA Controller (DMAC)**: Contains address registers, word count registers, and control registers.
*   **Modes of DMA**:
    *   **Burst Mode**: DMAC locks the system bus and transfers the entire block of data at once. CPU is blocked during this time.
    *   **Cycle Stealing Mode**: DMAC transfers one word at a time, stealing one memory cycle from the CPU. The CPU continues to execute instructions but may be slightly delayed if it needs the memory bus simultaneously.
    *   **Transparent Mode**: DMAC transfers data only when the CPU is not using the system buses.

### Comparison Table: Modes of Transfer

| Feature | Programmed I/O | Interrupt-Driven I/O | DMA |
| :--- | :--- | :--- | :--- |
| **CPU Involvement** | High (Busy-waiting) | Medium (ISR execution) | Low (Setup and completion only) |
| **Hardware Complexity** | Low | Medium | High (requires DMAC) |
| **Data Transfer Rate** | Low | Medium | High |
| **Best Used For** | Simple, slow devices | Moderate speed, unpredictable events | High-speed, large block transfers (disk, network) |

## 💡 7. Multiprocessor Characteristics

> [!NOTE]
> A **Multiprocessor System** contains two or more independent CPUs that share access to main memory, peripherals, and the system bus, operating cooperatively to execute tasks.

### Types of Multiprocessors
1.  **Symmetric Multiprocessing (SMP)**: All processors are identical, share the same main memory, and have equal access to all I/O devices. The operating system coordinates tasks evenly.
2.  **Asymmetric Multiprocessing (ASMP)**: One processor acts as a master, controlling the system and allocating tasks to the other slave processors. Processors may have specialized functions.

### Advantages
*   **Increased Throughput**: More tasks can be completed in less time.
*   **Economy of Scale**: Sharing memory, power supplies, and peripherals is cheaper than having multiple independent single-processor systems.
*   **Increased Reliability**: If one processor fails, the system can gracefully degrade and continue functioning with the remaining processors (Fault Tolerance).

### Challenges
*   **Resource Contention**: Processors competing for memory access or I/O.
*   **Cache Coherence**: Ensuring that if one processor updates a shared variable in its local cache, other processors see the updated value.

## 8. Interconnection Structures

In a multiprocessor system, processors, memory modules, and I/O devices must be connected. The choice of interconnection structure affects system cost, scalability, and bandwidth.

### 8.1 Time-Shared Common Bus
*   **Concept**: All processors, memory modules, and I/O devices connect to a single shared bus.
*   **Pros**: Simple structure, low cost, easy to add new devices.
*   **Cons**: Bus contention becomes a severe bottleneck as the number of processors increases. Low scalability.

```text
  Proc 1    Proc 2    Proc N
    |         |         |
================================ (System Bus)
    |         |         |
  Mem 1     Mem 2     Mem M
```

### 8.2 Crossbar Switch
*   **Concept**: A grid (matrix) of switching elements connects every processor to every memory module simultaneously.
*   **Pros**: Highest bandwidth; non-blocking (multiple simultaneous transfers are possible if they access different memory modules).
*   **Cons**: Extremely expensive and complex. Number of switches grows as $O(N \times M)$ where $N$ is processors and $M$ is memory modules. Poor scalability beyond a few dozen processors.

### 8.3 Multistage Interconnection Network (MIN)
*   **Concept**: Uses layers of smaller switching elements (e.g., $2 \times 2$ switches) connected in a specific topology (like Omega or Butterfly network) to route requests from processors to memory.
*   **Pros**: A compromise between bus (cheap/slow) and crossbar (expensive/fast). Switch cost grows as $O(N \log N)$.
*   **Cons**: Network latency is higher than a direct connection, and blocking can occur if multiple paths conflict.

### 8.4 Hypercube
*   **Concept**: A network of $N = 2^n$ nodes arranged in an $n$-dimensional cube. Each node has direct connections to exactly $n$ other nodes.
*   **Pros**: Good balance of diameter (max hops) and degree (connections per node). Highly scalable for message-passing architectures.
*   **Cons**: Wiring complexity increases logarithmically with system size.

## 9. Inter-processor Communication and Synchronization

Processors in a multiprocessor system must communicate to share data and coordinate tasks.

### Inter-processor Communication
1.  **Shared Memory System (Tightly Coupled)**: 
    *   Processors communicate by reading and writing variables located in a shared main memory space.
    *   *Advantage*: Communication is implicit and fast (memory speeds).
    *   *Disadvantage*: Requires strict synchronization and cache coherence mechanisms.
2.  **Message Passing System (Loosely Coupled)**:
    *   Processors have their own private memory and communicate by explicitly sending and receiving messages over an interconnection network (similar to network packets).
    *   *Advantage*: Highly scalable, no cache coherence issues.
    *   *Disadvantage*: Explicit programming is harder; communication overhead is higher.

### Synchronization
When multiple processors access shared resources (like shared variables in memory), race conditions can occur. Synchronization mechanisms are required to ensure data integrity.

> [!WARNING]
> **Mutual Exclusion** is the critical requirement that only one processor can access a shared resource (critical section) at any given time.

1.  **Hardware Primitives**: Special atomic instructions provided by the CPU architecture (e.g., Test-and-Set, Compare-and-Swap). These allow a processor to read and modify a memory location in a single uninterruptible bus cycle.
2.  **Semaphores**: An integer variable used for signaling among processes. Operations `Wait()` (decrement and block if zero) and `Signal()` (increment and wake up) are used to protect critical sections.
3.  **Spinlocks**: A synchronization lock where a processor simply waits in a loop ("spins") repeatedly checking if the lock is available. Useful for very short wait times as it avoids context switching overhead, but wastes CPU cycles.
4.  **Barriers**: A synchronization point where all processors in a group must arrive before any of them are allowed to proceed to the next phase of computation.

## 🔍 10. Worked Examples

**Example 1: DMA Transfer Time Calculation**
A DMA controller transfers a block of $2$ KB data to memory. The system bus clock is $10$ MHz, and each word transfer (16 bits) takes $2$ clock cycles. If the disk transfer rate is $1$ MBps, how much time does the DMA transfer take assuming burst mode?

**Solution**:
Total data to transfer = $2 \text{ KB} = 2048 \text{ Bytes} = 1024 \text{ words}$.
Since the disk transfer rate is $1 \text{ MBps}$, time to read from disk into DMA buffer:
$$T_{disk} = \frac{2 \text{ KB}}{1 \text{ MBps}} = 2 \text{ ms}$$
Time for one bus cycle = $1 / (10 \text{ MHz}) = 100 \text{ ns}$.
Time for one word transfer over bus = $2 \times 100 \text{ ns} = 200 \text{ ns}$.
Total time to transfer $1024$ words over bus = $1024 \times 200 \text{ ns} = 204.8 \text{ \mu s}$.
Assuming the buffer reads and bus writes are pipelined or burst mode operates directly on bus availability, the dominant time is often the bus transfer time *if* the data is already buffered. However, the bottleneck here is the disk speed. The total minimum time is bounded by the disk read time: **$2$ ms**.

**Example 2: Crossbar Switch Calculation**
A multiprocessor system has $16$ processors and $16$ memory modules. If a crossbar switch is used, how many crosspoint switches are required?
**Solution**:
Number of switches = Processors $\times$ Memory Modules = $16 \times 16 = 256$.

## 💡 11. Exam Tips and Common Mistakes
*   **Polling vs Interrupt**: Remember that polling wastes CPU time looking for work, while interrupts let the work look for the CPU.
*   **Cycle Stealing vs Burst Mode**: Cycle stealing slows down the CPU slightly but maintains responsiveness; burst mode locks out the CPU entirely but finishes the transfer faster.
*   **Cache Coherence**: Often tested in multiprocessor sections. Know that it's a major issue in shared-memory systems but not in message-passing systems.
*   **Symmetric vs Asymmetric**: SMP = all CPUs equal (peer-to-peer), ASMP = master/slave relationship.

## ✏️ 12. Practice Problems

1.  **Which data transfer technique requires the least CPU intervention?**
    a) Programmed I/O
    b) Interrupt-driven I/O
    c) DMA
    d) Isolated I/O
    *Answer: (c) DMA.*

2.  **In an Omega network connecting 8 processors to 8 memory modules, what size of switching elements is typically used and how many stages are there?**
    a) $4 \times 4$, 2 stages
    b) $2 \times 2$, 3 stages
    c) $8 \times 8$, 1 stage
    d) $2 \times 2$, 4 stages
    *Answer: (b). For $N=8$, using $2 \times 2$ switches requires $\log_2(8) = 3$ stages.*

3.  **A special atomic instruction used for synchronization in multiprocessors is:**
    a) LOAD
    b) JUMP
    c) Test-and-Set
    d) PUSH
    *Answer: (c) Test-and-Set.*
