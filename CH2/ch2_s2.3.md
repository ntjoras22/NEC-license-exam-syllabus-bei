# Section 2.3: Sequential Logic Circuits (AExE0203)

> [!NOTE]
> **Syllabus Coverage:** RS Flip-Flops, Gated Flip-Flops, Edge Triggered Flip-Flops, Master-Slave Flip-Flops. Types of Registers, Applications of Shift Registers, Asynchronous Counters, Synchronous Counters.

## 📖 2.3.1 Introduction to Sequential Circuits

Combinational logic circuits are memoryless; their outputs depend only on their current inputs. Sequential logic circuits, however, have "memory." Their outputs depend not only on the present inputs but also on the past sequence of inputs. This is achieved by introducing feedback loops that retain past states.

### Why Is It Important?
*   **Memory Elements:** They form the basis for all storage devices like RAM, registers, and caches in modern computing.
*   **State Machines:** Essential for designing finite state machines (FSM) that control the flow of digital systems (e.g., CPUs, traffic lights).
*   **Synchronization:** Allow operations to be synchronized with a central clock, ensuring predictable and orderly data processing.
*   **Timing Control:** Used for delay generation, sequence generation, and timing logic.

### Basic Concept
A sequential circuit consists of a combinational logic circuit and a memory element (usually flip-flops). The outputs of the memory elements are fed back to the combinational circuit as inputs.

> **Definition**  
> A **Sequential Logic Circuit** is a digital circuit whose output is a function of both the current input variables and the present state (history) of the circuit.

### Physical/Logical Meaning
Imagine a combination lock (combinational logic): entering the right numbers opens it regardless of past attempts. Now imagine a typical ATM PIN (sequential logic): if you enter it wrong 3 times in a row (history), it locks your card, even if the 4th attempt is the correct PIN. The ATM has "memory" of your past attempts.

### Combinational vs Sequential Circuits

| Feature | Combinational Circuits | Sequential Circuits |
| :--- | :--- | :--- |
| **Output Dependency** | Present inputs only | Present inputs AND past state |
| **Memory** | None | Required (Flip-flops/Latches) |
| **Clock** | Usually not required | Typically required (Synchronous) |
| **Feedback** | No | Yes |
| **Speed** | Faster (only logic gate delay) | Slower (clock and memory delays) |
| **Examples** | Adders, Multiplexers, Encoders | Counters, Registers, Memory |

### Role of Memory and Feedback
Memory is achieved via **feedback**. By routing the output of a gate back to its input, the circuit can "hold" or latch onto a state even after the initial stimulus is removed.

### Synchronous vs Asynchronous Sequential Circuits
*   **Synchronous:** All memory elements change their states simultaneously, driven by a global clock signal. Easier to design and analyze.
*   **Asynchronous:** Memory elements change state independently upon input changes, without a global clock. Faster but prone to timing issues like hazards and race conditions.

### Clock Signal Concept
A **clock (CLK)** is a periodic square wave signal used to synchronize the state changes in a sequential circuit. It has two levels (High/1, Low/0) and two edges (Rising/Positive, Falling/Negative).

```text
    High (1)       ┌───────┐       ┌───────┐
                   │       │       │       │
    Low (0)  ──────┘       └───────┘       └───────
                   ▲       ▲       ▲       ▲
              Positive Negative Positive Negative
               Edge     Edge     Edge     Edge
```

---

## 2.3.2 SR (RS) Latch

The Set-Reset (SR) Latch is the most fundamental memory cell. It can store 1 bit of information. 

### Basic Concept
It has two inputs: **S (Set)** to store a '1', and **R (Reset)** to store a '0'. It has two outputs: $Q$ and its complement $\overline{Q}$. 

> **Definition**  
> A **Latch** is a level-sensitive memory element that changes state continuously as long as the enable signal is active.

### Using NOR Gates
An active-high SR latch is constructed using two cross-coupled NOR gates. 

```text
          S ───────┬───\
                   │    \ 
                   │ NOR ├──────┬──── Q
               ┌───┴───/        │
               │                │
               └────────────────┤
                                │
               ┌────────────────┘
               │                
               ├───┬───\        │
               │   │    \       │
          R ───┼───┤ NOR ├──────┴──── Q' (Q-bar)
               │   └───/
               │
```

**Truth Table (NOR Latch)**

| S | R | $Q_{next}$ | $\overline{Q}_{next}$ | State |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | $Q_{prev}$ | $\overline{Q}_{prev}$ | Hold (No Change) |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 0 | 1 | 0 | Set |
| 1 | 1 | 0 | 0 | **Invalid (Race Condition)** |

> [!WARNING]
> **⚠️ NEC Exam Trap:** For a NOR-based SR latch, the inputs are active-high. S=1, R=1 is the invalid state because it forces both $Q$ and $\overline{Q}$ to 0, which violates the condition that they must be complements.

### Using NAND Gates
An active-low $\overline{S}\overline{R}$ latch is constructed using two cross-coupled NAND gates.

```text
          S' ──────┬───\
                   │    \ 
                   │ NAND o─────┬──── Q
               ┌───┴───/        │
               │                │
               └────────────────┤
                                │
               ┌────────────────┘
               │                
               ├───┬───\        │
               │   │    \       │
          R' ──┼───┤ NAND o─────┴──── Q'
               │   └───/
               │
```

**Truth Table (NAND Latch)**

| $\overline{S}$ | $\overline{R}$ | $Q_{next}$ | $\overline{Q}_{next}$ | State |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | $Q_{prev}$ | $\overline{Q}_{prev}$ | Hold (No Change) |
| 1 | 0 | 0 | 1 | Reset |
| 0 | 1 | 1 | 0 | Set |
| 0 | 0 | 1 | 1 | **Invalid (Race Condition)** |

### Characteristic Equation
The behavior of the SR latch can be summarized mathematically:
$$ Q_{next} = S + \overline{R} \cdot Q_{prev} $$
**Constraint:** $S \cdot R = 0$ (S and R cannot both be 1 simultaneously).

| Symbol | Meaning | 
| :--- | :--- | 
| $Q_{next}$ | Next state of the output | 
| $Q_{prev}$ | Present state of the output | 
| $S$ | Set input | 
| $R$ | Reset input | 

### Timing Diagram
A timing diagram shows how the outputs respond to inputs over time. 

```text
S : ____|¯¯¯¯|_________|¯¯¯¯|____
R : ________________|¯¯¯¯|_______
Q : ____|¯¯¯¯¯¯¯¯¯¯¯|________|¯¯¯
```

---

## 2.3.3 Gated (Clocked) SR Flip-Flop

A simple SR latch responds to inputs instantly. To synchronize it, we add an Enable (EN) or Clock (CLK) input.

### Circuit Diagram
By adding two AND gates (or NAND gates) before the latch, we can control *when* the latch sees the inputs.

```text
       S ────┬────\
             │ AND ├───── S* (To SR Latch)
     CLK ────┤────/
             │
             │────\
       R ────┤ AND ├───── R* (To SR Latch)
             │────/
```

### Truth Table (Clocked)

| CLK | S | R | $Q_{next}$ | State |
| :--- | :--- | :--- | :--- | :--- |
| 0 | X | X | $Q_{prev}$ | Hold (Disabled) |
| 1 | 0 | 0 | $Q_{prev}$ | Hold (Enabled) |
| 1 | 0 | 1 | 0 | Reset |
| 1 | 1 | 0 | 1 | Set |
| 1 | 1 | 1 | ? | Invalid |

### Eliminating Unwanted Transitions
When $CLK = 0$, the outputs of the AND gates are forced to 0 (for NOR latch), acting like $S=0, R=0$. The latch holds its state. This gating mechanism prevents noise or asynchronous input changes from affecting the output until the clock goes high.

---

## 2.3.4 D Flip-Flop (Data/Delay Flip-Flop)

The D flip-flop ensures the invalid $S=R=1$ condition never occurs by ensuring S and R are always complements of each other.

### Circuit Derivation
Connect the D input directly to S, and connect an inverted D to R.

```text
       D ──┬───────────── S (To Gated Latch)
           │
           └───|>o─────── R (To Gated Latch)
```

### Truth Table and Characteristic Equation

| CLK | D | $Q_{next}$ | State |
| :--- | :--- | :--- | :--- |
| 0 | X | $Q_{prev}$ | Hold |
| 1 | 0 | 0 | Reset (Q follows D) |
| 1 | 1 | 1 | Set (Q follows D) |

**Characteristic Equation:**
$$ Q_{next} = D $$

> [!TIP]
> **💡 Engineering Intuition:** The D flip-flop is the workhorse of digital design. It simply samples the input D at the clock edge and holds it until the next edge. It acts as a 1-bit delay ($Q$ follows $D$ with a delay of one clock cycle).

### Edge-Triggered D Flip-Flop
Instead of being transparent while CLK=1 (level-sensitive), edge-triggered D flip-flops only capture data at the precise moment the clock transitions (e.g., from 0 to 1). This is vital for shift registers and synchronous counters to prevent data from rippling through multiple stages in a single clock cycle.

### Applications
*   **Data Storage:** Registers in CPUs.
*   **Delay Lines:** Introducing a known time delay.
*   **Pipeline Registers:** Holding intermediate data in microprocessors.

---

## 2.3.5 JK Flip-Flop

The JK flip-flop improves on the SR flip-flop by defining a useful behavior for the invalid $1,1$ state.

### Circuit Derivation
It feeds the outputs $Q$ and $\overline{Q}$ back to the input AND gates.
*   $S = J \cdot \overline{Q}_{prev}$
*   $R = K \cdot Q_{prev}$

### Truth Table

| CLK | J | K | $Q_{next}$ | State |
| :--- | :--- | :--- | :--- | :--- |
| $\uparrow$ | 0 | 0 | $Q_{prev}$ | Hold |
| $\uparrow$ | 0 | 1 | 0 | Reset |
| $\uparrow$ | 1 | 0 | 1 | Set |
| $\uparrow$ | 1 | 1 | $\overline{Q}_{prev}$ | **Toggle** |

### Characteristic Equation
$$ Q_{next} = J \cdot \overline{Q}_{prev} + \overline{K} \cdot Q_{prev} $$

### Toggle Mode (J=K=1)
When both J and K are 1, the flip-flop complements its present state. If it was 0, it becomes 1; if 1, it becomes 0. This is the foundation of digital counters.

> [!WARNING]
> **⚠️ NEC Exam Trap:** In a level-triggered JK flip-flop, if J=K=1 and the clock remains high for longer than the propagation delay, the output will continuously toggle, leading to an unpredictable final state. This is called the **Race-Around Condition**. Edge-triggering or Master-Slave configurations solve this.

### Excitation Table
While a truth table gives $Q_{next}$ based on current inputs, an excitation table gives the required inputs to achieve a desired state transition. **Critical for counter design.**

| $Q_{prev}$ | $Q_{next}$ | J | K |
| :--- | :--- | :--- | :--- |
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | X |
| 1 | 0 | X | 1 |
| 1 | 1 | X | 0 |
*(X = Don't Care)*

---

## 2.3.6 T Flip-Flop (Toggle Flip-Flop)

The T flip-flop is a simplified JK flip-flop with its inputs tied together.

### Derivation
Connect $J = K = T$. 

### Truth Table and Characteristic Equation

| T | $Q_{prev}$ | $Q_{next}$ | State |
| :--- | :--- | :--- | :--- |
| 0 | 0 | 0 | Hold |
| 0 | 1 | 1 | Hold |
| 1 | 0 | 1 | Toggle |
| 1 | 1 | 0 | Toggle |

**Characteristic Equation:**
$$ Q_{next} = T \oplus Q_{prev} = T \cdot \overline{Q}_{prev} + \overline{T} \cdot Q_{prev} $$

### Application
*   **Frequency Division:** A T flip-flop with T=1 divides the clock frequency by 2.
*   **Counters:** Binary ripple counters are built using cascaded T flip-flops.

---

## 2.3.7 Edge-Triggered vs Level-Triggered

### Comparison

| Feature | Level-Triggered (Latch) | Edge-Triggered (Flip-Flop) |
| :--- | :--- | :--- |
| **Sensitivity** | Sensitive to the voltage level (high or low) of the clock | Sensitive to the transition (rising or falling edge) of the clock |
| **Transparency** | Output can change multiple times as long as clock is active | Output changes only once per clock cycle |
| **Symbol** | No triangle at clock input | Triangle ($\triangleright$) at clock input |
| **Use Case** | Fast, simple local memory | Strict synchronous systems (CPUs) |

### Timing Parameters Definition
To function correctly, edge-triggered flip-flops require the input data to be stable around the clock edge.

> **Definition: Setup Time ($t_{su}$)**  
> The minimum time the input data must be stable *before* the clock edge.

> **Definition: Hold Time ($t_{h}$)**  
> The minimum time the input data must remain stable *after* the clock edge.

> **Definition: Propagation Delay ($t_{pd}$)**  
> The time taken for the output to change after the clock edge occurs.

> [!CAUTION]
> Violating setup or hold time leads to **metastability**, where the flip-flop output hovers in an indeterminate voltage state between 0 and 1, potentially crashing the digital system.

### Worked Example 1: Max Clock Frequency
**Problem:** A digital circuit uses D flip-flops with a setup time $t_{su} = 2\text{ ns}$, a hold time $t_{h} = 1\text{ ns}$, and a propagation delay $t_{pd} = 4\text{ ns}$. The combinational logic delay between them is $t_{comb} = 5\text{ ns}$. Calculate the maximum clock frequency.

**Solution:**
1.  **Given:** 
    $t_{su} = 2\text{ ns}$
    $t_{pd} = 4\text{ ns}$
    $t_{comb} = 5\text{ ns}$
2.  **Formula:** The minimum clock period $T_{min}$ must satisfy:

$$ T_{min} \ge t_{pd} + t_{comb} + t_{su} $$
3.  **Substitution:**

$$ T_{min} \ge 4\text{ ns} + 5\text{ ns} + 2\text{ ns} = 11\text{ ns} $$
4.  **Answer:** 
    Maximum Frequency $f_{max} = \frac{1}{T_{min}} = \frac{1}{11 \times 10^{-9}} \approx 90.9\text{ MHz}$
5.  **Engineering Interpretation:** The clock cannot run faster than 90.9 MHz, otherwise the data will arrive at the next flip-flop too late to meet the setup time requirement.

---

## 2.3.8 Master-Slave Flip-Flop

The Master-Slave (MS) configuration is a classic solution to the race-around condition in level-triggered JK flip-flops.

### Construction
It consists of two gated SR (or JK) latches connected in series. 
*   **Master:** Driven by the normal clock (CLK).
*   **Slave:** Driven by the inverted clock ($\overline{CLK}$).

```text
           Master Stage                   Slave Stage
         ┌──────────────┐               ┌──────────────┐
 J ─────►│              │       Q_m    │              │─────► Q
         │  JK Latch    ├─────────────►│  SR Latch    │
 K ─────►│              │       Q_m'   │              │─────► Q'
         └───▲──────────┘               └───▲──────────┘
             │                              │
CLK ─────────┴─────────────|>o──────────────┘
                          Inverter
```

### Operation
1.  **Positive Half Cycle (CLK = 1):** The Master is enabled and responds to J and K inputs. The Slave is disabled (clock is 0) and holds its previous output.
2.  **Negative Half Cycle (CLK = 0):** The Master is disabled and locks in its state. The Slave is enabled and copies the Master's state to the final output Q.

### Solving the Race-Around Problem
Since the slave only updates when the master is locked out from inputs, the final output changes only once per clock cycle (on the falling edge), completely eliminating race-around.

> [!WARNING]
> **⚠️ NEC Exam Trap: 1's Catching Problem**
> Master-Slave JK flip-flops suffer from "1's catching" (or "0's catching"). If a noise spike forces J=1 briefly while CLK=1, the master sets. Since the master cannot be reset (unless K=1), it "catches" the 1 and transfers it to the slave on the falling edge, even if the input was unintended. Modern edge-triggered flip-flops don't have this issue.

---

## 2.3.9 Flip-Flop Conversion

Converting one type of flip-flop to another involves designing combinational logic that maps the available inputs to the target inputs.

### General Procedure
1.  Write the characteristic table of the required (target) flip-flop.
2.  Write the excitation table of the available (source) flip-flop.
3.  Combine them to find the required inputs for the source flip-flop.
4.  Use K-maps to simplify the boolean expressions.
5.  Draw the final logic circuit.

### Worked Example 2: Convert SR Flip-Flop to JK Flip-Flop

**1. Define Goal:** We have an SR flip-flop, but we want it to act like a JK flip-flop.
**2. Combined Table:**

| $Q_p$ (Present) | J | K | $Q_n$ (Next, desired for JK) | S (Required for SR) | R (Required for SR) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | 0 | 0 (Hold) | 0 | X |
| 0 | 0 | 1 | 0 (Reset) | 0 | X |
| 0 | 1 | 0 | 1 (Set) | 1 | 0 |
| 0 | 1 | 1 | 1 (Toggle) | 1 | 0 |
| 1 | 0 | 0 | 1 (Hold) | X | 0 |
| 1 | 0 | 1 | 0 (Reset) | 0 | 1 |
| 1 | 1 | 0 | 1 (Set) | X | 0 |
| 1 | 1 | 1 | 0 (Toggle) | 0 | 1 |

**3. K-map Simplification:**
*   For S: K-map of S over $(Q_p, J, K)$ yields $S = J \cdot \overline{Q_p}$
*   For R: K-map of R over $(Q_p, J, K)$ yields $R = K \cdot Q_p$

**4. Circuit:** This exactly matches the internal feedback derivation of the JK flip-flop we saw earlier! We place two AND gates before the S and R inputs.

---

## 2.3.10 Registers

A single flip-flop stores 1 bit. To store N bits of data (e.g., an 8-bit byte), we cascade N flip-flops to create a **Register**.

### Types of Shift Registers
Data can be moved in and out of registers serially (one bit at a time) or in parallel (all bits at once).

1.  **SISO (Serial-In, Serial-Out):**
    Data goes in 1 bit per clock cycle, and comes out 1 bit per clock cycle. Used for introducing delay.
    ```text
    Data In ──►[ FF1 ]──►[ FF2 ]──►[ FF3 ]──►[ FF4 ]──► Data Out
    ```

2.  **SIPO (Serial-In, Parallel-Out):**
    Data is shifted in serially, but all bits can be read simultaneously. 
    ```text
    Data In ──►[ FF1 ]──►[ FF2 ]──►[ FF3 ]──►[ FF4 ]
                  │        │        │        │
                  ▼        ▼        ▼        ▼
                  Q0       Q1       Q2       Q3 (Parallel Out)
    ```

3.  **PISO (Parallel-In, Serial-Out):**
    Data is loaded all at once, then shifted out 1 bit per clock.

4.  **PIPO (Parallel-In, Parallel-Out):**
    Data is loaded all at once and read all at once. Used for temporary data storage (e.g., CPU data registers).

---

## 🔧 2.3.11 Shift Register Applications

*   **Serial-to-Parallel Conversion:** Using SIPO, communication protocols like UART or SPI take a single incoming data wire and convert it into a parallel byte for the CPU.
*   **Parallel-to-Serial Conversion:** Using PISO, the CPU can send an 8-bit byte over a single wire (USB, Ethernet).
*   **Ring Counter:** The output of a shift register is fed back to the input. If a single '1' is pre-loaded, it circulates infinitely. (Modulo-N counter).
*   **Johnson (Twisted Ring) Counter:** The *inverted* output of the last flip-flop is fed back to the input. An N-bit Johnson counter produces 2N states (Modulo-2N counter).
*   **Sequence Generator / PRNG:** Using XOR feedback, shift registers can generate pseudo-random bit sequences (Linear Feedback Shift Registers - LFSRs).

### Worked Example 3: Johnson Counter States
**Problem:** Determine the state sequence of a 3-bit Johnson counter initially cleared to 000.

**Solution:**
A 3-bit Johnson counter feeds $\overline{Q_2}$ back to $D_0$. 
Equation: $D_0 = \overline{Q_2}$, $D_1 = Q_0$, $D_2 = Q_1$

| Clock Pulse | $Q_0$ | $Q_1$ | $Q_2$ | $\overline{Q_2}$ (Next $D_0$) |
| :--- | :--- | :--- | :--- | :--- |
| Init | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 2 | 1 | 1 | 0 | 1 |
| 3 | 1 | 1 | 1 | 0 |
| 4 | 0 | 1 | 1 | 0 |
| 5 | 0 | 0 | 1 | 0 |
| 6 | 0 | 0 | 0 | 1 (Repeats) |

**Answer:** Sequence is 000 → 100 → 110 → 111 → 011 → 001 → 000. It has $2 \times 3 = 6$ states (MOD-6).

---

## 2.3.12 Asynchronous (Ripple) Counters

In asynchronous counters, the clock signal is applied only to the first flip-flop. The output of each flip-flop acts as the clock for the next one. The signal "ripples" through the counter.

### MOD-N Counters
A counter with N flip-flops can count up to $2^N$ states (e.g., 3 FFs = $2^3 = 8$ states = MOD-8 counter).

*   **Up Counter:** Connect $Q$ to the clock of the next stage (using negative-edge triggered FFs).
*   **Down Counter:** Connect $\overline{Q}$ to the clock of the next stage (using negative-edge triggered FFs).

### The Ripple Problem (Propagation Delay)
Because the clock is not simultaneous, the delays of each flip-flop add up. 
Total Delay = $N \times t_{pd}$. 
If this total delay exceeds the clock period, the counter will output incorrect transitional states (glitches), limiting the maximum frequency heavily.

### Worked Example 4: Asynchronous MOD-6 Counter Design
**Problem:** Design an asynchronous MOD-6 counter (counts from 0 to 5, then resets to 0) using negative edge-triggered T flip-flops with active-low asynchronous clear ($\overline{CLR}$).

**Solution:**
1.  **Number of FFs:** Since $2^2 < 6 \le 2^3$, we need 3 flip-flops (MOD-8 base).
2.  **Count Sequence:** 000, 001, 010, 011, 100, 101. On state 6 (110), it must instantly reset to 000.
3.  **Reset Logic:** We need to trigger the $\overline{CLR}$ pins when the count hits 6 ($Q_2=1, Q_1=1, Q_0=0$). 
    Using a NAND gate: Output = $\overline{Q_2 \cdot Q_1}$. 
4.  **Circuit Connection:**
    *   $T_0 = T_1 = T_2 = 1$ (Toggle mode).
    *   CLK goes to FF0.
    *   $Q_0$ goes to CLK of FF1.
    *   $Q_1$ goes to CLK of FF2.
    *   NAND output goes to all $\overline{CLR}$ pins.
5.  **Engineering Interpretation:** The counter temporarily enters state 110 for a tiny fraction of a nanosecond before the NAND gate clears all flip-flops. This glitch is a major disadvantage of asynchronous mod-N counters.

---

## 2.3.13 Synchronous Counters

In synchronous counters, the **global clock is applied simultaneously to all flip-flops**. This completely eliminates the cumulative ripple delay, allowing much faster clock speeds. 

### Concept
Since all clocks trigger at once, combinational logic (using J and K inputs) determines which flip-flops should toggle on the *next* clock edge.

### Design Procedure (5 Steps)
1.  **State Diagram / State Table:** Define the desired sequence.
2.  **Determine Number of FFs:** $N \ge \log_2(\text{States})$.
3.  **Excitation Table:** Use the flip-flop excitation table to determine required inputs for each state transition.
4.  **K-Maps:** Derive simplified boolean expressions for every input (e.g., $J_0, K_0, J_1, K_1$).
5.  **Circuit Design:** Draw the combinational logic driving the flip-flops.

### Advantages over Asynchronous
| Feature | Asynchronous (Ripple) | Synchronous |
| :--- | :--- | :--- |
| **Clocking** | Serial (chained) | Parallel (simultaneous) |
| **Speed/Frequency** | Low (cumulative delay) | High (delay = $1 \times t_{pd} + t_{comb}$) |
| **Glitches/Decoding** | High probability of glitches | Clean state transitions |
| **Circuit Complexity** | Simple | Complex (needs extra gates) |

> [!TIP]
> **💡 Engineering Intuition:** If you need a simple divide-by-256 frequency divider, use an asynchronous counter (easy to build). If you need a precise 8-bit memory address counter for a CPU, you *must* use a synchronous counter.

### Worked Example 5: Synchronous MOD-5 Counter
**Problem:** Design a synchronous MOD-5 counter (000 → 001 → 010 → 011 → 100 → 000) using JK flip-flops.

**Solution:**
**Step 1 & 2:** 5 states require 3 flip-flops ($Q_2, Q_1, Q_0$).
**Step 3: State & Excitation Table**
(Using JK Excitation: 0→0=0X, 0→1=1X, 1→0=X1, 1→1=X0)

| Present ($Q_2 Q_1 Q_0$) | Next ($Q_2 Q_1 Q_0$) | $J_2 K_2$ | $J_1 K_1$ | $J_0 K_0$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 0 0 | 0 0 1 | 0 X | 0 X | 1 X |
| 0 0 1 | 0 1 0 | 0 X | 1 X | X 1 |
| 0 1 0 | 0 1 1 | 0 X | X 0 | 1 X |
| 0 1 1 | 1 0 0 | 1 X | X 1 | X 1 |
| 1 0 0 | 0 0 0 | X 1 | 0 X | 0 X |
| Others (101,110,111) | d d d (Don't Care) | X X | X X | X X |

**Step 4: K-map Simplification** (Skipping grid drawing for brevity)
Solving K-maps for J2, K2, J1, K1, J0, K0 treating 101, 110, 111 as Don't Cares (X):
*   $J_0 = \overline{Q_2}$
*   $K_0 = 1$
*   $J_1 = Q_0$
*   $K_1 = Q_0$
*   $J_2 = Q_1 \cdot Q_0$
*   $K_2 = 1$

**Step 5: Implementation (Logic)**
*   All FFs receive the same global CLK.
*   Connect logic gates exactly as per the K-map equations above. For instance, tie $K_0$ and $K_2$ directly to VCC (Logic 1).
