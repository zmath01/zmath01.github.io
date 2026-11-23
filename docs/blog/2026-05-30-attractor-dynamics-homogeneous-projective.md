# Attractor dynamics - homogeneous projective

The operation of converting "taking limits / differentiation" into "algebraic eigenvalues" does indeed correspond geometrically to **the dynamics in Projective Space**, and **homogeneous coordinates** are the mathematical language for realizing this perspective.
More precisely: **Eigenvectors correspond to "fixed points" in projective space (Fixed Points), and attraction depends on the relative growth of the other eigendirections.**

<!--more-->

## 1. Core mechanism: From differentiation to projective dynamics

### Step 1: Differential operator $\to$ linear operator (eigenvalue problem)
For the differentiation operator $L=d/dt$, the eigenvalue equation is $y'=\lambda y$:

*   **Analytical perspective**: Solve the differential equation to obtain the solution $y(t) = e^{\lambda t} y(0)$.
*   **Algebraic perspective**: Find the operator $L$'s **eigenfunctions** (Eigenfunctions) and **eigenvalues** (Eigenvalues).
    *   For each $\lambda$, $e^{\lambda t}$ spans the solution space of $y'=\lambda y$.
    *   The real part of $\lambda$ gives the exponential growth rate of the magnitude.

### Step 2: Linear operator $\to$ projective geometry (homogeneous coordinates)
When we introduce **homogeneous coordinates** to lift the linear space into projective space:

*   **Vector $\to$ point**: A nonzero vector $v$ in the linear space becomes the point $[v]$ in projective space.
*   **Linear transformation $\to$ projective transformation**: An invertible matrix $A$ induces a projective transformation $[v]\mapsto[Av]$. For singular $A$ this expression is defined only where $Av\ne0$.
*   **Eigenvector $\to$ fixed point**:
    *   If $Av=\lambda v$ with $\lambda\ne0$, then in projective space $[Av] = [\lambda v] = [v]$.
    *   **Key conclusion**: **The eigenvector direction is precisely the fixed point of the projective transformation.**

### Step 3: Taking limits $\to$ attractor dynamics
The process of "taking limits" (e.g., $t \to \infty$ or iteration $n \to \infty$) manifests in projective geometry as the process of **points flowing toward fixed points**:

*   **Dominant eigenvalue**: Suppose $A$ is diagonalizable and has a simple eigenvalue $\lambda_1$ of strictly largest modulus. Then $[A^n v]\to[v_1]$ if $v$ has a nonzero component along the corresponding eigenvector. For $e^{tA}$, compare the real parts of eigenvalues.
*   **Geometric interpretation**: The direction $[v_1]$ attracts those initial directions. In vector coordinates, normalized iterates may alternate in sign or rotate in phase even as their projective classes converge. The asymptotic rate depends on the ratio of the next contributing eigenvalue modulus to $\lvert\lambda_1\rvert$.

## 2. The key role of homogeneous coordinates

Homogeneous Coordinates are the bridge connecting "algebraic eigenvalues" and "geometric projection":

1.  **Unifying the point at infinity**:
    In the projective completion of affine space, a trajectory escaping to infinity converges to a point on the hyperplane at infinity if its direction converges. In homogeneous coordinates, those points have last coordinate zero.

    *   For example: $y'=y$, $y(0)=1$, gives $y=e^t$. As $t \to \infty$, $y \to \infty$.
    *   Under homogeneous coordinates $[y: 1]$, the transformation matrix is $\begin{pmatrix} e^t & 0 \\ 0 & 1 \end{pmatrix}$.
    *   After normalization, looking at the direction: $[e^t : 1] = [1 : e^{-t}] \xrightarrow{t \to \infty} [1:0]$.
    *   **Limit exists**: The limit is the point at infinity $[1:0]$ in projective space.

2.  **Linearizing nonlinear problems**:

The Möbius transformation $f(x) = \frac{ax+b}{cx+d}$ is a nonlinear rational function under ordinary coordinates, but under homogeneous coordinates it is a linear matrix multiplication $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$.

    *   When the orbit has a projective limit, continuity makes the limiting direction a fixed point. The spectral conditions above give one case of convergence.

For a Möbius map with $ad-bc\ne0$, the invertible matrix acts on the projective line. Under the same spectral conditions, iterates converge in direction. The affine limit is finite if the attracting eigenvector has a nonzero final coordinate.

The power method uses this direction convergence. PageRank applies power iteration to a stochastic matrix with teleportation under standard assumptions. PCA can use power iteration to compute leading eigendirections of a covariance matrix.
