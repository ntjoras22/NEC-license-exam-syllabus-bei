# Section 1.3: Alternating Current Fundamentals (AExE0103)

## 1. Principle of AC Generation

### Introduction
An Alternating Current (AC) is a current whose magnitude changes with time and whose direction reverses periodically. Unlike Direct Current (DC), which flows constantly in one direction, AC is dynamic and forms the backbone of modern electrical power grids.

### Why is it important?
AC is preferred over DC for power generation and transmission because AC voltage can be easily stepped up or stepped down using transformers. This allows power to be transmitted at very high voltages (reducing $I^2R$ line losses) and distributed at safer, lower voltages.

### Basic Concept
AC is generated using an alternator (AC generator). The fundamental principle relies on Faraday's Law of Electromagnetic Induction: when a conductor rotates within a uniform magnetic field (or when a magnetic field rotates around a stationary conductor), an electromotive force (EMF) is induced in the conductor.

### Physical Meaning
Imagine a rectangular wire coil rotating at a constant angular velocity inside a constant magnetic field. As it turns, the area of the coil perpendicular to the magnetic field changes, altering the magnetic flux passing through it. This changing flux induces a voltage.

### The Rotating Coil Diagram
```text
      N (North Pole)
      |         |
      |   ---   | 
      |  |   |  | <-- Rotating Rectangular Coil
      |   ---   |
      |         |
      S (South Pole)
      
          | |
          = =  <-- Slip Rings
          | |
       --Load--
```
*Figure: Basic AC Generator with a rotating coil, magnetic field, and slip rings.*

### Mathematical Formulation and Derivation
Let a coil of $N$ turns and area $A$ rotate at a constant angular velocity $\omega$ in a uniform magnetic field of flux density $B$.
The magnetic flux $\Phi$ linked with the coil at any time $t$ is:
$$\Phi = B \cdot A \cdot \cos(\theta) = B \cdot A \cdot \cos(\omega t)$$

According to Faraday’s Law, the induced EMF ($e$) is the negative rate of change of flux linkage:
$$e = -N \frac{d\Phi}{dt}$$
$$e = -N \frac{d}{dt} (B A \cos(\omega t))$$
$$e = -N B A (-\omega \sin(\omega t))$$
$$e = N B A \omega \sin(\omega t)$$

Let the maximum possible EMF (when $\sin(\omega t) = 1$) be $V_m = N B A \omega$. Then:
$$v(t) = V_m \sin(\omega t)$$

This shows why the output voltage is perfectly **sinusoidal**. One complete mechanical rotation ($360^\circ$ or $2\pi$ radians) of a 2-pole machine corresponds to one complete electrical cycle of the AC waveform.

---

## 2. Equations of AC Voltage and Current

The general equations for sinusoidal AC quantities are:
**Voltage:**

$$v(t) = V_m \sin(\omega t + \phi)$$
**Current:**

$$i(t) = I_m \sin(\omega t + \phi)$$

### Variable Table
| Symbol | Meaning | SI Unit |
|---|---|---|
| $v(t)$, $i(t)$ | Instantaneous voltage/current at time $t$ | Volts (V), Amperes (A) |
| $V_m$, $I_m$ | Peak (maximum) voltage/current | Volts (V), Amperes (A) |
| $\omega$ | Angular frequency ($\omega = 2\pi f$) | Radians per second (rad/s) |
| $f$ | Frequency (number of cycles per second) | Hertz (Hz) |
| $T$ | Time period of one cycle ($T = 1/f$) | Seconds (s) |
| $\phi$ | Phase angle (initial angle at $t=0$) | Radians (rad) or Degrees ($^\circ$) |

---

## 3. AC Waveforms

### Sinusoidal Waveform Diagram
```text
  V/I ^
      |     Peak (V_m)
  V_m |    .  .  .  
      |  .         .
      |.             .             T (One Cycle)
 -----+---------------+---------------+-----> t (or ωt)
      | 0            π/ω            2π/ω
      |                 .         .
 -V_m |                   .  .  .
      |                  Negative Peak (-V_m)
```
- **Zero Crossings:** Occur at $0, \pi, 2\pi, \dots$ radians. The instantaneous value is zero.
- **Positive Peak:** Occurs at $\pi/2$ radians.
- **Negative Peak:** Occurs at $3\pi/2$ radians.
- **Standard Frequencies:** In Nepal, the standard grid frequency is **50 Hz**. 
  - Time period $T = 1/f = 1/50 = 0.02$ seconds ($20$ ms).

---

## 4. Peak Value (Maximum Value)

**Definition:** The maximum amplitude reached by an alternating quantity during one cycle is called its peak value ($V_m$ or $I_m$).
- **Peak-to-Peak Value ($V_{pp}$):** The total voltage swing from the positive peak to the negative peak. 

$$V_{pp} = 2V_m$$

---

## 5. Average Value

**Definition:** The arithmetic average of all instantaneous values over one half-cycle. (For a full pure sine wave, the average value is exactly zero, so we always define it over a half-cycle).

**Derivation:**
$$V_{avg} = \frac{1}{\pi - 0} \int_{0}^{\pi} v(\theta) d\theta$$
$$V_{avg} = \frac{1}{\pi} \int_{0}^{\pi} V_m \sin(\theta) d\theta$$
$$V_{avg} = \frac{V_m}{\pi} [-\cos(\theta)]_0^\pi$$
$$V_{avg} = \frac{V_m}{\pi} (-\cos(\pi) + \cos(0))$$
$$V_{avg} = \frac{V_m}{\pi} (1 + 1) = \frac{2V_m}{\pi} \approx 0.637 V_m$$

---

## 6. RMS Value (Root Mean Square)

**Definition:** The RMS value of an AC current is the equivalent DC current that would produce the same amount of heat in a given resistor over a given time. It is the most important measurement in AC engineering.

**Derivation:**
$$V_{rms} = \sqrt{\frac{1}{2\pi} \int_{0}^{2\pi} [v(\theta)]^2 d\theta}$$
$$V_{rms} = \sqrt{\frac{1}{2\pi} \int_{0}^{2\pi} (V_m \sin \theta)^2 d\theta}$$
Using the identity $\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$:
$$V_{rms} = \sqrt{\frac{V_m^2}{2\pi} \int_{0}^{2\pi} \frac{1 - \cos(2\theta)}{2} d\theta}$$
$$V_{rms} = \sqrt{\frac{V_m^2}{4\pi} \left[ \theta - \frac{\sin(2\theta)}{2} \right]_0^{2\pi}}$$
$$V_{rms} = \sqrt{\frac{V_m^2}{4\pi} (2\pi - 0)} = \sqrt{\frac{V_m^2}{2}} = \frac{V_m}{\sqrt{2}}$$
$$V_{rms} \approx 0.707 V_m$$

💡 **Engineering Intuition:** When you say the household supply in Nepal is "220V", that is the **RMS value**. 
The peak voltage you are exposed to is $V_m = 220 \times \sqrt{2} \approx 311.1$ V!

---

## 7. Form Factor and Crest Factor

These factors describe the shape of the AC wave.

- **Form Factor ($K_f$):** Ratio of RMS value to Average value.

$$K_f = \frac{V_{rms}}{V_{avg}} = \frac{V_m/\sqrt{2}}{2V_m/\pi} = \frac{\pi}{2\sqrt{2}} \approx 1.11$$
- **Crest Factor ($K_c$ or Peak Factor):** Ratio of Peak value to RMS value.

$$K_c = \frac{V_m}{V_{rms}} = \frac{V_m}{V_m/\sqrt{2}} = \sqrt{2} \approx 1.414$$

---

## ⭐ 8. Relationships Summary Table

| Quantity | Formula | Value for Sine Wave |
|---|---|---|
| Peak Value | $V_m$ | $V_m$ |
| Average Value | $\frac{1}{\pi} \int_{0}^{\pi} v d\theta$ | $0.637 V_m$ |
| RMS Value | $\sqrt{\frac{1}{2\pi} \int_0^{2\pi} v^2 d\theta}$ | $0.707 V_m$ |
| Form Factor | RMS / Average | $1.11$ |
| Crest Factor | Peak / RMS | $1.414$ |

---

## 9. Phase and Phase Difference

- **Phase Angle ($\phi$):** Represents the initial state of the waveform at $t=0$.
- **Phase Difference:** The angular displacement between two AC quantities of the same frequency. 
  - If $v = V_m \sin(\omega t)$ and $i = I_m \sin(\omega t - \phi)$, the current **lags** the voltage by $\phi$.
  - If $v = V_m \sin(\omega t)$ and $i = I_m \sin(\omega t + \phi)$, the current **leads** the voltage by $\phi$.
  - **In-phase:** $\phi = 0^\circ$
  - **Quadrature:** $\phi = 90^\circ$
  - **Anti-phase:** $\phi = 180^\circ$

---

## 10. Three-Phase System

### Need for Three-Phase
Single-phase power drops to zero twice per cycle, causing pulsating power. Three-phase power delivers a constant, non-pulsating total power to balanced loads, which reduces vibrations in motors and improves efficiency. It also requires less conductor material to transmit the same power compared to single-phase.

### Generation
A three-phase alternator has three sets of coils arranged $120^\circ$ apart mechanically. This produces three sinusoidal voltages of equal magnitude and frequency, but phase-shifted by $120^\circ$ (electrical).

**Phase Sequence:** Typically Red, Yellow, Blue (R-Y-B).
$$v_R = V_m \sin(\omega t)$$
$$v_Y = V_m \sin(\omega t - 120^\circ)$$
$$v_B = V_m \sin(\omega t - 240^\circ) = V_m \sin(\omega t + 120^\circ)$$

```text
 Three-phase Waveforms:
     ^
  V  |   R      Y      B
     |  / \    / \    / \
     | /   \  /   \  /   \
 ----+/-----\/-----\/-----\----> t
     |       \      \      \
     |        \ /    \ /    \ /
```

### Star (Y) Connection
```text
       R
       |
      (Z)
       |
 N ----*----(Z)---- Y
       |
      (Z)
       |
       B
```
- **Neutral wire** is available from the common star point ($N$).
- **Line Current ($I_L$) vs Phase Current ($I_{ph}$):** They are the same series path.

$$I_L = I_{ph}$$
- **Line Voltage ($V_L$) vs Phase Voltage ($V_{ph}$):**

$$V_{RY} = \vec{V}_{RN} - \vec{V}_{YN}$$
  Using phasor subtraction of two vectors separated by $120^\circ$:

$$V_L = \sqrt{V_{ph}^2 + V_{ph}^2 - 2V_{ph}V_{ph}\cos(120^\circ)} = \sqrt{3} V_{ph}$$

$$V_L = \sqrt{3} V_{ph}$$

### Delta (Δ) Connection
```text
       R
       *----(Z)----* Y
        \         /
         (Z)   (Z)
          \   /
            *
            B
```
- No neutral wire exists.
- **Line Voltage vs Phase Voltage:** The line terminals are directly connected across the phase coils.

$$V_L = V_{ph}$$
- **Line Current vs Phase Current:** 

$$\vec{I}_R = \vec{I}_{RY} - \vec{I}_{BR}$$
  By phasor subtraction:

$$I_L = \sqrt{3} I_{ph}$$

### Three-Phase Power
For a balanced system, total power is the sum of power in 3 phases.
$$P_{total} = 3 \times P_{phase} = 3 \times V_{ph} \times I_{ph} \times \cos(\phi)$$

Expressing in terms of Line quantities:
- **In Star:** $V_{ph} = V_L/\sqrt{3}$, $I_{ph} = I_L$.

$$P = 3 \times \left(\frac{V_L}{\sqrt{3}}\right) \times I_L \times \cos(\phi) = \sqrt{3} V_L I_L \cos(\phi)$$
- **In Delta:** $V_{ph} = V_L$, $I_{ph} = I_L/\sqrt{3}$.

$$P = 3 \times V_L \times \left(\frac{I_L}{\sqrt{3}}\right) \times \cos(\phi) = \sqrt{3} V_L I_L \cos(\phi)$$

- **Active Power:** $P = \sqrt{3} V_L I_L \cos(\phi)$ (Watts, W)
- **Reactive Power:** $Q = \sqrt{3} V_L I_L \sin(\phi)$ (Volt-Amperes Reactive, VAR)
- **Apparent Power:** $S = \sqrt{3} V_L I_L$ (Volt-Amperes, VA)

### Star vs Delta Comparison Table
| Feature | Star (Y) Connection | Delta ($\Delta$) Connection |
|---|---|---|
| Neutral terminal | Present | Absent |
| Line vs Phase Voltage | $V_L = \sqrt{3} V_{ph}$ | $V_L = V_{ph}$ |
| Line vs Phase Current | $I_L = I_{ph}$ | $I_L = \sqrt{3} I_{ph}$ |
| Application | Distribution, loads requiring neutral | Transmission, large motors |

---

## ⭐ 11. Section Summary

### Worked Numerical Problem - LEVEL 2
**Problem:** A $400$ V (line-to-line), $50$ Hz, three-phase supply is connected to a balanced star-connected load. The phase current is $10$ A, lagging the phase voltage by $30^\circ$. Calculate the phase voltage, total active power, and total apparent power.

**Given:** 
- Line Voltage $V_L = 400$ V
- Frequency $f = 50$ Hz
- Phase Current $I_{ph} = 10$ A
- Phase Angle $\phi = 30^\circ$ (lagging)
- Connection = Star (Y)

**Required:** $V_{ph}$, $P_{total}$, $S_{total}$

**Principle & Formulas:** 
For Star: $V_{ph} = V_L / \sqrt{3}$, $I_L = I_{ph}$
$P = \sqrt{3} V_L I_L \cos(\phi)$
$S = \sqrt{3} V_L I_L$

**Substitution & Calculation:**
1. $V_{ph} = 400 / \sqrt{3} = 230.94$ V
2. $I_L = I_{ph} = 10$ A
3. $P = \sqrt{3} \times 400 \times 10 \times \cos(30^\circ) = \sqrt{3} \times 4000 \times (\sqrt{3}/2) = 6000$ W = $6$ kW
4. $S = \sqrt{3} \times 400 \times 10 = 6928.2$ VA = $6.93$ kVA

**Final Answer:**
- Phase Voltage = $230.9$ V
- Active Power = $6.0$ kW
- Apparent Power = $6.93$ kVA

**Engineering Interpretation:** A typical low-voltage distribution in Nepal provides 400V between lines, which naturally gives $400/\sqrt{3} \approx 230V$ for single-phase household loads across line and neutral.
**Common Mistake:** Using phase voltage instead of line voltage in the $\sqrt{3} V I$ power formula, or using line voltage in the $3 V I$ formula. Remember: $P = \sqrt{3} V_L I_L \cos\phi = 3 V_{ph} I_{ph} \cos\phi$.

### 5 Conceptual Questions
1. Why does a pure sine wave have an average value of zero over a full cycle?
2. Explain the physical significance of the RMS value. Why is it more useful than the peak value?
3. In a rotating coil AC generator, what determines the frequency of the generated voltage?
4. Why is a three-phase system preferred over a single-phase system for power transmission?
5. Under what conditions is the neutral current zero in a 3-phase, 4-wire star-connected system?

### 5 Numerical Problems
**Level 1**
1. An AC voltage is given by $v(t) = 311 \sin(314 t)$. Find the peak voltage, RMS voltage, and frequency.
2. Calculate the form factor and crest factor of a perfectly square wave (where $V_m = V_{rms} = V_{avg}$).

**Level 2**
3. Three identical impedances of $10\angle 30^\circ \, \Omega$ are connected in Delta across a $400V$, 3-phase supply. Find the phase current, line current, and total active power.
4. An AC current has an RMS value of $15$ A and a frequency of $60$ Hz. Write its time-domain equation $i(t)$, assuming zero phase angle.

**Level 3**
5. A factory has a balanced 3-phase load drawing $50$ kW at $0.8$ power factor lagging from a $415$ V supply. If the load is star-connected, determine the phase voltage, line current, and impedance per phase.

---

### 10 NEC-Style MCQs

1. The form factor of a standard sinusoidal AC wave is:
   A) 0.707
   B) 1.11
   C) 1.414
   D) 0.637

2. In Nepal, the standard domestic AC supply frequency is:
   A) 60 Hz
   B) 50 Hz
   C) 100 Hz
   D) 120 Hz

3. The RMS value of an AC wave is equivalent to a DC value that produces the same:
   A) Voltage drop
   B) Magnetic field
   C) Heating effect
   D) Charge transfer

4. In a pure sinusoidal wave, the relationship between peak value ($V_m$) and RMS value ($V_{rms}$) is:
   A) $V_{rms} = V_m / 2$
   B) $V_{rms} = V_m / \sqrt{2}$
   C) $V_{rms} = \sqrt{2} V_m$
   D) $V_{rms} = V_m / \pi$

5. Which connection requires a neutral wire for supplying unbalanced single-phase loads?
   A) Delta connection
   B) Star connection
   C) Series connection
   D) Parallel connection

6. In a balanced 3-phase Delta ($\Delta$) connection:
   A) $V_L = \sqrt{3} V_{ph}$ and $I_L = I_{ph}$
   B) $V_L = V_{ph}$ and $I_L = \sqrt{3} I_{ph}$
   C) $V_L = \sqrt{3} V_{ph}$ and $I_L = \sqrt{3} I_{ph}$
   D) $V_L = V_{ph}$ and $I_L = I_{ph}$

7. The total active power in a balanced 3-phase system is given by:
   A) $\sqrt{3} V_L I_L \cos\phi$
   B) $3 V_L I_L \cos\phi$
   C) $\sqrt{3} V_{ph} I_{ph} \cos\phi$
   D) $V_L I_L \cos\phi$

8. If two alternating quantities $A$ and $B$ are represented by $A = A_m \sin(\omega t)$ and $B = B_m \sin(\omega t + 90^\circ)$, then:
   A) $A$ leads $B$ by $90^\circ$
   B) $B$ leads $A$ by $90^\circ$
   C) $A$ and $B$ are in phase
   D) $A$ lags $B$ by $180^\circ$

9. A single-phase AC voltage is $v(t) = 141.4 \sin(314 t)$. Its approximate RMS value is:
   A) 100 V
   B) 141.4 V
   C) 200 V
   D) 314 V

10. Why are three-phase systems generally preferred over single-phase for transmission?
    A) They require exactly three wires, saving cost
    B) They produce constant power instead of pulsating power
    C) They generate less heat in the generator
    D) They do not require transformers

### MCQ Answers
1. B
2. B
3. C
4. B
5. B
6. B
7. A
8. B
9. A
10. B
