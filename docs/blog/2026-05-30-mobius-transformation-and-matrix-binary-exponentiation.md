# Möbius transformation and matrix binary exponentiation

The **Möbius transformation** (Möbius Transformation), i.e., the linear fractional transformation $f(x) = \frac{ax+b}{cx+d}$, can be solved for its value after $n$ iterations in $O(\log n)$ matrix multiplications using **matrix binary exponentiation**.

This is not merely a special case of the Fibonacci sequence, but a direct application of **homogeneous coordinates** and **projective geometry** in algorithms. Its core principle lies in transforming the nonlinear "fractional operation" into a linear "matrix multiplication".

<!--more-->

## 1. Core principle: homogeneous coordinates and dimension lifting

The reason the Möbius transformation can be represented by a matrix is that we introduce **homogeneous coordinates**, mapping the one-dimensional scalar $x$ to the two-dimensional vector $\begin{pmatrix} x \\ 1 \end{pmatrix}$ (or, more rigorously, the projective point $[x:1]$).

### Matrix representation of the transformation

For the transformation $f(x) = \frac{ax+b}{cx+d}$, we can construct the matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
The determinant must satisfy $ad-bc\ne0$. When we write $x$ as the homogeneous coordinate vector $\mathbf{v} = \begin{pmatrix} x \\ 1 \end{pmatrix}$, the matrix multiplication is as follows:

$$
M \mathbf{v} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ 1 \end{pmatrix} = \begin{pmatrix} ax+b \\ cx+d \end{pmatrix}
$$

In projective geometry, the vector $\begin{pmatrix} X \\ Y \end{pmatrix}$ is equivalent to the scalar $X/Y$ (as long as $Y \neq 0$). Therefore, converting the above result back to a scalar gives exactly:

$$
\frac{ax+b}{cx+d}
$$

**Key points**:

*   **Nonlinear $\to$ linear**: The originally complicated fractional iteration $f(f(x))$ becomes the simple matrix multiplication $M \times (M \times \mathbf{v}) = M^2 \mathbf{v}$ under homogeneous coordinates.
*   **Associativity**: Matrix multiplication is associative, so $n$ iterations are equivalent to computing $M^n$.

## 2. Algorithm implementation: matrix binary exponentiation

Once the problem is transformed into $M^n$, we can directly use the **matrix binary exponentiation** algorithm to reduce the number of matrix multiplications from linear to logarithmic in $n$.

### General steps

1.  **Construct the matrix**: Extract the coefficients from the fraction $f(x) = \frac{ax+b}{cx+d}$ and build $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
2.  **Binary exponentiation**: Compute $M^n = \underbrace{M \times M \times \dots \times M}_{n \text{ times}}$.
    *   If $n$ is even, $M^n = (M^{n/2})^2$
    *   If $n$ is odd, $M^n = M \cdot M^{n-1}$
3.  **Recover the result**: Let $M^n = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$, then $f^{(n)}(x_0) = \frac{A x_0 + B}{C x_0 + D}$.

### Code example (Python)

```python
from fractions import Fraction
from math import gcd

def mat_mul(A, B, mod=None):
    """2x2 matrix multiplication"""
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            if mod is not None:
                C[i][j] %= mod
    return C

def mat_pow(M, n, mod=None):
    """matrix binary exponentiation"""
    if n < 0:
        raise ValueError("n must be nonnegative")
    if mod is not None and mod < 2:
        raise ValueError("mod must be at least 2")
    res = [[1, 0], [0, 1]]  # identity matrix
    base = M
    while n > 0:
        if n % 2 == 1:
            res = mat_mul(res, base, mod)
        base = mat_mul(base, base, mod)
        n //= 2
    return res

def mobius_iterate(a, b, c, d, x0, n, mod=None):
    """
    compute f^n(x0), where f(x) = (ax+b)/(cx+d)
    """
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("a Möbius transformation needs an invertible matrix")
    if mod is not None and gcd(determinant, mod) != 1:
        raise ValueError("the determinant must be invertible modulo mod")
    M = [[a, b], [c, d]]
    Mn = mat_pow(M, n, mod)
    
    # recover as fraction: (A*x0 + B) / (C*x0 + D)
    A, B = Mn[0]
    C, D = Mn[1]
    
    numerator = (A * x0 + B)
    denominator = (C * x0 + D)
    
    if mod is not None:
        return (numerator * pow(denominator, -1, mod)) % mod
    if denominator == 0:
        return None  # The projective point at infinity.
    return Fraction(numerator, denominator)

print(mobius_iterate(2, 1, 1, 2, 3, 5))
print(mobius_iterate(2, 1, 1, 2, 3, 10**18, 101))
```

## 3. Scope of application and extensions

This method is not limited to simple fractions; it applies to all **linear fractional recurrences**.

| Scenario | Recurrence formula | Corresponding matrix $M$ | Remarks |
| :--- | :--- | :--- | :--- |
| **Fibonacci ratio** | $x_{n} = 1 + \frac{1}{x_{n-1}}$ | $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ | Continued fraction form, converges to the golden ratio |
| **General Möbius** | $x_{n} = \frac{ax_{n-1}+b}{cx_{n-1}+d}$ | $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ | Standard form |
| **Recurrence with constant term** | $x_{n} = \frac{a x_{n-1} + b}{c x_{n-1} + d} + k$ | Combine by finding common denominator first | Requires algebraic manipulation to reduce to standard fractional form |
| **Composite transformation** | $f(g(x))$ | $M_f \times M_g$ | Matrix multiplication order corresponds to function composition order |

### Notes

1.  **Zero denominator**: If at some step during iteration $cx+d=0$, the corresponding result in projective geometry is $\infty$. The matrix computation can pass through infinity. The code returns `None` when the final denominator is zero over the rationals.
2.  **Modular arithmetic**: In competitive programming, computation is usually required modulo $P$. In this case, division must be converted to **multiplicative inverse** and the denominator must be coprime to the modulus. In Python 3.8+, `pow(denominator, -1, mod)` raises `ValueError` when the inverse does not exist. The determinant must also be coprime to the modulus for the matrix to be invertible.
3.  **Limits of nonlinearity**: This method applies only to **linear fractional** transformations. If the recurrence contains $x^2$, $\sin(x)$, or other nonlinear terms, a constant matrix cannot be directly constructed for acceleration (unless more complex linearization techniques or approximations are used).

## Summary

*   **Essence**: Use **homogeneous coordinates** to lift a one-dimensional nonlinear fractional transformation into a two-dimensional linear transformation.
*   **Tool**: **Matrix multiplication** corresponds to function composition, and **matrix binary exponentiation** corresponds to multiple iterations.
*   **Advantage**: The number of matrix multiplications is logarithmic. Without a modulus, exact integers can grow to $O(n)$ digits for fixed integer coefficients, so the same bound does not apply to bit complexity or output size.
*   **Generalization**: This is a general paradigm for handling **linear recurrences** (including constant-coefficient linear recurrence sequences and linear fractional recurrences).
