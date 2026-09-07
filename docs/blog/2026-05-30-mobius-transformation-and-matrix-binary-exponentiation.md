# Möbius transformation and matrix binary exponentiation

The **Möbius transformation** (Möbius Transformation), i.e., the linear fractional transformation $f(x) = \frac{ax+b}{cx+d}$, can be solved for its value after $n$ iterations in $O(\log n)$ time using **matrix binary exponentiation**.

This is not merely a special case of the Fibonacci sequence, but a direct application of **homogeneous coordinates** and **projective geometry** in algorithms. Its core principle lies in transforming the nonlinear "fractional operation" into a linear "matrix multiplication".

<!--more-->

## 1. Core principle: homogeneous coordinates and dimension lifting

The reason the Möbius transformation can be represented by a matrix is that we introduce **homogeneous coordinates**, mapping the one-dimensional scalar $x$ to the two-dimensional vector $\begin{pmatrix} x \\ 1 \end{pmatrix}$ (or, more rigorously, the projective point $[x:1]$).

### Matrix representation of the transformation

For the transformation $f(x) = \frac{ax+b}{cx+d}$, we can construct the matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
When we write $x$ as the homogeneous coordinate vector $\mathbf{v} = \begin{pmatrix} x \\ 1 \end{pmatrix}$, the matrix multiplication is as follows:

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

Once the problem is transformed into $M^n$, we can directly use the **matrix binary exponentiation** algorithm to reduce the time complexity from $O(n)$ to $O(\log n)$.

### General steps

1.  **Construct the matrix**: Extract the coefficients from the fraction $f(x) = \frac{ax+b}{cx+d}$ and build $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
2.  **Binary exponentiation**: Compute $M^n = \underbrace{M \times M \times \dots \times M}_{n \text{ times}}$.
    *   If $n$ is even, $M^n = (M^{n/2})^2$
    *   If $n$ is odd, $M^n = M \cdot M^{n-1}$
3.  **Recover the result**: Let $M^n = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$, then $f^{(n)}(x_0) = \frac{A x_0 + B}{C x_0 + D}$.

### Code example (Python)

```python
def mat_mul(A, B, mod=None):
    """2x2 matrix multiplication"""
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            if mod: C[i][j] %= mod
    return C

def mat_pow(M, n, mod=None):
    """matrix binary exponentiation"""
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
    M = [[a, b], [c, d]]
    Mn = mat_pow(M, n, mod)
    
    # recover as fraction: (A*x0 + B) / (C*x0 + D)
    A, B = Mn[0]
    C, D = Mn[1]
    
    numerator = (A * x0 + B)
    denominator = (C * x0 + D)
    
    if mod:
        # under modulo: compute the modular inverse of the denominator
        return (numerator * pow(denominator, mod - 2, mod)) % mod
    else:
        return numerator / denominator

# example: f(x) = (2x + 1) / (x + 2), iterated 10^18 times
# print(mobius_iterate(2, 1, 1, 2, 3, 10**18)) 
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

1.  **Zero denominator**: If at some step during iteration $cx+d=0$, the corresponding result in projective geometry is $\infty$. This needs to be handled specially in code (usually mapped to the matrix condition $C x_0 + D = 0$).
2.  **Modular arithmetic**: In competitive programming, computation is usually required modulo $P$. In this case, division must be converted to **multiplicative inverse** (Fermat's little theorem or the extended Euclidean algorithm), and the denominator must be coprime to the modulus.
3.  **Limits of nonlinearity**: This method applies only to **linear fractional** transformations. If the recurrence contains $x^2$, $\sin(x)$, or other nonlinear terms, a constant matrix cannot be directly constructed for acceleration (unless more complex linearization techniques or approximations are used).

## Summary

*   **Essence**: Use **homogeneous coordinates** to lift a one-dimensional nonlinear fractional transformation into a two-dimensional linear transformation.
*   **Tool**: **Matrix multiplication** corresponds to function composition, and **matrix binary exponentiation** corresponds to multiple iterations.
*   **Advantage**: Optimizes $O(n)$ simulation iteration into $O(\log n)$, capable of handling extremely large iteration counts on the order of $n=10^{18}$.
*   **Generalization**: This is a general paradigm for handling **linear recurrences** (including constant-coefficient linear recurrence sequences and linear fractional recurrences).
