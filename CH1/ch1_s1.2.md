# Section 1.2: Network Theorems and AC Circuits (AExE0102)

## 📖 1. Introduction
This section forms the backbone of electrical circuit analysis. Understanding how to simplify complex networks using theorems like Thevenin’s and Norton’s, and how energy behaves in AC circuits with resistors, inductors, and capacitors, is fundamental to every branch of electrical and electronics engineering. The NEC Engineering License Exam heavily tests these concepts because they bridge pure theory with practical engineering design.

## Part A: Network Theorems

### 1. Superposition Theorem

#### 1.1 Statement and Conditions
The **Superposition Theorem** states that in any linear, active, bilateral network containing more than one independent source, the response (voltage or current) in any element is the algebraic sum of the responses caused by each independent source acting alone, while all other independent sources are deactivated.

**Conditions for validity:**
- The circuit must be **linear** (obeys Ohm's law, components don't change values with voltage/current).
- Applicable to voltage and current, but **NOT to power** (since power is proportional to the square of voltage/current, which is nonlinear).

#### 1.2 Procedure
1. Identify all independent sources in the circuit.
2. Select one independent source to remain active.
3. **Deactivate** all other independent sources:
   - Voltage sources $\rightarrow$ **Short Circuit** (0V)
   - Current sources $\rightarrow$ **Open Circuit** (0A)
   - *Note: Dependent sources remain active.*
4. Calculate the desired voltage or current due to this single source.
5. Repeat steps 2-4 for every independent source.
6. Algebraically sum the contributions to find the total response.

#### 1.3 Worked Numerical (Circuit with 2 Voltage Sources)

**Given:** A circuit with $V_1 = 12\text{V}$, $R_1 = 4\Omega$, $V_2 = 6\text{V}$, $R_2 = 2\Omega$, $R_L = 4\Omega$ forming a T-network where $R_L$ is the central shunt branch.
**Required:** Current through $R_L$ ($I_L$) using superposition.

**Step 1: Active $V_1 = 12\text{V}$, deactivate $V_2$ (Short Circuit)**
The circuit becomes $V_1$ in series with $R_1$, driving the parallel combination of $R_L$ and $R_2$.
Equivalent resistance: $R_{eq1} = R_1 + (R_L || R_2) = 4 + (4 || 2) = 4 + 1.33 = 5.33 \Omega$
Total current $I_{T1} = 12 / 5.33 = 2.25 \text{A}$
Current through $R_L$ (using current divider): $I_{L1} = I_{T1} \times \frac{R_2}{R_L + R_2} = 2.25 \times \frac{2}{6} = 0.75 \text{A}$ (downward)

**Step 2: Active $V_2 = 6\text{V}$, deactivate $V_1$ (Short Circuit)**
The circuit becomes $V_2$ in series with $R_2$, driving the parallel combination of $R_L$ and $R_1$.
Equivalent resistance: $R_{eq2} = R_2 + (R_L || R_1) = 2 + (4 || 4) = 2 + 2 = 4 \Omega$
Total current $I_{T2} = 6 / 4 = 1.5 \text{A}$
Current through $R_L$: $I_{L2} = I_{T2} \times \frac{R_1}{R_L + R_1} = 1.5 \times \frac{4}{8} = 0.75 \text{A}$ (downward)

**Step 3: Algebraic Sum**
$I_L = I_{L1} + I_{L2} = 0.75 + 0.75 = 1.5 \text{A}$ (downward)

> [!WARNING]
> **Common Mistake:** Trying to calculate total power by adding power contributions from individual sources. Total power $P \neq P_1 + P_2$.

### 2. Thevenin's Theorem

#### 2.1 Statement
Any linear two-terminal network of independent sources, dependent sources, and resistors can be replaced by an equivalent circuit consisting of a single voltage source ($V_{th}$) in series with a single resistor ($R_{th}$).

#### 2.2 Complete 10-Step Procedure
1. **Identify load:** Locate the load resistor $R_L$ where the response is to be found.
2. **Remove load:** Disconnect $R_L$, leaving terminals open (say A and B).
3. **Calculate open-circuit voltage ($V_{th}$):** Find the voltage across A-B.
4. **Deactivate independent sources:** Voltage sources to short circuits, current sources to open circuits.
5. **Calculate equivalent resistance ($R_{th}$):** Find the resistance looking into terminals A-B.
6. **Construct Thevenin equivalent:** Draw $V_{th}$ in series with $R_{th}$.
7. **Reconnect load:** Place $R_L$ back across terminals A-B.
8. **Calculate load current:** $I_L = \frac{V_{th}}{R_{th} + R_L}$
9. **Calculate load voltage:** $V_L = I_L \times R_L$
10. **Calculate load power:** $P_L = I_L^2 \times R_L$

#### 2.3 Worked Numerical (Level 2)
**Given:** Network with $V = 10\text{V}$ series $R_1=2\Omega$, parallel $R_2=3\Omega$, series $R_3=1\Omega$, connected to $R_L=4\Omega$.
**Required:** Current in $R_L$ using Thevenin.

1. Remove $R_L$.
2. $V_{th}$ across A-B is voltage across $R_2$. Voltage divider: $V_{th} = 10 \times \frac{3}{2+3} = 6\text{V}$.
3. Short 10V source. $R_{th}$ is $R_3 + (R_1 || R_2) = 1 + (2 || 3) = 1 + 1.2 = 2.2\Omega$.
4. Thevenin equivalent: $6\text{V}$ in series with $2.2\Omega$.
5. Reconnect $R_L=4\Omega$. $I_L = \frac{6}{2.2 + 4} = \frac{6}{6.2} = 0.967\text{A}$.

### 3. Norton's Theorem

#### 3.1 Statement
Any linear two-terminal network can be replaced by an equivalent circuit consisting of a single current source ($I_N$) in parallel with a single resistor ($R_N$).

#### 3.2 Procedure
1. Identify and remove load $R_L$.
2. **Short-circuit** the load terminals.
3. Calculate the short-circuit current ($I_N$) flowing through the shorted terminals.
4. Calculate $R_N$ (exactly the same procedure as $R_{th}$).
5. Construct Norton equivalent ($I_N || R_N$).
6. Reconnect $R_L$ and calculate $I_L = I_N \times \frac{R_N}{R_N + R_L}$.

#### 3.3 Relationship between Thevenin and Norton
- $R_N = R_{th}$
- $V_{th} = I_N \times R_N$
- $I_N = \frac{V_{th}}{R_{th}}$
This is an application of source transformation.

### 4. Maximum Power Transfer Theorem

#### 4.1 Statement
Maximum power is transferred from a source to a load when the load resistance equals the Thevenin equivalent resistance of the source network as viewed from the load terminals ($R_L = R_{th}$).

#### 4.2 Derivation
1. Power to load: $P_L = I_L^2 R_L = \left(\frac{V_{th}}{R_{th} + R_L}\right)^2 R_L$
2. To find maximum, take derivative with respect to $R_L$ and equate to zero:
   $\frac{dP_L}{dR_L} = V_{th}^2 \left[ \frac{(R_{th} + R_L)^2(1) - R_L(2)(R_{th} + R_L)}{(R_{th} + R_L)^4} \right] = 0$
3. Solving numerator gives: $R_{th} + R_L - 2R_L = 0 \implies R_L = R_{th}$
4. Substituting $R_L = R_{th}$ back into power equation:
   $P_{max} = \frac{V_{th}^2 R_{th}}{(2R_{th})^2} = \frac{V_{th}^2}{4R_{th}}$

#### 4.3 Efficiency
At maximum power transfer, $P_{load} = P_{loss} = I^2 R_{th}$. Total power generated is $2 \times P_{load}$.
Efficiency $\eta = \frac{P_{load}}{P_{total}} \times 100\% = 50\%$.

> [!TIP]
> **Engineering Intuition:** 50% efficiency is terrible for a power grid (we want $\eta > 95\%$), but acceptable in telecommunications (like an antenna receiving a weak signal) where capturing the maximum possible power is more critical than efficiency.

---

## Part B: R-L, R-C, R-L-C Circuits

### 5. R-L Circuit (AC)
- **Impedance:** $Z = R + jX_L = R + j\omega L$
- **Magnitude:** $|Z| = \sqrt{R^2 + X_L^2}$
- **Phase angle:** $\phi = \tan^{-1}\left(\frac{X_L}{R}\right)$
- **Current:** Lags voltage by angle $\phi$.

### 6. R-C Circuit (AC)
- **Impedance:** $Z = R - jX_C = R - j\frac{1}{\omega C}$
- **Magnitude:** $|Z| = \sqrt{R^2 + X_C^2}$
- **Phase angle:** $\phi = \tan^{-1}\left(\frac{-X_C}{R}\right)$
- **Current:** Leads voltage by angle $\phi$.

### 7. R-L-C Series Circuit (AC)
- **Impedance:** $Z = R + j(X_L - X_C)$
- **Three cases:**
  1. $X_L > X_C$: Inductive (current lags)
  2. $X_L < X_C$: Capacitive (current leads)
  3. $X_L = X_C$: Resonance (current in phase with voltage)

---

## Part C: Resonance

### 8. Series Resonance
Occurs when inductive reactance equals capacitive reactance: $X_L = X_C$
- $\omega L = \frac{1}{\omega C} \implies \omega^2 = \frac{1}{LC} \implies f_0 = \frac{1}{2\pi\sqrt{LC}}$
- **Characteristics at resonance:**
  - $Z = R$ (Minimum impedance)
  - Current is maximum ($I = V/R$)
  - Power factor is unity (pf = 1)
- **Quality Factor (Q):** Voltage magnification. $Q = \frac{X_L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$
- **Bandwidth:** $\Delta f = \frac{f_0}{Q} = \frac{R}{2\pi L}$

### 9. Parallel Resonance
For a practical tank circuit (inductor with internal resistance $R$ in parallel with a capacitor):
- Resonant frequency: $f_0 = \frac{1}{2\pi}\sqrt{\frac{1}{LC} - \frac{R^2}{L^2}}$
- If $R$ is very small, $f_0 \approx \frac{1}{2\pi\sqrt{LC}}$
- **At resonance:** Impedance is maximum, Current from source is minimum.

---

## Part D: Active and Reactive Power

### 10. Active Power (P)
- $P = VI \cos(\phi)$ (Watts, W)
- Real power that does useful work (e.g., turns a motor, generates heat).

### 11. Reactive Power (Q)
- $Q = VI \sin(\phi)$ (Volt-Amperes Reactive, VAR)
- Power that oscillates back and forth between source and reactive elements (inductors/capacitors). Maintains magnetic/electric fields.

### 12. Apparent Power (S)
- $S = VI$ (Volt-Amperes, VA)
- $S = P + jQ$ (Complex power)
- Magnitude: $|S| = \sqrt{P^2 + Q^2}$

### 13. Power Factor (pf)
- $pf = \cos(\phi) = \frac{P}{S}$
- Indicates how effectively apparent power is converted to useful work.

---

## End-of-Section

### Conceptual Questions
1. Why does the Superposition Theorem fail for calculating power?
2. Explain the difference between Thevenin's and Norton's equivalent circuits.
3. Why is maximum power transfer not utilized in high-voltage power transmission?
4. What does a leading power factor imply about the circuit load?
5. How does bandwidth relate to the Quality factor in a resonant circuit?

### Numerical Problems
**Level 1:** Find the resonant frequency of an RLC series circuit where $L=10\text{mH}$ and $C=1\mu\text{F}$.
**Level 2:** An AC circuit draws 10A at 220V with a pf of 0.8 lagging. Find Active, Reactive, and Apparent Power.
**Level 3:** Find the Thevenin equivalent of a circuit containing a 12V source in series with $5\Omega$, in parallel with a 2A current source.

### NEC-Style MCQs
1. At series resonance, the circuit impedance is:
   a) Maximum
   b) Minimum
   c) Zero
   d) Infinite
   **Answer:** b
