# Section 1.6: Amplifiers

## 📖 1. Introduction
Amplifiers are fundamental electronic circuits designed to increase the power, voltage, or current of an input signal without significantly distorting its waveform. From boosting a faint microphone signal to driving large loudspeakers, amplifiers form the backbone of modern electronics and communication systems. For the NEC Engineering License Examination, understanding the various classes of output stages, power handling components, tuned circuits, and the ubiquitous Operational Amplifier (Op-Amp) is absolutely critical.

## ⚠️ 2. Why is it Important?
In real-world engineering, sensors, antennas, and transducers often output signals in the microvolt or millivolt range. These weak signals cannot drive loads like motors, speakers, or transmission lines. Amplifiers bridge this gap, taking small-signal inputs and providing large-signal power outputs. The NEC exam frequently tests the efficiency, biasing, and application of these stages to ensure engineers can design and troubleshoot practical analog systems.

---

## Part A: Amplifier Fundamentals

### 1. Signal Amplification Concept
Amplification is the process of increasing the magnitude of a variable quantity (voltage, current, or power). 

#### Definition
The **Gain** (A) of an amplifier is the ratio of the output signal to the input signal.

#### Mathematical Formulation

| Symbol | Meaning | Formula | SI Unit |
|---|---|---|---|
| $A_v$ | Voltage Gain | $V_{out} / V_{in}$ | Dimensionless (V/V) |
| $A_i$ | Current Gain | $I_{out} / I_{in}$ | Dimensionless (A/A) |
| $A_p$ | Power Gain | $P_{out} / P_{in} = A_v \times A_i$ | Dimensionless (W/W) |

**Decibel (dB) Scale:**
Because gains can range from 1 to $10^6$, the logarithmic decibel scale is standard in engineering.
- Voltage Gain in dB: $A_{v(dB)} = 20 \log_{10}(|V_{out}/V_{in}|)$
- Power Gain in dB: $A_{p(dB)} = 10 \log_{10}(P_{out}/P_{in})$

> [!TIP] 
> 💡 **Engineering Intuition:** A power gain of +3 dB means the power has doubled. A voltage gain of +20 dB means the voltage has increased by a factor of 10.

---

## Part B: Classification of Output Stages

### 2. Overview of Output Stages
Output stages are classified based on the **conduction angle** ($\theta$), which is the portion of the input sinusoidal cycle (in degrees) during which the amplifying transistor conducts current.

| Class | Conduction Angle | Conduction Time | Efficiency | Distortion |
|---|---|---|---|---|
| **A** | 360° ($2\pi$) | Full cycle | Low (25%-50%) | Very Low |
| **B** | 180° ($\pi$) | Half cycle | High (78.5%) | High (Crossover) |
| **AB** | 180° < $\theta$ < 360° | Slightly > half cycle | Medium (50-78.5%) | Low |
| **C** | < 180° | Less than half cycle | Very High (>90%) | Very High |

---

### 3. Class A Output Stage

#### Basic Concept & Circuit
In a Class A amplifier, the transistor is biased such that it remains in the active region for the entire 360° of the input cycle. The Q-point is set exactly in the middle of the AC load line.

```text
       +Vcc
        |
       [Rc] (or Transformer)
        |
        +---- V_out
        |
       |/ c
V_in --|  BJT (NPN)
       |> e
        |
       GND
```

#### Maximum Efficiency Derivation (Resistive Load)
1. **DC Power Supplied:** $P_{dc} = V_{CC} I_{CQ}$
2. For maximum symmetric swing, the Q-point is exactly at $V_{CEQ} = V_{CC}/2$ and $I_{CQ} = I_{C(max)}/2$.
3. **Maximum AC Output Power:** 
   $P_{ac(max)} = \frac{V_{p} I_{p}}{2} = \frac{(V_{CC}/2) \times I_{CQ}}{2} = \frac{V_{CC} I_{CQ}}{4}$
4. **Efficiency ($\eta$):** 
   $\eta = \frac{P_{ac(max)}}{P_{dc}} \times 100\% = \frac{V_{CC} I_{CQ}/4}{V_{CC} I_{CQ}} = 25\%$

If a transformer is used instead of a collector resistor, $P_{dc} = V_{CC} I_{CQ}$, but the AC voltage can swing from 0 to $2V_{CC}$, doubling the AC power.
**Transformer-coupled Class A efficiency = 50% max.**

#### Engineering Interpretation
Class A wastes a massive amount of power as heat (especially when there is no input signal), but because the transistor never turns off, it offers the highest linearity and lowest distortion.
- **Applications:** Audio preamplifiers, low-power RF stages.

---

### 4. Class B Output Stage

#### Basic Concept & Circuit
Class B uses a complementary pair of transistors (NPN and PNP) biased exactly at cutoff ($I_{CQ} = 0$). The NPN conducts for the positive half-cycle, and the PNP conducts for the negative half-cycle.

```text
         +Vcc
          |
         |/ c  (Q1 NPN)
V_in ----| 
         |> e
          |------+---- V_out
         |< e    |
V_in ----|       [R_L]
         |\ c    |
          |     GND
         -Vcc  (Q2 PNP)
```

#### Crossover Distortion
Because BJTs require roughly $0.7\text{V}$ ($V_{BE}$) to turn on, there is a "dead zone" between $-0.7\text{V}$ and $+0.7\text{V}$ of the input signal where neither transistor conducts. This causes a flattened spot at the zero-crossing of the output waveform.

```text
Output Waveform with Crossover Distortion:
   /\
  /  \
-/-----\------
        \  /
         \/
 (Notice the flat step at the axis crossing)
```

#### Maximum Efficiency Derivation
1. **AC Output Power:** $P_{ac} = \frac{V_p^2}{2R_L}$ (where maximum $V_p = V_{CC}$)
2. **DC Power Supplied:** Current is half-sine. Average current from one supply = $I_p/\pi$. Total DC power from both supplies = $2 \times V_{CC} \times (I_p/\pi) = \frac{2 V_{CC} V_p}{\pi R_L}$
3. **Efficiency:** $\eta = \frac{\pi}{4} \frac{V_p}{V_{CC}}$. Max efficiency when $V_p = V_{CC}$:
   $\eta_{max} = \frac{\pi}{4} \approx 78.5\%$

> [!WARNING] 
> ⚠️ **NEC Exam Trap:** Exam questions often ask for efficiency of Class B. Remember 78.5% is the *theoretical maximum*. Actual efficiency is lower depending on signal amplitude.

---

### 5. Class AB Output Stage

Class AB solves the crossover distortion of Class B by biasing the transistors *slightly* above cutoff. A small quiescent current flows even with no input signal. The conduction angle is slightly greater than 180°.

- **Efficiency:** Compromise between A and B, practically around 50%-78%.
- **Applications:** Audio power amplifiers (the most common power amplifier class).

#### 6. Biasing the Class AB Stage
To bias the transistors at the edge of conduction, we need a DC voltage drop of $2V_{BE}$ (approx 1.4V) between the bases of the NPN and PNP transistors. This is achieved using:
1. **Diode Biasing:** Two diodes in series.
2. **$V_{BE}$ Multiplier (Rubber Diode):** A transistor with resistors $R_1$ and $R_2$ that acts as an adjustable zener diode with voltage $V_{bias} = V_{BE}(1 + R_1/R_2)$.

**Thermal Runaway Prevention:** By mounting the biasing diodes or $V_{BE}$ multiplier on the same heat sink as the power transistors, their $V_{BE}$ drops decrease with temperature at the same rate, keeping the quiescent current stable.

---

### 7. Class A vs Class B vs Class AB Comparison Table

| Parameter | Class A | Class B | Class AB |
|---|---|---|---|
| **Conduction Angle** | 360° | 180° | 180° to 360° |
| **Q-Point** | Center of active region | Cutoff on load line | Just above cutoff |
| **Max Efficiency** | 25% (RC) / 50% (Transformer) | 78.5% | 50% - 78.5% |
| **Distortion** | Lowest | Highest (Crossover) | Low |
| **No-Signal Power Dissipation**| Maximum | Zero | Very Small |
| **Applications** | Preamps | Rarely used alone | Standard audio amplifiers |

---

## Part C: Power BJTs

### 8. Power BJTs
Power BJTs differ from small-signal BJTs in physical size and layout. They are designed to handle tens of amperes and hundreds of volts.

- **Thermal Resistance ($\theta_{JA}$):** The resistance to heat flow from the junction to ambient air. $T_J = T_A + P_D \theta_{JA}$. To keep the junction temperature ($T_J$) below destruction limits (usually $150^\circ\text{C}$), **Heat Sinks** are attached to reduce the thermal resistance to ambient.
- **Safe Operating Area (SOA):** A graph of $I_C$ vs $V_{CE}$ showing the boundaries within which the BJT can operate without damage from thermal limits, voltage breakdown, or second breakdown.
- **Second Breakdown:** A localized thermal runaway within the BJT die, causing hot spots and catastrophic failure, even if average power is within limits.
- **Darlington Pair:** Power BJTs have low $\beta$ (often 20-50). To increase current gain, two BJTs are cascaded. $\beta_{total} \approx \beta_1 \times \beta_2$.

---

## Part D: Transformer-Coupled Push-Pull Stages

### 9. Transformer-Coupled Push-Pull Amplifier

```text
         +Vcc
          |
         [CT] (Center Tap of Output Transformer)
          |
         |/ c 
V_in1 ---|  (Q1 conducts pos half)
         |> e --- GND
          |
         |/ c
V_in2 ---|  (Q2 conducts neg half)
         |> e --- GND
```
*(Input signal is split by a center-tapped input transformer into $V_{in1}$ and $V_{in2}$, which are 180° out of phase).*

- **Working Principle:** One transistor handles the positive half of the signal, the other handles the negative. The output transformer combines them into a full wave.
- **Advantages:** Excellent impedance matching (can drive 8$\Omega$ speakers easily), DC isolation.
- **Disadvantages:** Transformers are heavy, bulky, expensive, suffer from core saturation, and have poor frequency response (limits low and high frequencies).

---

## Part E: Tuned Amplifiers

### 10. Tuned Amplifiers
Tuned amplifiers use an LC (inductor-capacitor) resonant tank circuit as the load instead of a resistor. They amplify only a narrow band of frequencies centered around the resonant frequency.

```text
       +Vcc
        |
       +---+
       |   |
      [L] [C]  <-- LC Tank Circuit
       |   |
       +---+
        |
        +---- V_out
        |
       |/ c
V_in --| 
       |> e
        |
       GND
```

#### Physical Meaning
At resonance ($f_0 = \frac{1}{2\pi\sqrt{LC}}$), the impedance of the LC tank is maximum. Since $A_v = -g_m Z_L$, the voltage gain is massive exactly at $f_0$ and drops off sharply at other frequencies.

#### Mathematics
- **Resonant Frequency:** $f_0 = \frac{1}{2\pi\sqrt{LC}}$
- **Quality Factor (Q):** Ratio of energy stored to energy dissipated. Higher Q = sharper peak.
- **Bandwidth (BW):** $BW = f_0 / Q$

#### Applications
Radio receivers (selecting one station out of many), IF amplifiers, RF transmitters.

---

## Part F: Operational Amplifiers (Op-Amps)

### 11. Ideal vs Practical Op-Amp (12 & 13)

| Parameter | Ideal Op-Amp | Practical Op-Amp (e.g., 741) |
|---|---|---|
| **Voltage Gain ($A_{OL}$)** | Infinite ($\infty$) | $10^5$ to $10^6$ |
| **Input Impedance ($Z_{in}$)**| Infinite ($\infty$) | $\approx 2\text{ M}\Omega$ |
| **Output Impedance ($Z_{out}$)**| Zero ($0\Omega$) | $50 - 75\Omega$ |
| **Bandwidth** | Infinite | Finite (Gain-Bandwidth Product limited) |
| **CMRR** | Infinite | $> 90\text{ dB}$ |
| **Input Currents ($I+, I-$)** | Zero | Nanoamps (Bias current) |

### 14. Key Concepts for Solving Op-Amp Circuits
When an op-amp has **Negative Feedback** (connection from output to inverting (-) input), it behaves according to two golden rules:
1. **Virtual Short:** The op-amp drives the output to whatever voltage is necessary to make the voltage difference between the inputs zero. Therefore, $V_+ \approx V_-$.
2. **Zero Input Current:** $I_+ = I_- = 0$.

*(If $V_+$ is grounded, $V_-$ becomes a "Virtual Ground", meaning it is at 0V but can accept current through feedback components).*

---

### 15. Inverting Amplifier

```text
       R1         Rf
V_in --[ ]--+-----[ ]----+--- V_out
            |            |
            |   |\       |
            +---| - \    |
                |    >---+
           GND--| + /
                |/
```
**Derivation:**
1. Node at inverting input is virtual ground ($V_- = 0\text{V}$).
2. KCL at $V_-$: $I_{in} + I_f = 0 \implies \frac{V_{in} - 0}{R_1} + \frac{V_{out} - 0}{R_f} = 0$
3. Gain: $A_v = \frac{V_{out}}{V_{in}} = -\frac{R_f}{R_1}$
- **Input Impedance:** $Z_{in} = R_1$.

---

### 16. Non-Inverting Amplifier

```text
                Rf
      +----+----[ ]----+--- V_out
      |    |           |
     [R1]  |   |\      |
      |    +---| - \   |
     GND       |    >--+
V_in ----------| + /
               |/
```
**Derivation:**
1. Virtual short: $V_- = V_+ = V_{in}$.
2. KCL at $V_-$: $\frac{0 - V_{in}}{R_1} + \frac{V_{out} - V_{in}}{R_f} = 0$
3. Gain: $A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_f}{R_1}$

---

### 17. Voltage Follower (Unity Gain Buffer)
Connect output directly to inverting input ($R_f = 0, R_1 = \infty$).
- Gain = 1 ($V_{out} = V_{in}$).
- **Application:** Buffer to prevent loading effects (high input impedance, low output impedance).

---

### 18. Summing Amplifier (Inverting)
Uses multiple input resistors connected to the virtual ground node.
- **Formula:** $V_{out} = -R_f \left( \frac{V_1}{R_1} + \frac{V_2}{R_2} + \dots \right)$
- **Application:** Audio mixing consoles, Digital-to-Analog Converters (DAC).

---

### 19. Difference Amplifier
Amplify the difference between two inputs.
- **Formula:** If $R_1=R_2$ and $R_f=R_3$, then $V_{out} = \frac{R_f}{R_1}(V_2 - V_1)$
- **Application:** Instrumentation, bridge sensor outputs.

---

### 20. Integrator
Replace $R_f$ with a Capacitor $C$.
- **Formula:** $V_{out} = -\frac{1}{RC} \int V_{in} \, dt$
- **Application:** Converts square wave to triangle wave; analog computing.

### 21. Differentiator
Capacitor at input, Resistor at feedback.
- **Formula:** $V_{out} = -RC \frac{dV_{in}}{dt}$
- **Application:** Waveform edge detection. *Practical note:* Highly susceptible to high-frequency noise.

### 22. Comparator
No negative feedback (Open loop).
- If $V_+ > V_-$, $V_{out} = +V_{sat}$ (approx $+V_{cc}$)
- If $V_+ < V_-$, $V_{out} = -V_{sat}$ (approx $-V_{cc}$)
- **Application:** Analog-to-digital conversion, zero-crossing detectors.

---
---

## 🎯 End-of-Section Content

### Key Equations
| Concept | Equation |
|---|---|
| Class A Max Efficiency | $\eta = 25\%$ (RC) |
| Class B Max Efficiency | $\eta = \pi/4 \approx 78.5\%$ |
| Tuned Amp Bandwidth | $BW = f_0 / Q$ |
| Inverting Op-Amp Gain | $A_v = -R_f / R_1$ |
| Non-Inverting Op-Amp Gain | $A_v = 1 + (R_f / R_1)$ |

### 5 Conceptual Questions
1. Why is Class A amplification not used in high-power battery-operated devices?
2. Explain the physical origin of crossover distortion in a Class B amplifier.
3. How does a $V_{BE}$ multiplier help stabilize a Class AB amplifier against temperature changes?
4. Why is the input impedance of an inverting amplifier practically equal to $R_1$, whereas the non-inverting amplifier has nearly infinite input impedance?
5. Why are practical differentiator circuits rarely used without an input resistor in series with the capacitor?

### 5 Numerical Problems

**Level 1 (Foundation)**
1. Calculate the voltage gain in dB of an amplifier with $V_{in} = 10\text{ mV}$ and $V_{out} = 2\text{ V}$. 
2. A non-inverting op-amp circuit uses $R_f = 47\text{ k}\Omega$ and $R_1 = 1\text{ k}\Omega$. Find its voltage gain.

**Level 2 (Engineering)**
3. A Class A transformer-coupled amplifier drives an $8\Omega$ speaker. If $V_{CC} = 12\text{V}$ and the quiescent current is $1\text{A}$, calculate the DC power consumed, and the maximum possible AC power delivered to the speaker.
4. Design an inverting summing amplifier to output $V_{out} = -(2V_1 + 5V_2)$. Select a feedback resistor $R_f = 10\text{ k}\Omega$ and calculate $R_1$ and $R_2$.

**Level 3 (NEC Challenge)**
5. **Given:** A tuned amplifier with an LC tank where $L = 1\text{mH}$ and $C = 1\text{nF}$. The tank has a quality factor $Q = 50$. 
**Required:** Resonant frequency and Bandwidth.
**Calculation:** $f_0 = 1 / (2\pi\sqrt{10^{-3} \times 10^{-9}}) \approx 159.15\text{ kHz}$. $BW = f_0/Q = 159.15/50 = 3.18\text{ kHz}$. 
**Interpretation:** This amp will only amplify signals strongly between roughly $157.5\text{ kHz}$ and $160.7\text{ kHz}$.

### 10 NEC-Style MCQs

1. The maximum theoretical efficiency of a Class B push-pull amplifier is:
   A) 25%
   B) 50%
   C) 78.5%
   D) 100%

2. Crossover distortion is a major disadvantage of which amplifier class?
   A) Class A
   B) Class B
   C) Class AB
   D) Class C

3. In a Class AB amplifier, the conduction angle is:
   A) Exactly 180°
   B) Exactly 360°
   C) Less than 180°
   D) Between 180° and 360°

4. The purpose of a heat sink in power transistors is to decrease the:
   A) Thermal resistance from junction to ambient
   B) Safe Operating Area
   C) Base current
   D) Current gain

5. In a tuned amplifier, the bandwidth is given by the ratio of:
   A) Resonant frequency to inductance
   B) Inductance to Quality Factor (Q)
   C) Resonant frequency to Quality Factor (Q)
   D) Quality factor to Resonant frequency

6. An ideal operational amplifier has an open-loop voltage gain of:
   A) Zero
   B) 1
   C) 100,000
   D) Infinite

7. The virtual ground concept in an op-amp relies on:
   A) Infinite input bias current
   B) Positive feedback
   C) Infinite open-loop gain and negative feedback
   D) Zero output impedance

8. For an inverting amplifier with $R_1 = 2\text{k}\Omega$ and $R_f = 10\text{k}\Omega$, the voltage gain is:
   A) 5
   B) -5
   C) 6
   D) -0.2

9. A voltage follower is constructed using an op-amp. Its primary application is:
   A) Voltage amplification
   B) High-frequency oscillation
   C) Impedance matching (buffer)
   D) Integration of signals

10. If an op-amp circuit replaces the feedback resistor with a capacitor, it becomes a/an:
    A) Integrator
    B) Differentiator
    C) Oscillator
    D) Summing amplifier

### Answers to MCQs
1. C, 2. B, 3. D, 4. A, 5. C, 6. D, 7. C, 8. B, 9. C, 10. A
