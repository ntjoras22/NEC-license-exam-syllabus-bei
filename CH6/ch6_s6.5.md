## Section Signal and System (AEiE0605)

## 📖 1. Introduction
Signals and Systems is the mathematical foundation of communication, control, and signal processing. For the NEC exam, understanding both continuous-time and discrete-time domains, Fourier analysis, and LTI systems is essential.

## ✏️ 2. Basic Signal Definitions
A signal is a function of one or more independent variables that contains information about the behavior or nature of some phenomenon.

> [!NOTE] Definition
> **Continuous-Time (CT) Signal**: Defined at every instant of time, e.g., $x(t)$.
> **Discrete-Time (DT) Signal**: Defined only at discrete instants of time, e.g., $x[n]$.

### Standard Elementary Signals
- **Unit Step Function $u(t)$**:
  $u(t) = 1$ for $t \ge 0$, and $0$ for $t < 0$.
- **Unit Impulse Function $\delta(t)$** (Dirac delta):
  $\delta(t) = 0$ for $t \ne 0$, and $\int_{-\infty}^{\infty} \delta(t)dt = 1$.
- **Sinc Function**:
  $\text{sinc}(t) = \frac{\sin(\pi t)}{\pi t}$.
- **Signum Function**:
  $\text{sgn}(t) = 1$ for $t > 0$, $-1$ for $t < 0$, $0$ for $t = 0$.

## 3. LTI Systems and Convolution
Linear Time-Invariant (LTI) systems satisfy both linearity (superposition) and time-invariance.

### Impulse Response and Convolution
The output $y(t)$ of a CT LTI system is the convolution of its input $x(t)$ and its impulse response $h(t)$.
$$ y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau)h(t - \tau) d\tau $$

For DT systems:
$$ y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]h[n - k] $$

## 4. Continuous-Time Fourier Series (CTFS)
Used for periodic CT signals. A periodic signal $x(t)$ with period $T_0$ can be represented as:
$$ x(t) = \sum_{k=-\infty}^{\infty} c_k e^{j k \omega_0 t} $$
where $\omega_0 = 2\pi/T_0$ and the coefficients are:
$$ c_k = \frac{1}{T_0} \int_{T_0} x(t) e^{-j k \omega_0 t} dt $$

### Properties of CTFS
- **Linearity**: $a x(t) + b y(t) \leftrightarrow a c_k + b d_k$
- **Time Shifting**: $x(t - t_0) \leftrightarrow c_k e^{-j k \omega_0 t_0}$
- **Parseval's Theorem**: Average power $P = \frac{1}{T_0}\int_{T_0}|x(t)|^2 dt = \sum |c_k|^2$.

## 5. Continuous-Time Fourier Transform (CTFT)
Used for aperiodic signals.
**Analysis Equation (Forward Transform):**
$$ X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j \omega t} dt $$
**Synthesis Equation (Inverse Transform):**
$$ x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega) e^{j \omega t} d\omega $$

### Properties of CTFT
| Property | Time Domain $x(t)$ | Frequency Domain $X(\omega)$ |
| :--- | :--- | :--- |
| Linearity | $ax_1(t) + bx_2(t)$ | $aX_1(\omega) + bX_2(\omega)$ |
| Time Shift | $x(t - t_0)$ | $X(\omega)e^{-j\omega t_0}$ |
| Frequency Shift | $x(t)e^{j\omega_0 t}$ | $X(\omega - \omega_0)$ |
| Convolution | $x_1(t) * x_2(t)$ | $X_1(\omega)X_2(\omega)$ |
| Multiplication | $x_1(t)x_2(t)$ | $\frac{1}{2\pi}X_1(\omega) * X_2(\omega)$ |

## 6. Discrete-Time Fourier Series (DTFS) and Transform (DTFT)
**DTFS (For periodic DT signals with period $N$):**
$$ x[n] = \sum_{k=\langle N \rangle} a_k e^{j k \Omega_0 n} $$
$$ a_k = \frac{1}{N} \sum_{n=\langle N \rangle} x[n] e^{-j k \Omega_0 n} $$

**DTFT (For aperiodic DT signals):**
$$ X(e^{j\Omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\Omega n} $$
$$ x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\Omega}) e^{j\Omega n} d\Omega $$

*Note that $X(e^{j\Omega})$ is always periodic with period $2\pi$.*

## 7. Energy and Power Spectral Densities
- **Energy Spectral Density (ESD)**: For energy signals. $E = \int |x(t)|^2 dt = \frac{1}{2\pi}\int |X(\omega)|^2 d\omega$. ESD $\Psi(\omega) = |X(\omega)|^2$.
- **Power Spectral Density (PSD)**: For power signals (e.g., periodic or random). $S_{xx}(\omega)$ is the Fourier transform of the autocorrelation function $R_{xx}(\tau)$.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not confuse $x(t) * h(t)$ (convolution) with normal multiplication. Convolution in the time domain equates to multiplication in the frequency domain.

> [!TIP]
> Remember that the Fourier transform of an impulse $\delta(t)$ is $1$, and the FT of a constant $1$ is $2\pi \delta(\omega)$.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - **Convolution**: $y(t) = \int x(\tau)h(t-\tau)d\tau$
> - **CTFT of $e^{-at}u(t)$**: $\frac{1}{a + j\omega}$
> - **Parseval's Theorem**: Energy in time domain equals energy in frequency domain.

## ✏️ Practice Problems
1. **Problem**: Find the CTFT of $x(t) = e^{-at}u(t)$ for $a > 0$.
   **Answer Sketch**: $X(\omega) = \int_{0}^{\infty} e^{-at}e^{-j\omega t}dt = \int_0^\infty e^{-(a+j\omega)t}dt = \frac{1}{a+j\omega}$.
2. **Problem**: A system has impulse response $h(t) = u(t)$ and input $x(t) = \delta(t) + \delta(t-1)$. Find $y(t)$.
   **Answer Sketch**: $y(t) = x(t)*h(t) = \delta(t)*u(t) + \delta(t-1)*u(t) = u(t) + u(t-1)$.
</Section 6.5: Signal and System (AEiE0605)>
