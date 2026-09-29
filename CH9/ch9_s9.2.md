## Section 9.2 — Equalization and Diversity Techniques (AEiE0902)

## 📖 1. Introduction
This section focuses on techniques used in receiver design to mitigate the adverse effects of the wireless channel, such as Inter-Symbol Interference (ISI) and fading. Equalization and diversity are essential concepts for ensuring reliable high-speed data transmission in telecommunications, making them highly probable exam topics.

## 💡 2. Basic Concept
When a signal passes through a wireless channel, multipath propagation causes different delayed versions of the signal to overlap at the receiver, causing Inter-Symbol Interference (ISI).

> [!NOTE] Definition
> **Equalization**: The process of correcting channel-induced distortion, primarily to minimize Inter-Symbol Interference (ISI).
> **Diversity**: A technique used to combat fading by providing the receiver with multiple, statistically independent fading copies of the same information-bearing signal.

## 3. Basic Equalization
An equalizer within a receiver compensates for the average range of expected channel amplitude and delay characteristics.

### Linear Equalizers
The most basic type of equalizer. It passes the received signal through a linear filter, typically a Transversal Filter (FIR filter).
- The output $y_k$ is a linear combination of the current and past received samples.
- **Zero-Forcing (ZF) Equalizer**: Inverts the frequency response of the channel. However, it can severely amplify noise at frequencies where the channel response has deep nulls.
- **Minimum Mean Square Error (MMSE) Equalizer**: Balances mitigating ISI and minimizing noise enhancement.

## 4. Adaptive Equalization
Wireless channels are time-varying; therefore, the equalizer must track the channel variations and adapt its coefficients continuously.

### Operating Modes
1. **Training Mode**: A known, fixed-length training sequence is sent by the transmitter so the receiver's equalizer can adapt to a proper setting.
2. **Tracking Mode**: After training, user data is sent. The equalizer updates its coefficients based on the data to track the time-varying channel.

### Algorithms for Adaptive Equalization
- **Least Mean Squares (LMS)**: Simple, low computational complexity, but slow convergence.
- **Recursive Least Squares (RLS)**: Fast convergence, but high computational complexity.

## ⚙️ 5. Diversity Methods
If one radio path undergoes a deep fade, another independent path may have a strong signal. By having more than one path to select from, both the instantaneous and average SNRs at the receiver may be improved.

### Space Diversity (Antenna Diversity)
The most common diversity technique. It uses multiple antennas separated in space.
- For the signals to be uncorrelated, antennas must be separated by a minimum distance (e.g., $\lambda / 2$ for mobile stations, $10\lambda$ to $20\lambda$ for base stations).
- **Selection Diversity**: The receiver selects the antenna with the highest SNR.
- **Maximal Ratio Combining (MRC)**: Signals from all antennas are co-phased and weighted according to their individual SNRs, then summed. Gives the best performance.
- **Equal Gain Combining (EGC)**: Signals are co-phased and summed with equal weights.

### Polarization Diversity
Uses multiple antennas with orthogonal polarizations (e.g., horizontal and vertical).
- Multipath reflections tend to scramble signal polarization. Thus, two orthogonally polarized signals will exhibit uncorrelated fading.
- Advantage: Saves physical space compared to spatial diversity, especially useful at base stations where placing antennas far apart is expensive.

### Frequency Diversity
The same information is transmitted simultaneously on two or more carrier frequencies.
- The frequency separation must be greater than the coherence bandwidth of the channel ($\Delta f > B_c$) for the fading to be uncorrelated.
- Drawback: Uses extra bandwidth.

### Time Diversity
The same information is transmitted at different times.
- The time separation must be greater than the coherence time of the channel ($\Delta t > T_c$).
- Often implemented via channel coding and interleaving.
- Drawback: Introduces latency.

## ⚖️ Comparison of Diversity Techniques
| Technique | Resource Used | Condition for Independence | Primary Advantage |
|---|---|---|---|
| Space Diversity | Multiple Antennas | Distance $d > \lambda/2$ | No extra bandwidth or time needed |
| Polarization | Antenna Polarization | Orthogonal polarizations | Saves space at cell sites |
| Frequency | Spectrum | $\Delta f >$ Coherence Bandwidth | Good for frequency-selective fading |
| Time | Time slots | $\Delta t >$ Coherence Time | Suitable for fast fading channels |

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not confuse Equalization and Diversity. Equalization combats ISI (caused by delay spread), while Diversity combats flat fading (caused by multipath interference causing deep nulls).

> [!TIP]
> For questions on combining techniques, remember the hierarchy of performance: MRC is always better than EGC, which is better than Selection Diversity.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - **Selection Diversity SNR Improvement**: $\bar{\gamma} = \gamma_0 \sum_{k=1}^{M} \frac{1}{k}$ (where $\gamma_0$ is average SNR of one branch, M is number of branches).
> - **Antenna Separation**: Must be $\ge \lambda/2$ to assure uncorrelated signals in uniform scattering environments.

## ✏️ Practice Problems
1. A base station uses two antennas for space diversity. If the operating frequency is 1800 MHz, what is the minimum required separation distance between the antennas to ensure uncorrelated fading at the mobile unit? (Assume $\lambda/2$ rule).
   *Answer sketch: $\lambda = c/f = 3 \times 10^8 / 1800 \times 10^6 = 0.166$ m. Minimum separation = $\lambda/2 = 0.083$ m or 8.33 cm.*

2. Explain the difference between Zero-Forcing and MMSE equalizers.
   *Answer sketch: ZF simply inverts the channel frequency response, which eliminates ISI but can drastically amplify noise at deep fades. MMSE takes noise into account, minimizing the total error from both ISI and noise, providing better overall performance.*

3. Why is polarization diversity preferred over space diversity in modern cellular base stations?
   *Answer sketch: Because space diversity requires large physical separation between antennas to achieve uncorrelated signals, which is bulky and expensive on towers. Polarization diversity achieves uncorrelated signals using orthogonal polarizations within a single compact antenna radome.*
</Section 9.2: Equalization and Diversity Techniques (AEiE0902)>
