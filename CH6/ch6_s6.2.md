## Section Wave Propagation and Antenna (AEiE0602)

## 📖 1. Introduction
This section explores time-varying electromagnetic fields, the cornerstone of wireless communication. We bridge the gap between statics and dynamics using Maxwell's equations and displacement current, study how waves propagate through different media, and finally examine how antennas radiate and receive these waves. This topic is heavily tested in the NEC exam for telecommunication and electronics roles.

## 2. Displacement Current
In static fields, Ampere's law is $\nabla \times \mathbf{H} = \mathbf{J}$. However, for time-varying fields, taking the divergence of both sides yields $\nabla \cdot (\nabla \times \mathbf{H}) = \nabla \cdot \mathbf{J} = 0$. This contradicts the continuity equation $\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$.
To resolve this, James Clerk Maxwell introduced the **displacement current density ($\mathbf{J}_d$)**.
$$\nabla \times \mathbf{H} = \mathbf{J} + \mathbf{J}_d$$
where $\mathbf{J}_d = \frac{\partial \mathbf{D}}{\partial t}$.

> [!NOTE] Definition
> **Displacement Current**: The current arising from a time-varying electric flux. It does not involve the physical movement of charges but rather the variation of the electric field with time (e.g., current 'flowing' through a capacitor).

## 3. Maxwell's Equations
Maxwell's equations are the fundamental laws governing all macroscopic electromagnetic phenomena.

| Law | Point (Differential) Form | Integral Form | Physical Meaning |
| :--- | :--- | :--- | :--- |
| **Faraday's Law** | $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ | $\oint_L \mathbf{E} \cdot d\mathbf{l} = -\int_S \frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{S}$ | Time-varying magnetic field induces an electric field. |
| **Ampere-Maxwell Law** | $\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$ | $\oint_L \mathbf{H} \cdot d\mathbf{l} = \int_S (\mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}) \cdot d\mathbf{S}$ | Time-varying electric field and current induce a magnetic field. |
| **Gauss's Law (Electric)**| $\nabla \cdot \mathbf{D} = \rho_v$ | $\oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v \rho_v dv$ | Electric flux through closed surface equals enclosed charge. |
| **Gauss's Law (Magnetic)**| $\nabla \cdot \mathbf{B} = 0$ | $\oint_S \mathbf{B} \cdot d\mathbf{S} = 0$ | No magnetic monopoles exist; magnetic flux lines are continuous loops. |

## 4. Wave Propagation in Media
The wave equations are derived from Maxwell's equations. For a source-free region ($\rho_v = 0, \mathbf{J} = 0$), the wave equation for $\mathbf{E}$ is:
$$\nabla^2 \mathbf{E} - \mu \varepsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0$$

For a time-harmonic field (varying as $e^{j\omega t}$), the wave propagation constant is $\gamma = \alpha + j\beta$.
$$\gamma = \sqrt{j\omega \mu (\sigma + j\omega \varepsilon)}$$
- $\alpha$: Attenuation constant (Np/m)
- $\beta$: Phase constant (rad/m)
- Intrinsic impedance: $\eta = \sqrt{\frac{j\omega \mu}{\sigma + j\omega \varepsilon}}$ ($\Omega$)
- Phase velocity: $v_p = \frac{\omega}{\beta}$ (m/s)

### 4.1 Plane Waves in Free Space
Free space parameters: $\sigma = 0, \varepsilon = \varepsilon_0, \mu = \mu_0$.
- $\alpha = 0$ (No attenuation)
- $\beta = \omega \sqrt{\mu_0 \varepsilon_0} = \frac{\omega}{c}$
- $v_p = c = 3 \times 10^8$ m/s
- $\eta = \eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 377 \Omega \approx 120\pi \Omega$

### 4.2 Lossless Dielectric
Parameters: $\sigma \approx 0, \varepsilon = \varepsilon_r \varepsilon_0, \mu = \mu_r \mu_0$.
- $\alpha = 0$
- $\beta = \omega \sqrt{\mu \varepsilon}$
- $v_p = \frac{1}{\sqrt{\mu \varepsilon}} = \frac{c}{\sqrt{\mu_r \varepsilon_r}}$
- $\eta = \sqrt{\frac{\mu}{\varepsilon}}$

### 4.3 Good Conductor
Parameters: $\sigma \gg \omega \varepsilon$.
- $\alpha = \beta = \sqrt{\frac{\omega \mu \sigma}{2}}$
- Skin Depth (Depth of penetration) $\delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega \mu \sigma}}$. It is the distance over which the wave amplitude drops to $e^{-1}$ (about 37%) of its initial value.
- $v_p = \omega \delta$
- $\eta = \sqrt{\frac{\omega \mu}{\sigma}} \angle 45^\circ$

## 5. Reflection of Plane Waves
When a wave hits a boundary between two media, part of it is reflected and part is transmitted.
- **Normal Incidence**: The wave strikes the boundary perpendicular to the surface.
  - Reflection Coefficient: $\Gamma = \frac{E_{r0}}{E_{i0}} = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}$
  - Transmission Coefficient: $\tau = \frac{E_{t0}}{E_{i0}} = \frac{2\eta_2}{\eta_2 + \eta_1}$
  - Note: $1 + \Gamma = \tau$.
- **Oblique Incidence**: Involves perpendicular and parallel polarizations, requiring Snell's laws and Fresnel equations.

## 6. Rectangular Waveguide
Waveguides are hollow metallic pipes used to confine and guide electromagnetic waves, typically at microwave frequencies.
- **Modes**: Waves propagate in specific configurations called modes.
- **TE (Transverse Electric) Mode**: Electric field has no component in the direction of propagation ($E_z = 0, H_z \neq 0$).
- **TM (Transverse Magnetic) Mode**: Magnetic field has no component in the direction of propagation ($H_z = 0, E_z \neq 0$).
- **TEM (Transverse Electromagnetic) Mode**: Neither $E$ nor $H$ has a component in the direction of propagation ($E_z = 0, H_z = 0$). *TEM mode cannot exist in a hollow rectangular waveguide.*

**Cutoff Frequency ($f_c$)**: The lowest frequency at which a specific mode will propagate. Frequencies below $f_c$ are attenuated (evanescent modes).
For a rectangular waveguide of dimensions $a \times b$ ($a > b$):
$$f_{c,mn} = \frac{v}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$
where $v$ is the phase velocity in the dielectric inside the waveguide.
**Dominant Mode**: The mode with the lowest cutoff frequency. For $a > b$, the dominant mode is $TE_{10}$.

## 7. Antenna Fundamentals
An antenna is a transducer that converts guided electromagnetic energy into radiating waves in free space, and vice versa.

### 7.1 Key Parameters
- **Radiation Pattern**: A mathematical or graphical representation of the radiation properties of the antenna as a function of space coordinates.
- **Directivity ($D$)**: Ratio of maximum radiation intensity to the average radiation intensity. $D = \frac{U_{max}}{U_{avg}}$.
- **Gain ($G$)**: Incorporates the antenna's efficiency ($e$). $G = eD$.
- **Effective Area ($A_e$)**: Measure of an antenna's ability to extract energy from a passing wave. $A_e = \frac{\lambda^2}{4\pi} D$.

### 7.2 Types of Antennas
- **Isotropic Antenna**: A hypothetical, lossless antenna having equal radiation in all directions ($D=1$). Used as a reference.
- **Omnidirectional Antenna**: Radiates equally in a given plane (e.g., horizontal plane) but not in other planes (e.g., a vertical dipole).
- **Directional Antenna**: Radiates/receives electromagnetic waves more effectively in some directions than in others (e.g., Yagi-Uda, Parabolic reflector).
- **Dipole Antenna**: The basic radiating element. A half-wave dipole ($L = \lambda/2$) has a directivity of 1.64 (2.15 dBi) and radiation resistance of 73 $\Omega$.
- **Travelling Wave Antenna**: Current travels in one direction (no standing waves). Examples: Beverage antenna, Rhombic antenna, Helical antenna (in axial mode). They are characteristically broadband.

## 🔍 Worked Example

**Example 1**: A $100$ MHz uniform plane wave propagates in a lossless medium with $\varepsilon_r = 4$ and $\mu_r = 1$. Calculate the phase velocity and intrinsic impedance.
**Solution**:
$\omega = 2\pi f = 2\pi \times 10^8$ rad/s
Phase velocity $v_p = \frac{c}{\sqrt{\mu_r \varepsilon_r}} = \frac{3 \times 10^8}{\sqrt{1 \times 4}} = 1.5 \times 10^8$ m/s
Intrinsic impedance $\eta = \sqrt{\frac{\mu}{\varepsilon}} = \sqrt{\frac{\mu_r \mu_0}{\varepsilon_r \varepsilon_0}} = \eta_0 \sqrt{\frac{\mu_r}{\varepsilon_r}} = 377 \sqrt{\frac{1}{4}} = 188.5 \Omega$.

---

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> - Confusing TE and TM modes. Remember: TE means $E$ is transverse (meaning $E_z = 0$).
> - Assuming TEM mode can propagate in hollow waveguides. It requires two separate conductors (like a coaxial cable).

> [!TIP]
> - **Skin depth ($\delta$)**: Remember that skin depth decreases as frequency or conductivity increases. High-frequency currents flow only on the surface of conductors.
> - **Dominant mode of rectangular waveguide ($a>b$)**: $TE_{10}$. For $TE_{10}$, the cutoff frequency is $f_{c,10} = \frac{c}{2a}$.
> - **Maxwell's Equations**: Be able to identify the mathematical expressions and match them to their physical laws (Faraday, Ampere, Gauss).

---

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - Free space intrinsic impedance: $\eta_0 \approx 377 \Omega$ or $120\pi \Omega$
> - Speed of light: $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 3 \times 10^8$ m/s
> - Reflection coefficient: $\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}$
> - Antenna effective area relation to directivity: $D = \frac{4\pi A_e}{\lambda^2}$

---

## ✏️ Practice Problems

1. An electromagnetic wave has an electric field $\mathbf{E} = 10 \cos(\omega t - \beta z) \mathbf{a}_x$ V/m in free space. Find the corresponding magnetic field $\mathbf{H}$.
   *Hint: In free space, $E$ and $H$ are perpendicular, and their ratio is $\eta_0$. The wave propagates in $+z$ direction, $\mathbf{E}$ is in $+x$, so $\mathbf{H}$ must be in $+y$ ($\mathbf{a}_x \times \mathbf{a}_y = \mathbf{a}_z$).*
   *Answer: $\mathbf{H} = \frac{10}{377} \cos(\omega t - \beta z) \mathbf{a}_y$ A/m*

2. Calculate the cutoff frequency for the dominant $TE_{10}$ mode in an air-filled rectangular waveguide with dimensions $a = 2$ cm and $b = 1$ cm.
   *Hint: $f_{c,10} = \frac{c}{2a}$.*
   *Answer: $f_c = \frac{3 \times 10^8}{2 \times 0.02} = 7.5$ GHz.*

3. What is the skin depth of copper ($\sigma = 5.8 \times 10^7$ S/m, $\mu_r = 1$) at 10 MHz?
   *Hint: Use $\delta = \frac{1}{\sqrt{\pi f \mu_0 \sigma}}$.*
   *Answer: $\delta \approx 20.9$ $\mu$m.*
</Section 6.2: Wave Propagation and Antenna (AEiE0602)>
