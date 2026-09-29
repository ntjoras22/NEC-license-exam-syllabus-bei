# Section 2.2: Combinational and Arithmetic Circuits (AExE0202)

## 📖 1. Introduction
Combinational logic circuits form the fundamental building blocks of modern digital systems, where the output depends solely on the current state of the inputs, without any memory elements. This section covers data routing circuits (Multiplexers/Demultiplexers), encoding/decoding circuits, and arithmetic circuits. These are heavily tested in the NEC Engineering License Exam as they are essential for microprocessor design and digital signal processing.

## ⚠️ 2. Why Is It Important?
- **Data Routing:** MUX and DEMUX are critical for time-division multiplexing (TDM) in communication systems.
- **ALU Design:** Adders and subtractors are the core components of the Arithmetic Logic Unit (ALU) in CPUs.
- **Memory Addressing:** Decoders are universally used for memory chip selection and address decoding.
- **Interface Design:** Encoders and decoders translate human-readable data (like decimal or keyboard inputs) into machine-readable binary code and vice versa.

---

## 💡 2.2.1 Multiplexer (MUX)

### Basic Concept
A multiplexer acts like a digitally controlled multi-position switch. It selects one of many input data lines and routes it to a single output line based on the value of the selection lines. 

### Definition
> **Multiplexer (MUX)** is a combinational logic circuit that selects one of $2^n$ data inputs and directs it to a single output, controlled by $n$ selection lines. It is also known as a **data selector**.

### Physical/Logical Meaning
Think of a MUX as a railway switch that routes multiple incoming tracks onto a single outgoing track. The selection lines are the levers that control which track gets connected to the main line.

### Mathematical Formulation
For $N$ input lines, there is $1$ output line, and $m$ selection lines such that:
$$ N = 2^m $$
The Boolean expression for a $2^m : 1$ MUX is the sum of minterms of selection lines ANDed with the corresponding input.

### 2:1 MUX
**Truth Table:**

| Selection (S) | Output (Y) |
| :---: | :---: |
| 0 | $I_0$ |
| 1 | $I_1$ |

**Boolean Expression:**
$$ Y = \overline{S}I_0 + S I_1 $$

**Circuit Diagram (ASCII):**
```text
      I0 ----|\
             | \
             |  |---- Y
      I1 ----| /
             |/
              |
              S
```

### 4:1 MUX
A 4-to-1 MUX has 4 inputs ($I_0, I_1, I_2, I_3$) and 2 select lines ($S_1, S_0$).

**Truth Table:**

| $S_1$ | $S_0$ | Output (Y) |
| :---: | :---: | :---: |
| 0 | 0 | $I_0$ |
| 0 | 1 | $I_1$ |
| 1 | 0 | $I_2$ |
| 1 | 1 | $I_3$ |

**Boolean Expression:**
$$ Y = \overline{S_1}\overline{S_0}I_0 + \overline{S_1}S_0 I_1 + S_1\overline{S_0}I_2 + S_1 S_0 I_3 $$

**Block Diagram (ASCII):**
```text
        _______
   I0 -|       |- Y
   I1 -|  4:1  |
   I2 -|  MUX  |
   I3 -|_______|
         |   |
        S1  S0
```

### 8:1 MUX Block Diagram
```text
        _______
   I0 -|       |- Y
   I1 -|       |
   I2 -|  8:1  |
   I3 -|  MUX  |
   I4 -|       |
   I5 -|       |
   I6 -|       |
   I7 -|_______|
        |  |  |
       S2 S1 S0
```

### Implementing Boolean Functions using MUX
A MUX can implement any Boolean function. An $n$-variable Boolean function can be implemented using a $2^{n-1} : 1$ MUX by using $n-1$ variables as selection lines and the remaining variable (and its complement, 0, or 1) as data inputs.

### MUX Tree
Larger MUXes can be built using smaller ones. For example, to build an 8:1 MUX using 4:1 MUXes, we need:
- Total MUXes = $\lceil 8/4 \rceil + \lceil 2/4 \rceil = 2 + 1 = 3$ (two 4:1 MUXes in first stage, one 2:1 MUX or half of a 4:1 MUX in second stage). Wait, usually it's $\frac{8}{4} = 2$, then $\frac{2}{4} = 0.5 \rightarrow 1$. Total = $2 + 1 = 3$. If we only have 4:1 MUX, we need two for inputs and one to select between the two outputs.

### Worked Example 1: Implement Boolean Function
**Given:** $F(A,B,C) = \sum m(1, 3, 5, 6)$
**Required:** Implement using a 4:1 MUX.

**Step 1:** We have 3 variables. A 4:1 MUX has 2 select lines. Let $S_1 = A, S_0 = B$.
**Step 2:** The remaining variable is $C$.
**Step 3:** Draw the implementation table.

| Inputs | $I_0$ | $I_1$ | $I_2$ | $I_3$ |
| :---: | :---: | :---: | :---: | :---: |
| $\overline{C}$ | 0 | 2 | 4 | (6) |
| $C$ | (1) | (3) | (5) | 7 |
| **Data In** | $C$ | $C$ | $C$ | $\overline{C}$ |

*Explanation:* For $I_0$ ($A=0, B=0$), minterms are 0 ($\overline{C}$) and 1 ($C$). Since minterm 1 is in $F$, $I_0 = C$. For $I_1$ ($A=0, B=1$), minterms are 2 and 3. Minterm 3 is present, so $I_1 = C$. For $I_2$, minterm 5 is present, so $I_2 = C$. For $I_3$, minterm 6 is present, so $I_3 = \overline{C}$.

**Answer:** Connect $I_0 = C, I_1 = C, I_2 = C, I_3 = \overline{C}$. Select lines $S_1=A, S_0=B$.

> [!WARNING]
> ⚠️ **NEC Exam Traps:** Always check which variables are assigned to the select lines. If you assign $B, C$ to select lines instead of $A, B$, the data inputs will be completely different!

> 💡 **Engineering Intuition:** A MUX is essentially a hardware lookup table (LUT). Modern FPGAs use exactly this principle—using MUXes to build logic cells that can implement any arbitrary logic function based on SRAM bits fed into the MUX data lines.

---

## 💡 2.2.2 Demultiplexer (DEMUX)

### Basic Concept
A demultiplexer does the exact opposite of a MUX. It takes a single input and routes it to one of many outputs.

### Definition
> **Demultiplexer (DEMUX)** is a logic circuit that takes a single input data line and distributes it to one of $2^n$ possible output lines, selected by $n$ control lines. It is known as a **data distributor**.

### 1:4 DEMUX
**Truth Table:**

| $S_1$ | $S_0$ | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | D | 0 | 0 | 0 |
| 0 | 1 | 0 | D | 0 | 0 |
| 1 | 0 | 0 | 0 | D | 0 |
| 1 | 1 | 0 | 0 | 0 | D |

**Boolean Expressions:**
$Y_0 = \overline{S_1}\overline{S_0}D$
$Y_1 = \overline{S_1}S_0D$
$Y_2 = S_1\overline{S_0}D$
$Y_3 = S_1S_0D$

**Circuit Diagram (ASCII):**
```text
           ___
D --------|   |-- Y0
S1 -------|1:4|-- Y1
S0 -------|   |-- Y2
          |___|-- Y3
```

### Relationship between DEMUX and Decoder
A DEMUX is functionally identical to a Decoder with an Enable input. If you treat the Data input ($D$) of the DEMUX as the Enable input ($E$) of a Decoder, and the Select lines as the Address inputs, a $1:2^n$ DEMUX becomes an $n$-to-$2^n$ Decoder.

---

## 2.2.3 Decoder

### Basic Concept
A decoder detects the presence of a specific combination of input bits and asserts the corresponding output line. 

### Definition
> **Decoder** is a multiple-input, multiple-output logic circuit that converts coded inputs into coded outputs, where the input and output codes are different. Typically, an $n$-to-$2^n$ decoder translates $n$ binary inputs into $2^n$ unique outputs.

### 2-to-4 Decoder
**Truth Table:**

| Enable (E) | $A_1$ | $A_0$ | $Y_3$ | $Y_2$ | $Y_1$ | $Y_0$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | X | X | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

**Circuit Diagram (ASCII):**
```text
E ----+----------------- [AND] --- Y0 (E.A1'.A0')
      |                    |
A1 ---+---|>o---[AND]------+
      |
A0 ---+---|>o---[AND]
```
*(Simplified view: 4 AND gates, each receiving E and a unique combination of A1, A0 or their complements).*

### 3-to-8 Decoder
Expands on the 2-to-4 decoder with 3 inputs producing 8 mutually exclusive outputs.

### BCD-to-7-Segment Decoder
This converts a 4-bit Binary Coded Decimal (BCD) number into signals needed to drive a 7-segment display.
- Inputs: A, B, C, D (BCD, values 0-9)
- Outputs: a, b, c, d, e, f, g (segments)

**Truth Table Segment (e.g., for 'a'):**
Displays digit '1' (BCD 0001) -> segments b, c are ON, rest OFF. Segment 'a' is OFF.
Displays digit '8' (BCD 1000) -> all segments ON.

### Implementing Boolean Functions using Decoders
An $n$-to-$2^n$ decoder produces all $2^n$ minterms. By simply logically OR-ing the required minterms, any Boolean function can be implemented.

### Worked Example 2: Implementing a Function with a Decoder
**Given:** Full Adder Sum = $\sum m(1, 2, 4, 7)$ and Carry = $\sum m(3, 5, 6, 7)$
**Required:** Implement using a 3-to-8 Decoder.

**Step 1:** Use a 3-to-8 decoder with inputs $A, B, C_{in}$.
**Step 2:** The outputs of the decoder correspond to minterms $m_0$ to $m_7$.
**Step 3:** Pass outputs 1, 2, 4, 7 into an OR gate to get the Sum.
**Step 4:** Pass outputs 3, 5, 6, 7 into another OR gate to get the Carry.

> [!TIP]
> This is a very common exam question. Remember: **Decoder + OR gates = Any Combinational Logic**.

---

## 2.2.4 Encoder

### Basic Concept
An encoder performs the inverse operation of a decoder. It condenses multiple inputs into a smaller number of outputs.

### Definition
> **Encoder** is a digital circuit that performs the inverse operation of a decoder. An encoder has $2^n$ (or fewer) input lines and $n$ output lines.

### Decimal-to-BCD Encoder (10-to-4)
Has 10 inputs ($D_0$ to $D_9$) and 4 outputs ($Y_3, Y_2, Y_1, Y_0$).
If $D_9$ is active, output is 1001.

### Octal-to-Binary Encoder (8-to-3)
Has 8 inputs ($D_0$ to $D_7$) and 3 outputs ($Y_2, Y_1, Y_0$).
Equations:
$Y_2 = D_4 + D_5 + D_6 + D_7$
$Y_1 = D_2 + D_3 + D_6 + D_7$
$Y_0 = D_1 + D_3 + D_5 + D_7$

### Priority Encoder
**Why it's needed:** A standard encoder fails if more than one input is active simultaneously. A priority encoder solves this by assigning a hierarchy. If multiple inputs are active, the one with the highest priority determines the output.

**Truth Table (4-to-2 Priority Encoder):**
Assume $D_3$ has highest priority, $D_0$ lowest. $V$ indicates valid input.

| $D_3$ | $D_2$ | $D_1$ | $D_0$ | $Y_1$ | $Y_0$ | $V$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | X | X | 0 |
| 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | X | 0 | 1 | 1 |
| 0 | 1 | X | X | 1 | 0 | 1 |
| 1 | X | X | X | 1 | 1 | 1 |

> [!NOTE]
> The 'X' represents a don't care condition. If $D_3=1$, the states of $D_2, D_1, D_0$ do not matter.

### Encoder vs Decoder Table
| Feature | Encoder | Decoder |
| :--- | :--- | :--- |
| **Function** | Converts familiar symbols to binary | Converts binary to familiar symbols |
| **Inputs/Outputs** | $2^n$ inputs, $n$ outputs | $n$ inputs, $2^n$ outputs |
| **Logic** | Uses OR gates | Uses AND / NAND gates |

---

## 2.2.5 Binary Addition Circuits

### Half Adder
Adds two 1-bit binary numbers ($A$ and $B$).
**Truth Table:**

| $A$ | $B$ | Sum ($S$) | Carry ($C$) |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

**Boolean Expressions:**
$S = A \oplus B$ (XOR)
$C = A \cdot B$ (AND)

**Circuit Diagram (ASCII):**
```text
A ----+----[ XOR ]----- S
      |
B --+-|----[ AND ]----- C
```

### Full Adder
Adds three 1-bit numbers ($A$, $B$, and Carry-in $C_{in}$).
**Truth Table:**

| $A$ | $B$ | $C_{in}$ | Sum ($S$) | Carry-out ($C_{out}$) |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

**Boolean Expressions:**
$S = A \oplus B \oplus C_{in}$
$C_{out} = A B + (A \oplus B)C_{in}$

**Implementation using Half Adders:**
A Full Adder can be built using TWO Half Adders and ONE OR gate.

### Ripple Carry Adder (4-bit)
Connects multiple Full Adders in cascade. The $C_{out}$ of one stage is the $C_{in}$ of the next.

```text
    A3 B3        A2 B2        A1 B1        A0 B0
    |  |         |  |         |  |         |  |
  [ FA3 ]<-----[ FA2 ]<-----[ FA1 ]<-----[ FA0 ]<--- C_in=0
   |   |        |   |        |   |        |   |
  C4   S3       C3  S2       C2  S1       C1  S0
```
**Problem:** Propagation delay. The last stage (FA3) cannot compute its final output until the carry ripples through all preceding stages.

### Carry Lookahead Adder (CLA)
Solves the ripple delay by calculating carry signals simultaneously based on input bits.
Define:
- Generate: $G_i = A_i \cdot B_i$ (Carry is generated if both inputs are 1)
- Propagate: $P_i = A_i \oplus B_i$ (Carry is propagated if one input is 1)
$C_{i+1} = G_i + P_i \cdot C_i$

---

## 2.2.6 Binary Subtraction Circuits

### Half Subtractor
Subtracts $B$ from $A$ ($A - B$).

| $A$ | $B$ | Difference ($D$) | Borrow ($B_{out}$) |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

$D = A \oplus B$
$B_{out} = \overline{A} \cdot B$

### Full Subtractor
Subtracts $B$ and $B_{in}$ from $A$.
$D = A \oplus B \oplus B_{in}$
$B_{out} = \overline{A} B + (\overline{A \oplus B})B_{in}$

### Subtraction using 2's Complement
In modern computers, dedicated subtraction circuits are rarely used. Instead, subtraction ($A - B$) is performed by adding $A$ to the 2's complement of $B$.
$A - B = A + (\text{2's complement of } B) = A + (\overline{B} + 1)$

### Adder-Subtractor Combined Circuit
Uses XOR gates to conditionally invert $B$ and uses a control signal ($M$) as $C_{in}$.
- If $M=0$: $B \oplus 0 = B$, $C_{in} = 0 \rightarrow$ ADDITION ($A+B$)
- If $M=1$: $B \oplus 1 = \overline{B}$, $C_{in} = 1 \rightarrow$ SUBTRACTION ($A + \overline{B} + 1$)

```text
M -----+-------+-------+-------+
       |       |       |       |
      XOR     XOR     XOR     XOR
     / |     / |     / |     / |
   B3  |   B2  |   B1  |   B0  |
       V       V       V       V (To FA B inputs)
```

---

## 2.2.7 Operations on Unsigned and Signed Binary Numbers

### Unsigned Binary
All bits represent magnitude. Range for $n$ bits: **0 to $2^n - 1$**.
*Example: 8 bits $\rightarrow$ 0 to 255.*

### Signed Binary Representations
For $n$ bits, the Most Significant Bit (MSB) is the sign bit (0 = positive, 1 = negative).

1. **Signed Magnitude:**
   - MSB is sign, remaining $(n-1)$ bits are magnitude.
   - Range: $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$.
   - Drawback: Two representations for zero (+0 and -0).

2. **1's Complement:**
   - Negative number is bitwise inversion of positive.
   - Range: $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$.
   - Drawback: Still has two zeros.

3. **2's Complement (Most Important):**
   - Negative number is 1's complement + 1.
   - Range: **$-2^{n-1}$ to $+(2^{n-1} - 1)$**.
   - Example: 8 bits $\rightarrow$ -128 to +127.
   - Advantage: Only one zero. Arithmetic is simplified.

### Worked Example 3: 2's Complement Range
**Given:** 16-bit processor.
**Required:** Range of signed integers it can hold.
**Answer:** $-2^{15}$ to $(2^{15} - 1) \implies -32,768$ to $+32,767$.

### Addition and Subtraction in 2's Complement
1. Represent both numbers in $n$-bit 2's complement.
2. Add them using standard binary addition.
3. Ignore any carry-out from the MSB.
4. The result is automatically in 2's complement form.

### Overflow Detection Rules
Overflow occurs when the result exceeds the representable range.
**Rule:** Overflow happens if two numbers of the *same* sign are added, and the result has the *opposite* sign.
Equivalently: **Overflow = Carry-in to MSB $\oplus$ Carry-out from MSB**.

### Worked Example 4: Signed Arithmetic and Overflow
**Given:** 4-bit numbers $A = 0101$ (+5), $B = 0100$ (+4).
**Required:** Compute $A + B$ in 2's complement and check for overflow.
**Answer:**
  0101 (+5)
+ 0100 (+4)
------
  1001 (-7 in 2's complement)
The actual sum is +9, but a 4-bit signed number only goes up to +7. The result sign is negative (1), while both inputs were positive. **Overflow occurred.**

### Worked Example 5: Subtraction using 2's Complement
**Given:** 8-bit numbers. Compute $25 - 40$.
**Answer:**
$A = 25 \rightarrow 0001 1001$
$B = 40 \rightarrow 0010 1000$
Find 2's complement of $B$: Invert bits $\rightarrow 1101 0111$, Add $1 \rightarrow 1101 1000$ (-40)
Add $A$ and $(-B)$:
   0001 1001 (+25)
+  1101 1000 (-40)
------------
   1111 0001
Result MSB is 1, so it's negative. To find magnitude, take 2's complement: Invert $\rightarrow 0000 1110$, Add $1 \rightarrow 0000 1111$ (15 in decimal). Result is **-15**.

---
