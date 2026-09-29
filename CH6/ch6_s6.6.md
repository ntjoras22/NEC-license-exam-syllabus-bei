## Section Digital Signal Processing (AEiE0606)

## 📖 1. Introduction
Digital Signal Processing (DSP) covers the manipulation of signals after they have been converted to a digital format. Key exam areas include z-transforms, DFT/FFT, and the design of digital filters (IIR and FIR).

## 2. The z-Transform
The z-transform is the discrete-time equivalent of the Laplace transform.

> [!NOTE] Definition
> **z-transform**: For a discrete sequence $x[n]$, the two-sided z-transform is defined as:

$$ X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n} $$
> where $z$ is a complex variable.

### Region of Convergence (ROC)
The set of values of $z$ for which the sum converges.
- **Right-sided sequence (causal)**: ROC is $|z| > r_1$ (outside a circle).
- **Left-sided sequence (anti-causal)**: ROC is $|z| < r_2$ (inside a circle).
- **Two-sided sequence**: ROC is an annular ring $r_1 < |z| < r_2$.

### Properties of z-transform
- **Time Shifting**: $x[n - k] \leftrightarrow z^{-k} X(z)$
- **Convolution**: $x_1[n] * x_2[n] \leftrightarrow X_1(z) X_2(z)$
- **Parseval's Theorem**: Energy of the signal can be calculated by integrating over a closed contour in the z-plane.

## 3. System Transfer Function and Stability
An LTI system with impulse response $h[n]$ has a transfer function $H(z) = \sum h[n] z^{-n}$.
$$ Y(z) = X(z) H(z) $$

### Causality and Stability (Pole-Zero Relationship)
- **Causality**: A system is causal if the ROC of $H(z)$ is the exterior of a circle and includes infinity ($z = \infty$).
- **Stability**: An LTI system is Bounded-Input Bounded-Output (BIBO) stable if and only if the ROC includes the unit circle ($|z| = 1$). For a causal system, this means **all poles must lie strictly inside the unit circle** ($|p_k| < 1$).

## 4. Discrete Fourier Transform (DFT)
The DFT computes discrete frequency samples of a finite-duration discrete-time signal.

**N-point DFT:**
$$ X[k] = \sum_{n=0}^{N-1} x[n] W_N^{kn} \quad \text{for } k=0, 1, \dots, N-1 $$
where $W_N = e^{-j 2\pi / N}$ is the twiddle factor.

**Inverse DFT (IDFT):**
$$ x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] W_N^{-kn} \quad \text{for } n=0, 1, \dots, N-1 $$

### Properties of DFT and Circular Convolution
- Multiplication of two DFTs $Y[k] = X_1[k] X_2[k]$ corresponds to the **circular convolution** of their time-domain sequences $y[n] = x_1[n] \circledast x_2[n]$.
- Circular convolution is evaluated over length $N$. To make circular convolution equivalent to linear convolution, zero-padding to length $N \ge L_1 + L_2 - 1$ is required.

## 5. Infinite Impulse Response (IIR) Filter Design
IIR filters have an infinite number of non-zero terms in their impulse response. They are often designed from continuous-time analog filters (Butterworth, Chebyshev) by mapping the s-plane to the z-plane.

### Impulse-Invariant Method
Maps the analog impulse response $h_a(t)$ to the digital impulse response $h[n] = T h_a(nT)$.
- Poles in s-plane map to $z = e^{s T}$.
- Drawback: Subject to aliasing if the analog filter is not strictly bandlimited. (Mainly used for low-pass and band-pass filters).

### Bilinear Transformation (For context, though syllabus highlights impulse-invariant)
Maps the entire $j\omega$ axis onto the unit circle via $s = \frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}}$. Avoids aliasing but introduces frequency warping.

## 6. Finite Impulse Response (FIR) Filter Design
FIR filters are inherently stable, can have exact linear phase, but require higher orders than IIR filters for the same magnitude specifications.

### Fourier Approximation (Windowing Method)
An ideal filter has a rectangular frequency response, corresponding to a sinc function impulse response $h_d[n]$ which is infinite and non-causal.
To make it finite and causal:
1. Truncate $h_d[n]$ to length $N$.
2. Shift by $(N-1)/2$.
3. Multiply by a window function $w[n]$ to reduce the Gibbs phenomenon (ripples).

$$ h[n] = h_d[n] \cdot w[n] $$

**Common Window Functions:**
- **Rectangular**: Sharpest transition, but largest sidelobes (ringing).
- **Hanning / Hamming**: Better sidelobe suppression, wider transition band.
- **Blackman**: Very good sidelobe suppression, widest transition band.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> In DFT, index $k$ represents digital frequency $\omega_k = \frac{2\pi k}{N}$. Do not confuse it with analog frequency.

> [!TIP]
> Stability of causal IIR filter: **All poles inside $|z|=1$**.
> FIR filter linear phase condition: $h[n]$ must be symmetric or anti-symmetric.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - **z-transform**: $X(z) = \sum x[n]z^{-n}$
> - **DFT**: $X[k] = \sum x[n] e^{-j 2\pi kn/N}$
> - **FIR Windowing**: $h[n] = h_{ideal}[n] \cdot w[n]$

## ✏️ Practice Problems
1. **Problem**: Find the z-transform of $x[n] = a^n u[n]$ and its ROC.
   **Answer Sketch**: $X(z) = \sum_{n=0}^{\infty} a^n z^{-n} = \sum (a/z)^n = \frac{1}{1 - az^{-1}} = \frac{z}{z-a}$. ROC: $|z| > |a|$.
2. **Problem**: A causal LTI system has transfer function $H(z) = \frac{1}{1 - 2z^{-1}}$. Is it stable?
   **Answer Sketch**: Pole is at $z=2$. Since $|2| > 1$, pole is outside unit circle. The system is unstable.
</Section 6.6: Digital Signal Processing (AEiE0606)>
