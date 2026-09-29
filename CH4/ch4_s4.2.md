# Section 4.2: Computer Arithmetic and Memory System (ACtE0402)

## 📖 1. Introduction
While the Control Unit orchestrates tasks, the ALU performs the heavy mathematical lifting, and the Memory System provides the data and instructions. Understanding computer arithmetic is essential to see how logic gates form complex mathematics. Furthermore, bridging the massive speed gap between the CPU and Main Memory requires an intricate Memory Hierarchy, primarily caching. This section covers binary arithmetic, logical operations, and the principles of modern memory systems.

## 💡 2. Basic Concept
A computer processes numbers using binary representations. Therefore, arithmetic operations are essentially bit manipulations. The Memory System is organized as a hierarchy: smaller, faster memories are placed closer to the CPU, while larger, slower memories are placed further away.

> [!NOTE] Definition
> **Memory Hierarchy** is an architectural design that separates computer storage based on response time, complexity, and capacity to optimize performance and cost.

### Real-World Analogy
*   **Registers (CPU)**: Your brain's immediate thoughts. Extremely fast, but limited capacity.
*   **Cache Memory**: Your desk. Fast access to the papers you are currently working on.
*   **Main Memory (RAM)**: A filing cabinet in your office. Slower to access, but holds many more documents.
*   **Secondary Storage (Disk/SSD)**: A warehouse archive. Huge capacity, but takes a long time to retrieve a file.

---

## 3. Arithmetic Operations
Computers use specialized algorithms to perform arithmetic using binary logic.

### 3.1 Addition and Subtraction
*   **Addition:** Handled by Half Adders and Full Adders cascaded into Ripple Carry Adders or optimized into Carry Lookahead Adders.
*   **Subtraction:** Usually performed by converting the subtrahend into its 2's complement form and adding it to the minuend.
    *   $A - B = A + (\text{2's complement of } B) = A + (\sim B + 1)$

### 3.2 Multiplication (Booth's Algorithm)
Multiplication in hardware can be done by repeated shift and add operations. **Booth's Algorithm** is an optimization technique that handles signed binary multiplication in 2's complement form and speeds up the process by skipping over strings of 1s.

**Algorithm Rule (Checking bits $Q_0$ and $Q_{-1}$):**
*   `00` or `11`: Arithmetic Shift Right (ASR) the Accumulator (A) and Multiplier (Q).
*   `01`: $A \leftarrow A + M$ (Add Multiplicand to A), then ASR.
*   `10`: $A \leftarrow A - M$ (Subtract Multiplicand from A), then ASR.

> [!IMPORTANT]
> Booth's algorithm reduces the number of additions required, especially when the multiplier has blocks of continuous 1s (e.g., `00111100`).

### 3.3 Division
Division is implemented using shift and subtract operations.
*   **Restoring Division:** If subtracting the divisor yields a negative result, the original value is restored (added back) before the next shift.
*   **Non-Restoring Division:** Avoids the restoration step by shifting first and deciding whether to add or subtract based on the sign of the previous partial remainder.

---

## 4. Logical Operations
ALUs perform bitwise operations:
*   **AND:** Used for masking out bits (forcing bits to 0).
*   **OR:** Used for setting bits (forcing bits to 1).
*   **XOR:** Used for toggling bits or checking if two words are different.
*   **NOT:** Inverts all bits (1's complement).
*   **Shift/Rotate:** Useful for multiplying/dividing by powers of 2 or examining specific bits.

---

## 5. The Memory Hierarchy
The goal of the memory hierarchy is to provide the illusion of a memory that is as fast as the cache and as large as the secondary storage.

```text
               / \
             /     \
           /Registers\    <-- CPU, Fastest, Smallest, Highest Cost/Bit
         /-------------\
       /   L1/L2 Cache   \  <-- SRAM, Very Fast
     /---------------------\
   /      Main Memory (RAM)  \ <-- DRAM, Moderate Speed
 /-----------------------------\
/ Magnetic Disk / Optical / SSD  \ <-- Non-volatile, Slowest, Largest, Lowest Cost
-----------------------------------
```

### 5.1 Internal vs. External Memory
*   **Internal Memory:** Directly accessible by the CPU without I/O modules. Includes Registers, Cache, and Main Memory.
*   **External Memory:** Accessible via I/O controllers. Includes Disks, SSDs, Tapes.

### RAM Types:
*   **SRAM (Static RAM):** Built using flip-flops. Does not need refreshing. Very fast, expensive, used for Cache.
*   **DRAM (Dynamic RAM):** Built using capacitors. Must be refreshed periodically. Slower, dense, cheaper, used for Main Memory.

---

## 6. Cache Memory Principles
Cache memory bridges the speed gap between the CPU and Main Memory. It operates on the principle of **Locality of Reference**:
1.  **Temporal Locality:** If a memory location is referenced, it will likely be referenced again soon (e.g., loops, variables).
2.  **Spatial Locality:** If a memory location is referenced, memory locations with nearby addresses will likely be referenced soon (e.g., arrays, sequential code).

When the CPU needs data:
1.  Checks Cache. If found $\rightarrow$ **Cache Hit**.
2.  If not found $\rightarrow$ **Cache Miss**. The block is fetched from Main Memory into Cache, then to the CPU.

**Hit Ratio (h):** $h = \frac{\text{Hits}}{\text{Hits} + \text{Misses}}$
**Average Memory Access Time (AMAT):** 
$$AMAT = T_{cache} + (1 - h) \times T_{memory}$$
Where $(1 - h)$ is the Miss Rate, and $T_{memory}$ is the Miss Penalty.

---

## 7. Elements of Cache Design

### 7.1 Cache Size
*   Larger caches have higher hit rates but are slower to search and more expensive.

### 7.2 Mapping Functions
Because cache is much smaller than main memory, we need a rule to map a main memory block to a cache line.

#### A. Direct Mapping
Each block of main memory maps to exactly one specific cache line.
*   $i = j \bmod m$ (where $i$ = cache line, $j$ = memory block number, $m$ = number of cache lines).
*   *Advantage:* Simple and fast.
*   *Disadvantage:* Thrashing (blocks constantly replacing each other if they map to the same line).

#### B. Associative Mapping (Fully Associative)
A main memory block can be loaded into *any* cache line.
*   *Advantage:* Maximizes cache usage, minimizes conflict misses.
*   *Disadvantage:* Hardware to search all lines simultaneously is complex and expensive.

#### C. Set-Associative Mapping
A compromise. The cache is divided into sets. A block maps to a specific *set*, but can be placed in *any line* within that set.
*   $s = j \bmod S$ (where $s$ = set number, $j$ = block number, $S$ = number of sets).
*   A $k$-way set associative cache has $k$ lines per set.

### Worked Example: Cache Mapping
**Problem:** A system has a main memory of 64KB, cache of 4KB, and a block size of 32 Bytes. Calculate the address format for Direct Mapping.
**Solution:**
1.  Memory Size = $64KB = 2^{16}$ bytes $\rightarrow$ **16-bit address**.
2.  Block Size = $32B = 2^5$ bytes $\rightarrow$ **5 bits for Word (Offset)**.
3.  Number of Memory Blocks = $64KB / 32B = 2048 = 2^{11}$.
4.  Number of Cache Lines = $4KB / 32B = 128 = 2^7$ $\rightarrow$ **7 bits for Line (Index)**.
5.  Tag Bits = Total Address - Line - Word = 16 - 7 - 5 = **4 bits for Tag**.

*Address Format: [ Tag (4) | Line (7) | Word (5) ]*

### 7.3 Replacement Algorithms
When the cache is full and a new block is fetched, which block is evicted?
*   **LRU (Least Recently Used):** Evict the block that has not been referenced for the longest time. Most effective.
*   **FIFO (First-In-First-Out):** Evict the oldest block in the cache.
*   **LFU (Least Frequently Used):** Evict the block with the fewest references.
*   **Random:** Pick a block at random.

### 7.4 Write Policy
When the CPU writes data to cache, when does main memory get updated?
*   **Write-Through:** Data is written to both cache and main memory simultaneously. Reliable but slow.
*   **Write-Back:** Data is written only to cache. Main memory is updated only when that cache block is evicted. Fast, requires a "dirty bit" to track modifications.

### 7.5 Number of Caches
*   **Multi-level:** L1 (closest, fast), L2, L3 (shared across cores, larger).
*   **Unified vs Split:** Unified cache holds both instructions and data. Split cache has separate L1 Data and L1 Instruction caches (prevents structural hazards in pipelining).

---

## 8. Memory Writability and Storage Permanence

### Memory Writability (ROM Types)
*   **ROM (Read-Only Memory):** Programmed during manufacturing.
*   **PROM (Programmable ROM):** Written once by the user using a special device.
*   **EPROM (Erasable PROM):** Erasable via UV light, reprogrammable.
*   **EEPROM (Electrically Erasable PROM):** Erasable electrically byte-by-byte.
*   **Flash Memory:** Erased electrically in large blocks rather than byte-by-byte (used in SSDs, USB drives).

### Storage Permanence
*   **Volatile Memory:** Loses data when power is turned off (SRAM, DRAM).
*   **Non-Volatile Memory:** Retains data without power (ROM, Flash, Magnetic Disks).

---

## 9. Composing Memory
To build larger memory capacities or wider data buses, individual memory chips are combined.

*   **Increasing Word Size:** Connect chips in parallel. E.g., combining two 1K x 4-bit chips to make a 1K x 8-bit memory. Address lines are shared; data lines are concatenated.
*   **Increasing Capacity (Number of Words):** Connect chips in series using decoders. E.g., combining two 1K x 8-bit chips to make a 2K x 8-bit memory. Data lines are shared; high-order address bits are used with a decoder to select the correct chip (Chip Select/CS).

---
## 📝 Key Formulas Summary

| Metric | Formula |
| :--- | :--- |
| **AMAT** | $T_{cache} + (Miss Rate \times Miss Penalty)$ |
| **Memory Address Bits** | $\log_2(\text{Total Memory Size in Bytes})$ |
| **Offset/Word Bits** | $\log_2(\text{Block Size in Bytes})$ |
| **Direct Cache Index Bits** | $\log_2(\text{Number of Cache Lines})$ |
| **Set-Assoc. Index Bits** | $\log_2(\text{Number of Sets})$ |

---
## ✏️ Practice Problems

1. **Question:** In a direct-mapped cache, where does memory block 15 map if the cache has 8 lines?
   *Answer:* Cache Line = $15 \bmod 8 = 7$. It maps to line 7.

2. **Question:** Why is a write-back policy generally faster than a write-through policy?
   *Answer:* Write-back only updates main memory when absolutely necessary (on eviction), thus reducing the number of slow main memory access operations compared to write-through, which updates memory on every single write.

3. **Question:** Calculate AMAT if Cache access time is 2ns, Main Memory access time is 50ns, and Hit Rate is 90%.
   *Answer:* AMAT = $2ns + (1 - 0.90) \times 50ns = 2ns + (0.10 \times 50ns) = 2ns + 5ns = 7ns$.
