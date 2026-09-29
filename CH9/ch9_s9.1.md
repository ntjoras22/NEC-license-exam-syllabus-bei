## Section 9.1 — Telecommunication and Wireless Communication (AEiE0901)

## 📖 1. Introduction
This section covers the fundamental principles of telecommunication and wireless systems. It is critical for the NEC exam as it builds the foundation for understanding how information is transmitted over various media, how channels are assigned, and how signal propagation is affected by the environment.

## 2. History and Generations of Telecommunication
The evolution of telecommunications is marked by major technological milestones, particularly in mobile wireless systems.

> [!NOTE] Definition
> **Telecommunication**: The transmission of signs, signals, messages, words, writings, images and sounds or information of any nature by wire, radio, optical or other electromagnetic systems.

### Cellular Generations and Future Trends
| Generation | Technology/Standard | Data Rate | Key Features |
|---|---|---|---|
| 1G | AMPS, TACS | 2.4 kbps | Analog voice, circuit-switched |
| 2G | GSM, CDMA, IS-95 | 10-200 kbps | Digital voice, SMS, TDMA/CDMA |
| 3G | WCDMA, CDMA2000 | 2-21 Mbps | High-speed data, video calling, packet-switched data |
| 4G | LTE, WiMAX | 100 Mbps - 1 Gbps | All-IP network, MIMO, OFDM |
| 5G | NR (New Radio) | 1-10 Gbps | Ultra-low latency, massive IoT, mmWave |
| 6G (Future) | AI-integrated | >1 Tbps | THz frequencies, holographic communications |

## 3. Transmission Media
Transmission media are the physical paths between transmitter and receiver.

### Guided Transmission Media
Signals are guided along a solid medium.
- **Twisted Pair Cable**: Used for voice and data. Prone to crosstalk.
- **Coaxial Cable**: Higher bandwidth, shielding against interference.
- **Optical Fiber**: Uses light. Lowest attenuation, highest bandwidth.

### Unguided Transmission Media (Wireless)
Signals are broadcast through free space or air.
- **Radio Waves**: Omnidirectional, penetrates buildings (LF/MF).
- **Microwaves**: Line-of-sight (LOS), used for satellite and terrestrial links.
- **Infrared**: Short-range, LOS only, no obstacle penetration.

## 4. Propagation Models
Propagation models predict the average received signal strength at a given distance.

### Free Space Propagation Model
Used to predict received signal strength when the transmitter and receiver have a clear, unobstructed LOS path.

The received power $P_r(d)$ at a distance $d$ is given by the Friis Free Space Equation:
$$ P_r(d) = \frac{P_t G_t G_r \lambda^2}{(4\pi)^2 d^2 L} $$
Where:
- $P_t$ = transmitted power
- $G_t, G_r$ = transmitter and receiver antenna gains
- $\lambda$ = wavelength in meters ($c/f$)
- $d$ = T-R separation distance in meters
- $L$ = system loss factor ($L \ge 1$, $L=1$ for no loss)

**Example**:
Calculate the received power in dBm for a free space link with $P_t=50$ W, $G_t=G_r=1$, $f=900$ MHz, $d=1$ km.
1. $\lambda = c/f = \frac{3 \times 10^8}{900 \times 10^6} = 0.333$ m
2. $P_r = \frac{50 \times 1 \times 1 \times (0.333)^2}{16 \pi^2 \times (1000)^2} = 3.5 \times 10^{-11}$ W
3. $P_r(dBm) = 10 \log_{10}(P_r / 1mW) = 10 \log_{10}(3.5 \times 10^{-8} mW) = -74.5$ dBm

## 5. Basic Propagation Mechanisms
When a signal propagates, it interacts with the environment through three main mechanisms.

### Reflection
Occurs when a propagating electromagnetic wave impinges upon an object that has very large dimensions compared to the wavelength of the propagating wave (e.g., surface of the earth, buildings, walls).

### Diffraction
Occurs when the radio path between transmitter and receiver is obstructed by a surface with sharp irregularities (edges). Explains how RF energy can travel in urban areas without a direct LOS.

### Scattering
Occurs when the medium through which the wave travels consists of objects with dimensions that are small compared to the wavelength (e.g., foliage, street signs, lamp posts).

## 6. Channel Assignment and Handover Process
Efficient utilization of the radio spectrum relies on frequency reuse and managing user mobility.

### Channel Assignment Strategies
- **Fixed Channel Assignment (FCA)**: Each cell is allocated a predetermined set of voice channels. If all channels are occupied, the call is blocked.
- **Dynamic Channel Assignment (DCA)**: Channels are not allocated permanently. The base station requests a channel from the MSC when a call is made, improving capacity and reducing blocking probability.

### Handover (Handoff) Process
The process of transferring an active call or data session from one cell in a cellular network to another without dropping the connection.
- **Hard Handoff**: "Break before make." Current connection is broken before a new one is established (common in GSM).
- **Soft Handoff**: "Make before break." Mobile is connected to two or more base stations simultaneously (common in CDMA).

## 💡 7. Small Scale Multipath Propagation and Fading
Small-scale fading refers to rapid changes in radio signal amplitude and phase over a short period of time or travel distance.

Caused by multipath propagation, where multiple versions of the transmitted signal arrive at the receiver at slightly different times. Effects include:
- Rapid changes in signal strength over a small travel distance or time interval.
- Random frequency modulation due to varying Doppler shifts on different multipath signals.
- Time dispersion caused by multipath propagation delays.

### Rayleigh Fading Model
Used to describe the statistical time varying nature of the received envelope of a flat fading signal, or the envelope of an individual multipath component. Applicable when there is **no direct LOS** path between transmitter and receiver.

The Rayleigh probability density function (PDF) is:
$$ p(r) = \frac{r}{\sigma^2} \exp\left(-\frac{r^2}{2\sigma^2}\right) \quad (0 \le r \le \infty) $$
Where $r$ is the envelope amplitude and $\sigma^2$ is the time-average power of the received signal before envelope detection.

> [!NOTE] Rician Fading
> If there is a dominant stationary (non-fading) LOS signal component present, the small-scale fading envelope is described by a Rician distribution.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not confuse large-scale fading (path loss, shadowing) with small-scale fading (multipath, Doppler spread).

> [!TIP]
> For the Friis equation, remember that received power falls off as the square of the distance ($d^{-2}$), but in real-world urban environments, the path loss exponent is typically between 3 and 4 (i.e., $d^{-3}$ or $d^{-4}$).

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - Friis free space equation: $P_r(d) = \frac{P_t G_t G_r \lambda^2}{(4\pi)^2 d^2}$
> - Wavelength: $\lambda = \frac{c}{f}$
> - dBm conversion: $P(dBm) = 10 \log_{10}\left(\frac{P_{watts}}{1 mW}\right)$

## ✏️ Practice Problems
1. Calculate the free space path loss in dB for a 2.4 GHz Wi-Fi signal at a distance of 100 meters. (Assume $G_t=G_r=1$).
   *Answer sketch: Find $\lambda = c/f = 0.125$ m. Path Loss $PL = -10 \log_{10}\left(\frac{\lambda^2}{(4\pi d)^2}\right) = 20 \log_{10}(\frac{4\pi d}{\lambda})$. $PL = 20 \log_{10}(\frac{4\pi \times 100}{0.125}) = 80$ dB.*

2. Explain the difference between Hard Handoff and Soft Handoff with examples.
   *Answer sketch: Hard handoff disconnects before connecting to the new BS (GSM). Soft handoff connects to the new BS before disconnecting the old one (CDMA).*

3. What condition necessitates the use of a Rayleigh fading model over a Rician fading model?
   *Answer sketch: Rayleigh fading models an environment with many multipath components and no dominant Line-Of-Sight (LOS) path. If an LOS path exists, Rician is used.*
</Section 9.1: Telecommunication and Wireless Communication (AEiE0901)>
