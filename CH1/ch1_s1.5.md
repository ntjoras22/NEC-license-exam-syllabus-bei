# Chapter 1, Section 1.5: Signal Generator (AExE0105)

**Syllabus:** Basic Principles of Oscillator, RC, LC and Crystal Oscillators Circuits. Waveform generators.

---

## 1. Introduction: The Engineering Problem

In electronics, we often need to create continuous, periodic waveforms (sine waves, square waves, pulses) without any external AC signal source. How can a circuit continuously generate an AC waveform from a pure DC supply? 

This is the fundamental problem solved by **oscillators** and **waveform generators**. 
An oscillator is a circuit that acts as an energy converter, transforming DC power from the power supply into AC power at a specific frequency and waveform. 

**Why is this important?**
*   **Clock Signals:** Every digital system, microcontroller, and computer requires a precise clock signal to synchronize operations.
*   **Carrier Waves:** Radio, television, and mobile communications rely on high-frequency sinusoidal carriers for modulation and transmission.
*   **Test Signals:** Signal generators are essential laboratory tools for testing and characterizing electronic circuits.

---

## 2. Basic Principles of Oscillation

### 2.1 Amplifier with Feedback

An oscillator is fundamentally an amplifier that provides its own input signal. This is achieved through **positive feedback**.

*   **Negative Feedback:** The feedback signal is out of phase (180°) with the input. It opposes the input, leading to stable, predictable amplification but reduced gain.
*   **Positive Feedback:** The feedback signal is in phase (0° or 360°) with the original input. It reinforces the input, which can lead to instability and, if controlled, sustained oscillation.

**Block Diagram of a Feedback Amplifier:**
```text
           +-------------------------+
           |                         |
      +--->|    Amplifier (Gain A)   |---+-----> Output (V_out)
      |    |                         |   |
      |    +-------------------------+   |
      |                                  |
 V_f  |    +-------------------------+   |
      +----|  Feedback Network (β)   |<--+
           |                         |
           +-------------------------+
```

### 2.2 Barkhausen Criterion

The Barkhausen Criterion defines the mathematical conditions required for a circuit to produce sustained oscillations.

**Statement:** For a feedback amplifier to oscillate continuously at a specific frequency, two conditions must be met simultaneously:
1.  **Loop Gain Magnitude:** $|A\beta| = 1$
2.  **Loop Phase Shift:** $\angle A\beta = 0^\circ$ (or $360^\circ$ or $2n\pi$)

**Physical Meaning:** 
Imagine a small noise voltage appearing at the amplifier input. It gets amplified by $A$, then attenuated and phase-shifted by the feedback network $\beta$. For the signal to perfectly recreate itself at the input—neither growing nor shrinking—it must return with the exact same amplitude ($|A\beta|=1$) and perfectly in phase with itself so it adds constructively ($\angle A\beta=0^\circ$).

**Mathematical Derivation:**
The closed-loop gain $A_f$ of a feedback amplifier with input $V_{in}$ is:
$$A_f = \frac{V_{out}}{V_{in}} = \frac{A}{1 - A\beta}$$
For an oscillator, there is no external input ($V_{in} = 0$), yet there is an output ($V_{out} \neq 0$). 
This implies that the closed-loop gain must be infinite ($A_f \to \infty$).
For $A_f$ to approach infinity, the denominator must be zero:
$$1 - A\beta = 0 \implies A\beta = 1$$
Since $A\beta$ is a complex quantity, this single equation yields the two Barkhausen conditions for magnitude and phase.

**Operating States based on Loop Gain:**
*   **$|A\beta| > 1$:** Growing oscillations. Energy is added to the loop faster than it is dissipated. Necessary for the oscillator to start up from thermal noise.
*   **$|A\beta| = 1$:** Sustained oscillations (Steady State). Energy added exactly balances energy lost.
*   **$|A\beta| < 1$:** Decaying oscillations. Energy dissipates, and the oscillation dies out.

### 2.3 Startup and Amplitude Stabilization

For an oscillator to start, it is designed such that initially $|A\beta| > 1$. Microscopic thermal noise in the circuit provides the initial "kick". Since $|A\beta| > 1$, the amplitude of the chosen frequency grows exponentially.
As the amplitude grows, the amplifier's non-linearities (or an active Automatic Gain Control circuit) cause the gain $A$ to decrease. The amplitude stabilizes exactly at the point where $|A\beta| = 1$.

---

## 3. RC Oscillators

RC (Resistor-Capacitor) oscillators use RC networks to provide the necessary phase shift. They are typically used for low-frequency oscillations (Audio Frequency, up to around 1 MHz) because LC circuits become impractically large at low frequencies.

### 3.1 Wien Bridge Oscillator

The Wien bridge oscillator is the standard for generating high-quality, low-distortion sine waves at audio frequencies.

**Circuit Diagram (Using Op-Amp):**
```text
                  +Vcc
                   |
                   |
             +-----------+
             |           |
             |   Op-Amp  |
             |           |
      +------|-\         |
      |      |  >--------+-----------> V_out
      |  +---|+/         |
      |  |   |           |
      |  |   +-----------+
      |  |         |
      R2 |        -Vcc
      |  |
      +--|-----------------+
      |  |                 |
      R1 |                 R
      |  |                 |
     GND |                 C
         |                 |
         |                 +---- (Feedback point to non-inverting input)
         |                 |
         +---- C ---- R ---+
```
*(Note: R1 and R2 form the negative feedback to set the gain. The series-parallel RC network forms the positive feedback.)*

**Working Principle:**
The positive feedback network consists of a series RC circuit and a parallel RC circuit. At a specific frequency $f_0$, this network provides a phase shift of exactly $0^\circ$, and its attenuation factor $\beta$ is $1/3$. 

**Frequency of Oscillation Derivation:**
Let $Z_1 = R - j\frac{1}{\omega C}$ (series arm)
Let $Z_2 = \frac{R(-j/\omega C)}{R - j/\omega C} = \frac{R}{1 + j\omega RC}$ (parallel arm)
The feedback factor $\beta = \frac{V_f}{V_{out}} = \frac{Z_2}{Z_1 + Z_2}$
Substituting and equating the imaginary part to zero (for $0^\circ$ phase shift) yields:
$$f_0 = \frac{1}{2\pi RC}$$

**Condition for Oscillation:**
At $f_0$, the feedback factor $\beta = 1/3$.
To satisfy $|A\beta| \ge 1$, the amplifier gain $A$ must be:
$$A \ge 3$$
Since $A = 1 + \frac{R_2}{R_1}$ for a non-inverting op-amp, this requires $1 + \frac{R_2}{R_1} \ge 3 \implies \frac{R_2}{R_1} \ge 2$.

**Characteristics:**
*   **Advantages:** Excellent frequency stability, very low distortion, wide frequency range easily tuned by varying C.
*   **Disadvantages:** Requires two identical variable capacitors or resistors for tuning; limited to audio frequencies.

#### Worked Numerical Problem (Level 2)
**Given:** A Wien bridge oscillator uses $R = 10 \text{ k}\Omega$ and $C = 0.01 \text{ }\mu\text{F}$. The feedback resistors are $R_1 = 10 \text{ k}\Omega$ and $R_2$.
**Required:** 1) Frequency of oscillation $f_0$. 2) Minimum value of $R_2$ for sustained oscillations.
**Formula:** $f_0 = \frac{1}{2\pi RC}$, $R_2 \ge 2R_1$
**Calculation:**
1) $f_0 = \frac{1}{2\pi \times 10^4 \times 10^{-8}} = \frac{1}{2\pi \times 10^{-4}} \approx 1591.5 \text{ Hz}$
2) For sustained oscillation, $R_2 \ge 2 \times 10 \text{ k}\Omega = 20 \text{ k}\Omega$.
**Answer:** $f_0 = 1.59 \text{ kHz}$, $R_2 \ge 20 \text{ k}\Omega$.

### 3.2 Phase-Shift Oscillator

The phase-shift oscillator uses a cascade of RC high-pass filters to achieve the necessary phase shift.

**Circuit Diagram (Using Op-Amp):**
```text
                     +Vcc
                      |
                 +-----------+
                 |           |
                 |   Op-Amp  |
          +------|-\         |
          |      |  >--------+--------> V_out
          |  +---|+/         |
          |  |   |           |
          Rf |   +-----------+
          |  |         |
          | GND       -Vcc
          |
          +---- C ----+---- C ----+---- C ----+
                      |           |           |
                      R           R           R
                      |           |           |
                     GND         GND         GND
```

**Working Principle:**
The inverting amplifier provides a $180^\circ$ phase shift. To satisfy the Barkhausen criterion for $0^\circ$ (or $360^\circ$) total phase shift, the feedback network must provide an additional $180^\circ$ phase shift.
The feedback network uses three RC sections. Each section provides a phase shift of $60^\circ$ at the resonant frequency ($3 \times 60^\circ = 180^\circ$).

**Frequency of Oscillation:**
By analyzing the 3-mesh RC network, the frequency where the phase shift is exactly $180^\circ$ is:
$$f_0 = \frac{1}{2\pi RC\sqrt{6}}$$

**Condition for Oscillation:**
At this frequency $f_0$, the signal is heavily attenuated by the RC network. The attenuation factor is $\beta = 1/29$.
Therefore, to satisfy $|A\beta| \ge 1$, the inverting amplifier must have a gain magnitude $|A| \ge 29$.
For an op-amp, $|A| = R_f / R$, so $R_f \ge 29R$.

**Characteristics:**
*   **Advantages:** Simple circuit, cheap, good for fixed-frequency audio signals.
*   **Disadvantages:** Difficult to tune (changing one R or C changes the attenuation and frequency unpredictably), requires high gain.

### 3.3 RC Oscillators Comparison

| Feature | Wien Bridge Oscillator | Phase-Shift Oscillator |
| :--- | :--- | :--- |
| **Phase Shift mechanism** | Network: $0^\circ$, Amp: $0^\circ$ | Network: $180^\circ$, Amp: $180^\circ$ |
| **Frequency ($f_0$)** | $\frac{1}{2\pi RC}$ | $\frac{1}{2\pi RC\sqrt{6}}$ |
| **Minimum Gain ($|A|$)** | $3$ | $29$ |
| **Tuning** | Easy (change C) | Difficult |

---

## 4. LC Oscillators

LC oscillators use a tuned circuit (an inductor and capacitor in parallel, known as a "tank circuit") to set the frequency. They are used for high frequencies (Radio Frequencies, 100 kHz to hundreds of MHz).

### 4.1 General LC Oscillator Principle
In an ideal parallel LC circuit, energy sloshes back and forth between the electric field of the capacitor and the magnetic field of the inductor. The natural resonant frequency is:
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$
However, real inductors have resistance. This causes the oscillations to damp out (decay). The amplifier's job is to inject just enough energy back into the tank circuit to overcome these resistive losses, maintaining sustained oscillations.

### 4.2 Hartley Oscillator

The Hartley oscillator is distinguished by its tapped inductor.

**Circuit Diagram (Conceptual):**
```text
           Vcc
            |
            R_bias
            |
            +------------+--------> V_out
            |            |
          |/ C         -----
    +-----|  NPN        ---  C
    |     |\ E           |
    |       |            |
    +-------|------------+
    |       |            |
    |       |           _|_
   _|_      |          /   \  L1
   L2       |          \___/
  /   \     |            |
  \___/     +------------+ (Tap)
    |                    |
   GND                  GND
```

**Working Principle:**
The tank circuit consists of capacitor $C$ in parallel with two series inductors $L_1$ and $L_2$ (often a single tapped coil). The tap is connected to the common terminal (usually ground in the AC equivalent circuit). The voltage across $L_1$ provides the input to the amplifier, and the output is fed across $L_2$.

**Frequency of Oscillation:**
Assuming no mutual inductance ($M=0$):
$$f_0 = \frac{1}{2\pi\sqrt{(L_1 + L_2)C}}$$
If mutual inductance $M$ exists between the coils:
$$f_0 = \frac{1}{2\pi\sqrt{(L_1 + L_2 + 2M)C}}$$

**Condition for Oscillation:**
The feedback fraction is determined by the ratio of the inductances. For oscillation:
$$A \ge \frac{L_1}{L_2}$$
*(Note: depending on the exact configuration, the ratio might be $L_2/L_1$. The key is that the gain must overcome the step-down ratio of the tapped coil).*

**Characteristics:**
*   **Advantages:** Easy to tune by making C a variable capacitor. Wide frequency range.
*   **Disadvantages:** Harmonic content can be high; poorer frequency stability than Colpitts.

### 4.3 Colpitts Oscillator

The Colpitts oscillator is the dual of the Hartley oscillator. It uses a tapped capacitor network.

**Circuit Diagram (Conceptual):**
```text
           Vcc
            |
            R_bias
            |
            +------------+--------> V_out
            |            |
          |/ C          _|_
    +-----|  NPN       /   \  L
    |     |\ E         \___/
    |       |            |
    +-------|------------+
    |       |            |
    |       |          -----
  -----     |           ---  C1
   ---  C2  |            |
    |       +------------+ (Tap)
    |                    |
   GND                  GND
```

**Working Principle:**
The tank circuit consists of inductor $L$ in parallel with two series capacitors $C_1$ and $C_2$. The junction between $C_1$ and $C_2$ acts as the tap.

**Frequency of Oscillation:**
The equivalent capacitance $C_{eq}$ of $C_1$ and $C_2$ in series is:
$$C_{eq} = \frac{C_1 C_2}{C_1 + C_2}$$
The frequency is:
$$f_0 = \frac{1}{2\pi\sqrt{L C_{eq}}}$$

**Condition for Oscillation:**
The feedback fraction is determined by the capacitor voltage divider:
$$A \ge \frac{C_1}{C_2}$$

**Characteristics:**
*   **Advantages:** Better frequency stability than Hartley. Excellent performance at high frequencies. Lower distortion because the capacitors provide a low-impedance path to ground for high-frequency harmonics.
*   **Disadvantages:** Harder to tune over a wide range since changing both capacitors simultaneously is mechanically complex.

### 4.4 LC Oscillators Comparison

| Feature | Hartley Oscillator | Colpitts Oscillator |
| :--- | :--- | :--- |
| **Tank Circuit** | Tapped Inductor ($L_1, L_2$), Single $C$ | Tapped Capacitor ($C_1, C_2$), Single $L$ |
| **Feedback Ratio** | $L_1 / L_2$ | $C_1 / C_2$ |
| **Frequency Formula** | $\frac{1}{2\pi\sqrt{(L_1+L_2)C}}$ | $\frac{1}{2\pi\sqrt{L(C_1C_2)/(C_1+C_2)}}$ |
| **Best Application** | Wideband variable frequency | High-frequency, fixed stability |

---

## 5. Crystal Oscillators

When extreme frequency stability is required (e.g., in digital watches, computers, transmitters), LC circuits are inadequate because L and C values drift with temperature and aging. Crystal oscillators solve this using the **piezoelectric effect**.

### 5.1 Piezoelectric Effect
Materials like quartz exhibit piezoelectricity:
*   Apply mechanical stress $\rightarrow$ Generates an electrical voltage.
*   Apply an electrical voltage $\rightarrow$ Crystal mechanically deforms (vibrates).
When an AC voltage is applied, the crystal vibrates. If the AC frequency matches the crystal's mechanical resonant frequency, the vibrations become very strong, and the crystal acts like a highly precise electrical resonant circuit.

### 5.2 Crystal Equivalent Circuit

Electrically, a quartz crystal behaves like a complex RLC circuit.

**ASCII Equivalent Circuit:**
```text
           +--- L_s --- C_s --- R_s ---+
           |                           |
   Pin 1 --+                           +-- Pin 2
           |                           |
           +----------- C_p -----------+
```
*   **$C_p$ (Parallel Capacitance):** Capacitance of the mounting electrodes and holder.
*   **$L_s$ (Series Inductance):** Represents the crystal's mass.
*   **$C_s$ (Series Capacitance):** Represents the crystal's mechanical stiffness (elasticity).
*   **$R_s$ (Series Resistance):** Represents internal mechanical friction losses.

**Resonant Frequencies:**
A crystal has two closely spaced resonant frequencies:
1.  **Series Resonant Frequency ($f_s$):** Due to $L_s$ and $C_s$. Impedance is minimum.

$$f_s = \frac{1}{2\pi\sqrt{L_s C_s}}$$
2.  **Parallel Resonant Frequency ($f_p$):** Due to $L_s$ resonating with the series combination of $C_s$ and $C_p$. Impedance is maximum.

$$f_p = \frac{1}{2\pi\sqrt{L_s \left(\frac{C_s C_p}{C_s + C_p}\right)}}$$
Since $C_p \gg C_s$, $f_p$ is slightly greater than $f_s$ (usually by less than 1%). The oscillator usually operates slightly above $f_s$, where the crystal behaves inductively.

**Q Factor:**
The quality factor (Q) of a crystal is exceptionally high—ranging from 10,000 to over 1,000,000 (compared to ~100 for a good LC circuit). This high Q is the source of its incredible frequency stability.

### 5.3 Crystal Oscillator Circuits
Crystals can be used to replace the inductor in a Colpitts oscillator (creating a Pierce oscillator) because between $f_s$ and $f_p$, the crystal exhibits an inductive reactance.

**Advantages:**
*   Unmatched frequency stability (measured in parts per million, ppm).
*   Extremely high Q factor.
*   Fixed, reliable frequency.

---

## 6. Waveform Generators

While harmonic oscillators (RC, LC, Crystal) generate sine waves, many engineering applications require non-sinusoidal waveforms like square, triangular, or sawtooth waves. These are generated using relaxation oscillators or shaping circuits.

### 6.1 Square Wave Generator (Astable Multivibrator)

An astable multivibrator has no stable states; it continuously switches back and forth between two voltage levels (e.g., $+V_{sat}$ and $-V_{sat}$), producing a square wave.

**Circuit Diagram (Op-Amp based):**
```text
                  +Vcc
                   |
             +-----------+
             |           |
      +------|-\         |
      |      |  >--------+----+------> V_out (Square Wave)
      |  +---|+/         |    |
      |  |   |           |    |
      |  |   +-----------+    R_f
      |  |         |          |
      C  R1       -Vcc        |
      |  |                    |
     GND +--------------------+
         |
         R2
         |
        GND
```
**Working Principle:**
*   The op-amp acts as a comparator with hysteresis (Schmitt Trigger) due to positive feedback via $R_1$ and $R_2$.
*   Capacitor $C$ charges and discharges through $R_f$ between the upper and lower threshold voltages set by the voltage divider $R_1, R_2$.
*   When $V_C$ hits a threshold, the output flips to the opposite saturation level, and the capacitor reverses its charging direction.

**Frequency Formula:**
$$f_0 = \frac{1}{2 R_f C \ln\left(\frac{1+\beta}{1-\beta}\right)}$$
where $\beta = \frac{R_2}{R_1+R_2}$. If $R_1 = R_2 \times 1.16$, then $f_0 \approx \frac{1}{2 R_f C}$.

### 6.2 Triangular Wave Generator

A triangular wave is created by mathematically integrating a square wave. If you feed a constant DC voltage (the top of a square wave) into an integrator, the output ramps up linearly. When the square wave flips to negative, the integrator ramps down.

**Circuit Concept:**
`[Square Wave Generator] ---> [Op-Amp Integrator] ---> Triangular Wave Out`

By combining an astable multivibrator (comparator) and an integrator, we generate both square and triangular waves simultaneously.

### 6.3 Sawtooth Wave Generator
Similar to a triangular wave, but the rise time is very different from the fall time (e.g., a slow linear ramp up, followed by an almost instantaneous flyback drop). 
**Applications:** Cathode Ray Tube (CRT) sweep circuits, time-base generators in oscilloscopes, PWM modulation.

---

## ⚖️ 7. Master Comparison Table

| Parameter | Wien Bridge | Phase-Shift | Hartley | Colpitts | Crystal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Frequency Range** | 1 Hz - 1 MHz (AF) | 1 Hz - 100 kHz (AF) | 100 kHz - 100 MHz (RF) | 100 kHz - 100 MHz (RF) | 10 kHz - 100 MHz |
| **Feedback Network** | Series-Parallel RC | 3-stage RC | Tapped Inductor | Tapped Capacitor | Quartz Crystal |
| **Frequency Formula**| $\frac{1}{2\pi RC}$ | $\frac{1}{2\pi RC\sqrt{6}}$ | $\frac{1}{2\pi\sqrt{L_{eq}C}}$ | $\frac{1}{2\pi\sqrt{LC_{eq}}}$ | $f_s = \frac{1}{2\pi\sqrt{L_s C_s}}$ |
| **Stability** | Good | Poor | Fair | Good | Excellent (Very High) |
| **Q Factor** | Low (<10) | Low (<10) | Medium (~100) | Medium (~100) | Extremely High (>10,000)|
| **Applications** | Audio Generators | Simple AF sources | Radio Receivers | RF Transmitters | Clocks, Microcontrollers |

---

## ⭐ 8. Section Summary & NEC Exam Prep

### Key Equations
| Description | Formula | Conditions |
| :--- | :--- | :--- |
| Barkhausen Criterion | $A\beta = 1$ | Magnitude $|A\beta|=1$, Phase $= 0^\circ$ |
| Wien Bridge Freq | $f = \frac{1}{2\pi RC}$ | $R_1=R_2, C_1=C_2$ |
| Wien Bridge Gain | $A \ge 3$ | To overcome $\beta = 1/3$ |
| Phase-Shift Freq | $f = \frac{1}{2\pi RC\sqrt{6}}$ | 3 RC sections |
| Phase-Shift Gain | $|A| \ge 29$ | To overcome $\beta = 1/29$ |
| Colpitts Freq | $f = \frac{1}{2\pi\sqrt{LC_{eq}}}$ | $C_{eq} = \frac{C_1 C_2}{C_1 + C_2}$ |

### ⚠️ NEC Exam Traps
1. **The $\sqrt{6}$ Trap:** Forgetting the $\sqrt{6}$ in the Phase-Shift oscillator formula. $f = \frac{1}{2\pi RC}$ is ONLY for the Wien bridge.
2. **Gain vs. Feedback:** Barkhausen requires $|A\beta| \ge 1$ to start. If an exam asks for the *feedback factor* $\beta$ of a Wien bridge, it's $1/3$. The *amplifier gain* required is $3$. Do not confuse the two.
3. **Hartley vs. Colpitts Identification:** 
   * **H**artley = **H**enries (Tapped Inductor).
   * **C**olpitts = **C**apacitors (Tapped Capacitor).
4. **Crystal Frequencies:** Remember $f_p$ is always slightly greater than $f_s$.

### 💡 Engineering Intuition
An oscillator is just an amplifier biting its own tail. The feedback network is a filter that strictly controls *which* frequency is allowed to pass back to the input exactly in phase. Only the frequency that successfully runs the gauntlet of the feedback network without being phase-shifted away from $0^\circ$ gets continuously amplified.

---

### Conceptual Questions
1. Why is positive feedback required in an oscillator, whereas negative feedback is used in standard amplifiers?
2. Explain the physical significance of the two parts of the Barkhausen criterion.
3. Why are LC oscillators generally not used for very low audio frequencies?
4. What physical property of quartz makes it suitable for use in oscillators?
5. How does a square wave generator fundamentally differ from a harmonic (sine wave) oscillator?

### Numerical Problems
**Level 1 (Foundation):**
1. Calculate the frequency of a Wien Bridge oscillator if $R = 5 \text{ k}\Omega$ and $C = 0.05 \text{ }\mu\text{F}$.
2. In a Colpitts oscillator, $L = 100 \text{ }\mu\text{H}$, $C_1 = 0.01 \text{ }\mu\text{F}$, and $C_2 = 0.01 \text{ }\mu\text{F}$. Find the oscillation frequency.

**Level 2 (Engineering):**
3. A phase-shift oscillator uses three identical RC sections. If $C = 0.1 \text{ }\mu\text{F}$ and the desired frequency is $1 \text{ kHz}$, calculate the required value of $R$ and the minimum amplifier gain.

**Level 3 (NEC Challenge):**
4. An engineer designs a Hartley oscillator with $L_1 = 2 \text{ mH}$, $L_2 = 1 \text{ mH}$, and mutual inductance $M = 0.5 \text{ mH}$. If the tuning capacitor $C$ is set to $200 \text{ pF}$, calculate the exact oscillation frequency and the minimum required voltage gain of the active device.
5. A quartz crystal has $L_s = 0.5 \text{ H}$, $C_s = 0.05 \text{ pF}$, and $C_p = 2 \text{ pF}$. Calculate both the series resonant frequency and the parallel resonant frequency, and find the percentage difference between them.

---

### NEC-Style MCQs

1. The Barkhausen criterion for sustained oscillations states that the loop gain $|A\beta|$ must be:
   a) $< 1$
   b) $> 1$
   c) $= 1$
   d) $= 0$

2. In a Wien bridge oscillator, the minimum voltage gain required for the amplifier to sustain oscillations is:
   a) $1$
   b) $3$
   c) $29$
   d) $\sqrt{6}$

3. Which oscillator uses a tapped inductor in its tank circuit?
   a) Colpitts
   b) Phase-shift
   c) Hartley
   d) Crystal

4. The phase shift provided by the feedback network in a standard 3-stage RC phase-shift oscillator is:
   a) $0^\circ$
   b) $90^\circ$
   c) $180^\circ$
   d) $360^\circ$

5. What is the primary advantage of a crystal oscillator over an LC oscillator?
   a) Higher output power
   b) Lower cost
   c) Exceptional frequency stability
   d) Wide variable frequency range

6. In a Colpitts oscillator, the feedback fraction is determined by the ratio of:
   a) Two inductors
   b) Two capacitors
   c) Resistor and capacitor
   d) Mutual inductance to self-inductance

7. A quartz crystal operates on the principle of:
   a) The Hall effect
   b) The Piezoelectric effect
   c) The Seebeck effect
   d) Electromagnetic induction

8. Which circuit is primarily used to generate a square wave?
   a) Astable multivibrator
   b) Integrator
   c) Wien bridge
   d) Pierce oscillator

9. For an oscillator to start reliably from thermal noise, the initial loop gain $|A\beta|$ should be:
   a) Exactly 1
   b) Slightly less than 1
   c) Slightly greater than 1
   d) Infinity

10. If $C_1$ and $C_2$ are the split capacitors in a Colpitts oscillator, the equivalent capacitance $C_{eq}$ determining the frequency is:
    a) $C_1 + C_2$
    b) $C_1 - C_2$
    c) $(C_1 C_2) / (C_1 + C_2)$
    d) $\sqrt{C_1 C_2}$

---

### Answers to MCQs
1. c
2. b
3. c
4. c
5. c
6. b
7. b
8. a
9. c
10. c
