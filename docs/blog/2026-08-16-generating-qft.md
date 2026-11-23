# Generating-QFT

https://pad.nixnet.services/s/38UMe7rTF

<!--more-->

# 01

## Overview

These three chapters represent foundational treatments of **Green's functions** in many-body quantum theory, each with a distinct pedagogical approach and focus:



## Fetter & Walecka: Chapter 3 — Green's Functions and Field Theory (Fermions)

Quantum Theory of Many-Particle Systems by Alexander L. Fetter and John Dirk Walecka presents a systematic, formal development of zero-temperature Green's function methods for fermionic systems.

### Core Content

**Chapter 3** is titled **"Green's Functions and Field Theory (Fermions)"** and covers:

**Pictures and Time Evolution** (Sections 6): The chapter begins by establishing the Schrödinger, interaction, and Heisenberg pictures, with detailed treatment of the adiabatic switching procedure and the **Gell-Mann and Low theorem**, which connects the interacting ground state to the non-interacting one.

**Green's Functions Definition and Properties** (Section 7): The one-particle Green's function is defined as:

$$G_{\alpha\beta}(t, t') = -i \langle \Psi_0 | T [c_\alpha(t) c_\beta^\dagger(t')] | \Psi_0 \rangle$$

Here and below $T$ denotes fermionic time ordering, including the minus sign when two fermionic operators are exchanged.

- Relation to physical observables (particle density, energy, momentum distribution)
- Free fermion Green's function as an explicit example
- The **Lehmann representation**, which expresses $G$ in terms of exact eigenstates and energies

**Diagrammatic Expansion**: The chapter develops Wick's theorem for time-ordered products and introduces Feynman diagrams for fermions. The Dyson equation relates the full Green's function to the self-energy $\Sigma$:

$$G(k,\omega)=[G_0(k,\omega)^{-1}-\Sigma(k,\omega)]^{-1}.$$

**Applications**: The electron gas is treated in Chapter 4. Screening and collective modes are developed in the later chapters on linear response.

## Mahan: Chapter 2 — Green's Functions at Zero Temperature

[Many-Particle Physics (3rd edition)](https://link.springer.com/book/10.1007/978-1-4757-5714-9) by Gerald D. Mahan takes a more computational and diagram-focused approach, emphasizing practical calculation techniques.

### Core Content

**Chapter 2** (pages 65–107) is titled **"Green's Functions at Zero Temperature"** and includes:

**Multiple Pictures and the S-Matrix** (Sections 2.1–2.2): Mahan introduces the Schrödinger, Heisenberg, and interaction pictures, then develops the **S-matrix formalism** for time evolution in the interaction picture.

**Green's Functions and Wick's Theorem** (Sections 2.3–2.4): The time-ordered Green's function is defined similarly to Fetter-Walecka, but Mahan emphasizes the connection to perturbation theory through **Wick's theorem**, which allows decomposition of time-ordered products into contractions.

**Feynman Diagrams** (Sections 2.5–2.8): This is a major focus. Mahan provides detailed **rules for constructing diagrams**, including:

- Vacuum polarization graphs
- Proper self-energy diagrams
- Vertex corrections

**Dyson's Equation** (Section 2.7): The relationship between the full and non-interacting Green's functions is developed:

$$G = G_0 + G_0 \Sigma G$$

or in compact notation: $G = [G_0^{-1} - \Sigma]^{-1}$

**Time-Loop S-Matrix and Six Green’s Functions** (Section 2.9): Mahan introduces the time-ordered, anti-time-ordered, retarded, advanced, lesser, and greater functions, which are related components used in nonequilibrium calculations. [Mahan, Chapter 2](https://link.springer.com/chapter/10.1007/978-1-4757-5714-9_2)

## Coleman: Chapter 6 — Landau Fermi-Liquid Theory

[Introduction to Many-Body Physics](https://www.cambridge.org/core/books/introduction-to-manybody-physics/B7598FC1FCEE0285F5EC767E835854C8) by Piers Coleman takes a conceptually driven approach, using Green's functions as a tool to develop **Landau's Fermi-liquid theory**.

### Core Content

**Chapter 6** is titled **"Landau Fermi-Liquid Theory"** and represents a different emphasis than the previous two texts:

**Quasiparticle Concept**: Coleman introduces the central idea that low-energy excitations of an interacting fermion system behave like weakly interacting **quasiparticles** with renormalized properties (effective mass, lifetime).

**Green's Function and Self-Energy**: The one-particle Green's function near the Fermi surface takes the form:

$$G^R(k, \omega) \approx \frac{Z_k}{\omega - \epsilon_k^* + i\Gamma_k} + G_{\text{incoh}}(k, \omega)$$

where:

- $Z_k$ is the **quasiparticle residue** (wavefunction renormalization)
- $\epsilon_k^*$ is the renormalized quasiparticle energy
- $\Gamma_k$ is the positive pole half-width in energy units. With $\hbar=1$, the amplitude decays at rate $\Gamma_k$ and its squared magnitude at rate $2\Gamma_k$.

**Comparison: Non-interacting vs. Interacting**: Coleman systematically compares the Fermi gas and Fermi liquid, showing how:

- A conventional Fermi liquid has a sharp Fermi surface. Luttinger’s theorem concerns its enclosed volume under the applicable assumptions.
- The low-temperature specific-heat coefficient $C_V/T$ is proportional to the quasiparticle density of states. For an isotropic Fermi surface at fixed density, it is proportional to $m^*$.
- Spin susceptibility is renormalized by Landau parameters

**Scattering and Collective Modes**: The chapter extends beyond single-particle properties to discuss:

- Quasiparticle scattering amplitudes
- **Collective excitations** (zero sound)
- Charge and spin response functions

**Landau Parameters**: The phenomenological Landau interaction function $f_{kk'}$ is introduced and related to microscopic Green's function calculations.

## Comparative Summary

| Aspect | Fetter & Walecka (Ch. 3) | Mahan (Ch. 2) | Coleman (Ch. 6) |
|--------|--------------------------|---------------|-----------------|
| **Primary Focus** | Formal field-theoretic foundation | Diagrammatic techniques and calculations | Physical interpretation via Fermi-liquid theory |
| **Green's Function Type** | Time-ordered (zero temperature) | Time-ordered + retarded/advanced/lesser/greater | Retarded form for the quasiparticle pole displayed above |
| **Key Formalism** | Gell-Mann & Low theorem, Lehmann representation | S-matrix, Wick's theorem, Dyson equation | Self-energy, quasiparticle residue, Landau parameters |
| **Diagrammatic Detail** | Moderate; emphasizes derivation | Extensive; detailed Feynman rules | Minimal; diagrams serve physical interpretation |
| **Physical Applications** | Electron gas, ground-state properties | General framework for later chapters | Fermi liquid, collective modes, scattering |
| **Pedagogical Style** | Rigorous, systematic | Computational, practical | Conceptual, phenomenological |



### Key Distinctions

**Fetter & Walecka** provides the most **mathematically rigorous** foundation, ideal for readers seeking a deep understanding of the formal underpinnings of many-body field theory.

**Mahan** is the most **computationally oriented**, with extensive diagrammatic rules and preparation for finite-temperature and non-equilibrium methods in later chapters.

**Coleman** emphasizes **physical intuition**, using Green's functions as a bridge to Landau's phenomenological theory, making it particularly valuable for understanding strongly correlated systems and experimental observables.

Together, these three chapters offer complementary perspectives: formal rigor (Fetter-Walecka), calculational power (Mahan), and physical insight (Coleman).

# 02

## The Propagator

In many-body physics and quantum field theory, the **propagator** (or single-particle Green's function) is a two-point correlation function. Its particle-addition and particle-removal contributions encode the single-particle excitation spectrum.

### Definition in Time Domain

The time-ordered propagator at zero temperature is defined as:

$$G(\mathbf{r}t, \mathbf{r}'t') = -i \langle \Psi_0 | T [\psi(\mathbf{r}, t) \psi^\dagger(\mathbf{r}', t')] | \Psi_0 \rangle$$

where:

- $T$ is the **time-ordering operator**
- $\psi(\mathbf{r}, t)$ and $\psi^\dagger(\mathbf{r}', t')$ are field operators in the Heisenberg picture
- $|\Psi_0\rangle$ is the many-body ground state

**Physical interpretation**: For $t > t'$, it represents the amplitude for adding a particle at $(\mathbf{r}', t')$ and removing it at $(\mathbf{r}, t)$. For $t < t'$, it describes hole propagation.

## Relation to Fourier Transform

The Fourier transform connects the **time-domain propagator** $G(t)$ to the **frequency (energy) domain propagator** $G(\omega)$, revealing the system's excitation spectrum.

### Mathematical Transformation

In a stationary and spatially translation-invariant system, use $t$ for the time difference and $\mathbf{k}$ for the momentum conjugate to the spatial difference. The time transform is:

$$G(\mathbf{k}, \omega) = \int_{-\infty}^{\infty} dt \, e^{i\omega t} \, G(\mathbf{k}, t)$$

with the inverse transform:

$$G(\mathbf{k}, t) = \int_{-\infty}^{\infty} \frac{d\omega}{2\pi} \, e^{-i\omega t} \, G(\mathbf{k}, \omega)$$

### Why Fourier Transform?

**Differential to Algebraic**: For a one-body Hamiltonian $H$, its Green’s operator satisfies a differential equation in time. For an interacting many-body Green’s function, the equation generally couples to higher correlators or includes a self-energy.

$$\left(i\frac{\partial}{\partial t} - H\right) G(t, t') = \delta(t - t')$$

Fourier transformation converts this to an **algebraic equation**:

$$(\omega - H) G(\omega) = 1 \quad \Rightarrow \quad G(\omega) = (\omega-H)^{-1}\quad\text{with the appropriate boundary prescription}$$

For a free fermion mode with energy $\epsilon_k\ne\mu$ at zero temperature:

$$G_0(\mathbf{k}, \omega) = \frac{1}{\omega - \epsilon_k + i\eta \, \text{sgn}(\epsilon_k - \mu)}$$

Here $\eta\to0^+$ implements the free time-ordered prescription. For a mode with $\epsilon_k=\mu$, its occupation determines the prescription. A retarded Green’s function uses $+i\eta$ for both occupied and unoccupied states.

## Physical Significance of Pole Structure

The **poles** of $G(\mathbf{k}, \omega)$ in the complex frequency plane carry fundamental physical information:

### Quasiparticle Properties

For an interacting system, the propagator near the Fermi surface takes the form:

$$G^R(\mathbf{k}, \omega) \approx \frac{Z_k}{\omega - \epsilon_k^* + i\Gamma_k} + G_{\text{incoh}}(\mathbf{k}, \omega)$$

where the pole structure reveals:

| Feature | Physical Meaning |
|---------|------------------|
| **Pole position** $\text{Re}[\omega_{\text{pole}}] = \epsilon_k^*$ | Renormalized quasiparticle energy |
| **Imaginary part** $\text{Im}[\omega_{\text{pole}}] = -\Gamma_k$ | Pole half-width (amplitude decay rate in $\hbar=1$ units) |
| **Residue** $Z_k$ | Quasiparticle weight (wavefunction renormalization) |

### Lehmann Representation

Using the retarded convention, the exact spectral representation is

$$
G^R(\mathbf{k},\omega)=\int_{-\infty}^{\infty}
\frac{A(\mathbf{k},\omega')}{\omega-\omega'+i0^+}\,d\omega',
\qquad
A(\mathbf{k},\omega)=-\frac{1}{\pi}\operatorname{Im}G^R(\mathbf{k},\omega).
$$

A stable excitation can give a delta peak. A finite lifetime broadens the quasiparticle peak, and incoherent excitations can contribute continua. At zero temperature, the time-ordered version instead uses $i0^+\operatorname{sgn}(\omega'-\mu)$ when frequencies are measured on an absolute energy scale.

## Key Insights

**Time domain** → Real-time dynamics, causality, transient behavior

**Frequency domain** → Energy spectrum, excitation lifetimes, resonance structure

The Fourier transform exposes the analytic structure of the correlator. Isolated poles can describe stable excitations that couple to its operators. Branch cuts can describe continua. Collective modes can appear as poles in response functions such as density–density correlators.

# 03

## Mathematical Difficulty Comparison

**Weinberg's *The Quantum Theory of Fields* is significantly more mathematically demanding** than the many-body physics texts by Fetter & Walecka, Mahan, or Coleman.

### Key Differences in Rigor and Approach

**Weinberg's Unique Difficulty**:
Steven Weinberg's three-volume series is widely regarded as the most challenging QFT textbook, not because of computational complexity, but due to its **foundational rigor**. Unlike the many-body texts, Weinberg:

- **Builds QFT from symmetry and locality**: Starts with unitary representations of the Poincaré group, then constructs fields for local interactions in relativistic scattering theory.
- **Demands mathematical maturity**: Requires comfort with advanced group theory, representation theory, and abstract algebra
- **Avoids pedagogical shortcuts**: Every index is shown, every assumption justified, with no "hand-waving"
- **Uses non-standard notation**: His conventions differ from most textbooks, making cross-referencing difficult for learners

**Many-Body Texts (Fetter-Walecka, Mahan, Coleman)**:
These books assume standard quantum mechanics and focus on **practical calculational techniques**:

- **Fetter & Walecka**: Rigorous within non-relativistic many-body theory, but uses conventional methods (canonical quantization, standard diagrammatics). Mathematically sophisticated but pedagogically systematic.
- **Mahan**: Emphasizes computational rules and diagrammatic techniques; less concerned with foundational proofs.
- **Coleman**: Prioritizes physical intuition over mathematical formality; the most accessible of the three.

### Prerequisite Gap

| Text | Mathematical Prerequisites |
|------|---------------------------|
| **Fetter & Walecka / Mahan / Coleman** | Advanced quantum mechanics, complex analysis, basic group theory (optional) |
| **Weinberg** | All of the above **plus** detailed knowledge of Lie groups, Lorentz group representations, and willingness to engage with abstract derivations spanning dozens of pages |

### Different purposes

Weinberg develops relativistic scattering theory through Poincaré symmetry, particle representations, and locality. The many-body texts emphasize calculating correlation functions and response. The difficulty depends on the reader’s background and purpose.

# 04

## Mathematical Difficulty Analysis

The topics you listed—**canonical measure in path integral loop space**, **S-matrix gauge independence**, and **renormalization**—represent a **dramatic increase in mathematical sophistication** compared to Fetter & Walecka, Mahan, or Coleman.

### Canonical Measure in Path Integral Loop Space

**Difficulty Level**: **Research-level mathematical physics**

The symbol $\mathcal{D}x$ is formal in real-time path integrals. Even for the free particle, the oscillatory kernel does not define a finite complex measure analogous to Wiener measure. Operator, oscillatory-integral, and Euclidean constructions can nevertheless make particular quantities rigorous.

**Key Challenges**:

- Requires **stochastic analysis**, **Wiener measure**, and **white noise calculus**
- Involves **loop space geometry** and **infinite-dimensional differential geometry**
- Distinguishes measure constructions in imaginary time from oscillatory-integral or operator constructions in real time

**Comparison**: Fetter & Walecka and Mahan treat path integrals as a **computational tool** with formal rules. The canonical measure problem asks *why the tool works at all*—a question requiring functional analysis at the level of constructive quantum field theory.

### S-Matrix Gauge Independence

**Difficulty Level**: **Advanced formal QFT**

Proving that physical S-matrix elements are independent of gauge-fixing parameter $\xi$ requires:

- **BRST cohomology** and **Slavnov-Taylor identities**
- An appropriate asymptotic-state construction and, when applicable, the LSZ reduction formula
- Subtle issues with **infrared divergences** in QED (photon clouds prevent rigorous LSZ)
- Non-perturbative proofs require **gauge covariance** arguments without relying on diagrammatic expansions

**Key Insight**: While Mahan introduces multiple Green's functions (retarded, advanced, lesser, greater), proving gauge independence demands showing that unphysical degrees of freedom (ghosts, longitudinal modes) **exactly cancel** in physical observables—a result that fails in naive perturbation theory and requires careful treatment of asymptotic states.

**Comparison**: Coleman discusses gauge theories phenomenologically; proving gauge independence is orders of magnitude harder, involving cohomological methods unfamiliar in condensed matter many-body theory.

### Renormalization

**Difficulty Level**: **Spans from graduate QFT to open mathematical problems**

Renormalization has **multiple layers of difficulty**:

**Perturbative Renormalization** (Graduate QFT):

- BPHZ subtraction, dimensional regularization, counterterms
- Rigorously formalized via **Costello's Batalin-Vilkovisky formalism** using $L_\infty$ algebras
- Manageable with strong calculus and complex analysis background

**Non-Perturbative Renormalization** (Research-level):

- **Constructive QFT**: Proving existence of continuum limits (e.g., the still-open four-dimensional [Yang–Mills existence and mass gap problem](https://www.claymath.org/millennium/yang-mills-the-maths-gap/))
- Requires **cluster expansions**, **renormalization group flows**, and explicit $\epsilon$-$\delta$ estimates
- The **infrared problem** in massless theories remains unsolved rigorously

**Comparison**:

| Aspect | Many-Body Texts (Fetter-Walecka, Mahan, Coleman) | Advanced Renormalization |
| :-----: | :----------------------------------------: | :-----------------: |
| **Divergences** | Regularized by physical cutoffs (lattice, bandwidth) | Must be removed via rigorous limits |
| **RG Flow** | Phenomenological (Landau parameters, scaling) | Constructive proofs with uniform bounds |
| **Mathematical Tools** | Complex analysis, diagrammatics | Functional analysis, probability theory, algebraic topology |
| **Status** | Well-defined for condensed matter systems | Open problems in 4D relativistic QFT |

### Overall Comparison

**Fetter & Walecka / Mahan / Coleman**:

- **Prerequisites**: Advanced quantum mechanics, complex variables, basic group theory
- **Goal**: Teach calculation of Green's functions, self-energies, and response functions for **physical systems**
- **Mathematical Style**: Formal but pragmatic; divergences handled by physical regularization

**Canonical Measure / Gauge Independence / Renormalization**:

- **Prerequisites**: All of the above **plus** measure theory, stochastic processes, cohomology, functional analysis
- **Goal**: Prove **consistency and existence** of the formalism itself
- **Mathematical Style**: Rigorous constructions with explicit bounds; avoids "physicist's hand-waving"

### Bottom Line

The three many-body texts are **tools for solving problems** in condensed matter physics. The topics you listed are **foundational questions** about whether the tools are mathematically well-defined. 

If mastering Fetter & Walecka Chapter 3 represents a **strong graduate education**, tackling canonical measures and constructive renormalization represents **specialized research in mathematical physics**—a domain where physicists and mathematicians collaborate to resolve issues that standard QFT textbooks (including Weinberg) treat heuristically.



# 05 

## Unified Mathematical Framework: Generating Functions

Generating functions offer several parallels with many-body physics. Source derivatives of a path integral generate correlation functions directly. Spectral representations and renormalization provide related examples with their own mathematical operations.



### 1. The Propagator as a Generating Function

In discrete math, a generating function $G(x) = \sum a_n x^n$ encodes a sequence $\{a_n\}$. In many-body physics, the **propagator** $G(k, \omega)$ encodes the **spectrum of excitations**.

**The analogy:**

*   **Discrete Math:** The coefficient $a_n$ counts the number of structures of size $n$ (e.g., trees, permutations).
*   **Physics:** The residue of a stable pole in $G^R(k,\omega)$ is its spectral weight.
*   **Fourier transform:** The frequency $\omega$ is conjugate to time. The spectral representation expresses $G^R$ as a resolvent integral, which can be compared with partial fractions when the contributing spectrum is finite.

**Lehmann representation:** For a zero-temperature retarded fermionic propagator with a discrete spectrum, let $|0,N\rangle$ be the $N$-particle ground state and $E_m^{(M)}$ the energies in the $M$-particle sector. In the absolute-energy convention,

$$
\begin{aligned}
G^R(k,\omega)
&=\sum_m
\frac{\lvert\langle m,N+1|c_k^\dagger|0,N\rangle\rvert^2}{\omega-(E_m^{(N+1)}-E_0^{(N)})+i0^+}\\
&\quad+\sum_m
\frac{\lvert\langle m,N-1|c_k|0,N\rangle\rvert^2}{\omega+(E_m^{(N-1)}-E_0^{(N)})+i0^+}.
\end{aligned}
$$

The two sums describe particle addition and removal. With finitely many poles this has the form of a partial fraction expansion. A continuum of excitation energies instead leads to the spectral integral above.

### 2. Path Integral as a Combinatorial Generator

The **path integral** $Z[J] = \int \mathcal{D}\phi \, e^{iS[\phi] + i\int J\phi}$ is the **generating functional** for all correlation functions (Green's functions).

**Combinatorial analogy:**

*   **Source Terms ($J$):** In CS, marking a specific element in a combinatorial class (e.g., a rooted tree) corresponds to differentiating the generating function with respect to a marker variable. In QFT, differentiating $Z[J]$ with respect to the source $J(x)$ generates the field insertion $\phi(x)$.

$$
\langle \phi(x_1)\dots\phi(x_n)\rangle_E =
\left.\frac{1}{Z_E[0]}\frac{\delta^n Z_E[J]}{\delta J(x_1)\dots\delta J(x_n)}\right|_{J=0}.
$$

This uses the Euclidean source convention $Z_E[J]=\int e^{-S_E+\int J\phi}\mathcal D\phi$. A real-time source term $i\int J\phi$ contributes a factor $i^{-n}$ in the corresponding differentiation formula.


*   **Feynman Diagrams:** These are literally **combinatorial graphs**. The expansion of the path integral in powers of the coupling constant generates a sum over graphs.
    *   **Wick’s theorem** supplies the contractions used to build diagrams. The **exponential formula** assembles arbitrary diagrams from connected components. In the Euclidean convention, derivatives of $W_E[J]=\log(Z_E[J]/Z_E[0])$ generate connected correlators.
    *   **Symmetry factors** arise from counting equivalent contractions. The expansion factorials combine with those multiplicities to give the inverse symmetry-group order for a diagram with its external labels fixed.

### 3. Renormalization as Recursive Decomposition

**Renormalization Group (RG)** flows can be compared to recursive coarse-graining.

**The Connection:**

*   **Coarse Graining:** Integrating out high-energy modes in physics is analogous to **aggregating states** in a Markov chain or simplifying a data structure (e.g., quad-trees, wavelet transforms).
*   **Flow Equations:** The RG flow equation (e.g., Wetterich equation) describes how the **effective action** (a generating functional for vertices) changes with scale. This is a differential equation for the generating function itself, similar to how **analytic combinatorics** uses differential equations to solve for the generating function of complex recursive structures (like trees or maps).
*   **Fixed points:** In dimensionless variables, an RG fixed point is invariant under the flow. Linearizing near a fixed point can give scaling exponents. In analytic combinatorics, the location and type of a dominant singularity can likewise give asymptotic exponents under the hypotheses of a transfer theorem.

**Constructive QFT:** The rigorous construction of measures (your previous topic) uses **cluster expansions**, which are essentially sophisticated **inclusion-exclusion principles** or **Möbius inversions** on the lattice of graph partitions.

### 4. S-Matrix and Gauge Independence

**S-matrix:** Source derivatives generate time-ordered correlators. When LSZ reduction applies, scattering amplitudes are obtained by removing the external propagators, accounting for field-strength normalization, and taking the external momenta on shell. [Tong, Interacting Fields](https://www.damtp.cam.ac.uk/user/tong/qft.html)

**Gauge Independence:**

*   **Redundancy:** Gauge symmetry represents a **redundant encoding** of information (multiple field configurations map to the same physical state).
*   **Equivalence Classes:** Physical observables depend on gauge-equivalence classes. Computing them can require gauge fixing and identities that control that choice.
*   **BRST cohomology:** In the usual perturbative construction, physical states are represented by BRST-closed states modulo BRST-exact states. Faddeev–Popov ghost fields represent the gauge-fixing determinant.

### 5. Computational Implications

The bridge between these fields is active research in **algorithmic physics** and **quantum computing**:

*   **Zero-dimensional QFT:** The path integral is an ordinary finite-dimensional integral. Its formal perturbation series counts diagrams with their symmetry weights.

### Summary Table

| Physics concept | Parallel in discrete mathematics | Operation in physics |
| :--- | :--- | :--- |
| **Propagator** $G(\omega)$ | Partial fractions for a rational generating function | Spectral sum or integral |
| **Path integral** $Z[J]$ | Multivariate generating function | Functional derivatives generate correlators |
| **Feynman diagrams** | Graphs assembled from connected components | Wick contractions generate diagrams, and the logarithm selects connected contributions |
| **Renormalization** | Recursive coarse graining | Flow of an effective action with scale |
| **Gauge symmetry** | Equivalence classes under a symmetry | BRST cohomology in the perturbative construction |
| **S-matrix** | Coefficient extraction as an analogy for source differentiation | Source differentiation followed by LSZ reduction |



# 06


## Relation to Statistical Mechanics and Statistical Field Theory

The mathematical concepts discussed (propagators, path integrals, renormalization, S-matrix) have analogues in statistical mechanics and statistical field theory. Wick rotation can relate real-time and imaginary-time quantities under appropriate analyticity assumptions. However, their **mathematical difficulty and rigor** differ significantly due to the nature of the problems (equilibrium vs. scattering, finite vs. infinite degrees of freedom).



### 1. Formal Equivalence: The Wick Rotation Bridge

For a quantum Hamiltonian $H$, imaginary-time evolution in units $\hbar=1$ is $e^{-\tau H}$. Taking the trace at $\tau=\beta$ gives the thermal partition function when the trace exists. The path-integral temporal boundary conditions are periodic for bosonic fields and antiperiodic for fermionic fields.

A system in $d$ spatial dimensions has a Euclidean description with $d$ spatial coordinates and one imaginary-time coordinate. A one-dimensional transverse-field Ising chain has a transfer-matrix correspondence with a two-dimensional classical Ising model in the appropriate limit. A positive classical probability weight need not exist for every quantum system.

### 2. Difficulty Comparison: Different Challenges

While the formulas look the same, the **mathematical hurdles** differ:

**Statistical Mechanics / SFT (Often "Easier" Rigorously):**

*   **Positive weights**: For a real classical Hamiltonian, the Boltzmann weight $e^{-\beta H}$ is nonnegative. It defines a probability measure after normalization if the partition function is finite.
*   **Infrared behavior**: Finite spatial volume can regulate long wavelengths, with zero modes requiring separate treatment in some models. Finite temperature still permits infrared singularities, for example at a thermal critical point.
*   **Constructive Success**: Many models (e.g., 2D/3D Ising, $\phi^4_3$) have been **rigorously constructed** by mathematical physicists (Glimm, Jaffe, Fröhlich) because the Euclidean measure is well-behaved.

**Quantum Field Theory (Often "Harder" Rigorously):**

*   **Oscillatory Integrals**: The real-time factor $e^{iS}$ is oscillatory. Controlled real-time constructions may use operators or oscillatory integrals, and suitable Euclidean constructions yield probability measures.
*   **UV and IR divergences**: Ultraviolet divergences in relativistic QFT require renormalization. Massless gauge bosons can cause infrared problems in scattering, such as soft photons in QED and soft gluons in perturbative QCD.
*   **Axiomatic Gaps**: The Clay problem asks for a nontrivial four-dimensional quantum Yang–Mills theory with a positive mass gap.

### 3. Renormalization: Statistical vs. Quantum

The **Renormalization Group (RG)** was born in statistical mechanics (Kadanoff, Wilson) before being imported to QFT.

*   **In Statistical Mechanics**: RG is a **coarse-graining** procedure. One integrates out short-distance fluctuations (high momentum) to find effective long-distance parameters.
    *   *Difficulty*: A critical point can govern a continuum scaling limit. Proving that such a limit exists requires control over the scaling procedure, with rigorous results available for specific models.
*   **In QFT**: Wilsonian coarse-graining applies here too. Perturbative renormalization absorbs ultraviolet divergences into counterterms. Effective theories can retain a finite cutoff.

### 4. Specific Concept Difficulty Levels

| Concept | Statistical Mechanics / SFT Difficulty | QFT Difficulty | Reason for Discrepancy |
| :--- | :--- | :--- | :--- |
| **Propagator** | **Moderate**: Defined on a lattice or continuous space with decay. Poles correspond to correlation lengths. | **High**: Requires $i\epsilon$ prescription, analytic continuation, and handling of real-time singularities. | Real-time causality vs. Euclidean decay. |
| **Path Integral** | **Moderate**: Wiener measure (Brownian motion) is rigorously defined. | **Very High**: Feynman measure is not a true measure; requires constructive methods or perturbation theory. | Oscillatory vs. Damped integrand. |
| **Renormalization** | **High (but solvable)**: Rigorous RG flows exist for 3D models. | **Extreme**: 4D constructive QFT is largely open; perturbative series are asymptotic. | Dimensionality and gauge symmetry complexities. |
| **S-Matrix** | **N/A**: SM deals with equilibrium, not scattering. | **Extreme**: Requires LSZ formalism, asymptotic completeness, and handling of infraparticles. | Scattering theory in infinite volume is uniquely hard in QFT. |
| **Gauge Independence** | **Moderate**: Lattice gauge theory provides a non-perturbative definition. | **Very High**: Continuum gauge fixing (Faddeev-Popov, BRST) is subtle; Gribov ambiguities exist. | Lattice regularization makes SM gauge theory well-defined. |

Euclidean methods can enable rigorous constructions. Recovering a corresponding real-time theory requires additional conditions, including reflection positivity in the Osterwalder–Schrader reconstruction framework. [Euclidean reconstruction](https://arxiv.org/abs/math-ph/9811002)

# 07

## Relation to PDE Classification (Elliptic, Parabolic, Hyperbolic)

Elliptic, parabolic, and hyperbolic describe properties of differential operators. For a scalar second-order equation in two variables written $Au_{xx}+Bu_{xy}+Cu_{yy}+\cdots=0$, the discriminant is $B^2-4AC$. Time-dependent evolution equations also require attention to their evolution operator and boundary conditions.

### 1. Propagator and Green's Functions

For a free field, propagators solve the Green’s function equation for the kinetic operator, with distinct boundary prescriptions. In interacting theories the full two-point function generally includes a self-energy. The free equations illustrate several PDE types:

*   **Hyperbolic (Real-Time Relativistic):** The **Klein-Gordon** and **Dirac** equations are **hyperbolic PDEs** (signature $-+++$).
    *   *Math:* Klein–Gordon is second order in time. Dirac is first order, and its components satisfy the Klein–Gordon equation in the free case.
    *   *Property:* Finite speed of propagation (causality/light cones). The retarded Green’s function is supported in the future light cone. The Feynman propagator generally has spacelike contributions.
*   **Dispersive (Real-Time Non-Relativistic):** The free **Schrödinger** equation is a unitary evolution with an imaginary coefficient multiplying the Laplacian in evolution form ($i\partial_t + \nabla^2$).
    *   *Math:* One time derivative ($i\partial_t$).
    *   *Property:* Infinite speed of propagation (instantaneous spreading of the wavefunction), yet it preserves unitarity (unlike true diffusion which dissipates).
*   **Imaginary-Time/Euclidean:** Upon Wick rotation ($t \to -i\tau$), the Schrödinger equation becomes the **Heat/Diffusion equation** (parabolic in $\tau$), and the Klein-Gordon operator becomes the **massive Euclidean Laplace operator** ($-\partial_\tau^2 - \nabla^2 + m^2$), which is **elliptic**.
    *   *Math:* No real time; all derivatives have the same sign signature ($++++$).
    *   *Property:* Ellipticity supports regularity away from singular sources. Exponential decay requires additional conditions, such as a positive mass.

### 2. Path Integral and Canonical Measure

The measure question depends on the action, dimension, and limiting procedure.

*   **Elliptic (Euclidean/QM Statistical):** The weight is $e^{-S_E}$, where $S_E$ is real and bounded below.
    *   *Measure:* Wiener measure and Brownian bridges give precise constructions in suitable quantum-mechanical examples. Interacting field theories need separate constructions and may require renormalization.
*   **Real-time (Minkowski) formulations:** The weight is $e^{iS}$, which is oscillatory.
    *   *Measure:* The free real-time path integral has no finite complex measure of the Wiener type (Cameron’s theorem). Oscillatory integrals and analytic continuation give ways to define suitable quantities when their hypotheses hold.

### 3. S-Matrix and Gauge Independence

*   **Real-time context:** The S-matrix relates incoming and outgoing asymptotic states when they exist. Nonrelativistic Schrödinger scattering also has an S-matrix.
    *   *Gauge independence:* Under the relevant perturbative assumptions, BRST identities control gauge-fixing dependence for physical states.
*   **Euclidean context:** Euclidean correlators can lead to a real-time scattering theory when reconstruction and scattering assumptions hold.

### 4. Renormalization Group (RG) Flow

Exact RG equations are functional flow equations in scale. Some truncations resemble nonlinear PDEs, with classification depending on the approximation and conventions.

*   **Polchinski and Wetterich equations:** Polchinski’s equation evolves a Wilsonian action. Wetterich’s equation evolves the effective average action $\Gamma_k$. A local-potential truncation can give a scale-evolution PDE for a function of the field. Its classification depends on the equation and the scale convention.
    *   *Time variable:* A common flow parameter is $\tau=\ln(k/k_0)$, where $k_0$ is a reference scale.
    *   *Coarse graining:* Changing the cutoff changes which fluctuations are included in the effective description.
    *   *Fixed points:* In dimensionless variables, a fixed point is a solution independent of the RG scale.

The PDE distinction helps explain differences between dispersive evolution, diffusion, and elliptic boundary-value problems. Existence of an interacting measure, reconstruction, and scattering each require additional hypotheses.
