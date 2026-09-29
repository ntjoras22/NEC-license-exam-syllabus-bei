# Chapter 1: Basic Concept (Section 1.1 — Part 2)

## 1.1.8 Conducting and Insulating Materials

### Introduction
Every material interacts with electric charge differently. While some materials permit easy flow of electrons (conductors), others strongly oppose it (insulators). Understanding these distinct properties is the foundation of circuit design, safety, and component selection.

### Basic Concept
The conductivity of a material depends primarily on its atomic structure, specifically the behavior of its valence electrons (electrons in the outermost shell).

**1. Conductors**
- **Definition:** Materials that offer very little resistance to the flow of electric current.
- **Physical Meaning:** In conductors, atoms have 1 to 3 loosely bound valence electrons. At room temperature, thermal energy is enough to free these electrons from their parent atoms. These **free electrons** form an "electron gas" and drift freely when an electric field (voltage) is applied.
- **Examples:** Silver (best), Copper, Gold, Aluminum.
- **Why Metals Conduct:** The metallic bond allows electrons to move freely throughout the crystal lattice. 

**2. Insulators**
- **Definition:** Materials that strongly resist the flow of electric current.
- **Physical Meaning:** Insulators have 5 to 8 tightly bound valence electrons. There are practically zero free electrons available for conduction. An enormous voltage (breakdown voltage) is required to rip these electrons from their atoms to force conduction.
- **Examples:** Glass, Rubber, Mica, Ceramic, Dry Air.
- **Why they don't conduct:** All valence electrons are locked in covalent or ionic bonds, leaving no charge carriers.

**3. Semiconductors** (Preview)
- **Definition:** Materials with electrical conductivity between that of a conductor and an insulator.
- **Physical Meaning:** At absolute zero, they act as perfect insulators. As temperature rises, some covalent bonds break, creating free electrons and holes, thus allowing some conduction. They have exactly 4 valence electrons.
- **Examples:** Silicon, Germanium.

### Comparison Table

| Feature | Conductor | Insulator | Semiconductor |
|---------|-----------|-----------|---------------|
| **Valence Electrons** | 1, 2, or 3 | 5, 6, 7, or 8 | Exactly 4 |
| **Resistivity ($\rho$)** | Low ($10^{-8} \ \Omega\cdot m$) | Very High ($10^{12} \ \Omega\cdot m$) | Moderate ($10^{-3} \ \Omega\cdot m$) |
| **Temperature Coefficient** | Positive (Resistance increases with Temp) | Negative (Resistance drops slightly) | Negative (Resistance drops heavily) |
| **Energy Gap** | Overlapping bands | Large (>5 eV) | Small (~1 eV) |

> [!WARNING]
> **⚠️ NEC Exam Trap:** You might be asked what happens to the resistance of a semiconductor or insulator when heated. Remember: Conductors get *more* resistive when hot; Semiconductors and Insulators get *less* resistive when hot (Negative Temperature Coefficient).

---

## 1.1.9 Series Electric Circuits

### Introduction
The series circuit is the simplest way to connect components. It forms a single, undivided path for current. 

### Definition
A series circuit is one in which components are connected end-to-end, so that the **same current** flows through all components.

### Circuit Diagram
```text
      +---[ R1 ]---[ R2 ]---[ R3 ]---+
      |                              |
     (+)                            (-)
      |-----------[ V ]--------------|
```

### Mathematical Formulation & Derivations

**1. Current**
Because there is only one path, the current is identical everywhere.
$$ I_{total} = I_1 = I_2 = I_3 $$

**2. Total Resistance**
From Ohm's Law and conservation of energy (KVL), the total voltage $V$ provided by the source equals the sum of voltage drops across resistors.
$$ V_{total} = V_1 + V_2 + V_3 $$
Substitute $V = I \times R$:
$$ I \cdot R_{eq} = I \cdot R_1 + I \cdot R_2 + I \cdot R_3 $$
Dividing by $I$:
$$ R_{eq} = R_1 + R_2 + R_3 + \dots + R_n $$

**3. Voltage Divider Rule (VDR)**
In a series circuit, the total voltage divides among the resistors in direct proportion to their resistance.
$$ V_k = I \cdot R_k = \left( \frac{V_{total}}{R_{eq}} \right) R_k $$
$$ V_k = V_{total} \times \frac{R_k}{R_{eq}} $$

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $V_k$ | Voltage drop across resistor $k$ | Volts (V) |
| $R_k$ | Resistance of resistor $k$ | Ohms ($\Omega$) |
| $R_{eq}$ | Total equivalent series resistance | Ohms ($\Omega$) |

**4. Power**
Total power dissipated is the sum of individual powers.
$$ P_{total} = P_1 + P_2 + P_3 = I^2 R_1 + I^2 R_2 + I^2 R_3 $$

> [!TIP]
> **💡 Engineering Intuition:** If you string a bunch of old Christmas lights in series and one burns out (breaks the circuit), they all go dark because the single current path is broken.

### Worked Numerical (Level 2)
**Given:** Three resistors, $R_1 = 10\ \Omega$, $R_2 = 20\ \Omega$, and $R_3 = 30\ \Omega$, are connected in series across a $120\text{V}$ supply.
**Required:** 
1. Total equivalent resistance
2. Circuit current
3. Voltage drop across $R_2$
**Principle:** Series circuit properties and Voltage Divider Rule.
**Calculation:**
1. $R_{eq} = 10 + 20 + 30 = 60\ \Omega$
2. $I = \frac{V}{R_{eq}} = \frac{120}{60} = 2\text{ A}$
3. Using VDR for $R_2$:
   $V_2 = 120 \times \frac{20}{60} = 120 \times \frac{1}{3} = 40\text{ V}$.
   (Check: $V_2 = I \times R_2 = 2 \times 20 = 40\text{ V}$).
**Interpretation:** The largest resistor ($30\ \Omega$) will have the largest voltage drop ($60\text{ V}$), keeping true to proportional division.

---

## 1.1.10 Parallel Electric Circuits

### Introduction
In a parallel circuit, components are connected across the same common nodes, providing multiple paths for the current to flow.

### Definition
A parallel circuit is one in which all components share the same two nodes, meaning the **same voltage** appears across all components.

### Circuit Diagram
```text
         +----------+----------+----------+
         |          |          |          |
        (+)        [R1]       [R2]       [R3]
      Voltage       |          |          |
       Source      [  ]       [  ]       [  ]
        (-)         |          |          |
         |          |          |          |
         +----------+----------+----------+
```

### Mathematical Formulation & Derivations

**1. Voltage**
The voltage across every parallel branch is identical.
$$ V_{total} = V_1 = V_2 = V_3 $$

**2. Total Resistance**
By KCL (conservation of charge), total current is the sum of branch currents:
$$ I_{total} = I_1 + I_2 + I_3 $$
Substitute $I = V / R$:
$$ \frac{V}{R_{eq}} = \frac{V}{R_1} + \frac{V}{R_2} + \frac{V}{R_3} $$
Dividing by $V$:
$$ \frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots + \frac{1}{R_n} $$

**Special Case (Two Resistors):**
For just two resistors in parallel:
$$ R_{eq} = \frac{R_1 \times R_2}{R_1 + R_2} $$
*(Product over Sum)*

**3. Current Divider Rule (CDR)**
Current divides inversely proportional to resistance (path of least resistance gets most current).
$$ I_k = \frac{V}{R_k} = \frac{I_{total} \times R_{eq}}{R_k} = I_{total} \times \frac{R_{eq}}{R_k} $$

**For exactly two resistors in parallel:**
$$ I_1 = I_{total} \times \frac{R_2}{R_1 + R_2} $$
$$ I_2 = I_{total} \times \frac{R_1}{R_1 + R_2} $$
*(Notice: To find $I_1$, use $R_2$ in the numerator!)*

**4. Power**
Total power is still the sum of individual powers.
$$ P_{total} = P_1 + P_2 + P_3 = \frac{V^2}{R_1} + \frac{V^2}{R_2} + \frac{V^2}{R_3} $$

> [!CAUTION]
> **Common Mistake:** Students often use $I_1 = I_{total} \frac{R_1}{R_1+R_2}$ which is WRONG. Remember current favors the *other* path if your resistance is high, so use the *opposite* resistance in the numerator.

### Series vs Parallel Comparison Table

| Property | Series | Parallel |
|----------|--------|----------|
| **Current** | Same through all elements | Divides among branches |
| **Voltage** | Divides among elements | Same across all branches |
| **Total Resistance** | Increases ($R_{eq} > R_{largest}$) | Decreases ($R_{eq} < R_{smallest}$) |
| **Open Circuit Effect** | Entire circuit stops functioning | Other branches continue functioning |
| **Household Wiring** | Seldom used (except switches) | Standard for all appliances |

---

## 1.1.11 Star (Y) Connection

### What is a Star/Y Connection?
A Star (or Wye, Y) connection is formed when one end of three components (typically resistors or coils) are joined together at a common point called the **neutral point** or **star point**, leaving the other three ends free to connect to the external circuit.

### Circuit Diagram
```text
           A
           |
          [Ra]
           |
           N (Neutral point)
          / \
      [Rb]   [Rc]
      /         \
     B           C
```

### Characteristics
- Symmetrical appearance resembles the letter Y.
- Accessible neutral point (N) allows for 3-phase, 4-wire systems (discussed later in AC).
- Between any two terminals (e.g., A and B), two resistors are in series if the third terminal is open.

---

## 1.1.12 Delta ($\Delta$) Connection

### What is a Delta Connection?
A Delta (or Mesh, $\Delta$) connection is formed when three components are connected end-to-end to form a closed loop. The three connection points (nodes) are used to connect to the external circuit.

### Circuit Diagram
```text
           A
          / \
      [Rab] [Rca]
        /     \
       B--[Rbc]--C
```

### Characteristics
- Resembles the Greek letter Delta ($\Delta$).
- No neutral point exists.
- Between any two terminals (e.g., A and B), there is one resistor ($R_{ab}$) in parallel with the series combination of the other two ($R_{bc} + R_{ca}$).

---

## 1.1.13 Star-Delta and Delta-Star Conversion

### Why we need to convert
In complex bridge networks (like a Wheatstone bridge that isn't balanced), resistors are neither purely in series nor in parallel. Star-Delta transformations allow us to redraw these stubborn geometries into simple series-parallel combinations to calculate equivalent resistance.

### 1. Delta to Star Conversion ($\Delta \rightarrow Y$)
To replace a Delta network ($R_{ab}, R_{bc}, R_{ca}$) with an equivalent Star network ($R_a, R_b, R_c$), the resistance between any two terminals must be identical in both configurations.

**Derivation Principle:**
Resistance between A and B in Star: $R_a + R_b$
Resistance between A and B in Delta: $R_{ab} \parallel (R_{bc} + R_{ca})$
Equating these for all three terminal pairs and solving algebraically yields:

**Formulas:**
$$ R_a = \frac{R_{ab} R_{ca}}{R_{ab} + R_{bc} + R_{ca}} $$
$$ R_b = \frac{R_{ab} R_{bc}}{R_{ab} + R_{bc} + R_{ca}} $$
$$ R_c = \frac{R_{bc} R_{ca}}{R_{ab} + R_{bc} + R_{ca}} $$

**Rule to remember:** The Star resistor connected to a terminal is the product of the two Delta resistors connected to that same terminal, divided by the sum of all three Delta resistors.

### 2. Star to Delta Conversion ($Y \rightarrow \Delta$)
**Formulas:**
$$ R_{ab} = R_a + R_b + \frac{R_a R_b}{R_c} = \frac{R_a R_b + R_b R_c + R_c R_a}{R_c} $$
$$ R_{bc} = R_b + R_c + \frac{R_b R_c}{R_a} = \frac{R_a R_b + R_b R_c + R_c R_a}{R_a} $$
$$ R_{ca} = R_c + R_a + \frac{R_c R_a}{R_b} = \frac{R_a R_b + R_b R_c + R_c R_a}{R_b} $$

**Rule to remember:** The Delta resistor between two terminals is the sum of all pair-wise products of Star resistors, divided by the Star resistor connected to the *opposite* (third) terminal.

### Special Case: Equal Resistances
If all resistors are equal ($R_a = R_b = R_c = R_Y$) and ($R_{ab} = R_{bc} = R_{ca} = R_\Delta$):
$$ R_\Delta = 3 \times R_Y $$
$$ R_Y = \frac{R_\Delta}{3} $$

> [!WARNING]
> **⚠️ NEC Exam Trap:** A frequent multiple-choice question: "If three $10\ \Omega$ resistors are connected in Delta, what is the equivalent Star resistance?" Answer: $10 / 3 = 3.33\ \Omega$. Students often mistakenly multiply by 3 instead of divide. Remember: Delta values are always LARGER than their equivalent Star values (by a factor of 3 for identical resistors).

### Worked Numerical (Level 3 - NEC Challenge)
**Given:** A bridge circuit where a Delta connection exists between terminals A, B, and C with $R_{ab} = 10\ \Omega$, $R_{bc} = 20\ \Omega$, $R_{ca} = 30\ \Omega$.
**Required:** Find the equivalent Star connection resistors $R_a$, $R_b$, $R_c$.
**Formula:** $R_{star} = \frac{\text{Product of adjacent } R_{\Delta}}{\Sigma R_{\Delta}}$
**Calculation:**
1. $\Sigma R_{\Delta} = 10 + 20 + 30 = 60\ \Omega$
2. $R_a$ (connected to node A, between $10\ \Omega$ and $30\ \Omega$):
   $R_a = \frac{10 \times 30}{60} = \frac{300}{60} = 5\ \Omega$
3. $R_b$ (connected to node B, between $10\ \Omega$ and $20\ \Omega$):
   $R_b = \frac{10 \times 20}{60} = \frac{200}{60} = 3.33\ \Omega$
4. $R_c$ (connected to node C, between $20\ \Omega$ and $30\ \Omega$):
   $R_c = \frac{20 \times 30}{60} = \frac{600}{60} = 10\ \Omega$
**Final Answer:** $R_a = 5\ \Omega$, $R_b = 3.33\ \Omega$, $R_c = 10\ \Omega$.

---

## 1.1.14 Kirchhoff's Current Law (KCL)

### Statement
Kirchhoff's First Law states that the algebraic sum of all currents entering and leaving a node (junction) must equal zero. Alternatively, the sum of currents entering a node equals the sum of currents leaving the node.

### Physical Basis
**Conservation of Charge:** Charge cannot be created or destroyed at a junction. Whatever electric charge flows in must flow out.

### Sign Convention
- Currents ENTERING the node: POSITIVE (+)
- Currents LEAVING the node: NEGATIVE (-)
*(Note: You can reverse this as long as you are consistent, but this is the standard convention).*

### Mathematical Formulation
$$ \sum_{n=1}^{N} i_n = 0 $$
OR
$$ \sum I_{in} = \sum I_{out} $$

### Diagram
```text
      I1 = 5A -----> (Node) -----> I3 = ?
                       ^
                       |
                     I2 = 3A
```
*Applying KCL:* $I_1 + I_2 = I_3 \implies 5A + 3A = I_3 \implies I_3 = 8A$

---

## 1.1.15 Kirchhoff's Voltage Law (KVL)

### Statement
Kirchhoff's Second Law states that the algebraic sum of all voltages (source voltages and voltage drops) around any closed loop in a circuit must equal zero.

### Physical Basis
**Conservation of Energy:** The total electrical energy supplied by the sources in a loop is exactly equal to the total energy dissipated or stored by the components in that loop. The net change in electrical potential energy around a closed path is zero.

### Sign Convention for Loop Traversal
When walking around a loop in a chosen direction (e.g., clockwise):
1. **Battery:** Going from (-) to (+) is a voltage RISE (+V). Going from (+) to (-) is a voltage DROP (-V).
2. **Resistor:** Going *with* the current direction is a voltage DROP (-IR). Going *against* the current is a voltage RISE (+IR).

### Mathematical Formulation
$$ \sum_{n=1}^{N} V_n = 0 $$
around any closed loop.

### Worked Numerical (Mesh Analysis concept using KVL)
**Given:** A single loop circuit with a 12V battery and two resistors $R_1=2\ \Omega$ and $R_2=4\ \Omega$ in series. 
**Required:** Find current $I$ using KVL.
**Procedure:**
1. Assume a current $I$ flowing clockwise.
2. Traverse loop clockwise from bottom-left corner.
3. Pass through battery: - to + (Rise: $+12\text{V}$)
4. Pass through $R_1$ with current: (Drop: $-I \times 2$)
5. Pass through $R_2$ with current: (Drop: $-I \times 4$)
6. Return to start point = 0.
$$ 12 - 2I - 4I = 0 $$
$$ 12 = 6I \implies I = 2\text{ A} $$

---

## 🏷️ 1.1.16 Circuit Classifications

In electrical engineering, circuits and elements are classified based on their V-I characteristics, energy contribution, and directional properties.

### 1. Linear vs. Non-linear
- **Linear Circuit:** A circuit whose parameters (R, L, C) do not change with voltage or current. The V-I characteristic is a straight line passing through the origin. **Ohm's law and Superposition principle apply.** (Example: Resistor).
- **Non-linear Circuit:** A circuit whose parameters change with voltage or current. The V-I characteristic is curved. (Example: Diode, Transistor, Incandescent bulb).

### 2. Bilateral vs. Unilateral
- **Bilateral Circuit:** Properties and characteristics are exactly the same in either direction of current flow. (Example: Resistor, Inductor).
- **Unilateral Circuit:** Properties change based on the direction of current flow. (Example: PN Junction Diode—conducts forward, blocks reverse).

### 3. Active vs. Passive
- **Active Element:** A component capable of generating or supplying electrical energy continuously. (Example: Voltage Source, Current Source, Operational Amplifier).
- **Passive Element:** A component that absorbs, dissipates, or temporarily stores energy, but cannot supply energy continuously. (Example: Resistor, Capacitor, Inductor).

### Comparison Table

| Category | Linear | Non-linear | Bilateral | Unilateral | Active | Passive |
|----------|--------|------------|-----------|------------|--------|---------|
| **V-I Graph** | Straight line | Curve | Symmetrical in quadrants | Asymmetrical | N/A | N/A |
| **Current Direction**| Doesn't matter | Doesn't strictly matter | Doesn't matter | Changes behavior | Supplies power | Absorbs power |
| **Examples** | Standard Resistor | Diode | Resistor, AC line | Diode, SCR | Battery, Generator | Resistor, Coil |

---

## ⭐ 1.1.17 Section Summary

### Key Equations Table

| Concept | Equation | Notes |
|---------|----------|-------|
| Series R | $R_{eq} = R_1 + R_2 + \dots$ | Voltage divides |
| Parallel R | $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$ | Current divides |
| Voltage Divider | $V_k = V_{total} \times \frac{R_k}{R_{eq}}$ | Series only |
| Current Divider | $I_1 = I_{total} \times \frac{R_2}{R_1 + R_2}$ | For 2 parallel branches |
| $\Delta \rightarrow Y$ | $R_a = \frac{R_{ab}R_{ca}}{R_{ab}+R_{bc}+R_{ca}}$ | Denominator is sum of $\Delta$ |
| $Y \rightarrow \Delta$ | $R_{ab} = \frac{R_aR_b + R_bR_c + R_cR_a}{R_c}$ | Numerator is sum of pairs |
| KCL | $\Sigma I_{in} = \Sigma I_{out}$ | Charge conservation |
| KVL | $\Sigma V = 0$ | Energy conservation |

---

### Conceptual Questions
1. Why does the equivalent resistance of a parallel circuit always end up smaller than the smallest individual branch resistance?
2. A diode behaves differently when the battery is reversed. Based on circuit classifications, how would you classify a diode?
3. Explain why KCL is said to be based on the principle of conservation of charge.
4. If one light bulb blows out in a series string, they all go out. Why doesn't this happen in house wiring?
5. When transforming identical resistors from Star to Delta, does the resistance per branch increase or decrease, and by what factor?

---

### Numerical Problems

**Level 1**
1. Two resistors of $12\ \Omega$ and $24\ \Omega$ are connected in parallel. Calculate the equivalent resistance.
2. Find the voltage drop across a $50\ \Omega$ resistor that is in series with a $150\ \Omega$ resistor, if the total applied voltage is $200\text{V}$.

**Level 2**
3. A current of $10\text{A}$ flows into a parallel combination of $R_1=6\ \Omega$ and $R_2=4\ \Omega$. Use the current divider rule to find the current in $R_1$.
4. Three resistors $10\ \Omega$, $10\ \Omega$, and $10\ \Omega$ are connected in Delta. They are to be replaced by an equivalent Star network. What is the value of each resistor in the Star network?

**Level 3 (NEC Challenge)**
5. A bridge circuit has a Delta loop with values $10\ \Omega$, $20\ \Omega$, and $30\ \Omega$. Convert it to Star. Then, place a $10\ \Omega$ resistor in series with the newly found $R_a$. What is the total resistance of that single branch now?

---

### NEC-Style MCQs

1. In a series circuit, which of the following remains constant across all elements?
   a) Voltage
   b) Current
   c) Power
   d) Resistance

2. Three resistors of $30\ \Omega$ each are connected in delta. The equivalent star resistance per phase will be:
   a) $90\ \Omega$
   b) $30\ \Omega$
   c) $10\ \Omega$
   d) $3\ \Omega$

3. Kirchhoff's Voltage Law (KVL) is based on the law of conservation of:
   a) Charge
   b) Momentum
   c) Mass
   d) Energy

4. A network that contains at least one source of energy is called a(n):
   a) Passive network
   b) Active network
   c) Linear network
   d) Bilateral network

5. The total resistance of two identical resistors in parallel is:
   a) Double of one resistor
   b) Half of one resistor
   c) Equal to one resistor
   d) Zero

6. Which material property causes insulators to block current flow?
   a) They have overlapping valence and conduction bands
   b) They have no tightly bound electrons
   c) They have a very large energy gap and tightly bound valence electrons
   d) They are very dense materials

7. If $V = 100V$ is applied to $R_1 = 20\ \Omega$ and $R_2 = 30\ \Omega$ in series, what is the voltage across $R_2$?
   a) 40V
   b) 60V
   c) 50V
   d) 100V

8. A circuit whose behavior depends upon the direction of current is known as:
   a) Unilateral
   b) Bilateral
   c) Linear
   d) Active

9. Using KCL at a node, if currents $3A$ and $5A$ are entering, and $I_x$ is leaving, what is $I_x$?
   a) $2A$
   b) $-2A$
   c) $8A$
   d) $15A$

10. Superposition theorem is applicable only to circuits that are:
    a) Non-linear
    b) Linear
    c) Unilateral
    d) Active only

---

### Answers

**Conceptual Questions:**
1. Adding paths in parallel provides additional routes for charge to flow, increasing overall conductance and thereby decreasing total resistance.
2. Unilateral and non-linear.
3. Charge cannot accumulate at a single point (node) over time in a stable circuit; thus, charge coming in must instantly equal charge going out.
4. House wiring is connected in parallel. Each appliance has its own independent loop with the voltage source.
5. The resistance increases by a factor of 3 ($R_\Delta = 3 R_Y$).

**Numerical Problems:**
1. $R_{eq} = (12 \times 24)/(12 + 24) = 288/36 = 8\ \Omega$.
2. $V_1 = 200 \times (50 / (50+150)) = 200 \times (50/200) = 50\text{V}$.
3. $I_1 = 10 \times (4 / (6+4)) = 10 \times (4/10) = 4\text{A}$.
4. $R_Y = 10 / 3 = 3.33\ \Omega$.
5. From previous example, $R_a = 5\ \Omega$. In series with $10\ \Omega$, total is $15\ \Omega$.

**MCQs:**
1. b, 2. c, 3. d, 4. b, 5. b, 6. c, 7. b, 8. a, 9. c, 10. b
