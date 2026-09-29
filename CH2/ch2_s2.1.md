# CHAPTER 2 — DIGITAL LOGIC AND MICROPROCESSORS

# Section 2.1 — Digital Logic (AExE0201)

---

## 📌 Prerequisite Note

This section covers the fundamental building blocks of all digital systems. Digital logic is the core of modern electronics, computers, and telecommunications. The NEC exam heavily tests binary arithmetic, logic gate universality, Boolean simplification, and Karnaugh Map techniques. Pay special attention to 2's complement arithmetic and K-map grouping rules, as these are very common sources of errors for candidates.

---

# 2.1.1 NUMBER SYSTEMS

## 📖 Introduction

Digital electronics operates on discrete signal levels, inherently represented by binary numbers (0s and 1s). However, to interface with the real world, human-readable data (decimal), and memory architectures (hexadecimal), an engineer must have a solid grasp of various number systems and the ability to rapidly convert among them.

## ⚠️ Why Is It Important?

An engineer needs a thorough understanding of number systems because:
- **Binary (Base-2)** is the native language of all digital hardware, logic gates, and microprocessors.
- **Hexadecimal (Base-16)** provides a compact way to write long binary strings, used universally in microprocessors, memory addressing, and IPv6.
- **Octal (Base-8)** is used in certain legacy computing systems and file permissions (like UNIX `chmod`).
- **BCD (Binary Coded Decimal)** is essential for interfacing digital systems with decimal displays (e.g., seven-segment displays) without requiring complex binary-to-decimal conversion circuits.
- **Gray Code** minimizes errors in electro-mechanical position sensors (like rotary encoders) by changing only one bit at a time during transitions.

## 💡 Basic Concept

A number system of base (radix) $r$ uses exactly $r$ distinct symbols. The value of a number is determined by the position of its digits. The positional weight of the $i$-th digit (moving away from the radix point) is $r^i$. 

| System | Base (r) | Symbols/Digits |
|--------|----------|----------------|
| Decimal | 10 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| Binary | 2 | 0, 1 |
| Octal | 8 | 0, 1, 2, 3, 4, 5, 6, 7 |
| Hexadecimal| 16 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F |

> [!NOTE]
> In Hexadecimal, the letters A through F represent decimal values 10 through 15 respectively: $A=10, B=11, C=12, D=13, E=14, F=15$.

## ✏️ Definition

> **Radix (Base)** is the number of unique digits, including zero, used to represent numbers in a positional numeral system.

## Physical/Logical Meaning

Think of a number system as a language. The same quantity (say, fifteen apples) can be described as "15" in decimal, "1111" in binary, "17" in octal, and "F" in hexadecimal. The underlying quantity is identical; only the representation changes to suit the "hardware" interpreting it.

## 📈 Mathematical Formulation

For a number in base $r$ written as $(d_n d_{n-1} \dots d_1 d_0 . d_{-1} d_{-2} \dots d_{-m})_r$, its equivalent decimal value is calculated as:

$$ \text{Value}_{10} = \sum_{i=-m}^{n} d_i \times r^i $$

$$ \text{Value}_{10} = (d_n \times r^n) + \dots + (d_1 \times r^1) + (d_0 \times r^0) + (d_{-1} \times r^{-1}) + \dots + (d_{-m} \times r^{-m}) $$

| Symbol | Meaning |
|--------|---------|
| $r$    | Base or Radix of the number system |
| $d_i$  | Digit at the $i$-th position |
| $n$    | Position of the Most Significant Digit (MSD) for the integer part |
| $m$    | Position of the Least Significant Digit (LSD) for the fractional part |

## Conversions Between Number Systems

### 1. Binary to Decimal
Multiply each binary digit by its positional weight ($2^i$) and sum the results.

**Worked Example 2.1: Binary to Decimal (Integer and Fractional)**
**Given:** Binary number $(1101.101)_2$
**Required:** Decimal equivalent
**Formula:** $\sum d_i \times 2^i$
**Substitution:** 
$$ 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 + 1 \times 2^{-1} + 0 \times 2^{-2} + 1 \times 2^{-3} $$
$$ = 8 + 4 + 0 + 1 + 0.5 + 0 + 0.125 $$
**Answer:** $(13.625)_{10}$
**Engineering Interpretation:** The integer part is 13, and the fractional part is exactly 5/8.

### 2. Decimal to Binary
- **Integer part:** Repeatedly divide by 2 and record remainders (read bottom-up).
- **Fractional part:** Repeatedly multiply by 2 and record integer overflows (read top-down).

**Worked Example 2.2: Decimal to Binary**
**Given:** Decimal $(25.375)_{10}$
**Required:** Binary equivalent
**Substitution (Integer Part 25):**
$$ 25 / 2 = 12 \text{ remainder } 1 \text{ (LSB)} $$
$$ 12 / 2 = 6 \text{ remainder } 0 $$
$$ 6 / 2 = 3 \text{ remainder } 0 $$
$$ 3 / 2 = 1 \text{ remainder } 1 $$
$$ 1 / 2 = 0 \text{ remainder } 1 \text{ (MSB)} $$
Integer binary (bottom-up): $11001$

**Substitution (Fractional Part 0.375):**
$$ 0.375 \times 2 = 0.75 \rightarrow \text{Integer } 0 $$
$$ 0.75 \times 2 = 1.50 \rightarrow \text{Integer } 1 $$
$$ 0.50 \times 2 = 1.00 \rightarrow \text{Integer } 1 $$
Fractional binary (top-down): $.011$
**Answer:** $(11001.011)_2$

### 3. Binary to Octal / Octal to Binary
Because $8 = 2^3$, one octal digit maps exactly to three binary bits.
- **Binary to Octal:** Group binary digits into sets of 3 from the radix point outward. Pad with leading/trailing zeros if necessary.
- **Octal to Binary:** Replace each octal digit with its 3-bit binary equivalent.

**Worked Example 2.3: Binary to Octal**
**Given:** $(101101011.11)_2$
**Substitution:**
Group by 3: $\underbrace{101}_{5} \underbrace{101}_{5} \underbrace{011}_{3} . \underbrace{110}_{6}$ (padded with zero on the right)
**Answer:** $(553.6)_8$

### 4. Binary to Hexadecimal / Hexadecimal to Binary
Because $16 = 2^4$, one hex digit maps exactly to four binary bits.
- **Binary to Hex:** Group into sets of 4 from the radix point outward.
- **Hex to Binary:** Replace each hex digit with its 4-bit binary equivalent.

**Worked Example 2.4: Binary to Hexadecimal**
**Given:** $(101101011.11)_2$
**Substitution:**
Group by 4: $\underbrace{0001}_{1} \underbrace{0110}_{6} \underbrace{1011}_{B} . \underbrace{1100}_{C}$ (padded zeros on left and right)
**Answer:** $(16B.C)_{16}$

### 5. Octal to Decimal / Hex to Decimal
Similar to binary to decimal, but use weights $8^i$ and $16^i$ respectively.

**Worked Example 2.5: Hexadecimal to Decimal**
**Given:** $(2A.F)_{16}$
**Substitution:**
$$ 2 \times 16^1 + 10 (A) \times 16^0 + 15 (F) \times 16^{-1} $$
$$ = 32 + 10 + \frac{15}{16} = 42 + 0.9375 $$
**Answer:** $(42.9375)_{10}$

## BCD (Binary Coded Decimal) Representation

BCD expresses each decimal digit (0-9) as a 4-bit binary sequence. It is structurally different from pure binary conversion. BCD is widely used in digital clocks, calculators, and multimeters.

| Decimal Digit | BCD Code |
|---------------|----------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| ... | ... |
| 9 | 1001 |

> [!WARNING]
> ⚠️ **NEC Exam Trap:** Do not confuse BCD with pure binary. $(25)_{10}$ in pure binary is $(11001)_2$. In BCD, it is represented digit-by-digit: $2 = 0010, 5 = 0101 \rightarrow (0010 0101)_{BCD}$. Sequences like $1010$ (10) to $1111$ (15) are **invalid** in BCD.

## Gray Code and Binary-to-Gray Conversion

Gray code is an unweighted code where successive values differ by only one bit. This eliminates the transient states that occur when multiple bits change simultaneously in pure binary.

**Binary to Gray Conversion:**
1. The Most Significant Bit (MSB) of Gray is the same as the Binary MSB.
2. For subsequent bits: $G_i = B_i \oplus B_{i+1}$ (XOR the current binary bit with the previous binary bit).

**Gray to Binary Conversion:**
1. Binary MSB = Gray MSB.
2. For subsequent bits: $B_i = B_{i+1} \oplus G_i$ (XOR the previously calculated binary bit with the current Gray bit).

**Worked Example 2.6: Binary to Gray**
**Given:** Binary $(1011)_2$
**Substitution:**
$G_3 = B_3 = 1$
$G_2 = B_3 \oplus B_2 = 1 \oplus 0 = 1$
$G_1 = B_2 \oplus B_1 = 0 \oplus 1 = 1$
$G_0 = B_1 \oplus B_0 = 1 \oplus 1 = 0$
**Answer:** Gray Code is $1110$.

---

# 2.1.2 BINARY ARITHMETIC

## 📖 Introduction

Binary arithmetic forms the core of the Arithmetic Logic Unit (ALU) in microprocessors. Understanding addition, subtraction, and the representation of negative numbers is fundamental to computer architecture. Computers generally do not use subtractors; they perform subtraction by adding the complement of a number.

## Binary Addition

Rules for binary addition are identical to decimal, just modulo 2:
- $0 + 0 = 0$
- $0 + 1 = 1$
- $1 + 0 = 1$
- $1 + 1 = 0 \text{ (with a carry of } 1)$
- $1 + 1 + 1 = 1 \text{ (with a carry of } 1)$

## ⚙️ Binary Subtraction (Borrow Method)

Rules for basic borrow method:
- $0 - 0 = 0$
- $1 - 0 = 1$
- $1 - 1 = 0$
- $0 - 1 = 1 \text{ (requires a borrow of } 1 \text{ from the next higher bit)}$

While the borrow method is easy for humans, it is inefficient for hardware design. Hence, complements are used.

## Signed Number Representation

To represent negative numbers in digital systems, we must encode the sign within the binary bits. We use the Most Significant Bit (MSB) as a sign bit ($0$ for positive, $1$ for negative).

1. **Sign-Magnitude:** The MSB is the sign, remaining bits are magnitude. 
   - Example (8-bit): $+5 = 00000101$, $-5 = 10000101$.
   - **Problem:** Two representations for zero ($+0$ and $-0$), complicating ALU design.

2. **1's Complement:** Invert all bits of the positive number to get the negative representation.
   - Example: $+5 = 00000101$, $-5 = 11111010$.
   - Still has two zeros ($00000000$ and $11111111$).

3. **2's Complement:** 1's complement $+ 1$. 
   - Example: $+5 = 00000101$, $-5 = 11111010 + 1 = 11111011$.
   - **Advantage:** Only one representation for zero ($00000000$). Arithmetic operations are streamlined. This is the standard in all modern computers.

## Subtraction using Complements

Instead of borrowing, computers subtract by adding the complement: $A - B = A + (-B)$.

### Using 1's Complement
1. Find 1's complement of the subtrahend (B).
2. Add it to the minuend (A).
3. **End-Around Carry Rule:** If there is a final carry out of the MSB, add it back to the LSB. If there is no carry, the result is negative and is in its 1's complement form.

### Using 2's Complement
1. Find 2's complement of the subtrahend (B).
2. Add it to the minuend (A).
3. **Carry Rule:** Discard any final carry out of the MSB. The result is positive. If there is no carry, the result is negative and is in its 2's complement form.

**Worked Example 2.7: 2's Complement Subtraction**
**Given:** $13 - 18$ using 8-bit 2's complement arithmetic.
**Required:** Binary result.
**Substitution:**
1. Convert to binary: $A (13) = 00001101$, $B (18) = 00010010$.
2. Find 2's comp of $18$: Invert bits $\rightarrow 11101101$, add $1 \rightarrow 11101110$.
3. Add A + (-B): 

$$ \ \ \ 00001101 $$

$$ + 11101110 $$

$$ = 11111011 $$
4. There is no carry out. The result is negative and in 2's complement form.
5. To verify magnitude, take 2's comp of the result: $00000100 + 1 = 00000101 \rightarrow (5)_{10}$. Thus, the result is $-5$.
**Answer:** $11111011$

## Overflow Detection

In signed arithmetic, an **overflow** occurs when the addition of two numbers of the same sign produces a result of the opposite sign. 
- Positive + Positive = Negative (Overflow!)
- Negative + Negative = Positive (Overflow!)
- Positive + Negative = Never overflows.

**Detection logic:** In 2's complement, overflow has occurred if the carry *into* the sign bit differs from the carry *out of* the sign bit. Mathematically, $\text{Overflow} = C_{\text{in}} \oplus C_{\text{out}}$.

---

# 2.1.3 LOGIC LEVELS

## 📖 Introduction

In the real physical world, signals are continuous voltages or currents. Digital circuits abstract these continuous analog values into discrete ranges representing logic $0$ and logic $1$. These ranges are called logic levels.

## Positive Logic vs Negative Logic

- **Positive Logic:** A higher voltage level represents logic $1$, and a lower voltage level represents logic $0$.
- **Negative Logic:** A lower voltage level represents logic $1$, and a higher voltage level represents logic $0$.

> [!NOTE]
> In most NEC exam problems and standard digital design, Positive Logic is implicitly assumed unless explicitly stated otherwise.

## Voltage Levels and Noise Margins

Digital logic gates are not perfect; they output voltages within a specified range, and they expect inputs within a specified range.

- **$V_{OH}$**: Minimum output voltage guaranteed for Logic High.
- **$V_{OL}$**: Maximum output voltage guaranteed for Logic Low.
- **$V_{IH}$**: Minimum input voltage recognized by a gate as Logic High.
- **$V_{IL}$**: Maximum input voltage recognized by a gate as Logic Low.

For a logic gate to function reliably, $V_{OH}$ must be strictly greater than $V_{IH}$, and $V_{OL}$ must be strictly less than $V_{IL}$. The difference between these bounds provides a buffer against electrical noise, known as the **Noise Margin**.

**High-Level Noise Margin:** $NM_H = V_{OH} - V_{IH}$
**Low-Level Noise Margin:** $NM_L = V_{IL} - V_{OL}$

## ⚖️ Logic Families Comparison

| Characteristic | TTL (Transistor-Transistor Logic) | CMOS (Complementary MOS) |
|----------------|-----------------------------------|--------------------------|
| **Active Devices** | Bipolar Junction Transistors (BJTs) | MOSFETs |
| **Power Dissipation** | High (constant static current) | Very Low (only consumes power during switching) |
| **Speed** | Very Fast | Traditionally slower, but modern CMOS (e.g. FinFET) is extremely fast |
| **Fan-out** | Low (usually around 10) | High (usually 50+, limited only by input capacitance) |
| **Noise Margin** | Poor (approx 0.4V for 5V TTL) | Excellent (approx 1.5V for 5V CMOS) |

> **💡 Engineering Intuition**
> Why did the industry move from TTL to CMOS? Power. If modern CPUs with billions of gates were built using TTL, they would melt instantly due to static power dissipation. CMOS only consumes significant power when a gate transitions from 0 to 1 or 1 to 0.

---

# 2.1.4 LOGIC GATES

## 📖 Introduction

Logic gates are the physical hardware implementations of Boolean functions. They are the fundamental building blocks of all digital electronic systems. 

## Basic Logic Gates

### AND Gate
- **Function:** Output is $1$ if and only if ALL inputs are $1$.
- **Symbol:** `-[ & ]-` (D-shaped symbol)
- **Boolean Expression:** $Y = A \cdot B$
- **Truth Table:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### OR Gate
- **Function:** Output is $1$ if ANY input is $1$.
- **Symbol:** Curved input, pointed output.
- **Boolean Expression:** $Y = A + B$
- **Truth Table:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### NOT Gate (Inverter)
- **Function:** Output is the complement of the input.
- **Symbol:** Triangle with a bubble at the output.
- **Boolean Expression:** $Y = \overline{A}$
- **Truth Table:**

| A | Y |
|---|---|
| 0 | 1 |
| 1 | 0 |

## Universal Gates

NAND and NOR gates are termed **Universal Gates** because any boolean logic function (including the basic AND, OR, NOT gates) can be implemented using *only* NAND gates or *only* NOR gates.

> **💡 Engineering Intuition**
> Why use universal gates? Fabricating a million identical NAND gates on a silicon die is cheaper, structurally simpler, and more reliable than mixing AND, OR, and NOT gates physically in silicon lithography.

### NAND Gate
- **Function:** NOT-AND. Output is $0$ only if ALL inputs are $1$.
- **Boolean Expression:** $Y = \overline{A \cdot B}$
- **Truth Table:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### NOR Gate
- **Function:** NOT-OR. Output is $1$ only if ALL inputs are $0$.
- **Boolean Expression:** $Y = \overline{A + B}$
- **Truth Table:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

## Exclusive Gates

### XOR Gate (Exclusive-OR)
- **Function:** Output is $1$ if inputs are *different*. Acts as a modulo-2 adder. For multi-input XOR, output is $1$ if there is an *odd number* of $1$s at the inputs.
- **Boolean Expression:** $Y = A \oplus B = A\overline{B} + \overline{A}B$
- **Truth Table:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### XNOR Gate (Exclusive-NOR)
- **Function:** Output is $1$ if inputs are *the same*. Acts as an equivalence gate.
- **Boolean Expression:** $Y = A \odot B = A B + \overline{A}\overline{B} = \overline{A \oplus B}$
- **Truth Table:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## Implementation of Basic Gates Using NAND

1. **NOT using NAND:** Tie all inputs of a NAND gate together. $Y = \overline{A \cdot A} = \overline{A}$
2. **AND using NAND:** Pass the output of a NAND gate through a NOT-NAND. $Y = \overline{\overline{A \cdot B}} = A \cdot B$
3. **OR using NAND:** Invert both inputs using NOT-NANDs, then pass those inverted signals through a third NAND gate. $Y = \overline{\overline{A} \cdot \overline{B}} = A + B$ (By De Morgan's Law).

---

# 2.1.5 BOOLEAN ALGEBRA

## 📖 Introduction

Boolean algebra provides the mathematical framework for analyzing and simplifying digital logic circuits. By applying mathematical rules to logic variables, we can reduce complex circuits to their simplest forms, saving hardware costs and reducing delay.

## 🎓 Postulates and Basic Theorems

Boolean algebra variables can only take values of $0$ or $1$.

| Theorem | AND Form | OR Form |
|---------|----------|---------|
| **Identity** | $A \cdot 1 = A$ | $A + 0 = A$ |
| **Null elements** | $A \cdot 0 = 0$ | $A + 1 = 1$ |
| **Idempotent** | $A \cdot A = A$ | $A + A = A$ |
| **Involution (Double Negation)** | $\overline{\overline{A}} = A$ | |
| **Complementary** | $A \cdot \overline{A} = 0$ | $A + \overline{A} = 1$ |
| **Commutative** | $A \cdot B = B \cdot A$ | $A + B = B + A$ |
| **Associative** | $A \cdot (B \cdot C) = (A \cdot B) \cdot C$ | $A + (B + C) = (A + B) + C$ |
| **Distributive** | $A + (B \cdot C) = (A + B) \cdot (A + C)$ | $A \cdot (B + C) = (A \cdot B) + (A \cdot C)$ |
| **Absorption** | $A \cdot (A + B) = A$ | $A + (A \cdot B) = A$ |

> [!IMPORTANT]
> The distributive law in Boolean algebra works both ways! In standard algebra, $A + (B \cdot C) \neq (A + B) \cdot (A + C)$, but in Boolean algebra, it is a perfectly valid and frequently used identity.

## 🎓 De Morgan's Theorems

De Morgan's Theorems are the most critical tool for converting between AND, OR, NAND, and NOR logic.

1. **Theorem 1:** The complement of a product is equal to the sum of the complements.

$$ \overline{A \cdot B} = \overline{A} + \overline{B} $$
   *(NAND is equivalent to Negative-OR)*

2. **Theorem 2:** The complement of a sum is equal to the product of the complements.

$$ \overline{A + B} = \overline{A} \cdot \overline{B} $$
   *(NOR is equivalent to Negative-AND)*

## Duality Principle

The principle of duality states that every valid Boolean algebraic expression remains valid if you:
1. Swap all OR ($+$) and AND ($\cdot$) operators.
2. Swap all $0$s and $1$s.
3. Keep the variables as they are (do not complement them).

## Simplification Using Algebraic Manipulation

**Worked Example 2.8: Algebraic Simplification**
**Given:** $F = A\overline{B}C + A B C + \overline{A} C$
**Required:** Minimal Boolean expression.
**Substitution:**
1. Group the first two terms by factoring out $AC$: 

$$ F = A C (\overline{B} + B) + \overline{A} C $$
2. Apply the Complementary Law ($\overline{B} + B = 1$): 

$$ F = A C(1) + \overline{A} C = A C + \overline{A} C $$
3. Factor out $C$: 

$$ F = C (A + \overline{A}) $$
4. Apply the Complementary Law again ($A + \overline{A} = 1$): 

$$ F = C(1) = C $$
**Answer:** $F = C$
**Engineering Interpretation:** The original circuit required two NOT gates, three 3-input AND gates, and one 3-input OR gate. The simplified circuit is literally just a wire connecting input C to output F. This demonstrates the immense power of logic minimization.

**Worked Example 2.9: Simplification using Consensus Theorem**
**Given:** $F = AB + \overline{A}C + BC$
**Rule:** The Consensus Theorem states $XY + \overline{X}Z + YZ = XY + \overline{X}Z$.
**Substitution:**
Let $X=A, Y=B, Z=C$. The term $BC$ is the consensus term (formed by the variables that are not complemented and not $A$).
The consensus term is completely redundant.
**Answer:** $F = AB + \overline{A}C$

---

# 2.1.6 SUM-OF-PRODUCTS (SOP) METHOD

## 📖 Introduction

Sum-of-Products (SOP) is a standard method of expressing Boolean logic where product terms (variables joined by AND) are summed (joined by OR) together. SOP maps directly to a two-level AND-OR logic circuit.

## Minterms

A **minterm** is a product term that contains all variables in the system exactly once, either in true (uncomplemented) or complemented form. 
- For an $n$-variable system, there are $2^n$ unique minterms. 
- A minterm evaluates to $1$ for exactly one specific combination of inputs.
- Notation: $m_0, m_1, m_2, \dots$

For a 3-variable system (A, B, C):
| A | B | C | Minterm Notation | Product Term |
|---|---|---|------------------|--------------|
| 0 | 0 | 0 | $m_0$ | $\overline{A}\overline{B}\overline{C}$ |
| 0 | 0 | 1 | $m_1$ | $\overline{A}\overline{B}C$ |
| ... | ... | ... | ... | ... |
| 1 | 1 | 1 | $m_7$ | $ABC$ |

## Canonical SOP Form

A boolean function expressed purely as a sum of minterms is in **canonical (or standard) SOP form**.
Example: $F(A,B,C) = \sum m(1, 3, 5, 7)$ represents $F = \overline{A}\overline{B}C + \overline{A}BC + A\overline{B}C + ABC$.

## Converting Truth Table to SOP

To extract an SOP expression from a truth table:
1. Identify all rows where the output $Y$ is $1$.
2. For each such row, write out the minterm. If an input is $0$, write it as complemented ($\overline{A}$). If an input is $1$, write it as true ($A$).
3. OR all the minterms together.

---

# 2.1.7 PRODUCT-OF-SUMS (POS) METHOD

## 📖 Introduction

Product-of-Sums (POS) is the dual of SOP. It expresses logic as sum terms (variables joined by OR) multiplied (joined by AND) together. POS maps directly to a two-level OR-AND logic circuit.

## Maxterms

A **maxterm** is a sum term containing all variables in the system exactly once. 
- A maxterm evaluates to $0$ for exactly one specific combination of inputs.
- Notation: $M_0, M_1, M_2, \dots$

For a 3-variable system (A, B, C):
| A | B | C | Maxterm Notation | Sum Term |
|---|---|---|------------------|----------|
| 0 | 0 | 0 | $M_0$ | $A + B + C$ |
| 0 | 0 | 1 | $M_1$ | $A + B + \overline{C}$ |
| ... | ... | ... | ... | ... |
| 1 | 1 | 1 | $M_7$ | $\overline{A} + \overline{B} + \overline{C}$ |

> [!WARNING]
> Note the inversion! In maxterms, an input of $0$ means the variable is uncomplemented ($A$), while an input of $1$ means it is complemented ($\overline{A}$). This is the exact opposite of minterms.

## Canonical POS Form

A boolean function expressed purely as a product of maxterms is in **canonical POS form**.
Example: $F(A,B,C) = \prod M(0, 2, 4, 6)$.

## Relationship Between SOP and POS

A function expressed as a sum of minterms can be easily converted to POS by taking the product of the *missing* maxterms, and vice versa.
If $F(A,B,C) = \sum m(1,3,5,7)$, then the $0$ outputs occur at $0, 2, 4, 6$.
Therefore, $F(A,B,C) = \prod M(0,2,4,6)$.

---

# 2.1.8 KARNAUGH MAPS (K-MAPS)

## 📖 Introduction

Algebraic simplification is highly prone to human error and does not guarantee that a minimal solution will be found. The Karnaugh Map (K-map) is a graphical technique providing a systematic, visual method for Boolean minimization up to 4 or 5 variables.

## Structure

A K-map is a 2D grid of cells. Each cell corresponds directly to one minterm (or maxterm). The critical feature of a K-map is that the grid is ordered in **Gray code** ($00, 01, 11, 10$) so that any two adjacent cells differ by only one boolean variable.

### Variable Maps
- **2-Variable K-Map:** 4 cells.
- **3-Variable K-Map:** 8 cells (usually $2 \times 4$).
- **4-Variable K-Map:** 16 cells ($4 \times 4$).

## Grouping Rules

To simplify an expression using a K-map, you must group adjacent $1$s (for SOP) or $0$s (for POS).
1. **Size:** Groups must contain exactly $1, 2, 4, 8, 16 \dots$ cells (always powers of 2).
2. **Shape:** Groups must be rectangular or square. No diagonals or L-shapes.
3. **Overlap:** Cells can and should be shared between multiple groups if it helps make larger groups.
4. **Wrap-around:** The map is topologically a torus! The top edge is adjacent to the bottom edge. The left edge is adjacent to the right edge. The four corners of a 4-variable map form a valid group of 4.
5. **Maximization:** Always form the *largest possible* groups. A group of 4 eliminates two variables; a group of 8 eliminates three.
6. **Completeness:** Ensure every single $1$ (for SOP) is covered by at least one group.

## Don't-Care Conditions (X or d)

In many real-world systems, certain input combinations will never occur (e.g., in a BCD system, inputs $1010$ through $1111$ are impossible). The output for these impossible inputs doesn't matter. We call these **Don't-Care conditions (X)**.
- When grouping, you can treat an 'X' as a $1$ if it helps you form a *larger* group.
- You can treat it as a $0$ if it doesn't help.
- You NEVER form a group entirely consisting of 'X's.

## 🔍 Worked K-Map Examples

**Worked Example 2.10: 3-Variable K-Map (SOP)**
**Given:** $F(A,B,C) = \sum m(0, 2, 4, 6)$
**Required:** Minimized SOP expression.
**Substitution (K-Map Setup):**
```text
      BC
   \  00  01  11  10
  A +---+---+---+---+
  0 | 1 | 0 | 0 | 1 |
    +---+---+---+---+
  1 | 1 | 0 | 0 | 1 |
    +---+---+---+---+
```
**Grouping:**
We have $1$s at the far left ($BC=00$) and far right ($BC=10$). Because of the wrap-around rule, the left edge is adjacent to the right edge. 
We can form a single large group of 4 covering the entire left column and right column.
- Analyzing the group: Variable $A$ changes from $0$ to $1$ (eliminated). Variable $B$ changes from $0$ to $1$ (eliminated). Variable $C$ remains $0$ throughout the entire group.
- Because $C=0$, the term is $\overline{C}$.
**Answer:** $F = \overline{C}$

**Worked Example 2.11: 4-Variable K-Map with Don't Cares**
**Given:** $F(W,X,Y,Z) = \sum m(1, 3, 7, 11, 15) + d(0, 2, 5)$
**Required:** Minimized SOP expression.
**Substitution (K-Map Setup):**
(Note: $m_1$ is at $WXYZ=0001$, etc. $d$ are don't cares 'X').
```text
       YZ
    \  00  01  11  10
  WX+---+---+---+---+
 00 | X | 1 | 1 | X |
    +---+---+---+---+
 01 | 0 | X | 1 | 0 |
    +---+---+---+---+
 11 | 0 | 0 | 1 | 0 |
    +---+---+---+---+
 10 | 0 | 0 | 1 | 0 |
    +---+---+---+---+
```
**Grouping:**
1. Look at the $11$ column ($YZ=11$). It is full of $1$s. We form a group of 4 spanning the entire column. 
   - Term: $YZ$ (since $W$ and $X$ change across the column).
2. We still have an uncovered $1$ at $0001$ ($WX=00, YZ=01$). 
   - Can we make a group of 4? Yes! If we include the $1$ at $0011$, and the Don't Cares (X) at $0000$ and $0010$, we can form a horizontal group of 4 across the entire first row.
   - Term: $\overline{W}\overline{X}$ (since $Y$ and $Z$ change across the row).
3. The remaining 'X' at $0101$ is left as a $0$ because we don't need it to cover any $1$s.
**Answer:** $F = YZ + \overline{W}\overline{X}$

## ⚠️ NEC Exam Traps

- **Trap 1:** Forgetting wrap-around adjacency. Many students miss that the 4 corners of a 4-variable map form a valid group of 4, yielding a term with two variables eliminated.
- **Trap 2:** Including a Don't Care (X) just because it's there. Only include an X if it helps double the size of a group of 1s.
- **Trap 3:** In POS K-maps, remember to group the **$0$s** instead of $1$s. Furthermore, in POS, a $0$ corresponds to a true variable ($A$) and a $1$ corresponds to a complemented variable ($\overline{A}$).
- **Trap 4:** Mixing up the Gray code ordering ($00, 01, 11, 10$). If you write $00, 01, 10, 11$, your K-map will fail completely.
