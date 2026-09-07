# Attractor dynamics - homogeneous projective

The operation of converting "taking limits / differentiation" into "algebraic eigenvalues" does indeed correspond geometrically to **the dynamics in Projective Space**, and **homogeneous coordinates** are the mathematical language for realizing this perspective.
More precisely: **Eigenvectors correspond to "fixed points" in projective space (Fixed Points), and the eigenvalue determines whether that fixed point is an "attractor" (attracting limit) or a "repeller".**

<!--more-->

## 1. Core mechanism: From differentiation to projective dynamics

### Step 1: Differential operator $\to$ linear operator (eigenvalue problem)
For a linear differential equation $L y = \lambda y$ (e.g., $y' = \lambda y$):

*   **Analytical perspective**: Solve the differential equation to obtain the solution $y(t) = e^{\lambda t} y(0)$.
*   **Algebraic perspective**: Find the operator $L$'s **eigenfunctions** (Eigenfunctions) and **eigenvalues** (Eigenvalues).
    *   The eigenfunction $e^{\lambda x}$ is the "basis".
    *   The eigenvalue $\lambda$ describes the "growth rate" on this basis.

### Step 2: Linear operator $\to$ projective geometry (homogeneous coordinates)
When we introduce **homogeneous coordinates** to lift the linear space into projective space:

*   **Vector $\to$ point**: A vector $v$ in the linear space becomes the point $[v]$ in projective space.
*   **Linear transformation $\to$ projective transformation**: The matrix $A$ acting on vector $v$ becomes a projective transformation acting on point $[v]$.
*   **Eigenvector $\to$ fixed point**:
    *   If $Av = \lambda v$, then in projective space $[Av] = [\lambda v] = [v]$.
    *   **Key conclusion**: **The eigenvector direction is precisely the fixed point of the projective transformation.**

### Step 3: Taking limits $\to$ attractor dynamics
The process of "taking limits" (e.g., $t \to \infty$ or iteration $n \to \infty$) manifests in projective geometry as the process of **points flowing toward fixed points**:

*   **Dominant largest eigenvalue**: If $|\lambda_1| > |\lambda_2| > \dots$, then for almost all initial vectors $v$, as we iterate $A^n v$, its direction gets closer and closer to the eigenvector direction corresponding to the largest eigenvalue $\lambda_1$.
*   **Geometric interpretation**:
    *   The fixed point corresponding to $\lambda_1$ is an **attractor (Attractor)**.
    *   Taking the limit $\lim_{n \to \infty} \frac{A^n v}{\|A^n v\|}$ is essentially searching for the **global attracting fixed point** in projective space.
    *   This explains why the Power Iteration method can find the principal eigenvalue: it is precisely simulating the dynamical flow in projective space.

## 2. The key role of homogeneous coordinates

Homogeneous Coordinates are the bridge connecting "algebraic eigenvalues" and "geometric projection":

1.  **Unifying the point at infinity**:
    Solutions to differential equations sometimes tend toward infinity (diverge). In Euclidean space this is "no solution" or "divergence", but in projective space it corresponds to the point moving onto the **line/plane at infinity** (the last component of the homogeneous coordinates is 0).

    *   For example: $y' = y \implies y = e^t$. As $t \to \infty$, $y \to \infty$.
    *   Under homogeneous coordinates $[y: 1]$, the transformation matrix is $\begin{pmatrix} e^t & 0 \\ 0 & 1 \end{pmatrix}$.
    *   After normalization, looking at the direction: $[e^t : 1] = [1 : e^{-t}] \xrightarrow{t \to \infty} [1:0]$.
    *   **Limit exists**: The limit is the point at infinity $[1:0]$ in projective space.

2.  **Linearizing nonlinear problems**:

The Möbius transformation $f(x) = \frac{ax+b}{cx+d}$ is a nonlinear rational function under ordinary coordinates, but under homogeneous coordinates it is a linear matrix multiplication $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$.

    *   Finding the limit of rational iteration $\to$ finding the matrix eigenvector direction.

Operating in projective space, the final result is often that any vector is "projected" onto the principal eigenvector direction (spectral projection).

*   **What needs to be added**: This process is essentially **dynamics (Dynamics)**.
    *   The **differential operator** defines the "velocity field".
    *   The **eigenvalue** defines the "fixed point" and its stability (attracting/repelling).
    *   **Taking the limit** is the process of the system evolving over time and finally **converging** to a stable fixed point.

**In one sentence**:
**The operation of taking limits (differentiation/iteration), in the projective space constructed by homogeneous coordinates, is equivalent to finding the "attracting fixed point" of a linear transformation (i.e., the principal eigenvector direction). The magnitude of the eigenvalue determines the speed and direction of convergence.**

This is precisely why the **Power Method**, the **PageRank algorithm**, and **Principal Component Analysis (PCA)** can all be understood geometrically as searching for the most stable direction in projective space.
