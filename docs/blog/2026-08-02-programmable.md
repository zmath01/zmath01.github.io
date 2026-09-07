# Programmable

A perspective from the history of technology. To understand the limitations of **fx-160** and its essential difference from **Bismarck's analog computer** and **modern embedded systems**, we must return to the roots of computer architecture — the **"von Neumann bottleneck"** and **"hardwired algorithms"**.

Below, we provide an in-depth analysis using **concrete mathematical examples (Simpson's integration)**, **practical code comparisons**, and **hardware architecture analysis**.

<!--more-->

---

### 1. A Concrete Mathematical Problem: Why Can't the fx-160 Perform Calculus?

Take the computation of a definite integral as an example:

$$
\int_{0}^{1} e^{-x^2} \, dx \quad (\text{no elementary antiderivative, numerical methods are required})
$$

The iteration formula for the **numerical method (Simpson's rule)** is:

$$
\int_a^b f(x) dx \approx \frac{h}{3} \left[ f(a) + f(b) + 4\sum_{i=1}^{n/2} f(x_{2i-1}) + 2\sum_{i=1}^{n/2-1} f(x_{2i}) \right]
$$

where $ h = (b-a)/n $, requiring $ n+1 $ repeated function evaluations, **accumulated** into different sums.

---

### 2. The "Achilles' Heel" of the fx-160 (Non-programmable Calculator): No Loops and No Branching

The internal architecture of the fx-160 is **hardwired sequential execution**. It has no **program counter (PC) jump instruction**, nor any **conditional branch (IF)**.

**What can only be done on the fx-160:**

1. Compute $ f(0) = 1 $ → write it on paper.
2. Compute $ f(0.1) \approx 0.990 $ → write it on paper.
3. Manually compute in your head $ 1 + 0.990 + ... $
4. Keep pressing until $ f(1) $, then multiply/divide manually at the end.

**Expressing the limitation in code (pseudocode in a human's mind, but the machine cannot execute it):**
```text
// internal logic of the fx-160 (cannot be implemented):
STORE Sum = 0
FOR i = 0 TO 100 STEP 1:   // <-- no FOR loop instruction
    Sum = Sum + f(i*0.01)  // <-- no accumulator storage register
NEXT
PRINT Sum * 0.01          // <-- cannot print/store a program
```

---

### 3. Solution on Modern Electronic Computers (Python / C): Stored Program and Looping

On a modern CPU (von Neumann architecture), code and data reside in the same memory, and loops are realized through **PC pointer auto-increment + conditional jumps**.

**Python code (runs on modern embedded Linux or a host computer):**
```python
import math

def simpson(f, a, b, n):
    if n % 2 == 1: n += 1  # must be even
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):  # <--- core: loop iteration
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)
    return total * h / 3

# invocation
result = simpson(lambda x: math.exp(-x**2), 0, 1, 100)
print(result)  # output 0.746824
```

**C code (runs on an MCU for hard real-time control):**
```c
double f(double x) { return exp(-x*x); }

double simpson(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = f(a) + f(b);
    for (int i = 1; i < n; i++) { // deterministic loop costs O(n)
        double x = a + i*h;
        sum += (i%2==0) ? 2*f(x) : 4*f(x);
    }
    return sum * h / 3.0;
}
```

---

### 4. How Do Bismarck / Hornet's Mechanical Analog Computers "Compute" Integration?

This is the most counterintuitive point: **an analog computer does not run "code" at all; it needs no loops because physical laws are themselves parallel and continuous.**

- **Principle**: In Bismarck's fire-control system, integration is implemented by a **"disk-ball-cylinder" integrator** or an **operational amplifier (Op-Amp)**.
- **Physical mapping**: The rotation angle of the input shaft represents $ f(x) $; the rotation angle of the output shaft is driven by a friction wheel, and its **angular velocity** is proportional to the input. To compute the integral $\int f(x) dx$, one only needs to accumulate the **total number of revolutions** of the output shaft.
- **Mathematical advantage**: Solving differential equations (ODEs) is **real-time**. When the shell is fired, changes in wind speed are directly transmitted through gears to alter the gun's elevation angle — **no sampling period is needed, and there is no discretization error**.

**Analog "code" (a conceptual description; in reality it is physical wiring):**
```text
// on an analog computer, this is not code but circuit/gear connections:
// input: voltage signal V_in (represents acceleration)
// output: V_out = -1/(RC) * ∫ V_in dt
// the integrator is implemented by charge accumulation in a capacitor; this is continuous-time behavior.
```

---

### 5. In-depth Comparison Table: From the fx-160 to Modern Embedded Systems (Iowa)

| Dimension | **fx-160 (non-programmable digital)** | **Bismarck / Hornet (analog mechanical)** | **Iowa (modern embedded digital)** |
| :--- | :--- | :--- | :--- |
| **Computation method** | Manual step-by-step key presses, no stored program | **Continuous physical simulation** (charge / gear rotation) | **Discrete iteration** (von Neumann looping) |
| **Solving integrals** | **Cannot be solved automatically**. Only point-by-point computation, with manual summation by a human. | **Solved in real time**. Physical components naturally perform integration (integrator). | **Solved in software**. Runs the `for` loop algorithm above. |
| **Real-time performance** | N/A (depends on the human brain, seconds to minutes) | **Hard real-time (nanosecond physical response)** | Hard real-time (MCU, <1ms) or non-real-time (Linux, >10ms) |
| **Looping / iteration** | **None**. No `GOTO` or `LOOP` instruction. | **None**. Physical laws are parallel and need no "loop". | **Yes**. Program counter (PC) jumps implement iteration. |
| **Precision and noise** | Extremely high (digital BCD precision, ~10 digits) | Extremely low (affected by gear tolerance, temperature, friction, ~2-3 significant digits) | Extremely high (double-precision floating point, but with accumulated rounding error). |
| **Programmability** | **Zero** (firmware fixed, formulas cannot be changed) | **Zero** (hardware topology fixed unless rewired / gears replaced) | **Extremely high** (OTA software updates, can switch between MPC/PID/NN). |
| **Sources of error** | Human key-press errors | Mechanical wear, physical noise, gravitational effects | Numerical discretization error, overflow, quantization noise. |

---

### 6. Conclusion: Why the fx-160 is a "Dead End" while Modern Computers are "General-Purpose Machines"?

1. **The fx-160 is a "hardwired calculator"**: Its ROM contains only the first few terms of the Taylor expansions for trigonometric and logarithmic functions. It **has no** instruction register to store the user-written "loop-and-accumulate" instructions. It can only perform one operation at a time, after which a human takes over.
2. **The analog computer (Bismarck) is a "physical equation solver"**: It uses physics (charge flow, Newtonian mechanics) to directly map mathematical problems. Its advantages are no discretization error and an extremely high real-time ceiling; its drawbacks are **poor precision** and **weak noise immunity** (wave-induced vibration causes gear errors).
3. **Modern embedded systems (Iowa / drones) are a "hybrid"**:
   - **General-purpose CPU / GPU** (non-real-time): Runs Python/C++ for complex integration, SLAM, and LLM inference (exploiting loops and branches).
   - **Dedicated MCU** (hard real-time): Runs the C code above; although looping takes time (e.g., 100 iterations in 100μs), its deterministic scheduling (RTOS) guarantees the computation completes before the 1ms interrupt arrives.

**The most ironic truth:**

- To compute $\int e^{-x^2}dx$, **Iowa in 2025** would simply run 100 loops on its MCU, taking 0.5ms;
- whereas **Bismarck in 1941**, despite having no digital loop, had its analog integrator perform physical integration **continuously and without interruption** within the 0.5 seconds the shell was in flight.
- The fx-160 (1980) sits in between — **possessing neither the continuity of analog nor the looping capability of digital, awkwardly stuck in the position of an "advanced abacus."**
