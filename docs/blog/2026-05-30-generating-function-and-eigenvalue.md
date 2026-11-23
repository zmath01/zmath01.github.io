# Generating function and eigenvalue

The poles of the Fibonacci generating function are reciprocals of the transition matrix’s eigenvalues. The matrix is symmetric, so its eigenvectors can be chosen orthonormal.

<!--more-->

---

## 1. The essential connection between generating functions and eigenvalues

The generating function method and the matrix eigenvalue method are essentially **two different expressions of the same mathematical structure**.

### Mathematical correspondence

For the Fibonacci sequence $F_0=0$, $F_1=1$, with $F_n=F_{n-1}+F_{n-2}$ for $n\ge2$:

*   **Generating function perspective**:
    The generating function is $G(x) = \frac{x}{1-x-x^2}$.
    The roots of its **denominator** (i.e., poles) are obtained by solving $1-x-x^2=0$:

$$x_1 = \frac{1}{\phi}, \quad x_2 = \frac{1}{\psi}$$

    where $\phi = \frac{1+\sqrt{5}}{2}, \psi = \frac{1-\sqrt{5}}{2}$.

*   **Matrix eigenvalue perspective**:
    The transition matrix $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
    Its **characteristic polynomial** is $\det(M-\lambda I)=\lambda^2-\lambda-1$.
    The eigenvalues are:

$$\lambda_1 = \phi, \quad \lambda_2 = \psi$$

### Core conclusion

**In this example, the reciprocal of each generating-function pole is a matrix eigenvalue.** The matrix resolvent $(I-xM)^{-1}$ has poles at reciprocals of nonzero eigenvalues. Projecting it onto a scalar sequence can cancel some poles.

$$ \lambda_i = \frac{1}{x_i} $$

*   **Reason**: The radius of convergence of the generating function $G(x) = \sum F_n x^n$ is determined by the pole closest to the origin, while the growth rate of the sequence $F_n \sim C \cdot \lambda^n$ is determined by the contributing eigenvalue of largest modulus. Both describe the same **asymptotic behavior**.
*   **Application**: For this sequence, partial fractions and spectral decomposition give the same two exponential terms. Coefficients can also be extracted by Cauchy’s coefficient formula.

---

## 2. The misconception about "orthogonal matrices" and "Fourier series"

The normalized DFT matrix is unitary, so its inverse is its conjugate transpose. The Fibonacci matrix is symmetric. Its orthogonal **eigenvector matrix** provides a transpose-as-inverse shortcut for diagonalization.

### Why is the Fibonacci matrix not orthogonal/unitary?

The Fibonacci transition matrix $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.

*   **Checking orthogonality**: If $M$ is an orthogonal matrix, it must satisfy $M^T M = I$.

$$ M^T M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \neq I $$

*   **Eigenvalue properties**:
    *   The eigenvalues of an **orthogonal/unitary matrix** must have modulus **1** ($|\lambda|=1$), which means the system conserves energy—it neither diverges nor decays (e.g., a rotation matrix).
    *   The Fibonacci matrix has eigenvalues $\phi \approx 1.618$ and $\psi \approx -0.618$. Since $\lvert\phi\rvert > 1$, the sequence is **exponentially growing**.

**Conclusion**: Although $M$ itself is not orthogonal, its eigenvectors $v_1=(\phi,1)^T$ and $v_2=(\psi,1)^T$ satisfy $v_1^T v_2=\phi\psi+1=0$. Normalize them to form the orthogonal matrix $P$. Then

$$
M=P\operatorname{diag}(\phi,\psi)P^T,\qquad M^n=P\operatorname{diag}(\phi^n,\psi^n)P^T.
$$

---

## 3. When can the Fourier transform be used for recurrence sequences?

Although the Fibonacci matrix itself is not orthogonal, the **Fourier method (FFT)** is very powerful when handling **specific types** of recurrences or generating functions, but this typically occurs in the following scenarios:

1.  **Circular convolution and polynomial multiplication**:
    If the recurrence involves convolution (e.g., $c_n = \sum a_k b_{n-k}$), using the generating function $C(x) = A(x)B(x)$, the coefficients can be computed via **FFT** (an algorithm for the DFT) in $O(n \log n)$ time. The DFT diagonalizes circulant matrices. For ordinary polynomial multiplication, zero-pad to avoid wraparound.

2.  **Root-of-unity filtering**:
    Using the orthogonality of the Fourier series ($\sum_{j=0}^{N-1}\omega^{kj}=0$ for a primitive $N$-th root $\omega$ and $k$ not divisible by $N$), one can extract specific terms from the generating function (e.g., extracting all even-indexed terms $F_{2n}$). This exploits the **unitary property of the Discrete Fourier Transform (DFT) matrix**, but it acts on the **coefficient extraction** process rather than directly diagonalizing the Fibonacci matrix.

---

## Summary comparison table

| Concept | Generating function method | Matrix eigenvalue method | Fourier/orthogonal matrix method |
| :--- | :--- | :--- | :--- |
| **Core object** | $G(x) = \frac{P(x)}{Q(x)}$ | $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ | $F_N$ (DFT matrix) |
| **Key quantity** | **Poles** (denominator roots) | **Eigenvalues** ($\lambda$) | **Roots of unity** ($e^{i 2\pi/N}$) |
| **Relation** | Reciprocals of poles are contributing eigenvalues | **Eigenvalues determine growth rate** | **Orthogonal basis for expansion/convolution** |
| **Recovery step** | Partial fractions and coefficient extraction | $P^{-1}=P^T$ in this example | $U^{-1} = U^H$ (conjugate transpose) |
| **Applicability here** | Constant-coefficient linear recurrences have rational generating functions | Constant-coefficient linear recurrences have a fixed transition matrix, with Jordan form available when it is defective | Convolution and coefficient filtering |
| **Applicable to Fibonacci?** | **Yes** (perfect match) | **Yes** (perfect match) | Useful for coefficient filtering |


