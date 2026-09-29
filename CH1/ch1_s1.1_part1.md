# CHAPTER 1 — CONCEPT OF BASIC ELECTRICAL AND ELECTRONICS ENGINEERING

# Section 1.1 — Basic Concept (AExE0101)

# PART 1: Electric Charge, Voltage, Current, Resistance, and Ohm's Law

---

## 📌 Prerequisite Note

This section builds foundational concepts from the ground up. Even if you studied these in your BE program, review them carefully. NEC exam questions often test subtle understanding of fundamentals — not just formula recall.

---

# 1.1.1 ELECTRIC CHARGE

## 📖 Introduction

Electric charge is the most fundamental quantity in electrical engineering. Every electrical phenomenon — from a simple flashlight circuit to a complex communication system — originates from the existence and movement of electric charges. Without understanding charge, nothing else in this chapter makes sense.

## ⚠️ Why Is It Important?

An engineer needs the concept of charge because:
- **Voltage** is defined as energy per unit charge
- **Current** is defined as the rate of flow of charge
- **Capacitance** stores charge
- **Coulomb's law** governs force between charges
- All electromagnetic phenomena arise from charges (stationary or moving)

## 💡 Basic Concept

All matter is composed of atoms. Each atom contains:

| Particle | Location | Charge |
|----------|----------|--------|
| Proton | Nucleus | Positive (+) |
| Neutron | Nucleus | Neutral (0) |
| Electron | Orbits around nucleus | Negative (−) |

In a neutral atom, the number of protons equals the number of electrons. When an atom **loses** electrons, it becomes positively charged (cation). When it **gains** electrons, it becomes negatively charged (anion).

**The fundamental unit of charge is the charge of one electron (or proton).**

## ✏️ Definition

> **Electric charge** is a fundamental physical property of matter that causes it to experience a force when placed in an electromagnetic field. It is a scalar quantity measured in **coulombs (C)**.

## Physical Meaning

Charge is not something you can see or touch directly. What you observe are its **effects**:
- Two like charges repel each other
- Two unlike charges attract each other
- Moving charges create magnetic fields
- Accelerating charges radiate electromagnetic waves

Think of charge as a "label" on certain particles that determines how they interact with electric and magnetic fields.

## 📈 Mathematical Formulation

The charge of a single electron:

$$e = 1.602 \times 10^{-19} \text{ C}$$

If a body has lost or gained $n$ electrons, its net charge is:

$$Q = n \times e$$

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $Q$ | Electric charge | Coulomb (C) |
| $n$ | Number of electrons transferred | Dimensionless |
| $e$ | Charge of one electron | $1.602 \times 10^{-19}$ C |

### Important Relationships

$$1 \text{ C} = \frac{1}{1.602 \times 10^{-19}} \approx 6.242 \times 10^{18} \text{ electrons}$$

> [!NOTE]
> One coulomb is an **enormous** amount of charge. In practical circuits, charges of microcoulombs (μC) or even picocoulombs (pC) are common in electronic devices.

## 📋 Properties of Electric Charge

1. **Quantization**: Charge always exists in integer multiples of $e$. You cannot have $0.5e$.
2. **Conservation**: Charge can neither be created nor destroyed. The total charge in an isolated system remains constant.
3. **Additive**: Total charge = algebraic sum of individual charges.

## Engineering Interpretation

In circuit analysis, we rarely think about individual electrons. Instead, we work with **current** (rate of charge flow) and **voltage** (energy per unit charge). However, understanding that current is fundamentally moving charges helps you understand:
- Why conductors conduct (free electrons)
- Why insulators don't (bound electrons)
- Why semiconductors are special (controllable conductivity)

## 💡 💡 Engineering Intuition

> Think of charge like water. You don't usually measure individual water molecules — you measure flow rate (current) and pressure (voltage). But knowing that water is made of molecules helps you understand why certain pipes (conductors) let water through and others (insulators) don't.

---

# 1.1.2 ELECTRIC VOLTAGE (POTENTIAL DIFFERENCE)

## 📖 Introduction

Voltage is arguably the most important concept in electrical engineering. It is the "driving force" that pushes electric charges through a circuit. Without voltage, there is no current, no power, and no useful work.

## ⚠️ Why Is It Important?

- Voltage determines whether current will flow
- Voltage ratings define the operating limits of every electrical device
- Voltage measurement is the most common electrical measurement
- Understanding voltage is essential for applying Kirchhoff's Voltage Law (KVL)
- Power calculation requires voltage: $P = VI$

## 💡 Basic Concept — Building From Energy

To move a charge against an electric field, you must do **work** on it (spend energy). This is analogous to lifting a mass against gravity — you expend energy, and the mass gains potential energy.

Similarly, when work is done to move a charge from one point to another in an electric field, the charge gains **electrical potential energy**.

**Voltage (potential difference)** is defined as the work done per unit charge in moving a charge between two points.

## ✏️ Definition

> **Voltage** (or **potential difference**) between two points $A$ and $B$ is the work done per unit positive charge in moving a test charge from $B$ to $A$.

$$V_{AB} = \frac{W}{Q}$$

Or equivalently:

> **Voltage** is the energy transferred per unit charge.

## Physical Meaning

Voltage represents an **energy difference** between two points. It tells you:
- How much energy each coulomb of charge gains (at a source) or loses (across a load) as it moves between those two points
- The "electrical pressure" driving charges through a circuit

```
Higher Potential (+)        Lower Potential (−)
       A ──────────────────────── B
              V_AB = V_A − V_B

       Conventional current flows from A to B (high to low potential)
       Electrons actually move from B to A (low to high potential)
```

> [!IMPORTANT]
> **Voltage is always measured BETWEEN two points.** Saying "the voltage at point A" actually means "the voltage at point A with respect to some reference point (usually ground)."

## 📈 Mathematical Formulation

$$V = \frac{W}{Q}$$

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $V$ | Voltage (potential difference) | Volt (V) |
| $W$ | Work done / Energy transferred | Joule (J) |
| $Q$ | Charge | Coulomb (C) |

### Dimensional Check

$$[V] = \frac{[W]}{[Q]} = \frac{\text{J}}{\text{C}} = \text{V}$$

**1 Volt = 1 Joule per Coulomb**

This means: If 1 joule of energy is needed to move 1 coulomb of charge between two points, the potential difference between those points is 1 volt.

## EMF vs Voltage Drop

Two related but distinct concepts:

| Quantity | Symbol | Meaning |
|----------|--------|---------|
| **EMF (Electromotive Force)** | $\mathcal{E}$ or $E$ | Energy supplied per unit charge by a source (battery, generator) |
| **Voltage Drop** | $V$ | Energy consumed per unit charge by a circuit element (resistor, load) |

- A **battery** provides EMF — it converts chemical energy to electrical energy
- A **resistor** causes a voltage drop — it converts electrical energy to heat

In an ideal circuit with no internal resistance:

$$\text{EMF} = \text{Sum of voltage drops around the loop}$$

This is the foundation of **Kirchhoff's Voltage Law**, which we will study in detail later.

## 🔍 Worked Example

**Example 1.1**: A battery does 48 J of work to move 6 C of charge from its negative terminal to its positive terminal. What is the EMF of the battery?

**Given:** $W = 48$ J, $Q = 6$ C

**Required:** EMF ($V$)

**Formula:** $V = \frac{W}{Q}$

**Substitution:** $V = \frac{48}{6}$

**Answer:** $V = 8$ V

**Engineering Interpretation:** Each coulomb of charge gains 8 joules of energy as it passes through the battery.

## Worked Numerical Problem

**Problem 1.1** (Level 1): How much energy is transferred when 15 mC of charge moves through a potential difference of 12 V?

**Given:** $Q = 15 \text{ mC} = 15 \times 10^{-3} \text{ C} = 0.015$ C, $V = 12$ V

**Required:** Energy transferred ($W$)

**Principle:** Definition of voltage

**Formula:** $V = \frac{W}{Q} \implies W = VQ$

**Substitution:** $W = 12 \times 0.015$

**Calculation:** $W = 0.18$ J $= 180$ mJ

**Final Answer:** $W = 180$ mJ

**Unit Check:** V × C = (J/C) × C = J ✓

**Engineering Interpretation:** 180 millijoules of energy is transferred as 15 millicoulombs of charge moves through a 12 V potential difference.

**Common Mistake:** Forgetting to convert mC to C before substituting. $15 \text{ mC} \neq 15 \text{ C}$.

## ⚠️ NEC Exam Traps

1. **Confusing EMF and terminal voltage**: A real battery with internal resistance $r$ has terminal voltage $V_T = \mathcal{E} - Ir$, which is less than EMF when current flows.
2. **Sign of voltage**: Voltage can be positive or negative depending on the reference direction. In KVL, getting signs wrong is the most common error.
3. **Voltage at a point**: Always ask "with respect to what?" There is no absolute voltage — only potential differences.

## 💡 💡 Engineering Intuition

> Voltage is like the height difference in a waterfall. Water (charge) flows from high to low. The greater the height difference (voltage), the more energy the water (charge) carries. A pump (battery) lifts water back up (provides EMF), while the waterfall (resistor) converts that potential energy into kinetic energy and heat (voltage drop).

---

# 1.1.3 ELECTRIC CURRENT

## 📖 Introduction

While voltage is the "cause," current is the "effect." Electric current is the flow of electric charges through a conductor. It is the quantity that actually does useful work in circuits — it heats filaments, spins motors, charges capacitors, and carries signals.

## ⚠️ Why Is It Important?

- Current through a resistor determines heat dissipation ($P = I^2R$)
- Current determines the magnetic field around a conductor
- Circuit protection (fuses, breakers) is based on current limits
- Kirchhoff's Current Law is fundamental to circuit analysis
- Signal processing deals with time-varying currents

## 💡 Basic Concept

When a voltage (potential difference) is applied across a conductor, the free electrons inside the conductor experience an electric force and begin to drift from the region of lower potential (negative terminal) toward the region of higher potential (positive terminal).

This ordered movement of charges constitutes **electric current**.

```
  Battery
  + ───────────────────── −
  │                       │
  │   ← Electron flow     │
  │                       │
  │   → Conventional       │
  │     current (I)        │
  │                       │
  ├───────[R]─────────────┤
      Resistor (Load)
```

### Conventional Current vs Electron Flow

| Convention | Direction |
|-----------|-----------|
| **Conventional current** | From positive (+) to negative (−) terminal externally |
| **Electron flow** | From negative (−) to positive (+) terminal externally |

> [!IMPORTANT]
> In circuit analysis and all engineering calculations, we use **conventional current direction** unless explicitly stated otherwise. This is a universal convention — do NOT mix up the two in NEC exam problems.

## ✏️ Definition

> **Electric current** is the rate of flow of electric charge through a cross-section of a conductor.

$$I = \frac{Q}{t} \quad \text{(for steady/DC current)}$$

$$i = \frac{dq}{dt} \quad \text{(general/instantaneous current)}$$

## Physical Meaning

Current tells you **how many coulombs of charge pass through a point per second**.

If $I = 1$ A, it means $6.242 \times 10^{18}$ electrons pass through any cross-section of the conductor every second.

## 📈 Mathematical Formulation

### For constant (DC) current:

$$I = \frac{Q}{t}$$

### For time-varying current:

$$i(t) = \frac{dq}{dt}$$

### Conversely, charge from current:

$$Q = \int_{t_1}^{t_2} i(t) \, dt$$

For constant current: $Q = I \times t$

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $I$ or $i$ | Electric current | Ampere (A) |
| $Q$ or $q$ | Electric charge | Coulomb (C) |
| $t$ | Time | Second (s) |

### Dimensional Check

$$[I] = \frac{[Q]}{[t]} = \frac{\text{C}}{\text{s}} = \text{A}$$

**1 Ampere = 1 Coulomb per Second**

### Common Prefixes

| Prefix | Symbol | Value | Typical Use |
|--------|--------|-------|-------------|
| Milliampere | mA | $10^{-3}$ A | Electronic circuits |
| Microampere | μA | $10^{-6}$ A | Sensor circuits, leakage |
| Nanoampere | nA | $10^{-9}$ A | Very sensitive instruments |
| Kiloampere | kA | $10^3$ A | Power systems, lightning |

## 📚 Types of Current

| Type | Symbol | Description | Waveform |
|------|--------|-------------|----------|
| **Direct Current (DC)** | $I$ | Constant magnitude, unidirectional | Straight horizontal line |
| **Alternating Current (AC)** | $i(t)$ | Varies sinusoidally with time, reverses direction periodically | Sine wave |
| **Pulsating DC** | — | Varies in magnitude but does not reverse direction | Varying above zero |

```
DC Current                    AC Current
I ↑                          i ↑
  │ ─────────────              │    ╱╲      ╱╲
  │                            │  ╱    ╲  ╱    ╲
  │                            │╱        ╲╱      ╲─→ t
  └──────────→ t               │          
                               │
```

## Drift Velocity (Supporting Concept)

Although individual electrons move randomly at high speeds (~$10^6$ m/s), their net directed motion under an applied electric field is very slow. This net velocity is called **drift velocity** ($v_d$).

$$I = nAv_d e$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $n$ | Number density of free electrons | m⁻³ |
| $A$ | Cross-sectional area of conductor | m² |
| $v_d$ | Drift velocity | m/s |
| $e$ | Charge of electron | C |

For copper, $v_d$ is typically on the order of $10^{-4}$ m/s (a fraction of a millimeter per second!). Yet the **signal** (electric field) propagates at nearly the speed of light, which is why a light turns on almost instantly when you flip a switch.

## 🔍 Worked Example

**Example 1.2**: A current of 2 A flows through a wire for 5 minutes. How much charge has passed through the wire?

**Given:** $I = 2$ A, $t = 5 \text{ min} = 300$ s

**Required:** Charge $Q$

**Formula:** $Q = I \times t$

**Substitution:** $Q = 2 \times 300 = 600$ C

**Answer:** $Q = 600$ C

**Common Mistake:** Forgetting to convert minutes to seconds. $t = 5$ min ≠ 5 s.

## Worked Numerical Problem

**Problem 1.2** (Level 2): The current through a conductor varies as $i(t) = 3t^2 + 2t$ amperes. Find the total charge that flows between $t = 1$ s and $t = 3$ s.

**Given:** $i(t) = 3t^2 + 2t$ A, $t_1 = 1$ s, $t_2 = 3$ s

**Required:** Total charge $Q$

**Principle:** Charge is the integral of current over time

**Formula:** $Q = \int_{t_1}^{t_2} i(t) \, dt$

**Substitution:**

$$Q = \int_1^3 (3t^2 + 2t) \, dt$$

**Calculation:**

$$Q = \left[ t^3 + t^2 \right]_1^3$$

$$Q = (3^3 + 3^2) - (1^3 + 1^2)$$

$$Q = (27 + 9) - (1 + 1)$$

$$Q = 36 - 2 = 34 \text{ C}$$

**Final Answer:** $Q = 34$ C

**Unit Check:** $\int A \cdot s = C$ ✓

**Engineering Interpretation:** 34 coulombs of charge flowed through the conductor in the 2-second interval. The current is increasing with time (due to the $t^2$ and $t$ terms), so most of this charge flows during the latter part of the interval.

## ⚠️ NEC Exam Traps

1. **Unit conversion**: Always convert time to seconds before calculation.
2. **Current direction**: In circuit analysis, if you assume a current direction and get a negative answer, it means the actual current flows opposite to your assumed direction — it does NOT mean your analysis is wrong.
3. **DC vs AC current**: In DC, $I = Q/t$ directly. For AC or time-varying current, you must integrate.

## 💡 💡 Engineering Intuition

> Current is like the flow rate of water in a pipe. A 1-ampere current means 1 coulomb of charge passes any point per second. A thicker pipe (larger conductor cross-section) doesn't mean more current unless you increase the pressure (voltage). Current depends on voltage AND resistance.

---

# 1.1.4 RESISTANCE AND OHM'S LAW

## 📖 Introduction

Resistance is the property of a material that **opposes** the flow of electric current. It is the "friction" of the electrical world. Understanding resistance is essential because every real conductor has some resistance, and this resistance determines how much current flows for a given voltage.

**Ohm's Law** — the relationship between voltage, current, and resistance — is the single most important equation in electrical engineering.

## ⚠️ Why Is It Important?

- Ohm's Law is the foundation of ALL circuit analysis
- Resistance determines current for a given voltage
- Resistance determines power dissipation (heat)
- Understanding resistance is needed for: series/parallel circuits, voltage dividers, current dividers, network theorems, impedance (AC), and transistor biasing
- Every NEC exam will have problems requiring Ohm's Law

---

## RESISTANCE

### Basic Concept

When current flows through a conductor, the moving electrons collide with the fixed atoms of the conductor material. These collisions:
- Impede the flow of electrons (resistance)
- Convert electrical energy to heat (Joule heating)

Different materials offer different levels of opposition:
- **Copper**: Low resistance → Good conductor
- **Glass**: Extremely high resistance → Insulator
- **Silicon**: Moderate resistance → Semiconductor

### Definition

> **Resistance** is the property of a material that opposes the flow of electric current through it. It is measured in **ohms (Ω)**.

> Mathematically, resistance is the ratio of voltage across an element to the current through it.

$$R = \frac{V}{I}$$

**1 Ohm**: A conductor has a resistance of 1 Ω if a potential difference of 1 V across it produces a current of 1 A.

### Physical Meaning

Resistance represents **how difficult it is for current to flow through a material**. High resistance means:
- For the same voltage, less current flows
- More energy is converted to heat per unit charge
- The material is a poorer conductor

### Factors Affecting Resistance

The resistance of a conductor depends on:

$$R = \frac{\rho L}{A}$$

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $R$ | Resistance | Ohm (Ω) |
| $\rho$ | Resistivity (material property) | Ω·m |
| $L$ | Length of conductor | m |
| $A$ | Cross-sectional area | m² |

### Derivation of $R = \rho L / A$

Consider a uniform cylindrical conductor:

```
       ← L (length) →
    ┌─────────────────────┐
    │                     │   A (cross-sectional area)
    │  ← Current flow →   │
    └─────────────────────┘
```

**Physical reasoning:**
1. **Length ($L$)**: A longer conductor means electrons must travel farther and undergo more collisions. Therefore, $R \propto L$.
2. **Area ($A$)**: A larger cross-section provides more "lanes" for electrons. Therefore, $R \propto \frac{1}{A}$.
3. **Resistivity ($\rho$)**: Different materials have different atomic structures and electron densities. This material-dependent constant captures the intrinsic opposition of the material.

Combining: $R = \rho \frac{L}{A}$

### Important Resistivity Values

| Material | Resistivity $\rho$ (Ω·m) at 20°C | Classification |
|----------|-----------------------------------|----------------|
| Silver | $1.59 \times 10^{-8}$ | Conductor |
| Copper | $1.68 \times 10^{-8}$ | Conductor |
| Aluminum | $2.65 \times 10^{-8}$ | Conductor |
| Tungsten | $5.6 \times 10^{-8}$ | Conductor |
| Silicon | $6.4 \times 10^{2}$ | Semiconductor |
| Glass | $10^{10}$ to $10^{14}$ | Insulator |
| Rubber | $\sim 10^{13}$ | Insulator |

### Conductance

The reciprocal of resistance is **conductance**:

$$G = \frac{1}{R} = \frac{A}{\rho L} = \frac{\sigma A}{L}$$

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $G$ | Conductance | Siemens (S) or mho (℧) |
| $\sigma$ | Conductivity ($= 1/\rho$) | S/m |

### Temperature Effect on Resistance

For most metals, resistance **increases** with temperature:

$$R_T = R_0 [1 + \alpha (T - T_0)]$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $R_T$ | Resistance at temperature $T$ | Ω |
| $R_0$ | Resistance at reference temperature $T_0$ | Ω |
| $\alpha$ | Temperature coefficient of resistance | °C⁻¹ |
| $T$ | Operating temperature | °C |
| $T_0$ | Reference temperature (usually 20°C) | °C |

- **Metals**: $\alpha > 0$ (positive temperature coefficient — PTC)
- **Semiconductors**: $\alpha < 0$ (negative temperature coefficient — NTC)
- **Alloys** (e.g., Manganin, Constantan): $\alpha \approx 0$ (used for precision resistors)

---

## OHM'S LAW

### Basic Concept

Georg Simon Ohm discovered experimentally (1827) that for many materials, the current through a conductor is **directly proportional** to the voltage across it, provided the temperature and other physical conditions remain constant.

### Statement

> **Ohm's Law**: The current flowing through a conductor is directly proportional to the potential difference across it and inversely proportional to its resistance, provided the temperature remains constant.

### Mathematical Formulation

$$V = IR$$

This can be rearranged into three forms:

| Form | Formula | Use When You Know | And Need |
|------|---------|-------------------|----------|
| 1 | $V = IR$ | Current and Resistance | Voltage |
| 2 | $I = \frac{V}{R}$ | Voltage and Resistance | Current |
| 3 | $R = \frac{V}{I}$ | Voltage and Current | Resistance |

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $V$ | Voltage across the element | Volt (V) |
| $I$ | Current through the element | Ampere (A) |
| $R$ | Resistance of the element | Ohm (Ω) |

### Conditions of Validity

Ohm's Law is valid when:
1. **Temperature is constant** (resistance changes with temperature)
2. **The material is ohmic** (linear V-I relationship)
3. **Physical conditions are constant** (no mechanical stress, constant dimensions)

### V-I Characteristic of an Ohmic Resistor

```
    V ↑
      │        ╱
      │      ╱
      │    ╱   slope = R
      │  ╱
      │╱
      └──────────→ I
```

The V-I characteristic of an ohmic (linear) resistor is a **straight line through the origin**. The slope equals the resistance $R$.

### Ohm's Law — Circuit Diagram

```
         I →
    ┌────────────┐
    │            │
   (+)          ┌┤
    V     R =   ││  Resistor
   (−)          └┤
    │            │
    └────────────┘
    
    V = IR
    
    Note: Current enters the positive terminal
    of the resistor (passive sign convention)
```

### Passive Sign Convention

> [!IMPORTANT]
> In **passive sign convention**, the current enters the positive terminal of a passive element (resistor). This gives $V = +IR$. If current enters the negative terminal, then $V = -IR$. Getting this convention right is critical for KVL problems.

### Physical Interpretation

Ohm's Law tells us:
1. **For fixed R**: Doubling the voltage doubles the current (linear relationship)
2. **For fixed V**: Doubling the resistance halves the current
3. **For fixed I**: Doubling the resistance doubles the required voltage

### Derivation (Microscopic)

While Ohm's Law is empirical (discovered through experiment), it can be derived from the microscopic behavior of electrons in a conductor.

Starting from the drift velocity relation:

$$J = \sigma E$$

where $J$ is current density (A/m²), $\sigma$ is conductivity (S/m), and $E$ is electric field (V/m).

For a uniform conductor of length $L$ and cross-section $A$:

$$J = \frac{I}{A}, \quad E = \frac{V}{L}$$

Substituting:

$$\frac{I}{A} = \sigma \frac{V}{L}$$

$$I = \frac{\sigma A}{L} \cdot V$$

$$I = \frac{V}{R} \quad \text{where } R = \frac{L}{\sigma A} = \frac{\rho L}{A}$$

This gives us Ohm's Law: $V = IR$, derived from the fundamental relationship between current density and electric field.

### Worked Example

**Example 1.3**: A resistor of 470 Ω has a current of 20 mA flowing through it. What is the voltage across the resistor?

**Given:** $R = 470$ Ω, $I = 20 \text{ mA} = 0.02$ A

**Required:** Voltage $V$

**Formula:** $V = IR$

**Substitution:** $V = 0.02 \times 470$

**Answer:** $V = 9.4$ V

### Worked Numerical Problem

**Problem 1.3** (Level 2): A copper wire is 200 m long with a cross-sectional area of $2 \text{ mm}^2$. The resistivity of copper is $1.68 \times 10^{-8}$ Ω·m. (a) Find the resistance of the wire. (b) If a voltage of 5 V is applied across the wire, find the current. (c) Find the power dissipated.

**Given:** $L = 200$ m, $A = 2 \text{ mm}^2 = 2 \times 10^{-6} \text{ m}^2$, $\rho = 1.68 \times 10^{-8}$ Ω·m, $V = 5$ V

**(a) Find Resistance:**

**Formula:** $R = \frac{\rho L}{A}$

**Substitution:** $R = \frac{1.68 \times 10^{-8} \times 200}{2 \times 10^{-6}}$

**Calculation:**

$$R = \frac{3.36 \times 10^{-6}}{2 \times 10^{-6}} = 1.68 \text{ Ω}$$

**(b) Find Current:**

**Formula:** $I = \frac{V}{R}$

**Substitution:** $I = \frac{5}{1.68}$

**Calculation:** $I = 2.976$ A $\approx 2.98$ A

**(c) Find Power:** (Using concept from next section)

$$P = VI = 5 \times 2.976 = 14.88 \text{ W}$$

**Unit Check:** $\frac{[\Omega \cdot \text{m}][\text{m}]}{[\text{m}^2]} = \Omega$ ✓

**Common Mistake:** Forgetting to convert mm² to m². $2 \text{ mm}^2 = 2 \times 10^{-6} \text{ m}^2$, NOT $2 \times 10^{-3} \text{ m}^2$.

> [!WARNING]
> **Area conversion is the #1 source of errors in resistance calculations:**
> - $1 \text{ mm}^2 = 10^{-6} \text{ m}^2$ (NOT $10^{-3}$)
> - $1 \text{ cm}^2 = 10^{-4} \text{ m}^2$ (NOT $10^{-2}$)
> 
> Remember: $1 \text{ mm} = 10^{-3} \text{ m}$, so $1 \text{ mm}^2 = (10^{-3})^2 = 10^{-6} \text{ m}^2$

### Numerical Problem — Level 3 (NEC Challenge)

**Problem 1.4**: A heating element made of nichrome wire has a resistance of 50 Ω at 20°C. The temperature coefficient of nichrome is $\alpha = 0.0004$ °C⁻¹. If the element operates at 520°C, find:
(a) The resistance at operating temperature
(b) The current drawn from a 220 V supply at operating temperature
(c) The percentage change in current compared to the current at 20°C

**Given:** $R_0 = 50$ Ω, $T_0 = 20$°C, $\alpha = 0.0004$ °C⁻¹, $T = 520$°C, $V = 220$ V

**(a) Resistance at 520°C:**

$$R_T = R_0[1 + \alpha(T - T_0)]$$

$$R_{520} = 50[1 + 0.0004(520 - 20)]$$

$$R_{520} = 50[1 + 0.0004 \times 500]$$

$$R_{520} = 50[1 + 0.2] = 50 \times 1.2$$

$$R_{520} = 60 \text{ Ω}$$

**(b) Current at operating temperature:**

$$I_{520} = \frac{V}{R_{520}} = \frac{220}{60} = 3.667 \text{ A}$$

**(c) Percentage change in current:**

Current at 20°C: $I_{20} = \frac{220}{50} = 4.4$ A

$$\text{Percentage change} = \frac{I_{20} - I_{520}}{I_{20}} \times 100\%$$

$$= \frac{4.4 - 3.667}{4.4} \times 100\% = \frac{0.733}{4.4} \times 100\% \approx 16.67\%$$

**Engineering Interpretation:** The resistance increased by 20% (from 50 Ω to 60 Ω) due to temperature rise, causing the current to decrease by about 16.7%. This is why incandescent bulbs draw a large surge current when first turned on (filament is cold = low resistance) and then the current settles down as the filament heats up.

## 🔧 Applications

1. **Resistors in electronics**: Current limiting, voltage division, biasing
2. **Heating elements**: Ohmic heating (electric stoves, heaters)
3. **Sensors**: Thermistors (NTC, PTC), strain gauges
4. **Fuses**: Designed to melt (break circuit) when current exceeds rated value

## Ohmic vs Non-Ohmic Devices

| Property | Ohmic Device | Non-Ohmic Device |
|----------|-------------|-----------------|
| V-I curve | Straight line through origin | Non-linear / Curved |
| Resistance | Constant | Varies with V or I |
| Obeys Ohm's Law? | Yes | Not strictly |
| Examples | Metal resistors, copper wire | Diodes, transistors, filament lamps |

```
   Ohmic (Resistor)              Non-Ohmic (Diode)
    V ↑                          V ↑
      │      ╱                     │       │
      │    ╱                       │       │
      │  ╱                         │      ╱
      │╱                           │   ╱╱
      └──────→ I                   │╱╱
                                   └──────→ I
```

> [!NOTE]
> **Non-ohmic devices do NOT violate Ohm's Law.** Ohm's Law ($V = IR$) still applies instantaneously — the key difference is that $R$ is not constant. At any given operating point, we can define a **dynamic resistance** $r = dV/dI$.

## ⚠️ NEC Exam Traps — Ohm's Law and Resistance

1. **Using $R = V/I$ for a diode**: This gives the static (DC) resistance, NOT the dynamic (AC) resistance. The dynamic resistance is $r_d = dV/dI$, which is different.

2. **Applying Ohm's Law across a voltage source**: A voltage source has (ideally) zero resistance. $R = V/I$ applied to the source gives you the load resistance, NOT the source resistance.

3. **Unit traps in resistance calculation**: 
   - $\text{mm}^2 \to \text{m}^2$: multiply by $10^{-6}$
   - $\text{cm} \to \text{m}$: multiply by $10^{-2}$
   - $\text{k}\Omega \to \Omega$: multiply by $10^3$

4. **Temperature effects**: NEC may give resistance at one temperature and ask for current at another. You must use the temperature formula.

5. **Sign convention**: Current ENTERS the positive terminal of a resistor. If you define the current the other way, you must use $V = -IR$.

## 💡 💡 Engineering Intuition — Ohm's Law

> **Ohm's Law is not just a formula — it is a way of thinking.**
> 
> When you see a resistor in a circuit, immediately think:
> - "What voltage is across it?"
> - "What current flows through it?"
> - "How much power does it dissipate?"
> 
> These three questions, answerable by $V = IR$, $I = V/R$, and $P = I^2R = V^2/R = VI$, are the core of circuit analysis. Every network theorem (Thevenin, Norton, Superposition) ultimately reduces a complex circuit to a simple Ohm's Law problem.

## Ohm's Law — Quick Revision Triangle

A useful memory aid:

```
        ┌─────┐
        │  V  │
        ├──┬──┤
        │ I│ R│
        └──┴──┘
        
  Cover what you want:
  - Cover V: V = I × R
  - Cover I: I = V / R  
  - Cover R: R = V / I
```

---

# 1.1.5 ELECTRIC POWER

## 📖 Introduction

Power is the rate at which energy is transferred or converted. In electrical circuits, power tells us how fast a circuit element is converting electrical energy into another form (heat, light, mechanical energy, etc.) or how fast a source is supplying energy to the circuit.

## ⚠️ Why Is It Important?

- Power determines the **rating** of every electrical device
- Power dissipation determines **heat generation** (thermal management)
- Power efficiency determines **energy costs** and **battery life**
- Power calculations are needed for: component selection, safety analysis, efficiency calculations, and billing

## ✏️ Definition

> **Electric power** is the rate at which electrical energy is transferred by a circuit element.

$$P = \frac{W}{t} = \frac{\text{Energy}}{\text{Time}}$$

## 📈 Mathematical Formulation

### Fundamental Formula

$$P = VI$$

### Derivation

Starting from the definitions of voltage and current:

$$V = \frac{W}{Q} \implies W = VQ$$

$$I = \frac{Q}{t} \implies Q = It$$

Substituting:

$$W = V \times It = VIt$$

$$P = \frac{W}{t} = \frac{VIt}{t} = VI$$

### Derived Forms (using Ohm's Law)

Since $V = IR$:

$$P = VI = (IR) \times I = I^2 R$$

Since $I = V/R$:

$$P = VI = V \times \frac{V}{R} = \frac{V^2}{R}$$

### Complete Power Formula Set

| Formula | Variables Known | Best Used When |
|---------|----------------|---------------|
| $P = VI$ | Voltage and Current | General case |
| $P = I^2R$ | Current and Resistance | Current is known/given |
| $P = \frac{V^2}{R}$ | Voltage and Resistance | Voltage is known/given |

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $P$ | Electric power | Watt (W) |
| $V$ | Voltage | Volt (V) |
| $I$ | Current | Ampere (A) |
| $R$ | Resistance | Ohm (Ω) |

### Dimensional Check

$$[P] = [V][I] = \frac{\text{J}}{\text{C}} \times \frac{\text{C}}{\text{s}} = \frac{\text{J}}{\text{s}} = \text{W}$$

### Common Prefixes

| Prefix | Value | Typical Use |
|--------|-------|-------------|
| mW (milliwatt) | $10^{-3}$ W | Electronic ICs, sensors |
| W (watt) | $10^0$ W | Light bulbs, small appliances |
| kW (kilowatt) | $10^3$ W | Heaters, motors, homes |
| MW (megawatt) | $10^6$ W | Power stations, industrial |
| GW (gigawatt) | $10^9$ W | National power grids |

## Physical Meaning

**Power consumed by a resistor:** Electrical energy is irreversibly converted to heat. This is called **Joule heating** or **ohmic loss**.

**Power delivered by a source:** The source (battery, generator) converts another form of energy (chemical, mechanical) into electrical energy and supplies it to the circuit.

### Sign Convention for Power

| Condition | Power | Meaning |
|-----------|-------|---------|
| Current enters (+) terminal | $P > 0$ | Element **absorbs** (consumes) power |
| Current enters (−) terminal | $P < 0$ | Element **delivers** (supplies) power |

```
  Absorbing power:           Delivering power:
       I →                        I →
    (+)────(−)                (−)────(+)
      P = +VI                  P = −VI
    (Resistor)                 (Battery)
```

## Worked Numerical Problem

**Problem 1.5** (Level 2): An electric heater is rated at 1500 W, 220 V. Find:
(a) The current drawn
(b) The resistance of the heating element
(c) The cost of running the heater for 8 hours if electricity costs NPR 10 per kWh

**Given:** $P = 1500$ W, $V = 220$ V, $t = 8$ hours, cost = NPR 10/kWh

**(a) Current:**

$$I = \frac{P}{V} = \frac{1500}{220} = 6.82 \text{ A}$$

**(b) Resistance:**

$$R = \frac{V^2}{P} = \frac{220^2}{1500} = \frac{48400}{1500} = 32.27 \text{ Ω}$$

**Verification:** $P = I^2 R = 6.82^2 \times 32.27 = 46.51 \times 32.27 \approx 1500$ W ✓

**(c) Cost:**

$$\text{Energy consumed} = P \times t = 1500 \times 8 = 12{,}000 \text{ Wh} = 12 \text{ kWh}$$

$$\text{Cost} = 12 \times 10 = \text{NPR } 120$$

**Engineering Interpretation:** The heater draws about 6.82 A from a 220 V supply. This is within the typical 16 A socket rating in Nepal. The heating element resistance is about 32 Ω. Running for 8 hours consumes 12 kWh of energy.

---

# 1.1.6 ELECTRIC ENERGY

## 📖 Introduction

While power tells us the *rate* of energy transfer, energy tells us the *total amount* of work done or energy consumed over a period of time. Energy is what you pay for in your electricity bill.

## ✏️ Definition

> **Electric energy** is the total amount of work done by or on electric charges over a period of time.

$$W = Pt$$

## 📈 Mathematical Formulation

### From power:

$$W = Pt = VIt = I^2Rt = \frac{V^2}{R} t$$

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $W$ (or $E$) | Electric energy | Joule (J) |
| $P$ | Power | Watt (W) |
| $t$ | Time | Second (s) |

### Commercial Unit

In power systems, the joule is too small for practical use. The commercial unit is:

$$1 \text{ kWh} = 1 \text{ kilowatt} \times 1 \text{ hour} = 1000 \times 3600 = 3.6 \times 10^6 \text{ J} = 3.6 \text{ MJ}$$

> [!IMPORTANT]
> **kWh is a unit of ENERGY, not power.** This is one of the most common confusions.
> - **kW** → Power (rate)
> - **kWh** → Energy (total amount)

## Comparison: Power vs Energy

| Property | Power | Energy |
|----------|-------|--------|
| **Definition** | Rate of energy transfer | Total energy transferred |
| **Formula** | $P = VI$ | $W = Pt = VIt$ |
| **SI Unit** | Watt (W) | Joule (J) |
| **Commercial Unit** | kW, MW | kWh |
| **Analogy** | Speed of water flow | Total water flowed |
| **Time dependency** | Instantaneous | Cumulative over time |
| **What it measures** | How fast energy is used | How much energy is used |
| **What you pay for** | No (indirectly through demand charges) | Yes (energy charges) |

## ⚠️ NEC Exam Traps — Power and Energy

1. **Confusing power and energy**: The question may ask for energy but give power, or vice versa. Read carefully.
2. **Unit mismatch**: If power is in kW and time is in hours, energy is directly in kWh. But if time is in seconds, convert: $E(\text{kWh}) = \frac{P(\text{W}) \times t(\text{s})}{3.6 \times 10^6}$.
3. **"Power consumed by a 100 W bulb for 5 hours"**: The power is always 100 W. The ENERGY consumed is 500 Wh = 0.5 kWh.

---

# SECTION 1.1 PART 1 — SUMMARY AND KEY EQUATIONS

## Key Concepts Covered

| # | Concept | Key Equation |
|---|---------|-------------|
| 1 | Electric Charge | $Q = ne$ |
| 2 | Voltage (Potential Difference) | $V = W/Q$ |
| 3 | Electric Current | $I = Q/t$ or $i = dq/dt$ |
| 4 | Resistance | $R = \rho L/A$ |
| 5 | Ohm's Law | $V = IR$ |
| 6 | Temperature Effect | $R_T = R_0[1 + \alpha(T - T_0)]$ |
| 7 | Electric Power | $P = VI = I^2R = V^2/R$ |
| 8 | Electric Energy | $W = Pt = VIt$ |

## ⚠️ Important Relationships Map

```
    Charge (Q) ─── defines ─── Current (I = Q/t)
        │                           │
        │                           │ Ohm's Law
    defines                    V = IR
        │                           │
    Voltage (V = W/Q)               │
        │                           │
        └───── Power (P = VI) ──────┘
                    │
              Energy (W = Pt)
```

## Comparison Table: Voltage vs Current

| Property | Voltage | Current |
|----------|---------|---------|
| **Definition** | Energy per unit charge | Charge per unit time |
| **Symbol** | $V$ | $I$ |
| **SI Unit** | Volt (V) | Ampere (A) |
| **Measured** | Between two points (across) | At a point (through) |
| **Instrument** | Voltmeter (connected in parallel) | Ammeter (connected in series) |
| **Analogy** | Water pressure (height) | Water flow rate |
| **Cause/Effect** | Cause | Effect |
| **In series circuit** | Divides across elements | Same through all elements |
| **In parallel circuit** | Same across all elements | Divides among branches |

## Comparison Table: Power vs Energy

| Property | Power | Energy |
|----------|-------|--------|
| **Definition** | Rate of energy transfer | Total energy transferred |
| **Formula** | $P = VI$ | $W = Pt$ |
| **SI Unit** | Watt (W) = J/s | Joule (J) |
| **Commercial Unit** | kW | kWh |
| **Relationship** | $P = dW/dt$ | $W = \int P \, dt$ |

---

## What's Next

**Section 1.1 — Part 2** will cover:
- Conducting and Insulating Materials
- Series Electric Circuits (with voltage divider)
- Parallel Electric Circuits (with current divider)
- Star (Y) and Delta (Δ) Connections
- Star-Delta and Delta-Star Conversion (with derivation)

These build directly on the V, I, R, P, and E concepts established in this part.
