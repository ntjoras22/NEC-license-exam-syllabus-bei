# Section 1.4: Semiconductor Devices (AExE0104)

> [!NOTE]
> **Syllabus Coverage:** Semiconductor diode and its characteristics, BJT Configuration and biasing, small and large signal model, working principle and application of MOSFET and CMOS.

## 📖 Introduction
Semiconductor devices form the fundamental building blocks of modern electronics. From a simple diode rectifying AC power to billions of CMOS transistors inside a microprocessor, understanding how semiconductors behave under various electrical conditions is critical for any electrical or electronics engineer. This section covers the fundamental physics of semiconductors, diodes, BJTs, MOSFETs, and CMOS technology.

---

## Part A: Semiconductor Fundamentals (Prerequisite)

### 1. Conductors, Semiconductors, Insulators
The electrical properties of materials are defined by their atomic structure, specifically their energy bands.

*   **Valence Band:** The highest energy band completely filled with electrons at absolute zero temperature.
*   **Conduction Band:** The energy band above the valence band. Electrons here are free to move and conduct electricity.
*   **Forbidden Gap ($E_g$):** The energy difference between the conduction and valence bands where no electron states can exist.

| Property | Conductors | Semiconductors | Insulators |
| :--- | :--- | :--- | :--- |
| **Band Gap ($E_g$)** | Overlapping ($E_g \approx 0$) | Small ($E_g \approx 1\text{ eV}$) | Large ($E_g > 5\text{ eV}$) |
| **Conductivity** | Very High | Moderate, controllable | Negligible |
| **Examples** | Copper, Gold, Aluminum | Silicon, Germanium | Glass, Rubber, Diamond |

> [!TIP]
> **💡 Engineering Intuition:** Semiconductors are special not because they conduct "semi-well", but because their conductivity is *controllable* via temperature, voltage, or doping.

### 2. Intrinsic Semiconductor
An intrinsic semiconductor is a perfectly pure semiconductor crystal (e.g., pure Silicon or Germanium).
*   **Covalent Bonding:** Each atom shares 4 valence electrons with its neighbors.
*   **Electron-Hole Pairs:** At room temperature (300K), thermal energy breaks some covalent bonds, creating free electrons and leaving behind vacancies called **holes** (which act as positive charge carriers).
*   **Carrier Concentration:** In intrinsic semiconductors, the number of electrons ($n$) equals the number of holes ($p$). 

$$n = p = n_i$$
    where $n_i$ is the intrinsic carrier concentration.

### 3. Extrinsic Semiconductor
To make semiconductors useful, we deliberately introduce impurities in a process called **doping**.

| Feature | N-Type Semiconductor | P-Type Semiconductor |
| :--- | :--- | :--- |
| **Dopant Impurity** | Pentavalent (Group V: P, As, Sb) | Trivalent (Group III: B, Al, Ga) |
| **Dopant Name** | Donor (donates an electron) | Acceptor (accepts an electron) |
| **Majority Carriers**| Electrons | Holes |
| **Minority Carriers**| Holes | Electrons |
| **Fermi Level** | Shifts towards Conduction Band | Shifts towards Valence Band |

### 4. PN Junction
When P-type and N-type materials are joined, a **PN junction** is formed.

**Formation of Depletion Region:**
1.  High concentration of holes in P and electrons in N causes them to diffuse across the junction.
2.  As electrons cross to the P-side, they leave behind positively charged donor ions. Holes crossing to the N-side leave behind negatively charged acceptor ions.
3.  These immobile ions create a **depletion region** (devoid of mobile charge carriers) and an internal electric field.

**Built-in Potential ($V_{bi}$):**
The electric field creates a barrier potential that opposes further diffusion.
*   Silicon (Si): $\approx 0.7\text{ V}$
*   Germanium (Ge): $\approx 0.3\text{ V}$

```text
       P-Type             Depletion Region            N-Type
 ____________________   ___________________   ____________________
|  +   +   +   +     | |    -    |    +    | |     -   -   -   -  |
|      Majority      | |  Immobile Ions    | |       Majority     |
|  +    (Holes)  +   | |    -    |    +    | |  -  (Electrons) -  |
|____________________| |_________|_________| |____________________|
                           Electric Field
                            E ───────▶
```

---

## Part B: Semiconductor Diode

### 5. Diode Construction and Operation
A diode is simply a PN junction with electrical terminals attached. It allows current to flow in one direction but blocks it in the other.
*   **Symbol:**
    ```text
       Anode (A) ──────▷|────── Cathode (K)
               (P-type)     (N-type)
    ```

### 6. Forward Bias
When the positive terminal of a battery is connected to the Anode (P) and the negative to the Cathode (N):
*   The external voltage *opposes* the built-in potential.
*   The depletion region narrows.
*   Once $V_{external} > V_{barrier}$, large current flows.
*   **Mathematical Formulation (Shockley Diode Equation):**

$$I = I_s \left( e^{\frac{V}{n V_T}} - 1 \right)$$
    | Symbol | Meaning | SI Unit |
    | :--- | :--- | :--- |
    | $I$ | Diode current | A |
    | $I_s$ | Reverse saturation current | A |
    | $V$ | Voltage across diode | V |
    | $n$ | Ideality factor (1 to 2) | Unitless |
    | $V_T$ | Thermal voltage ($kT/q \approx 26\text{mV}$ at 300K) | V |

### 7. Reverse Bias
When positive is connected to Cathode (N) and negative to Anode (P):
*   The external voltage *adds* to the built-in potential.
*   The depletion region widens.
*   Majority carrier current is blocked. Only a tiny minority carrier drift current ($I_s$, leakage current) flows.

### 8. V-I Characteristics
```text
           I (mA)
             |
             |       /
             |     /
             |   /  (Forward Bias)
             | /
  ───────────┼─────────────── V (Volts)
   Breakdown |  0.7V (Knee)
             |
             | (Reverse Leakage, uA)
             |
```
*   **Knee/Cut-in Voltage:** The forward voltage at which current starts to increase rapidly (0.7V for Si).
*   **Breakdown Voltage:** The reverse voltage at which the diode fails and conducts heavily in reverse.

### 9. Diode Models
1.  **Ideal Diode Model:** Acts as a perfect switch. (0V drop when forward, 0A when reverse).
2.  **Constant Voltage Drop (CVD) Model:** Forward-biased diode acts like a constant 0.7V battery opposing current flow.

**Worked Numerical:**
*Given:* A 10V DC source is in series with a Si diode and a $1\text{ k}\Omega$ resistor.
*Required:* Find the current using the CVD model.
*Principle:* KVL.
*Calculation:* $10\text{V} - 0.7\text{V} - I \cdot 1000\Omega = 0 \Rightarrow I = 9.3\text{V} / 1000\Omega = 9.3\text{ mA}$.

### 10. Breakdown
*   **Zener Breakdown:** Occurs in heavily doped diodes. The depletion region is so thin that the strong electric field tears electrons from covalent bonds (tunneling). Usually occurs $< 5V$.
*   **Avalanche Breakdown:** Occurs in lightly doped diodes. High reverse voltage accelerates minority carriers, causing them to collide with atoms and free other electrons in an avalanche effect. Usually occurs $> 5V$.

### 11. Diode Applications
*   **Rectification:** Converting AC to DC (Half-wave, Full-wave).
*   **Voltage Regulation:** Zener diodes in reverse breakdown maintain constant voltage.
*   **Clipping/Clamping:** Limiting waveforms or shifting DC levels.

---

## Part C: Bipolar Junction Transistor (BJT)

### 12. BJT Construction
A BJT consists of three alternating layers of P and N type semiconductors.
*   **NPN:** Emitter (N), Base (P), Collector (N)
*   **PNP:** Emitter (P), Base (N), Collector (P)

**Doping and Sizing:**
1.  **Emitter (E):** Heavily doped (to inject many carriers).
2.  **Base (B):** Very thin and lightly doped (so carriers pass through without recombining).
3.  **Collector (C):** Moderately doped, largest area (to dissipate heat).

```text
       NPN Transistor Symbol
             C
             |
           /¯¯¯\
        B ─|   |─ E (Arrow points outward: NPN)
           \___/
```

### 13. Transistor Action (For NPN)
To use a BJT as an amplifier, it operates in the **Active Region**:
1.  **Base-Emitter (BE) Junction:** Forward-biased. Electrons are injected from the heavily doped emitter into the base.
2.  **Base-Collector (BC) Junction:** Reverse-biased.
3.  Because the base is very thin and lightly doped, 95-99% of electrons shoot straight through the base and are swept into the collector by the strong reverse-bias electric field.
4.  Fundamental KCL Equation: $I_E = I_B + I_C$

### 14. Current Relationships
*   **$\alpha$ (Common-Base Current Gain):** $\alpha = \frac{I_C}{I_E}$. Usually $0.95 \text{ to } 0.998$.
*   **$\beta$ (Common-Emitter Current Gain):** $\beta = \frac{I_C}{I_B}$. Usually $50 \text{ to } 300$.

**Derivation of Relationship:**
1.  Start with $I_E = I_B + I_C$.
2.  Divide by $I_C$: $\frac{I_E}{I_C} = \frac{I_B}{I_C} + 1$.
3.  Substitute $\frac{1}{\alpha} = \frac{1}{\beta} + 1$.
4.  Rearrange: $\beta = \frac{\alpha}{1 - \alpha}$ and $\alpha = \frac{\beta}{\beta + 1}$.

### 15. BJT Configurations

| Characteristic | Common Emitter (CE) | Common Base (CB) | Common Collector (CC) |
| :--- | :--- | :--- | :--- |
| **Input/Output** | Base / Collector | Emitter / Collector | Base / Emitter |
| **Voltage Gain ($A_v$)**| High | High | $\approx 1$ |
| **Current Gain ($A_i$)**| High ($\beta$) | $< 1$ ($\alpha$) | High ($\approx \beta$) |
| **Power Gain** | Very High | Moderate | Moderate |
| **Input Impedance**| Moderate ($\approx 1k\Omega$) | Very Low ($\approx 20\Omega$) | Very High (several $k\Omega$) |
| **Output Impedance**| Moderate | Very High | Low |
| **Phase Shift** | $180^\circ$ (Inverting) | $0^\circ$ | $0^\circ$ |
| **Main Application** | General amplification | High-frequency | Buffer (Impedance matching) |

### 16. Operating Regions
| Region | BE Junction | BC Junction | Application |
| :--- | :--- | :--- | :--- |
| **Cutoff** | Reverse | Reverse | Open Switch (Logic 0) |
| **Active** | Forward | Reverse | Amplifier |
| **Saturation**| Forward | Forward | Closed Switch (Logic 1) |

> [!WARNING]
> ⚠️ **NEC Exam Trap:** BJT Saturation means both junctions are forward-biased, $V_{CE}$ drops to $\approx 0.2V$, and $I_C$ is determined by the external circuit, NOT $\beta I_B$. Do not use $I_C = \beta I_B$ in saturation!

### 17. Biasing and Q-Point
Biasing sets the steady DC operating point (Q-point) in the middle of the active region so that AC signals can swing without clipping.
**Voltage Divider Bias (Most Stable):**
Uses resistors $R_1$ and $R_2$ to divide $V_{CC}$ and set a stable $V_B$.
$V_B \approx V_{CC} \frac{R_2}{R_1 + R_2}$ (assuming $\beta$ is large).
$V_E = V_B - 0.7V$. $I_E = \frac{V_E}{R_E} \approx I_C$. $V_{CE} = V_{CC} - I_C(R_C + R_E)$.

### 18. Small-Signal Model
Small signal analysis treats the BJT as a linear two-port network for small AC variations around the Q-point.
*   **Transconductance ($g_m$):** The ratio of small change in output current to small change in input voltage.
    $g_m = \frac{I_{CQ}}{V_T}$ where $V_T \approx 26\text{mV}$.
*   **Input Resistance ($r_\pi$):** $r_\pi = \frac{\beta}{g_m}$.
*   **Voltage Gain ($A_v$) of CE Amplifier:** $A_v \approx -g_m R_{C\text{(eff)}}$.

### 19. Large-Signal Model vs Small-Signal
*   **Large-Signal (Ebers-Moll):** Non-linear model covering all regions (cutoff, active, sat). Used for DC biasing and switching.
*   **Small-Signal (Hybrid-$\pi$):** Linearized model. Valid only for small AC signals around a fixed DC point.

---

## Part D: MOSFET
**Metal-Oxide-Semiconductor Field-Effect Transistor**

### 20. MOSFET Construction
Instead of a PN junction controlling the current (like BJT), a MOSFET uses an electric field across a dielectric (oxide) to control channel conductivity.
*   **Terminals:** Gate (G), Source (S), Drain (D), Body/Substrate (B). (Body usually tied to Source).
*   **Structure:** Metal Gate, separated from a semiconductor body by a thin layer of Silicon Dioxide ($SiO_2$).

### 21. Working Principle
*   **Enhancement Mode (E-MOSFET):** Normally OFF. A Gate-Source voltage ($V_{GS}$) greater than a threshold ($V_{th}$) must be applied to "enhance" or create a conducting channel by attracting electrons to the surface under the oxide.
*   **Depletion Mode (D-MOSFET):** Normally ON. Channel physically exists; varying $V_{GS}$ modulates its depth.

### 22. Regions of Operation (Enhancement NMOS)
1.  **Cutoff:** $V_{GS} < V_{th}$. No channel. $I_D = 0$.
2.  **Linear / Triode:** $V_{GS} > V_{th}$ and $V_{DS} < V_{GS} - V_{th}$. Channel behaves like a voltage-controlled resistor.
    $I_D = k_n \left[ (V_{GS} - V_{th})V_{DS} - \frac{V_{DS}^2}{2} \right]$
3.  **Saturation:** $V_{GS} > V_{th}$ and $V_{DS} \ge V_{GS} - V_{th}$. Channel "pinches off". Current becomes independent of $V_{DS}$ and acts as a constant current source.
    $I_D = \frac{k_n}{2} (V_{GS} - V_{th})^2$
    *(Where $k_n = \mu_n C_{ox} \frac{W}{L}$ is the conduction parameter)*

> [!WARNING]
> ⚠️ **NEC Exam Trap:** Notice that "Saturation" in a MOSFET means it is acting as a constant current source (ideal for amplification). In a BJT, "Saturation" means it acts as a short circuit (switch ON). The terminology is exactly opposite in meaning for amplifiers!

### 23. MOSFET Applications
*   Microprocessors, memory chips (Digital logic).
*   Power electronics (Power MOSFETs for high current switching).
*   Analog amplification (due to high input impedance).

### 24. BJT vs MOSFET Comparison

| Feature | BJT | MOSFET |
| :--- | :--- | :--- |
| **Control Variable** | Current controlled ($I_B$ controls $I_C$) | Voltage controlled ($V_{GS}$ controls $I_D$) |
| **Carriers** | Bipolar (electrons and holes) | Unipolar (only majority carriers) |
| **Input Impedance**| Low to Moderate | Extremely High (virtually infinite at DC) |
| **Size / Packing** | Larger | Very small (excellent for VLSI) |
| **Thermal Stability**| Poor (Prone to thermal runaway) | Excellent (Positive temp coefficient) |

---

## Part E: CMOS

### 25. CMOS Concept
**Complementary MOS (CMOS)** uses both NMOS and PMOS transistors in pairs.

**CMOS Inverter:**
```text
           +VDD
            |
           _|_
     Vin --||_  (PMOS: turns ON when Vin is LOW)
            |
            +------- Vout
            |
           _|_
     Vin --||_  (NMOS: turns ON when Vin is HIGH)
            |
           GND
```
*   When $V_{in} = \text{HIGH}$ (VDD): NMOS is ON, PMOS is OFF. $V_{out}$ is pulled to GND.
*   When $V_{in} = \text{LOW}$ (GND): NMOS is OFF, PMOS is ON. $V_{out}$ is pulled to VDD.

### 26. CMOS Advantages
1.  **Zero Static Power:** In steady state (either Logic 0 or 1), one transistor is always OFF. There is no direct path from VDD to GND. Power is only consumed during *switching* (dynamic power).
2.  **High Noise Margin:** VTC is nearly ideal.
3.  **High Density:** Tiny footprint, making billions of transistors on a chip possible.

### 27. Applications
Almost all modern digital ICs, microprocessors, ASICs, and memory (SRAM) are built using CMOS technology.

---

## End-of-Section

### Key Equations
| Concept | Equation |
| :--- | :--- |
| **Intrinsic Carriers** | $n = p = n_i$ |
| **Shockley Diode** | $I = I_s \left( e^{\frac{V}{n V_T}} - 1 \right)$ |
| **BJT Current** | $I_E = I_B + I_C$ |
| **BJT Alpha/Beta** | $\beta = \frac{\alpha}{1-\alpha} \quad ; \quad \alpha = \frac{\beta}{\beta+1}$ |
| **MOSFET Saturation** | $I_D = \frac{k_n}{2} (V_{GS} - V_{th})^2$ |
| **BJT Transconductance** | $g_m = \frac{I_{CQ}}{V_T}$ |

### 5 Conceptual Questions
1. Why does an intrinsic semiconductor behave like an insulator at absolute zero temperature (0 K)?
2. Why is the base of a BJT made very thin and lightly doped?
3. Explain why the input impedance of a MOSFET is vastly higher than that of a BJT.
4. Why does a BJT enter thermal runaway while a MOSFET does not?
5. Why is CMOS the dominant technology for digital integrated circuits?

### 5 Worked Numerical Problems

**LEVEL 1 (Foundation)**
**Q1:** A silicon diode has a reverse saturation current of $10\text{ nA}$ at 300K. Calculate the forward current if a forward voltage of $0.6\text{ V}$ is applied. (Assume $n=1$, $V_T=26\text{mV}$)
*   **Given:** $I_s = 10\text{ nA} = 10 \times 10^{-9}\text{A}$, $V = 0.6\text{V}$, $V_T = 0.026\text{V}$.
*   **Formula:** $I = I_s e^{V/V_T}$
*   **Calculation:** $I = (10 \times 10^{-9}) \times e^{0.6/0.026} = 10 \times 10^{-9} \times 1.05 \times 10^{10} = 0.105\text{ A} = 105\text{ mA}$.
*   **Answer:** $105\text{ mA}$.

**Q2:** A BJT has an $\alpha$ of 0.99. If the base current is $20\text{ \mu A}$, calculate the collector current and emitter current.
*   **Given:** $\alpha = 0.99$, $I_B = 20\text{ \mu A}$.
*   **Formula:** $\beta = \frac{\alpha}{1-\alpha}$, $I_C = \beta I_B$, $I_E = I_C + I_B$.
*   **Calculation:** $\beta = 0.99 / 0.01 = 99$. $I_C = 99 \times 20\text{\mu A} = 1.98\text{ mA}$. $I_E = 1.98\text{ mA} + 0.02\text{ mA} = 2.0\text{ mA}$.
*   **Answer:** $I_C = 1.98\text{ mA}$, $I_E = 2.0\text{ mA}$.

**LEVEL 2 (Engineering)**
**Q3:** For a CE amplifier, $V_{CC} = 12\text{V}$, $R_C = 2\text{k}\Omega$, and $\beta = 100$. If it is biased such that $V_{CE} = 6\text{V}$ (midpoint), calculate the required base current $I_B$. (Assume $R_E=0$).
*   **Given:** $V_{CC}=12\text{V}$, $V_{CE}=6\text{V}$, $R_C=2000\Omega$.
*   **Principle:** KVL at output: $V_{CC} - I_C R_C - V_{CE} = 0$.
*   **Calculation:** $I_C = (12 - 6)/2000 = 3\text{ mA}$. $I_B = I_C / \beta = 3\text{mA} / 100 = 30\text{ \mu A}$.
*   **Answer:** $30\text{ \mu A}$.

**Q4:** An NMOS transistor has $V_{th} = 1\text{V}$ and $k_n = 1\text{ mA/V}^2$. It is biased with $V_{GS} = 3\text{V}$ and $V_{DS} = 4\text{V}$. Determine the region of operation and the drain current.
*   **Given:** $V_{th}=1\text{V}$, $V_{GS}=3\text{V}$, $V_{DS}=4\text{V}$.
*   **Principle:** Check condition: $V_{GS} > V_{th}$ ($3>1$, ON). Check saturation: $V_{GS} - V_{th} = 3 - 1 = 2\text{V}$. Since $V_{DS} (4\text{V}) > (V_{GS}-V_{th})$ (2V), the MOSFET is in **Saturation**.
*   **Formula:** $I_D = \frac{k_n}{2}(V_{GS}-V_{th})^2$
*   **Calculation:** $I_D = \frac{1\text{m}}{2} (3-1)^2 = 0.5\text{m} \times 4 = 2\text{ mA}$.
*   **Answer:** Saturation Region, $I_D = 2\text{ mA}$.

**LEVEL 3 (NEC Challenge)**
**Q5:** Calculate the small signal transconductance ($g_m$) and input resistance ($r_\pi$) of a BJT at room temperature (300K) if it is biased with a collector current of $2.6\text{ mA}$ and has $\beta = 100$.
*   **Given:** $I_{CQ} = 2.6\text{ mA}$, $\beta = 100$, $V_T = 26\text{ mV}$.
*   **Formula:** $g_m = \frac{I_C}{V_T}$, $r_\pi = \frac{\beta}{g_m}$.
*   **Calculation:** $g_m = \frac{2.6\text{ mA}}{26\text{ mV}} = 0.1\text{ S} = 100\text{ mA/V}$.
$r_\pi = 100 / 0.1 = 1000\Omega = 1\text{ k}\Omega$.
*   **Answer:** $g_m = 100\text{ mA/V}$, $r_\pi = 1\text{ k}\Omega$.

### 10 NEC-Style MCQs

**1. The forbidden energy gap in Silicon at room temperature is approximately:**
A) $0.3\text{ eV}$
B) $0.7\text{ eV}$
C) $1.1\text{ eV}$
D) $5.0\text{ eV}$

**2. In an N-type semiconductor, the Fermi level lies:**
A) exactly in the middle of the forbidden gap.
B) closer to the conduction band.
C) closer to the valence band.
D) inside the valence band.

**3. In a reverse-biased PN junction diode, the current is mainly due to:**
A) Majority carriers
B) Minority carriers
C) Holes only
D) Surface leakage only

**4. The relation between $\alpha$ and $\beta$ in a BJT is:**
A) $\beta = \frac{\alpha}{\alpha + 1}$
B) $\beta = \frac{\alpha}{1 - \alpha}$
C) $\beta = \frac{1 - \alpha}{\alpha}$
D) $\alpha = \frac{\beta - 1}{\beta}$

**5. For a BJT to operate in the saturation region:**
A) Both BE and BC junctions must be reverse-biased.
B) BE junction must be forward-biased and BC reverse-biased.
C) BE junction must be reverse-biased and BC forward-biased.
D) Both BE and BC junctions must be forward-biased.

**6. Which BJT configuration provides a phase reversal of $180^\circ$ between input and output?**
A) Common Base
B) Common Emitter
C) Common Collector
D) All of the above

**7. In an enhancement-type NMOS, the channel is formed when:**
A) $V_{GS} < V_{th}$
B) $V_{GS} > V_{th}$
C) $V_{DS} > V_{GS}$
D) $V_{DS} = 0$

**8. When a MOSFET acts as an amplifier, it is operated in the:**
A) Cut-off region
B) Linear (Triode) region
C) Saturation region
D) Breakdown region

**9. The primary advantage of CMOS over other logic families is:**
A) Higher speed
B) Higher current handling capacity
C) Extremely low static power consumption
D) Simpler manufacturing process

**10. Small-signal modeling of a BJT is used to analyze its:**
A) DC biasing point
B) AC response around the Q-point
C) Maximum power dissipation
D) Switching speed

### Answers to MCQs
1. C | 2. B | 3. B | 4. B | 5. D | 6. B | 7. B | 8. C | 9. C | 10. B
