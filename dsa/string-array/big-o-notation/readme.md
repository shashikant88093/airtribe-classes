## Course Structure & Expectations

* **Schedule & Duration:** 32-week program, 2 classes/week (Saturdays & Sundays, 11:00–13:00).
* **Active Participation Required:** Join by 11:05 (11:07 grace cutoff). Use a laptop with your camera on. Expect live dry runs, interactive chat responses, and unmuting to explain logic. Material is not repeated for latecomers.
* **Mandatory Assignments:** Structured into bands (**Easy**, **Easy-to-Medium**, **Medium**, **Hard**) with 20–50 questions per class across practice and homework. These are central to the course, not optional side work.

---

## DSA in the Tech Market

DSA is currently an **elimination criterion** rather than a selection criterion—failing to demonstrate competence stops the interview process immediately. Companies prioritize DSA to filter for engineers who can think reliably, write clean code, and merge pull requests without extensive training.

### Company Tiers & Career Trade-Offs

* **Service-Based (TCS, Infosys, Wipro):** Less DSA-heavy.
* **Funded Startups (Flipkart, PhonePe, CRED):** Multiple heavy DSA rounds + practical execution. Expect high workload, fast learning, and high compensation.
* **Top Tech (Google, Amazon, Microsoft):** Standard pattern involves 2–3 DSA rounds followed by Low-Level Design (LLD) and core principles. Better work-life balance compared to early startups.
* **Off-Campus Strategy:** Proactively target early-stage startups, build practical project experience, and leverage direct founder/HR outreach to compensate for lacking campus pipelines.

---

## Modern Learning Strategy & AI

### 1. Pattern Recognition Over Problem Count

Do not collect 50 isolated solutions. Deeply understand a single underlying algorithmic pattern and apply it across different problems ("Question 1, 2, and 3: same approach").

### 2. Momentum > Motivation

Motivation starts the process; momentum sustains it. Build a daily habit of **1 to 1.5 hours of high-quality, focused practice** rather than sporadic, high-volume sessions. LeetCode Premium is optional—its primary value lies in company tagging and frequency filtering, not learning fundamentals.

### 3. Using ChatGPT Correctly

Never paste a problem statement and copy the generated code—this creates a false sense of progress. Use AI as a **thinking partner and debugger**:

* **Do:** Explain your logic, ask for hints, request failing test cases, or have it validate your self-completed dry run.
* **Don't:** Ask for the full solution when your code fails. Always dry-run logic manually first to spot missing base cases or edge conditions.

---

## Time Complexity & Big O Fundamentals

Time complexity evaluates how operation counts scale as input size $n$ grows. Evaluate based on **worst-case behavior** (similar to P99 latency guarantees in engineering), ignoring stopwatch time due to varying hardware.

### Core Mathematical Formulas

* **Sum of first $n$ integers:** $\frac{n(n + 1)}{2}$
* **Range count in $[L, R]$:** $R - L + 1$
* **Halving / Doubling steps:** Taking an integer $n$ and dividing by $2$ until reaching $1$ requires $\approx \log_2(n)$ steps.

### The Algebraic Simplification Rule

**Always expand variable expressions first, then drop constants and lower-order terms.**

* **Constants don't matter:** $1000n$, $10n$, and $\frac{n + 1}{2}$ all simplify to $O(n)$.
* **Expand before simplifying:** $n(n + 1)$ must be expanded to $n^2 + n$ before reducing to $O(n^2)$. Do not mistakenly drop variables like constants.

---

## Common Complexity Patterns

To correctly analyze nested loops, build a quick tracking table mapping **outer-loop values to inner-loop iteration counts**, sum the total work, and apply asymptotic reduction.

| Pattern | Big O Notation | Example / Root Cause |
| --- | --- | --- |
| **Constant** | $O(1)$ | Fixed operations (e.g., a loop that always runs 100 times). |
| **Linear** | $O(n)$ | Single traversal from $1$ to $n$. |
| **Logarithmic** | $O(\log n)$ | Loop variable repeatedly halved ($n \rightarrow \frac{n}{2} \rightarrow 1$) or doubled. |
| **Linearithmic** | $O(n \log n)$ | Outer loop runs $n$ times; inner loop halves/doubles. |
| **Quadratic** | $O(n^2)$ | Dependent nested loops where inner runs $\approx n$ times per outer step. |
| **Two-Variable** | $O(n \cdot m)$ | Independent nested loops with different bounds ($n$ and $m$). |
| **Exponential** | $O(2^n)$ | Geometric series expansions like $2^1 + 2^2 + \dots + 2^n$. |

> **Critical Trap:** Do not assume two nested loops automatically equal $O(n^2)$. If the inner loop bounds depend on an independent variable $m$, the complexity is strictly $O(n \cdot m)$. If the inner loop doubles or halves, it reduces to $O(n \log n)$.