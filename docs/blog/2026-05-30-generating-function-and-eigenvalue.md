# Generating function and eigenvalue

1.  **Generating function $\leftrightarrow$ matrix eigenvalue**: **Correct**. The **poles (singularities)** of the generating function directly correspond to the **eigenvalues** of the transition matrix.
2.  **Fourier series orthogonality $\leftrightarrow$ Fibonacci matrix**: **Not fully applicable**. Although the Fourier transform is based on **orthogonal/unitary matrices** ($U^T = U^{-1}$), the Fibonacci transition matrix (Q-matrix) is **not** an orthogonal or unitary matrix, so we cannot directly exploit the property "transpose equals inverse" to simplify the computation.

<!--more-->

---

## 1. The essential connection between generating functions and eigenvalues

The generating function method and the matrix eigenvalue method are essentially **two different expressions of the same mathematical structure**.

### Mathematical correspondence

For the Fibonacci sequence $F_n = F_{n-1} + F_{n-2}$:

*   **Generating function perspective**:
    The generating function is $G(x) = \frac{x}{1-x-x^2}$.
    The roots of its **denominator** (i.e., poles) are obtained by solving $1-x-x^2=0$:

$$x_1 = \frac{1}{\phi}, \quad x_2 = \frac{1}{\psi}$$

    where $\phi = \frac{1+\sqrt{5}}{2}, \psi = \frac{1-\sqrt{5}}{2}$.

*   **Matrix eigenvalue perspective**:
    The transition matrix $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
    Its **characteristic equation** is $\det(M-\lambda I) = \lambda^2 - \lambda - 1 = 0$.
    The eigenvalues are:

$$\lambda_1 = \phi, \quad \lambda_2 = \psi$$

### Core conclusion

**The reciprocal of the generating function's poles equals the matrix's eigenvalues**.

$$ \lambda_i = \frac{1}{x_i} $$

*   **Reason**: The radius of convergence of the generating function $G(x) = \sum F_n x^n$ is determined by the pole closest to the origin, while the growth rate of the sequence $F_n \sim C \cdot \lambda^n$ is determined by the largest eigenvalue. Both describe the same **asymptotic behavior**.
*   **Application**: Using the Residue Theorem to perform contour integration on the generating function is, in essence, performing **spectral decomposition**, and the result is completely consistent with matrix diagonalization $M = PDP^{-1}$.

---

## 2. The misconception about "orthogonal matrices" and "Fourier series"

"The Fourier series, over the reals, has an orthogonal matrix whose transpose equals its inverse, and over the complex numbers it is a unitary matrix" — this is **correct** for the Fourier transform itself, but it **cannot be directly applied to the Fibonacci matrix**.

### Why is the Fibonacci matrix not orthogonal/unitary?

The Fibonacci transition matrix $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.

*   **Checking orthogonality**: If $M$ is an orthogonal matrix, it must satisfy $M^T M = I$.

$$ M^T M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \neq I $$

*   **Eigenvalue properties**:
    *   The eigenvalues of an **orthogonal/unitary matrix** must have modulus **1** ($|\lambda|=1$), which means the system conserves energy—it neither diverges nor decays (e.g., a rotation matrix).
    *   The Fibonacci matrix has eigenvalues $\phi \approx 1.618$ and $\psi \approx -0.618$. Since $|\phi| > 1$, the sequence is **exponentially growing**.

**Conclusion**: The Fibonacci matrix **cannot be diagonalized into an orthogonal matrix**. Its eigenvectors are **not orthogonal**.

$$ v_1 \cdot v_2 \neq 0 $$

Therefore, you **cannot** simply use $P^{-1} = P^T$ to simplify the matrix diagonalization process. You must explicitly compute $P^{-1}$.

---

## 3. When can the Fourier transform be used for recurrence sequences?

Although the Fibonacci matrix itself is not orthogonal, the **Fourier method (FFT)** is very powerful when handling **specific types** of recurrences or generating functions, but this typically occurs in the following scenarios:

1.  **Circular convolution and polynomial multiplication**:
    If the recurrence involves convolution (e.g., $c_n = \sum a_k b_{n-k}$), using the generating function $C(x) = A(x)B(x)$, the coefficients can be computed via **FFT** (an orthogonal-based discrete Fourier transform) in $O(n \log n)$ time. This exploits the diagonalization property of **circulant matrices**, not the Fibonacci matrix.

2.  **Root-of-unity filtering**:
    Using the orthogonality of the Fourier series ($\sum \omega^{kj} = 0$), one can extract specific terms from the generating function (e.g., extracting all even-indexed terms $F_{2n}$). This exploits the **unitary property of the Discrete Fourier Transform (DFT) matrix**, but it acts on the **coefficient extraction** process rather than directly diagonalizing the Fibonacci matrix.

---

## Summary comparison table

| Concept | Generating function method | Matrix eigenvalue method | Fourier/orthogonal matrix method |
| :--- | :--- | :--- | :--- |
| **Core object** | $G(x) = \frac{P(x)}{Q(x)}$ | $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ | $F_N$ (DFT matrix) |
| **Key quantity** | **Poles** (denominator roots) | **Eigenvalues** ($\lambda$) | **Roots of unity** ($e^{i 2\pi/N}$) |
| **Relation** | **Reciprocal of poles = eigenvalues** | **Eigenvalues determine growth rate** | **Orthogonal basis for expansion/convolution** |
| **Inverse matrix** | Partial fraction decomposition | $P^{-1}$ (requires explicit computation) | $U^{-1} = U^H$ (conjugate transpose) |
| **Applicability** | All linear recurrences | All linear recurrences | Only circular convolution or specific extraction |
| **Applicable to Fibonacci?** | **Yes** (perfect match) | **Yes** (perfect match) | **No** (matrix is not orthogonal) |


