# Section 2.6: Interrupt Operations (AExE0206)

## 📖 Introduction
Interrupts are one of the most critical concepts in microprocessor architecture and real-time systems. They provide a mechanism for external devices to immediately grab the microprocessor's attention, pausing its current execution to handle an urgent task before resuming. This section covers the fundamental theory of interrupts, the specific interrupt structure of the 8085 microprocessor, the execution sequence of an Interrupt Service Routine (ISR), and the critical SIM/RIM instructions.

## 1. Interrupt Concept

### Basic Concept
An **interrupt** is an asynchronous signal sent to the microprocessor (by hardware or software) indicating that an event needs immediate attention. When an interrupt occurs, the microprocessor suspends its current main program, executes a special subroutine called the Interrupt Service Routine (ISR) to handle the event, and then returns to the main program exactly where it left off.

> [!NOTE]  
> **Analogy:** Imagine reading a book (main program) when your phone rings (interrupt). You put a bookmark on the page (save address in Stack), answer the call (execute ISR), and when the call is over, you return to reading your book from the bookmarked page.

### Definition
> An **interrupt** is a condition that halts the microprocessor temporarily to work on a different task and then return to its previous task.

### Polling vs. Interrupt-Driven I/O

| Feature | Polling | Interrupt-Driven I/O |
|---------|---------|----------------------|
| **Definition** | CPU continuously checks device status. | Device alerts the CPU when it needs service. |
| **CPU Efficiency** | Low (CPU wastes time checking). | High (CPU executes other tasks until interrupted). |
| **Response Time** | Slow (Depends on loop execution). | Fast (Immediate attention). |
| **Hardware Setup** | Simple. | Complex (Requires interrupt lines). |
| **Use Case** | Slow devices, simple systems. | Real-time systems, time-critical tasks. |

## 📚 2. Types of Interrupts in the 8085 Microprocessor

The 8085 microprocessor has a robust interrupt system, classified into **Hardware** and **Software** interrupts.

### 2.1 Hardware Interrupts
There are 5 physical hardware interrupt pins on the 8085: TRAP, RST 7.5, RST 6.5, RST 5.5, and INTR.

1. **TRAP (RST 4.5):**
   - **Type:** Non-maskable (cannot be disabled by DI instruction).
   - **Triggering:** Edge and Level triggered (must go HIGH and stay HIGH until acknowledged).
   - **Priority:** Highest (1st).
   - **Vector Address:** $0024H$.
   - **Usage:** Catastrophic events like power failure or emergency shut-down.

2. **RST 7.5:**
   - **Type:** Maskable.
   - **Triggering:** Positive Edge triggered (stores request in an internal flip-flop).
   - **Priority:** 2nd.
   - **Vector Address:** $003CH$.

3. **RST 6.5:**
   - **Type:** Maskable.
   - **Triggering:** Level triggered.
   - **Priority:** 3rd.
   - **Vector Address:** $0034H$.

4. **RST 5.5:**
   - **Type:** Maskable.
   - **Triggering:** Level triggered.
   - **Priority:** 4th.
   - **Vector Address:** $002CH$.

5. **INTR:**
   - **Type:** Maskable, Non-vectored.
   - **Triggering:** Level triggered.
   - **Priority:** Lowest (5th).
   - **Vector Address:** Determined by external hardware (e.g., 8259 PIC) sending a CALL or RST instruction during the $\overline{INTA}$ cycle.

### 2.2 Software Interrupts
The 8085 has 8 software interrupts, `RST 0` through `RST 7`, which are 1-byte instructions. They are inserted into the program to trigger an interrupt manually.

#### Vector Address Calculation Formula
The vector address for any RST $n$ instruction (hardware or software) is calculated as:
$$ \text{Vector Address (in Hex)} = n \times 0008H $$

For example, for RST 7.5:
$7.5 \times 8 = 60_{10}$
$60_{10}$ in Hex is $3CH$. Thus, the vector address is $003CH$.

### Comparison of 8085 Hardware Interrupts

| Interrupt | Maskable? | Vectored? | Trigger Type | Priority | Vector Address |
|-----------|-----------|-----------|--------------|----------|----------------|
| **TRAP** | No | Yes | Edge + Level | 1 (Highest)| $0024H$ |
| **RST 7.5**| Yes | Yes | Edge | 2 | $003CH$ |
| **RST 6.5**| Yes | Yes | Level | 3 | $0034H$ |
| **RST 5.5**| Yes | Yes | Level | 4 | $002CH$ |
| **INTR** | Yes | No | Level | 5 (Lowest) | Ext. Hardware |

> [!WARNING]  
> **Exam Tip:** Remember that TRAP is also known as **RST 4.5**. Do not get confused if an exam question uses "RST 4.5" instead of TRAP.

## 3. Interrupt Service Routine (ISR)

When an interrupt occurs, the microprocessor jumps to an **Interrupt Service Routine (ISR)**. An ISR is a subroutine written by the programmer to handle the specific interrupt.

### Actions Performed Upon Entering the ISR
1. **Save Context:** The main program's context must be saved so it can be resumed later. The microprocessor automatically saves the Program Counter (PC) on the Stack.
2. **Save Registers:** The programmer must push the accumulator, flags, and other used registers onto the Stack at the beginning of the ISR.
3. **Execute:** The actual logic of the interrupt task is performed.
4. **Restore Context:** The saved registers are popped from the Stack in reverse order.
5. **Enable Interrupts:** Use the `EI` instruction to re-enable interrupts (as they are automatically disabled when an interrupt is acknowledged).
6. **Return:** Use the `RET` instruction to pop the PC back from the Stack and return to the main program.

### Example ISR Structure
```assembly
; ISR for RST 7.5 at address 003CH
ORG 003CH
    JMP ISR_7_5    ; Space is limited (only 8 bytes between vectors), so jump to main ISR

ORG 2000H          ; Main ISR code
ISR_7_5:
    PUSH PSW       ; Save Accumulator and Flags
    PUSH B         ; Save BC register pair
    
    ; ... [Interrupt handling logic here] ...
    
    POP B          ; Restore BC
    POP PSW        ; Restore Accumulator and Flags
    EI             ; Re-enable interrupts
    RET            ; Return to main program
```

## 4. Interrupt Processing Sequence

### Step-by-Step Execution
When a valid interrupt signal arrives:
1. The CPU finishes the **current instruction** it is executing.
2. It checks the interrupt lines at the **last T-state** of the last machine cycle of the instruction.
3. If an interrupt is active (and enabled/unmasked), the CPU initiates an **Interrupt Acknowledge Cycle** (for INTR) or directly pushes the PC to the stack (for vectored interrupts).
4. The internal **Interrupt Enable Flip-Flop (INTE)** is reset, disabling all further maskable interrupts.
5. The CPU branches to the vector address.
6. The ISR executes.
7. The `RET` instruction at the end of the ISR pops the return address from the stack to the PC, resuming main execution.

### Interrupt Enable / Disable Instructions
- **EI (Enable Interrupts):** Sets the INTE flip-flop to 1. All maskable interrupts are enabled.
- **DI (Disable Interrupts):** Resets the INTE flip-flop to 0. All maskable interrupts (RST 7.5, 6.5, 5.5, INTR) are disabled. TRAP is unaffected.

### ASCII Flowchart of Interrupt Processing

```text
              [ Main Program Executing ]
                         |
                         v
              (Check for Interrupts at 
               end of current instruction)
                         |
           +-------------+-------------+
           |                           |
        No Interrupt             Interrupt Exists
           |                           |
           v                           v
     [Continue Main]          Is INTE = 1? (Or is it TRAP?)
                                       |
                                +------+------+
                                |             |
                                No           Yes
                                |             |
                                v             v
                          [Continue Main] [Acknowledge Interrupt]
                                              |
                                              v
                                       Push PC to Stack
                                              |
                                              v
                                       Disable Interrupts (INTE=0)
                                              |
                                              v
                                       Load PC with Vector Addr.
                                              |
                                              v
                                       [ Execute ISR ]
                                              |
                                              v
                                       Pop PC from Stack (RET)
                                              |
                                              v
                                     [ Return to Main Program ]
```

## 5. SIM and RIM Instructions (Crucial for Exam)

The 8085 provides two special, multi-purpose instructions for manipulating interrupts and serial I/O: **SIM (Set Interrupt Mask)** and **RIM (Read Interrupt Mask)**.

### 5.1 SIM (Set Interrupt Mask)
The SIM instruction is a 1-byte instruction used to:
1. Mask or unmask RST 7.5, 6.5, and 5.5.
2. Reset the pending RST 7.5 flip-flop.
3. Output serial data on the SOD pin.

Before executing `SIM`, you must load a specific 8-bit pattern into the **Accumulator**.

#### SIM Accumulator Bit Pattern

| D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 |
|----|----|----|----|----|----|----|----|
| **SOD** | **SDE** | **X** | **R7.5** | **MSE** | **M7.5** | **M6.5** | **M5.5** |

- **D0 (M5.5):** Mask bit for RST 5.5 (1 = Masked/Disabled, 0 = Unmasked/Enabled)
- **D1 (M6.5):** Mask bit for RST 6.5 (1 = Masked, 0 = Unmasked)
- **D2 (M7.5):** Mask bit for RST 7.5 (1 = Masked, 0 = Unmasked)
- **D3 (MSE):** Mask Set Enable (Must be 1 to apply changes to D0, D1, D2. If 0, mask bits are ignored).
- **D4 (R7.5):** Reset RST 7.5 (If 1, resets the internal RST 7.5 flip-flop, clearing pending interrupts).
- **D5 (X):** Don't care (usually set to 0).
- **D6 (SDE):** Serial Data Enable (Must be 1 to output data from D7).
- **D7 (SOD):** Serial Output Data (The actual bit to be transmitted serially).

### 5.2 RIM (Read Interrupt Mask)
The RIM instruction is used to:
1. Read the current status of interrupt masks.
2. Check for pending interrupts.
3. Read the status of the INTE flip-flop.
4. Read serial data from the SID pin.

When `RIM` is executed, it loads an 8-bit pattern into the **Accumulator**.

#### RIM Accumulator Bit Pattern

| D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 |
|----|----|----|----|----|----|----|----|
| **SID** | **I7.5** | **I6.5** | **I5.5** | **IE** | **M7.5** | **M6.5** | **M5.5** |

- **D0 (M5.5):** Mask status of RST 5.5 (1 = Masked, 0 = Unmasked)
- **D1 (M6.5):** Mask status of RST 6.5 (1 = Masked, 0 = Unmasked)
- **D2 (M7.5):** Mask status of RST 7.5 (1 = Masked, 0 = Unmasked)
- **D3 (IE):** Interrupt Enable flag status (1 = Interrupts enabled, 0 = disabled)
- **D4 (I5.5):** Pending status of RST 5.5 (1 = Pending, 0 = Not pending)
- **D5 (I6.5):** Pending status of RST 6.5 (1 = Pending)
- **D6 (I7.5):** Pending status of RST 7.5 (1 = Pending)
- **D7 (SID):** Serial Input Data (The bit read from the SID pin).

> [!IMPORTANT]  
> **Pending Interrupts:** A pending interrupt is an interrupt request that has been received by the CPU but has not yet been serviced because interrupts are currently masked or disabled.

## 🔍 6. Worked Examples

### Example 1: Configuring Interrupts with SIM
**Problem:** Write a sequence of instructions to enable RST 7.5 and RST 5.5, while masking RST 6.5. Do not affect serial data.

**Solution:**
We need to form the control byte for the Accumulator before calling SIM.
- D7 (SOD) = 0
- D6 (SDE) = 0 (Serial data disabled)
- D5 (X) = 0
- D4 (R7.5) = 0 (No need to reset flip-flop)
- D3 (MSE) = 1 (Must be 1 to enable mask modification)
- D2 (M7.5) = 0 (Unmask RST 7.5)
- D1 (M6.5) = 1 (Mask RST 6.5)
- D0 (M5.5) = 0 (Unmask RST 5.5)

Binary Pattern: `0000 1010` = `0AH`

```assembly
EI          ; Enable global interrupts first
MVI A, 0AH  ; Load the control byte
SIM         ; Apply the masks
```

### Example 2: Checking Pending Interrupts with RIM
**Problem:** Write a program to check if RST 6.5 is pending. If it is, output `FFH` to port `01H`; otherwise, output `00H`.

**Solution:**
We use `RIM` and check bit D5 (I6.5).

```assembly
        RIM           ; Read interrupt status into Accumulator
        ANI 20H       ; Mask all bits except D5 (0010 0000 = 20H)
        JZ  NOT_PEND  ; If result is 0, D5 was 0 (not pending)
        MVI A, FFH    ; If pending, load FFH
        JMP OUTPUT
NOT_PEND: 
        MVI A, 00H    ; If not pending, load 00H
OUTPUT: 
        OUT 01H       ; Output result to port 01H
        HLT
```

### Example 3: Serial Data Output using SIM
**Problem:** Output a logic 1 on the Serial Output Data (SOD) line using SIM, without changing existing interrupt masks.

**Solution:**
- D7 (SOD) = 1 (Data to output)
- D6 (SDE) = 1 (Enable serial output)
- D5 (X) = 0
- D4 (R7.5) = 0
- D3 (MSE) = 0 (Crucial: Prevents changing interrupt masks)
- D2, D1, D0 = Don't care (0)

Binary Pattern: `1100 0000` = `C0H`

```assembly
MVI A, C0H
SIM
```

## 7. Chapter 2 Summary: Digital Logic and Microprocessor

As this concludes Chapter 2, here is a comprehensive review of the entire module for the NEC License Exam:

1. **Digital Logic (§2.1-2.3):**
   - **Combinational Circuits:** Multiplexers, Decoders, Adders. Output depends purely on current inputs.
   - **Sequential Circuits:** Flip-Flops (SR, D, JK, T), Registers, Counters (Synchronous/Asynchronous). Output depends on inputs and previous state (memory).
   - *Key Exam Focus:* Boolean simplification, Flip-flop truth tables, Counter modulo calculations.

2. **8085 Microprocessor Architecture (§2.4):**
   - 8-bit CPU, 16-bit address bus ($64$ KB memory).
   - **Registers:** Accumulator (A), B, C, D, E, H, L, SP, PC.
   - **Flags:** Sign, Zero, Auxiliary Carry, Parity, Carry (SZ-APC).
   - **Instruction Cycle:** Opcode Fetch, Memory Read, Memory Write, I/O Read, I/O Write.
   - *Key Exam Focus:* Flag conditions after ALU operations, Addressing modes (Immediate, Register, Direct, Indirect), T-states.

3. **Memory & I/O Interfacing (§2.5):**
   - Address decoding (using 3-to-8 decoders like 74LS138).
   - Memory mapped I/O vs. I/O mapped I/O.
   - **8255 PPI:** Modes 0, 1, and 2. Control word configuration.
   - **8237 DMA:** Direct Memory Access for fast bulk data transfer without CPU intervention (HOLD/HLDA).
   - *Key Exam Focus:* 8255 Control Word format, DMA transfer cycles.

4. **Interrupt Operations (§2.6):**
   - **Interrupts:** TRAP, RST 7.5, 6.5, 5.5, INTR.
   - **Vector Addresses:** Calculated as $n \times 8$.
   - **SIM/RIM:** Control byte formats.
   - *Key Exam Focus:* SIM/RIM bits, Interrupt Priority, TRAP characteristics.

---
## ✏️ 8. Practice Problems for Exam Preparation

1. **Which of the following interrupts is non-maskable in the 8085 microprocessor?**
   a) RST 7.5
   b) INTR
   c) TRAP
   d) RST 5.5
   *Answer: c) TRAP*

2. **What is the vector address of RST 6.5?**
   a) $002CH$
   b) $0034H$
   c) $003CH$
   d) $0024H$
   *Answer: b) $0034H$ ($6.5 \times 8 = 52 = 34H$)*

3. **In the SIM instruction control byte, what is the purpose of bit D3 (MSE)?**
   a) Enables serial data output
   b) Enables changes to the interrupt mask bits (D0-D2)
   c) Resets the RST 7.5 flip-flop
   d) It is the mask bit for RST 5.5
   *Answer: b) Enables changes to the interrupt mask bits*

4. **Which instruction is used to read pending interrupts in the 8085?**
   a) SIM
   b) EI
   c) RIM
   d) INTR
   *Answer: c) RIM*

5. **When an interrupt occurs, what does the 8085 automatically save on the stack?**
   a) Accumulator
   b) Flag register
   c) Program Counter (PC)
   d) Stack Pointer (SP)
   *Answer: c) Program Counter (PC)*
