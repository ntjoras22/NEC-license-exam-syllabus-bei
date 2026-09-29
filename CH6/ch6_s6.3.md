## Section Communication System (AEiE0603)

## 📖 1. Introduction
Communication systems are designed to transmit information from a source to a destination reliably and efficiently. This section covers the foundational aspects of both analog and digital communication, focusing on signal representation, system bandwidth, signal distortion, and various modulation techniques (AM, FM, PM). This is a high-yield topic for the NEC exam.

## 2. Basic Building Blocks of Communication Systems
Every communication system comprises three essential components:
1.  **Transmitter**: Converts the source information (voice, data, video) into a signal suitable for transmission. This often involves filtering, amplification, and modulation.
2.  **Channel/Medium**: The physical path over which the signal travels (e.g., copper wire, optical fiber, free space). The channel introduces attenuation and noise.
3.  **Receiver**: Extracts the desired information from the received signal. This involves amplification, demodulation, and filtering.

> [!NOTE] Definition
> **Modulation**: The process of varying one or more properties (amplitude, frequency, or phase) of a periodic waveform, called the *carrier signal*, with a modulating signal that contains information to be transmitted.

## 3. Signal and Noise in Communication System
-   **Signal**: The desired electrical or electromagnetic representation of the information.
-   **Noise**: Unwanted, random electrical energy that interferes with the transmitted signal. Noise can be internal (thermal noise in electronics) or external (atmospheric, cosmic, industrial).
-   **Signal-to-Noise Ratio (SNR)**: A critical parameter indicating system quality. It is the ratio of signal power to noise power.

$$SNR_{dB} = 10 \log_{10} \left( \frac{P_{signal}}{P_{noise}} \right)$$

## 4. Low Pass and Band Pass Signals and Systems
-   **Low Pass Signal**: A signal whose frequency spectrum is concentrated around zero frequency (DC) and drops off at higher frequencies. Baseband signals (like voice or unmodulated data) are low pass.
-   **Band Pass Signal**: A signal whose frequency spectrum is concentrated around a non-zero frequency (the carrier frequency $f_c$). Modulated signals transmitted over the air are band pass.
-   **Bandwidth ($BW$)**: The range of frequencies over which a signal has significant power or a system can effectively operate. For a low pass system, $BW = f_{upper}$. For a band pass system, $BW = f_{upper} - f_{lower}$.

## 5. Distortionless Transmission
For a signal $x(t)$ to pass through a system with impulse response $h(t)$ and emerge perfectly undistorted as $y(t)$, the output must be an exact replica of the input, except for a possible amplitude scaling ($K$) and a time delay ($t_d$).
$$y(t) = K \cdot x(t - t_d)$$
Taking the Fourier Transform:
$$Y(f) = K \cdot X(f) \cdot e^{-j2\pi f t_d}$$
Since $Y(f) = H(f) \cdot X(f)$, the transfer function for a distortionless system must be:
$$H(f) = K e^{-j2\pi f t_d}$$
This implies two conditions for the system:
1.  **Amplitude Response**: $|H(f)| = K$ (constant for all frequencies).
2.  **Phase Response**: $\angle H(f) = -2\pi f t_d$ (linear phase shift proportional to frequency).

## 6. The Hilbert Transform
The Hilbert transform does not change the amplitude spectrum of a signal but applies a $-90^\circ$ ($-\pi/2$) phase shift to all positive frequencies and a $+90^\circ$ ($+\pi/2$) phase shift to all negative frequencies.
Mathematically, the Hilbert transform $\hat{x}(t)$ of a signal $x(t)$ is its convolution with $1/(\pi t)$:
$$\hat{x}(t) = x(t) * \frac{1}{\pi t} = \frac{1}{\pi} \int_{-\infty}^{\infty} \frac{x(\tau)}{t - \tau} d\tau$$
In the frequency domain:
$$\mathcal{F}\{\hat{x}(t)\} = -j \cdot \text{sgn}(f) \cdot X(f)$$
where $\text{sgn}(f)$ is the signum function.
**Application**: Hilbert transform is extensively used to generate Single Sideband (SSB) modulated signals and in representing bandpass signals in terms of their analytic signal components.

## 7. Amplitude Modulation (AM)
In AM, the amplitude of a high-frequency carrier wave is varied in accordance with the instantaneous amplitude of the modulating signal.

### Time Domain Expression (Standard AM)
Let the carrier be $c(t) = A_c \cos(2\pi f_c t)$ and the message be $m(t)$.
The standard AM signal (DSB-FC: Double Sideband Full Carrier) is:
$$s_{AM}(t) = [A_c + m(t)] \cos(2\pi f_c t) = A_c [1 + k_a m(t)] \cos(2\pi f_c t)$$
where $k_a$ is the amplitude sensitivity.
**Modulation Index ($\mu$)**: For a sinusoidal message $m(t) = A_m \cos(2\pi f_m t)$, $\mu = \frac{A_m}{A_c} = k_a A_m$. For undistorted envelope detection, $\mu \le 1$.

### Frequency Domain Representation
The spectrum of AM contains a carrier impulse and two sidebands (Upper Sideband USB and Lower Sideband LSB).
$$S_{AM}(f) = \frac{A_c}{2}[\delta(f-f_c) + \delta(f+f_c)] + \frac{1}{2}[M(f-f_c) + M(f+f_c)]$$
**Bandwidth of AM**: $BW = 2f_m$ (where $f_m$ is the maximum frequency of the message).
**Power**: Total power $P_t = P_c (1 + \frac{\mu^2}{2})$.

### Types of AM Signals
1.  **DSB-FC (Standard AM)**: Carrier + both sidebands. Very inefficient in power but simple to demodulate (Envelope detector).
2.  **DSB-SC (Double Sideband Suppressed Carrier)**: Carrier is suppressed. Power efficient but requires synchronous demodulation. $s(t) = m(t) \cdot A_c \cos(2\pi f_c t)$.
3.  **SSB-SC (Single Sideband)**: Only one sideband is transmitted. Highly bandwidth efficient ($BW = f_m$). Used in point-to-point voice communication.
4.  **VSB (Vestigial Sideband)**: One sideband is almost entirely transmitted, and a trace (vestige) of the other sideband is transmitted. Used in standard television broadcasting.

## 8. Angle Modulation: Frequency (FM) and Phase (PM)
In angle modulation, the phase angle of the carrier is varied according to the message signal, while the amplitude remains constant.
Let carrier $c(t) = A_c \cos(\theta_i(t))$.
-   **Phase Modulation (PM)**: The instantaneous phase varies linearly with the message.

$$\theta_i(t) = 2\pi f_c t + k_p m(t)$$

$$s_{PM}(t) = A_c \cos(2\pi f_c t + k_p m(t))$$
-   **Frequency Modulation (FM)**: The instantaneous frequency varies linearly with the message. Instantaneous frequency $f_i(t) = \frac{1}{2\pi} \frac{d\theta_i(t)}{dt}$.

$$f_i(t) = f_c + k_f m(t)$$

$$\theta_i(t) = 2\pi f_c t + 2\pi k_f \int_0^t m(\tau) d\tau$$

$$s_{FM}(t) = A_c \cos\left(2\pi f_c t + 2\pi k_f \int_0^t m(\tau) d\tau\right)$$

### FM Bandwidth (Carson's Rule)
For FM, the modulation index is $\beta = \frac{\Delta f}{f_m}$, where frequency deviation $\Delta f = k_f A_m$.
The practical bandwidth is given by **Carson's Rule**:
$$BW_{FM} \approx 2(\Delta f + f_m) = 2f_m(\beta + 1)$$

### Types of FM Signals
1.  **Narrowband FM (NBFM)**: $\beta \ll 1$. $BW \approx 2f_m$ (similar to AM). Used in mobile radios.
2.  **Wideband FM (WBFM)**: $\beta \gg 1$. $BW \approx 2\Delta f$. Used in FM radio broadcasting (high fidelity, better noise immunity).

---

## Comparison Table: AM vs FM

| Feature | Amplitude Modulation (AM) | Frequency Modulation (FM) |
| :--- | :--- | :--- |
| **Parameter Varied** | Amplitude of carrier | Frequency of carrier |
| **Bandwidth** | $2f_m$ (constant) | $2(\Delta f + f_m)$ (depends on $\beta$) |
| **Noise Immunity** | Poor | Very Good |
| **Power Efficiency** | Poor (most power in carrier) | Constant power ($P = A_c^2 / 2$) |
| **Modulation Index** | $\mu = A_m / A_c$ ($0 \le \mu \le 1$) | $\beta = \Delta f / f_m$ (can be $>1$) |
| **Applications** | MW/SW Radio broadcasting | High-quality radio, TV audio |

---

## 🔍 Worked Example

**Example 1**: An AM wave has a total power of 1000 Watts with a modulation index of 0.5. Calculate the carrier power and the power in each sideband.
**Solution**:
Total Power $P_t = P_c (1 + \frac{\mu^2}{2})$
$1000 = P_c \left(1 + \frac{0.5^2}{2}\right) = P_c \left(1 + \frac{0.25}{2}\right) = P_c (1.125)$
Carrier Power $P_c = \frac{1000}{1.125} = 888.89$ Watts.
Total sideband power $P_{SB} = P_t - P_c = 1000 - 888.89 = 111.11$ Watts.
Power in each sideband (USB or LSB) $= P_{SB} / 2 = 55.55$ Watts.

---

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> - Confusing the formulas for AM power vs FM bandwidth. In AM, power depends on the modulation index. In FM, the total transmitted power is *constant* regardless of modulation.
> - Forgetting that phase must be linear for distortionless transmission; constant phase shift still causes phase distortion (except for a flat delay).

> [!TIP]
> - **Hilbert Transform property**: Applying the Hilbert transform twice gives the negative of the original signal: $\hat{\hat{x}}(t) = -x(t)$.
> - **Carson's Rule**: This is universally tested. Always remember $BW = 2(\Delta f + f_m)$.
> - AM envelope detection works only for DSB-FC when $\mu \le 1$. Overmodulation ($\mu > 1$) causes envelope distortion and requires synchronous detection.

---

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - Distortionless System: $|H(f)| = K$, $\angle H(f) = -2\pi f t_d$
> - AM Standard Equation: $s(t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)$
> - FM Modulation Index: $\beta = \frac{\Delta f}{f_m}$
> - FM Bandwidth: $BW = 2(\Delta f + f_m)$

---

## ✏️ Practice Problems

1. What is the Hilbert transform of $\cos(\omega_0 t)$?
   *Hint: The Hilbert transform delays all frequencies by $90^\circ$. $\cos(\omega_0 t - 90^\circ) = \sin(\omega_0 t)$.*
   *Answer: $\sin(\omega_0 t)$*

2. An FM signal is given by $s(t) = 10 \cos(2\pi \times 10^8 t + 5 \sin(2\pi \times 10^3 t))$. Determine the carrier frequency, modulating frequency, modulation index, and bandwidth.
   *Hint: Compare with standard form $A_c \cos(2\pi f_c t + \beta \sin(2\pi f_m t))$.*
   *Answer: $f_c = 100$ MHz, $f_m = 1$ kHz, $\beta = 5$. $BW = 2(1\text{kHz})(5 + 1) = 12$ kHz.*

3. A standard AM transmission has a carrier power of 400 W and is modulated to a depth of 70%. What is the total transmitted power?
   *Hint: $P_t = P_c(1 + \mu^2/2)$.*
   *Answer: $P_t = 400(1 + 0.7^2 / 2) = 400(1 + 0.49/2) = 400(1.245) = 498$ W.*
</Section 6.3: Communication System (AEiE0603)>
