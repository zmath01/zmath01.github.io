# Linear Theory vs Non-linear Reality -- Update

## 1. Overview

// 1. Multiscale models can be difficult to connect. Effective theories describe behavior at selected scales, and renormalization-group or limit theorems can explain how those descriptions are related.

// 2. The claim "linear = cheap" requires a triple correction:

- ( a ) Linearity alone places no useful bound on computational complexity. Particular quantum scattering problems and exact Ising partition-function problems are computationally hard.
- ( b ) Landauer’s bound applies to resetting an unbiased bit in the standard ideal memory model. The quantum no-cloning theorem concerns copying an arbitrary unknown quantum state.
- ( c ) In holographic settings, area formulas describe certain entanglement entropies. Proposals relating gravitational observables to circuit complexity remain conjectural.

// 3. Agriculture → Aristocracy → Theoretical Science:

- Transitioning from hunter-gatherer to agricultural society, whether humans on average "lived longer?" — the answer is most likely no (paleopathology: the agricultural transition is often accompanied by health deterioration; modern longevity is a 19th–20th century phenomenon).
- "Inequality expanded" has quantitative evidence (Kohler 2017: Gini rises with agriculture; plough–gender norms, Alesina et al.).
- **"Periodicity arises from the wealth gap" has a serious model: the Malthusian trap + Goodwin's predator–prey cycle**;
- The **"Great Leveler"** is Scheidel's *The Great Leveler* (war/plague/death/collapse are the only forces in history that lower the Gini);
- **Knowledge explosion vs. lifespan limit** = Jones's burden of knowledge + de Solla Price + Park 2023 disruptive decline + knowledge-graph percolation **islanding**.

Linearity vs. non-linearity in physics
Bits vs. atoms in information
Surplus leisure vs. inequality externalities in economics
Generation vs. verification of knowledge
— illustrate different kinds of cost asymmetry. The thermodynamic language is an analogy when applied to institutions, theories, or the growth of knowledge.

For the first time in 2026, AI has made "verification" — the most expensive low-entropy process — scalable, at the cost that we must now start auditing the auditors.

<!--more-->

## 2. Item-by-Item Analysis of the Core Claims

### 2.1 "More modern theories are harder to axiomatize" (Hypothesis 1)

It is not "modern = hard", but rather "multi-scale + explosion of degrees of freedom + non-linearity + singular limits + emergence".

The true structure of modern physics is Wilson's effective field theory (EFT) tower:

Theory = equivalence classes organized by scale, each layer having its own effective Lagrangian; inter-layer connection = renormalization-group flow / limit theorems (Boltzmann–Grad limit, hydrodynamic limit).

The precise statement of why QFT is hard to axiomatize:

- Formal perturbation theory is fine (Feynman diagrams, finite renormalization);
- Existence of a nontrivial four-dimensional quantum Yang–Mills theory with a positive mass gap remains a [Millennium Prize problem](https://www.claymath.org/millennium/yang-mills-the-maths-gap/).
- Constructive QFT includes low-dimensional examples such as $\phi^4_3$;
- Haag’s theorem obstructs the usual interaction picture that relates free and interacting relativistic fields by a unitary at a fixed time, under its hypotheses.

The "measurement scale expands" hypothesis concerns the range of scales that a model must connect. For example, the ratio of the illustrative lengths $10^{26}\,\text{m}$ and $10^{-35}\,\text{m}$ is $10^{61}$. These scales do not define an experimentally validated window or determine how many theories are needed. As a rigorous example of a connection between scales, Deng–Hani–Ma derive the compressible Euler and incompressible Navier–Stokes–Fourier equations for hard-sphere systems on two- and three-dimensional tori, under prescribed initial data and scaling limits, via the Boltzmann equation. The Clay Navier–Stokes problem asks a separate question about existence and smoothness. [Deng–Hani–Ma, Theorems 1–3](https://arxiv.org/abs/2503.01800v1)

### 2.2 "Quantization is linear / information propagation is cheap / GR is non-linear / moving atoms is expensive"

Yau's argument (QM linear spectral analysis vs. GR non-linear PDE), but the claim "linear = cheap" requires a triple correction:

**(1) Linear equations can still be computationally hard.** A generic pure state of $n$ qubits has $2^n$ complex amplitudes in a product basis. A specified scattering problem for scalar quantum field theory with classical sources is BQP-complete. Exact evaluation of the Ising partition function on general graphs is #P-hard for certain coupling choices. In a Transformer, $QK^T$ is bilinear in $Q$ and $K$, and softmax makes the resulting attention map nonlinear. [Jordan et al.](https://arxiv.org/abs/1703.00454) [Welsh and Merino](https://doi.org/10.1016/S0378-4371(01)00445-9)

**(2) The physical basis for "bits cheap / atoms expensive":**

- Landauer's principle: resetting one unbiased bit releases at least $k_B T\ln 2$ of heat to a bath at temperature $T$ in the standard ideal model. Actual copying and communication still have physical costs.
- The quantum no-cloning theorem rules out a universal operation that perfectly copies an arbitrary unknown quantum state. States from a known orthogonal basis can be copied. Moving a particle can be a reversible evolution and does not itself constitute a logical reset.

**(3) it-from-qubit / AdS/CFT:** "Is non-linear gravity = high computational complexity?" The duality provides concrete results about some entanglement observables and motivates conjectures about complexity. It does not establish this general equality.

- The Ryu–Takayanagi prescription relates the leading holographic entanglement entropy of a boundary region to $\operatorname{Area}(\gamma_A)/(4G_N)$ in units with $\hbar=1$, using the corresponding minimal bulk surface in a static setting. [Ryu and Takayanagi](https://arxiv.org/abs/hep-th/0603001)
- The fast-scrambling conjecture concerns how quickly initially localized information spreads. The complexity–action and complexity–volume proposals concern different quantities and are conjectural. [Sekino and Susskind](https://arxiv.org/abs/0808.2096) [Brown et al.](https://arxiv.org/abs/1509.07876)
- Circuit complexity measures state-preparation cost relative to a specified reference state and gate set.
- These proposals concern specific holographic models. Energy, transport costs, and circuit complexity are distinct quantities.

### 2.3 Agricultural Society → Aristocracy → Theoretical Mathematics and Theoretical Science (Hypothesis 2, "Negative Entropy")

Examining each point:

**(1) "Did agricultural society extend average lifespan?"** — The question mark is correct; the answer is most likely no (in the early period). Paleopathology (Cohen & Armelagos 1984; Steckel & Rose 2002): the agricultural transition is often accompanied by declining height, worsening nutrition, and rising infectious disease; Paleolithic adult life expectancy ~20–35 years, Neolithic ~ similar or lower; modern longevity is a product of 19th–20th century public health / the Industrial Revolution (+30 years in the 20th century). What agriculture brought was "total population growth (Malthusian)" rather than "extended individual lifespan."

**(2) "Inequality expanded from agricultural society"** — The direction is correct and there is quantitative evidence: Kohler et al. 2017 (Nature) "Greater post-Neolithic wealth disparities in Eurasia": the Gini coefficient of house-floor area rises with agriculture / domestication / political complexity. Alesina–Giuliano–Nunn 2013 "On the Origins of Gender Roles: Women and the Plough": plough agriculture shaped gender norms that persist to this day (women were excluded from field labor / the public sphere). Patriarchy, slavery, and caste were systematized in agricultural empires → "the double hell of lower-class women and minorities" is widely supported by historical sources.

**(3) "Theoretical science began with the few who had leisure and wealth"** — Largely holds (Veblen's leisure class; Greek axiomatization, temple / court scholars), but "hunter-gatherer societies had no theoretical science" is challenged by Graeber & Wengrow (2021, *The Dawn of Everything*): pre-agricultural societies had complex social organization (Göbekli Tepe, the Pacific Northwest, seasonal cities), and the linear narrative "agricultural revolution → hierarchy" is itself an Enlightenment myth. Sahlins's "original affluent society" (primitive peoples enjoying abundant leisure) also weakens the necessary chain "agriculture = surplus = leisure." A safer formulation: the emergence of theoretical science requires (a) surplus / leisure, (b) writing and records → "accumulation of knowledge", (c) competitive patronage networks & institutionalization; agriculture greatly raised (a)(b), but is not a sufficient condition.

**(4) "Linear theories in a hothouse cannot be applied to non-linear real production"** — This is precisely the criticism of the "linear model of innovation" in innovation economics (Bush 1945); the actual direction of the Industrial Revolution was the reverse: craftsman experience → science (thermodynamics came from the steam engine, information theory from the telegraph, computer science from the computer). Mokyr (2002, *The Gifts of Athena*) models $\Omega$ (propositional knowledge / theory) vs. $\lambda$ (prescriptive knowledge / craft): growth = the coupling of $\Omega$ and $\lambda$; the First Industrial Revolution = the Industrial Enlightenment (craftsman + literati networks), not the direct application of aristocratic theory. Allen (2009): high wages + cheap coal + craftsman trial-and-error. So "the post-1750 Industrial Revolution stemmed from craftsman experiential technology" holds (the Mokyr / Allen consensus), but "aristocratic linear theory was useless" must be softened to "at the time $\Omega$ had not yet coupled with $\lambda$." Women's exclusion from apprenticeships / schools: institutionally true (gender exclusion in guilds and universities; women still participated in domestic production and some industries) — the direction is correct, with exceptions in the details.

**(5) "Negative entropy"** — Schrödinger / Brillouin: information is negative entropy; the aristocratic class can be modeled as a dissipative structure (Prigogine): by extracting the agricultural surplus it sustains a low-entropy ordered subsystem (the leisure class), at the cost of entropy production in the rest of the system (the peasants). This analogy has a thermodynamic flavor, but as a historical causal law it is overstated.

**(6) "Periodicity arises from the wealth gap"** — There is a serious model: the Malthusian trap (population–wage negative feedback); Goodwin (1967) growth cycles (the Lotka–Volterra predator–prey oscillation of employment rate and wage share); Scheidel (2017, *The Great Leveler*): historically, Gini declines occurred almost only through war / revolution / collapse / plague (the Great Levelers) → perfectly consistent with "all relatively egalitarian periods were achieved through the Great Levelers"; Piketty $r > g$: absent shocks, the return on capital > growth → inequality rises endogenously.

**(7) "Substantive justice precedes procedural justice"** — A proposition in the history of philosophy (Rawls's classification of procedural justice); as a historical generalization it is undecided; what can be observed is only that written / procedural law (Hammurabi, Roman law) appeared during state formation, and the earliest procedural justice was precisely hierarchical (different punishments for different classes). It is recommended to downgrade this to a "conjecture yet to be argued."

### 2.4 Knowledge Explosion vs. Human Lifespan Limit; Bridge-builders vs. Pioneers

This is the part best supported by models:

**(1) de Solla Price (1963):** Scientific literature grows exponentially, roughly doubling every 10–15 years; modern paper volume ~ ×2 per generation.

**(2) Jones (2009, "The Burden of Knowledge and the 'Death of the Renaissance Man'"):** Exponential growth of the knowledge stock + constant learning speed + finite lifespan → the time to reach the frontier grows exponentially → researchers are forced to specialize, per-capita frontier output declines, the "Renaissance man" dies.

Formalized:

$$
K(t)=K_{0}e^{gt},\qquad T(t)=\frac{K(t)}{c},\qquad \frac{L}{T(t)}\longrightarrow 0
$$

Here $c$ is the individual absorption rate, $L$ is lifespan, and the number of fields one can master is $\sim L/T(t)$. "Most people only care about the part combining renormalization + DL applications, while only the wealthy and leisured mathematical physicists care about canonical measure in path integral, loop space" is precisely a portrait of individual behavior under this model (and "wealthy and leisured" echoes Veblen: pure curiosity-driven research is a luxury).

**(3) Park–Leahey–Funk (2023, Nature):** "Papers and patents are becoming less disruptive over time" — in the era of knowledge explosion, the "disruptiveness" of papers (disruption index) actually keeps declining, while consolidating / bridge-building work rises as a share. The index is based on citation patterns and does not directly measure the number of pioneers or bridge-builders. As an analogy, in the Erdős–Rényi model a giant component emerges around mean degree $1$, while full connectivity emerges around mean degree $\log n$. These are different thresholds and do not by themselves imply fragmentation of an actual knowledge graph. [Park, Leahey, and Funk](https://doi.org/10.1038/s41586-022-05543-x)

**(4) Knowledge generation and dissemination are out of sync:** The generation side (researchers × compute) is super-exponential; the dissemination side (human reading / learning) is linear; the verification side (peer review) is linear and already overloaded in 2026 (ICML 23,918 submissions, 30 emails to find one reviewer). HF's 2,226 automatically reproduced papers are the first industrial-scale expansion of the "verification side" — but it introduces a new error source (83.2%-precision-type metrics), i.e., "trading error for coverage."

### 2.5 The Verification Crisis in the AI Era (Detecting Fraud / Reproducibility)

- **Statistical model:** Let $s$ be sensitivity, $q$ specificity, and $\pi$ the prevalence of the condition being detected. When the denominator is nonzero, Bayes’ rule gives
  $\mathrm{PPV}=\frac{s\pi}{s\pi+(1-q)(1-\pi)}$.
  Precision is already PPV, so it cannot be substituted for sensitivity. A precision figure measured on one benchmark does not establish precision at a different base rate. An error detector also cannot establish intent to commit fraud.

- **Mechanistic innovation in the reproducibility challenge:** claims extraction → built-in agent reproduction → public logbook → human judges treat the logbook's self-assessment as untrustworthy → auditing the audit. This is the first step in bringing "procedural justice" into scientific verification: shifting from "trusting reviewers" to "auditable automated reproduction."

- **Case:** Two examples of how mathematical claims circulate before readers can verify them are the 2026 polynomial-map counterexamples to the Jacobian conjecture in dimension three and the manuscript proposing a complex structure on the six-sphere. Gao’s revised preprint gives explicit examples in higher dimensions and explains the tangent-sweep construction. [Gao, arXiv v2](https://arxiv.org/abs/2608.00222v2)

## 3. Deep Connections

Unifying thread: all the fragments of this article (the difficulty of axiomatization, linear / non-linear, agriculture → aristocracy → theory, knowledge explosion, verification crisis, financialization, the Great Leveler) can be compressed into a single "cost asymmetry" thread:

| Layer | Cost characteristic |
| :--- | :--- |
| Information (bits) | Resetting an unbiased bit has a thermodynamic cost in the ideal memory model. Copying and communication costs depend on the implementation. |
| Matter (atoms) | Transport costs depend on the physical process, required work, and dissipation. |
| Understanding (human brain) | Constant absorption rate, finite lifespan, scarce attention (Simon: information abundance → attention poverty) |
| Verification (peers) | Linear supply, super-exponential demand, already broken in 2026 (ICML figures) |

The imbalance among these four cost curves produces four phenomena:

1. **The difficulty of axiomatization** = "writing the laws of the matter layer as axioms of the information layer" requires cross-layer connection theorems (Hilbert VI / RG / EFT); the more layers, the harder — this is the precisification of the "measurement scale expands" hypothesis.
2. **Knowledge explosion vs. lifespan limit** = the scissors gap between the generation curve and the absorption curve (Jones's burden of knowledge; de Solla Price; Park's disruptive decline; percolation islanding).
3. **Class and theoretical science** = the social engineering of converting surplus (material abundance) into leisure (information-production time); the Malthus / Goodwin cycle = the oscillation of the distribution curve; Scheidel's Great Leveler = the only "entropy reset."
4. **The AI era** = the first expansion of the "verification curve" (automated reproduction), but at the cost of trading precision for coverage, and the new error source itself re-enters the knowledge graph — the verification crisis has not disappeared, it has merely moved up one layer (who audits the auditors).

## Appendix

- [Deng–Hani–Ma, Hilbert VI](https://arxiv.org/abs/2503.01800)
-  https://claymath.org/millennium/Navier-Stokes-Equation/
- [Gao, Jacobian counterexamples](https://arxiv.org/abs/2608.00222)
- https://vibemathed.com/problem/modular-family-of-2-tori-as-a-complex-structure-on-s6
- https://arstechnica.com/science/2026/08/peer-review-is-overwhelmed-can-it-survive-in-the-ai-era/
- https://huggingface.co/blog/icml-2026-open-reproductions
- https://simonsfoundation.org/mathematics-physical-sciences/it-from-qubit/
- https://swarma.org/?p=37614
