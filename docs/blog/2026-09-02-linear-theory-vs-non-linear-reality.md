# Linear Theory vs Non-linear Reality -- Update

## 1. Overview

// 1. The difficulty of axiomatization = the difficulty of the number of scale layers. The analyzable scale window has expanded from $\sim 10^{2}$ to $\sim 10^{60}$, with inter-layer coupling; a single axiomatic system cannot span micro-meso-macro; **each layer needs its own effective theory (Wilson EFT) + connection theorem (Hilbert VI problem / Renormalization Group)**. "The more modern, the harder" is not a generational effect — it is the growth in the "number of distinct scale layers that must be explicitly connected."

// 2. The claim "linear = cheap" requires a triple correction:

- ( a ) Linear equations ≠ low complexity — Schrödinger is linear but its simulation is BQP-hard, and the Ising partition function is #P-hard;
- ( b ) The rigorous version of "bits cheap / atoms expensive" is **Landauer** (erasure costs $kT\ln 2$, copying is free) + the quantum no-cloning theorem;
- ( c ) it-from-qubit / AdS/CFT provides a legitimate mathematical form of "gravitational non-linearity = boundary state-preparation complexity" (Ryu–Takayanagi area = entanglement entropy; complexity = action; black hole = maximal-complexity state), **but it holds only in holographic settings**.

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
— are projections of the same "cost asymmetry" law at different scales: low-entropy structures (theory / aristocracy / order / axioms) must pay entropy elsewhere (experiment / peasants / chaos / trial-and-error) in order to be sustained;

For the first time in 2026, AI has made "verification" — the most expensive low-entropy process — scalable, at the cost that we must now start auditing the auditors.

<!--more-->

## 2. Item-by-Item Analysis of the Core Claims

### 2.1 "More modern theories are harder to axiomatize" (Hypothesis 1)

It is not "modern = hard", but rather "multi-scale + explosion of degrees of freedom + non-linearity + singular limits + emergence".

The true structure of modern physics is Wilson's effective field theory (EFT) tower:

Theory = equivalence classes organized by scale, each layer having its own effective Lagrangian; inter-layer connection = renormalization-group flow / limit theorems (Boltzmann–Grad limit, hydrodynamic limit).

The precise statement of why QFT is hard to axiomatize:

- Formal perturbation theory is fine (Feynman diagrams, finite renormalization);
- Non-perturbative existence of 4D interacting QFT = unsolved (Yang–Mills mass gap, Clay);
- Constructive QFT (Glimm–Jaffe) succeeds only in 2D/3D ($\phi^{4}_{3}$);
- Haag's theorem: interacting QFT has no Fock-space representation → "naive axiomatization" fails structurally.

The "measurement scale expands" hypothesis is upgraded to: the analyzable scale window (ratio $\ell_{\text{macro}}/\ell_{\text{micro}}$) has expanded from $\sim 10^{2}$ in the agricultural era to $\sim 10^{60}$ today ($10^{-35}\,\text{m}$ to $10^{26}\,\text{m}$), with inter-layer coupling → a single closed axiomatic system cannot span micro-meso-macro, and each level needs its own effective theory + connection theorem. Deng–Hani–Ma is precisely a rigorous connection theorem for this chain (Newton → Boltzmann → Euler/NSF); whereas the Clay NS problem is about "well-posedness of the equations themselves", pointing in the opposite direction. The two problems constitute the two ends of modern mathematical physics: where the equations come from / whether the equations are well-posed.

### 2.2 "Quantization is linear / information propagation is cheap / GR is non-linear / moving atoms is expensive"

Yau's argument (QM linear spectral analysis vs. GR non-linear PDE), but the claim "linear = cheap" requires a triple correction:

**(1) Linear equations ≠ low computational complexity.** The Schrödinger equation is linear, but the dimension of the state space grows exponentially with the number of particles: $2^{n}$ amplitudes. Simulating quantum many-body systems is BQP-hard (Jordan–Lee–Preskill); Ising / partition-function counting is #P-hard (Barahona; Vertigan–Welsh). So the "cheapest equation" describes the "most expensive system." The rise of deep learning is precisely "linear algebra winning at scale" (matrix multiplication, attention is bilinear), yet it approximates non-linear functions through composition — a linear computational skeleton + a non-linear data distribution.

**(2) The physical basis for "bits cheap / atoms expensive":**

- Landauer's principle: erasing 1 bit costs at least $kT\ln 2$ of energy; copying (propagation) has no thermodynamic lower bound.
- Quantum no-cloning theorem: an unknown quantum state cannot be perfectly copied → only "classicalized" information (macroscopic state + error correction) can be copied for free. The fiber-optic internet copies classical information; moving an atom = having to erase the original location = paying entropy. "Cheap information propagation vs. expensive matter transport" has a rigorous thermodynamic / quantum-information version.

**(3) it-from-qubit / AdS/CFT:** "Is non-linear gravity = high computational complexity?" The answer: yes, in the sense of holographic duality.

- The bulk geometry ↔ boundary entanglement structure (Ryu–Takayanagi: area = entanglement entropy; ER = EPR; tensor networks).
- Black hole = maximal-complexity state (fastest scrambler); complexity growth ~ action (complexity = action/volume, Brown–Susskind, Stanford–Susskind).
- "The heaviness and immovability of atoms (high energy / high complexity)" ↔ the circuit depth / resources required to prepare that state on the boundary;
- "Low cost of bit propagation" ↔ the propagation of entanglement / information can be accomplished on the boundary at polynomial cost. But a caveat must be added: the duality holds rigorously only in specific backgrounds (AdS-like spacetimes), not as a universal theorem.

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

**(3) Park–Leahy–Funk (2023, Nature):** "Papers and patents are becoming less disruptive over time" — in the era of knowledge explosion, the "disruptiveness" of papers (disruption index) actually keeps declining, while consolidating / bridge-building work rises as a share. → "Bridge-builders" are indeed increasing, but the relative share of "pioneers" is declining; this is two sides of the same coin as the worry about "academic islands": as network size $n$ grows, the number of edges needed to stay connected is $\sim n\log n$ (random-graph giant-component threshold), yet if bridge-building output grows only linearly with $n$, the graph necessarily fragments. This is the precise version from percolation / network science: islanding = the knowledge graph falling below the connectivity threshold.

**(4) Knowledge generation and dissemination are out of sync:** The generation side (researchers × compute) is super-exponential; the dissemination side (human reading / learning) is linear; the verification side (peer review) is linear and already overloaded in 2026 (ICML 23,918 submissions, 30 emails to find one reviewer). HF's 2,226 automatically reproduced papers are the first industrial-scale expansion of the "verification side" — but it introduces a new error source (83.2%-precision-type metrics), i.e., "trading error for coverage."

### 2.5 The Verification Crisis in the AI Era (Detecting Fraud / Reproducibility)

- **Statistical model:** Suppose the detector has precision $p=0.832$, specificity $q$ (unknown), and base rate $\mathrm{prev}$ (the proportion of papers that truly contain errors, unknown); then the positive predictive value is $\mathrm{PPV}=\frac{p\cdot\mathrm{prev}}{p\cdot\mathrm{prev}+(1-q)(1-\mathrm{prev})}$. Reporting only "83.2% precision" is insufficient for evaluation; if $\mathrm{prev}$ is low (fraud rate ~1%), then even with high $p$, many "positives" are false alarms. So the number "83.2%" itself needs context — this is a methodological critique of the article's citation.

- **Mechanistic innovation in the reproducibility challenge:** claims extraction → built-in agent reproduction → public logbook → human judges treat the logbook's self-assessment as untrustworthy → auditing the audit. This is the first step in bringing "procedural justice" into scientific verification: shifting from "trusting reviewers" to "auditable automated reproduction."

- **Case:** The Jacobian counterexample (released 2026-07-19, compiled by Gao on 07-31, no peer review) and Alpöge's manuscript on a complex structure for $S^{6}$ (108 pages, unverified) are both in a state of "claims already propagated, verification lagging behind" — the doubt ("can someone with a number-theory background check complex geometry?") is precisely the everyday form of the verification crisis. Ironically: the geometric mechanism of the Jacobian counterexample (tangent sweep, Speyer) is "pure mathematics," while the Gröbner-basis computation needed to verify it is "mechanized" — verification increasingly resembles computation, and computation increasingly resembles verification.

## 3. Deep Connections

Unifying thread: all the fragments of this article (the difficulty of axiomatization, linear / non-linear, agriculture → aristocracy → theory, knowledge explosion, verification crisis, financialization, the Great Leveler) can be compressed into a single "cost asymmetry" thread:

| Layer | Cost characteristic |
| :--- | :--- |
| Information (bits) | Fast generation, copying nearly free (Landauer only penalizes erasure), linear propagation |
| Matter (atoms) | Expensive generation, expensive movement (erasure pays entropy), expensive trial-and-error |
| Understanding (human brain) | Constant absorption rate, finite lifespan, scarce attention (Simon: information abundance → attention poverty) |
| Verification (peers) | Linear supply, super-exponential demand, already broken in 2026 (ICML figures) |

The imbalance among these four cost curves produces four phenomena:

1. **The difficulty of axiomatization** = "writing the laws of the matter layer as axioms of the information layer" requires cross-layer connection theorems (Hilbert VI / RG / EFT); the more layers, the harder — this is the precisification of the "measurement scale expands" hypothesis.
2. **Knowledge explosion vs. lifespan limit** = the scissors gap between the generation curve and the absorption curve (Jones's burden of knowledge; de Solla Price; Park's disruptive decline; percolation islanding).
3. **Class and theoretical science** = the social engineering of converting surplus (material abundance) into leisure (information-production time); the Malthus / Goodwin cycle = the oscillation of the distribution curve; Scheidel's Great Leveler = the only "entropy reset."
4. **The AI era** = the first expansion of the "verification curve" (automated reproduction), but at the cost of trading precision for coverage, and the new error source itself re-enters the knowledge graph — the verification crisis has not disappeared, it has merely moved up one layer (who audits the auditors).

## Appendix

- arXiv abs 2503.01800（Deng–Hani–Ma, Hilbert VI）
-  https://claymath.org/millennium/Navier-Stokes-Equation/
- arXiv 2608.00222（Gao, Jacobian counterexamples）
- https://vibemathed.com/problem/modular-family-of-2-tori-as-a-complex-structure-on-s6
- https://arstechnica.com/science/2026/08/peer-review-is-overwhelmed-can-it-survive-in-the-ai-era/
- https://huggingface.co/blog/icml-2026-open-reproductions
- https://simonsfoundation.org/mathematics-physical-sciences/it-from-qubit/
- https://swarma.org/?p=37614
