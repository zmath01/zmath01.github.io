# Generating function and discrete transformations

An ordinary generating function and the unilateral Z-transform of the same sequence use reciprocal variables, $x=z^{-1}$. The generating function can be treated as a formal series. The Z-transform and its evaluation on the unit circle require convergence.

<!--more-->

## 1. Core correspondence: from time domain to complex frequency domain

In signal processing, the process of transforming a discrete sequence $a_n$ (time domain) into the complex frequency domain is identical in form for the unilateral transform to the process of constructing a generating function in combinatorics.

| Transform name | Mathematical definition | Variable substitution relation | Physical/mathematical meaning |
| :--- | :--- | :--- | :--- |
| **Ordinary generating function (OGF)** | $A(x) = \sum_{n=0}^{\infty} a_n x^n$ | $x = z^{-1}$ | Z-transform of a discrete sequence (reciprocal variable) |
| **Z-transform (Z-Transform)** | $X(z) = \sum_{n=0}^{\infty} x[n] z^{-n}$ | $z = x^{-1}$ | Discrete version of the Laplace transform |
| **Laplace transform** | $F(s) = \int_{0}^{\infty} f(t) e^{-st} dt$ | $z = e^{sT}$ for a sampled impulse train | Complex frequency-domain analysis of continuous signals |
| **Fourier transform (DTFT)** | $X(e^{i\omega}) = \sum x[n] e^{-i\omega n}$ | $z = e^{i\omega}$ | Special case of the Z-transform on the unit circle |

*   **Discrete vs continuous**: Generating functions deal with discrete sequences $\{a_n\}$ (corresponding to discrete signals), whereas Laplace/Fourier typically handle continuous functions $f(t)$ (corresponding to continuous signals).
*   **Summation vs integration**: Generating functions use series summation $\sum$, while Laplace uses integration $\int$. This is the fundamental distinction between discrete and continuous.

## 2. Detailed correspondence analysis

### Generating function $\leftrightarrow$ Z-transform (discrete Laplace)

*   **Unified form**:
    *   Generating function: $A(x) = a_0 + a_1 x + a_2 x^2 + \dots$
    *   Z-transform: $X(z) = x[0] + x[1] z^{-1} + x[2] z^{-2} + \dots$
    *   With $x=z^{-1}$ and $a_n=x[n]$, the analytic functions agree on the corresponding region of convergence. Writing $z=e^{sT}$ gives $\sum_{n\ge0}a_n e^{-snT}$, the Laplace transform of the impulse train $\sum_{n\ge0}a_n\delta(t-nT)$. The latter depends on the samples.
*   **Physical meaning**:
    *   In control theory, the region of convergence of the impulse-response Z-transform determines BIBO stability. It must contain the unit circle. For a causal rational system the poles must lie inside that circle.
    *   In combinatorics, the location of the **singularities** of the generating function $A(x)$ determines the **asymptotic growth rate** of the sequence $a_n$ (e.g., $a_n\sim C R^{-n}$ for a suitable unique dominant simple pole at $x=R$).
    *   **Conclusion**: Analyzing the singularities of a generating function is, in essence, performing pole analysis of a discrete system.

### Generating function $\leftrightarrow$ Fourier transform

*   **The perspective on the unit circle**:
    *   If we set $x = e^{-i\omega}$ in the generating function $A(x)$ (i.e., evaluate it on the unit circle of the complex plane), the generating function gives the **discrete-time Fourier transform (DTFT)** of the zero-extended sequence when the series converges there. Absolute summability is sufficient.
    *   $A(e^{-i\omega}) = \sum a_n e^{-i n \omega}$.
*   **Applications**:
    *   In signal processing, this is used to analyze the **frequency components** of a signal.
    *   In combinatorics/number theory, this corresponds to using **roots of unity** to extract specific terms of a sequence (e.g., extracting the sum of every $k$-th term), which follows from summing powers of roots of unity. The FFT is a family of algorithms for computing the DFT.



## 3. Mapping of operational properties

This correspondence is not limited to definitions; the operational properties are also completely isomorphic:

| Operation | Generating function (combinatorics) | Z/Fourier transform (signal processing) | Intuitive explanation |
| :--- | :--- | :--- | :--- |
| **Convolution** | $C(x) = A(x) \cdot B(x)$ $\implies c_n = \sum a_k b_{n-k}$ | Time-domain convolution $\leftrightarrow$ frequency-domain multiplication | Polynomial multiplication is convolution |
| **Shift/delay** | $x^k A(x)$ (coefficients shifted right) | $z^{-k} X(z)$ (time delay) | Multiplying by a power corresponds to a time shift |
| **Differentiation** | $x A'(x)$ (yields $n \cdot a_n$) | $-zX^\prime(z)$ for the Z-transform, or $i\frac{d}{d\omega}X(e^{i\omega})$ when termwise differentiation is valid | Weighted operation |
| **Initial value** | $A(0) = a_0$ | Initial value theorem $\lim_{z\to\infty} X(z) = x[0]$ | Determines the starting value |

## 4. Why is this perspective useful?

Viewing generating functions as "discrete Fourier/Laplace transforms" is more than an analogy; it provides powerful problem-solving tools:

1.  **Asymptotic analysis (Asymptotics)**:
    Using complex analysis (analytic combinatorics), by studying the **distribution of singularities** of the generating function in the complex plane (similar to pole analysis in control theory), one can directly obtain the growth behavior of $a_n$ as $n \to \infty$. This is an advanced method for analyzing algorithmic complexity.

2.  **Fast algorithms (FFT)**:
    Polynomial multiplication (multiplying generating functions) is naively $O(n^2)$, but using the viewpoint that "a generating function is a frequency-domain signal," **FFT** can accomplish it in $O(n \log n)$ time. This is essentially multiplying first in the "frequency domain" (point-value representation), then inverse-transforming back to the "time domain" (coefficient representation).

3.  **Solving for closed-form formulas**:
    Using partial fraction decomposition, a complex generating function is broken down into a polynomial plus terms of the form $C/(1-ax)^j$, which corresponds to decomposing a system into a parallel connection of first-order subsystems in signal processing.

## Summary

*   The **generating function** is the **Z-transform** of a discrete sequence (with different variable notation, $x$ vs $z^{-1}$).
*   The **Z-transform** is the discrete version of the **Laplace transform**.
*   On the unit circle, it gives the DTFT when the transform converges there.

**Essence**: They all transform the complex convolution operation in the **time/sequence domain** into a simple multiplication operation in the **complex frequency/transform domain**. Combinatorialists and signal engineers are essentially describing the same mathematical structure in different languages.

