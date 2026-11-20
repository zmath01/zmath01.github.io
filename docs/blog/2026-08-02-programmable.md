# Programmable

A perspective from the history of technology. To understand the limitations of **fx-160** and its essential difference from **an analog computer** and **modern embedded systems**, we must return to the roots of computer architecture — the **"von Neumann bottleneck"** and **"hardwired algorithms"**.

Below, we provide an in-depth analysis using **concrete mathematical examples (Simpson's integration)**, **practical code comparisons**, and **hardware architecture analysis**.

<!--more-->

---

### 1. A Concrete Mathematical Problem: Why Can't the fx-160 Perform Calculus?

Take the computation of a definite integral as an example:

$$
\int_{0}^{1} e^{-x^2} \, dx \quad \left(=\frac{\sqrt{\pi}}{2}\operatorname{erf}(1)\right)
$$

The iteration formula for the **numerical method (Simpson's rule)** is:

$$
\int_a^b f(x) dx \approx \frac{h}{3} \left[ f(a) + f(b) + 4\sum_{i=1}^{n/2} f(x_{2i-1}) + 2\sum_{i=1}^{n/2-1} f(x_{2i}) \right]
$$

Here $h=(b-a)/n$, $x_j=a+jh$, and $n$ is a positive even integer. The rule uses $n+1$ function evaluations.

---

### 2. The "Achilles' Heel" of the fx-160 (Non-programmable Calculator): No Loops and No Branching

The relevant limitation is that the calculator does not let the user store a program for the weighted sum. Internal firmware and user programmability are separate questions. A person can still tabulate $f(x_j)$, apply the alternating weights $4,2,\dots,4$, add the endpoints with weight $1$, and multiply the total by $h/3$.

---

### 3. Solution on Modern Electronic Computers (Python / C): Stored Program and Looping

A stored-program machine can automate the repeated evaluations and weighted sum. A compiled loop typically uses a counter, a conditional branch, and an accumulator.

**Python code (runs on modern embedded Linux or a host computer):**
```python
import math

def simpson(f, a, b, n):
    if n <= 0 or n % 2:
        raise ValueError("n must be a positive even integer")
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
print(f"{result:.6f}")  # 0.746824
```

**C implementation for a target with floating-point support:**
```c
#include <math.h>

double f(double x) { return exp(-x*x); }

double simpson(double a, double b, int n) {
    if (n <= 0 || n % 2 != 0) return NAN;
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

### 4. How analog computers perform integration

An analog computer represents quantities with continuous physical variables. For example, an ideal inverting electronic integrator with input $V_{\mathrm{in}}$, resistance $R$, and capacitance $C$ produces

$$
V_{\mathrm{out}}(t)=V_{\mathrm{out}}(0)-\frac{1}{RC}\int_0^t V_{\mathrm{in}}(\tau)\,d\tau.
$$

Mechanical integrators can likewise represent the integral by accumulating shaft rotation. Continuous operation avoids time-stepping error, but the physical device has finite bandwidth, limited precision, and implementation errors.

### 5. Comparison

| Dimension | Non-programmable calculator | Analog computer | Stored-program processor |
| :--- | :--- | :--- | :--- |
| Integration | User evaluates and sums terms | Physical state accumulates over time | Software evaluates a numerical quadrature |
| Error sources | Rounding and manual entry | Calibration, drift, noise, and physical limits | Quadrature error and finite-precision arithmetic |
| Timing | Depends on manual operation | Depends on bandwidth and settling time | Depends on algorithm, hardware, and scheduling |

A hard real-time deadline requires a bound on worst-case response time for the actual hardware and software. A loop count alone gives no such guarantee. The USS Iowa comparison is historical. The Navy decommissioned BB-61 in 1990, so it is not an example of a modern production MCU system. [Naval History and Heritage Command](https://www.history.navy.mil/our-collections/photography/us-navy-ships/battleships/iowa-bb-61.html)
