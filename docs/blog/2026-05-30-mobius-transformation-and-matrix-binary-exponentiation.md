# Möbius transformation and matrix binary exponentiation

**莫比乌斯变换（Möbius Transformation）**，即分式线性变换 $f(x) = \frac{ax+b}{cx+d}$，可以通过**矩阵快速幂**在 $O(\log n)$ 时间内求解 $n$ 次迭代后的结果。

这不仅仅是斐波那契数列的特例，而是 **齐次坐标 ( Homogeneous Coordinates )** 与 **射影几何 ( Projective Geometry )** 在算法中的直接应用。其核心原理在于将非线性的“分式运算”转化为线性的“矩阵乘法”。

<!--more-->

## 1. 核心原理：齐次坐标与升维

莫比乌斯变换之所以能用矩阵表示，是因为引入了**齐次坐标**，将一维标量 $x$ 映射为二维向量 $\begin{pmatrix} x \\ 1 \end{pmatrix}$（或更严谨的射影点 $[x:1]$）。

### 变换的矩阵化
对于变换 $f(x) = \frac{ax+b}{cx+d}$，我们可以构造矩阵 $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$。
当我们将 $x$ 写成齐次坐标向量 $\mathbf{v} = \begin{pmatrix} x \\ 1 \end{pmatrix}$ 时，矩阵乘法如下：

$$
M \mathbf{v} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ 1 \end{pmatrix} = \begin{pmatrix} ax+b \\ cx+d \end{pmatrix}
$$

在射影几何中，向量 $\begin{pmatrix} X \\ Y \end{pmatrix}$ 等价于标量 $X/Y$（只要 $Y \neq 0$）。因此，上述结果还原回标量正是：

$$
\frac{ax+b}{cx+d}
$$

**关键点**：

*   **非线性 $\to$ 线性**：原本复杂的分式迭代 $f(f(x))$ 在齐次坐标下变成了简单的矩阵乘法 $M \times (M \times \mathbf{v}) = M^2 \mathbf{v}$。
*   **结合律**：矩阵乘法满足结合律，因此 $n$ 次迭代等价于计算 $M^n$。

## 2. 算法实现：矩阵快速幂

一旦将问题转化为 $M^n$，就可以直接使用**矩阵快速幂**算法，将时间复杂度从 $O(n)$ 降低到 $O(\log n)$。

### 通用步骤

1.  **构造矩阵**：根据分式 $f(x) = \frac{ax+b}{cx+d}$ 提取系数，构建 $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$。
2.  **快速幂计算**：计算 $M^n = \underbrace{M \times M \times \dots \times M}_{n \text{ times}}$。
    *   若 $n$ 为偶数，$M^n = (M^{n/2})^2$
    *   若 $n$ 为奇数，$M^n = M \cdot M^{n-1}$
3.  **还原结果**：设 $M^n = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$，则 $f^{(n)}(x_0) = \frac{A x_0 + B}{C x_0 + D}$。

### 代码示例 (Python)

```python
def mat_mul(A, B, mod=None):
    """2x2 矩阵乘法"""
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            if mod: C[i][j] %= mod
    return C

def mat_pow(M, n, mod=None):
    """矩阵快速幂"""
    res = [[1, 0], [0, 1]]  # 单位矩阵
    base = M
    while n > 0:
        if n % 2 == 1:
            res = mat_mul(res, base, mod)
        base = mat_mul(base, base, mod)
        n //= 2
    return res

def mobius_iterate(a, b, c, d, x0, n, mod=None):
    """
    计算 f^n(x0), 其中 f(x) = (ax+b)/(cx+d)
    """
    M = [[a, b], [c, d]]
    Mn = mat_pow(M, n, mod)
    
    # 还原为分式: (A*x0 + B) / (C*x0 + D)
    A, B = Mn[0]
    C, D = Mn[1]
    
    numerator = (A * x0 + B)
    denominator = (C * x0 + D)
    
    if mod:
        # 模意义下需计算分母的逆元
        return (numerator * pow(denominator, mod - 2, mod)) % mod
    else:
        return numerator / denominator

# 示例：f(x) = (2x + 1) / (x + 2), 迭代 10^18 次
# print(mobius_iterate(2, 1, 1, 2, 3, 10**18)) 
```

## 3. 适用范围与扩展

这种方法不仅限于简单的分式，它适用于所有**线性分式递推**（Linear Fractional Recurrences）。

| 场景 | 递推公式 | 对应矩阵 $M$ | 备注 |
| :--- | :--- | :--- | :--- |
| **斐波那契比值** | $x_{n} = 1 + \frac{1}{x_{n-1}}$ | $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ | 连分数形式，收敛于黄金分割比 |
| **一般莫比乌斯** | $x_{n} = \frac{ax_{n-1}+b}{cx_{n-1}+d}$ | $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ | 标准形式 |
| **带常数项递推** | $x_{n} = \frac{a x_{n-1} + b}{c x_{n-1} + d} + k$ | 需先通分合并 | 需代数变形化为标准分式 |
| **复合变换** | $f(g(x))$ | $M_f \times M_g$ | 矩阵乘法顺序对应函数复合顺序 |

### 注意事项

1.  **分母为零**：若迭代过程中某一步 $cx+d=0$，在射影几何中对应结果为 $\infty$。在代码实现中需特判（通常映射为矩阵的 $C x_0 + D = 0$）。
2.  **模运算**：在算法竞赛中，通常要求在模 $P$ 意义下计算。此时除法需转换为**乘法逆元**（费马小定理或扩展欧几里得算法），且需保证分母与模数互质。
3.  **非线性的界限**：此方法仅适用于**分式线性**变换。如果递推式中包含 $x^2$、$\sin(x)$ 或其他非线性项，则无法直接构造常数矩阵进行加速（除非使用更复杂的线性化技巧或近似）。

## 总结

*   **本质**：利用**齐次坐标**将一维非线性分式变换提升为二维线性变换。
*   **工具**：**矩阵乘法**对应函数复合，**矩阵快速幂**对应多次迭代。
*   **优势**：将 $O(n)$ 的模拟迭代优化为 $O(\log n)$，能够处理 $n=10^{18}$ 级别的超大迭代次数。
*   **推广**：这是处理**线性递推**（包括常系数线性递推数列、分式线性递推）的通用范式。

