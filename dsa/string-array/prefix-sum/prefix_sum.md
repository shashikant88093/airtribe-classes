## Prefix Sums & Range Queries

When an array must answer multiple contiguous range queries $[L, R]$, a brute-force scan costs $O(N)$ per query, leading to an inefficient $O(Q \cdot N)$ total runtime. **Prefix sums** eliminate redundant calculations by trading one-time $O(N)$ preprocessing for $O(1)$ query lookups.

### =============================== The Prefix Sum Formula ===============================

A prefix sum array stores cumulative totals from index $0$ to $i$:

$$\text{prefix}[i] = \text{prefix}[i - 1] + \text{arr}[i]$$

To find the sum of any range $[L, R]$ in $O(1)$ time:

$$\text{sum}(L, R) = \begin{cases} \text{prefix}[R] & \text{if } L = 0 \\ \text{prefix}[R] - \text{prefix}[L - 1] & \text{if } L > 0 \end{cases}$$

---

## Classic Interview Patterns Using Cumulative Thinking

The core idea of tracking left-side and right-side cumulative data solves several classic $O(N)$ array problems without brute-force $O(N^2)$ scanning.

### 1. ===================================  Pivot Index (Equilibrium Point) =================================

A pivot index is where the sum of elements strictly to the left equals the sum of elements strictly to the right.

Instead of recalculating sums for every index, use the total sum ($\text{prefix}[n - 1]$) to derive left and right boundaries dynamically:

* **Left Sum:** $0$ if $i = 0$, else $\text{prefix}[i - 1]$
* **Right Sum:** $\text{prefix}[n - 1] - \text{prefix}[i]$

> **Key Insight:** Subtracting $\text{prefix}[i]$ from the total sum removes everything up to and including index $i$, leaving only the right-side elements.

---

### 2. ========================= Trapping Rain Water ================================

Water trapped above a bar depends entirely on the shortest of the two tallest boundaries enclosing it from the left and right.

$$\text{water}[i] = \max(0, \min(\text{left\_max}[i], \text{right\_max}[i]) - \text{height}[i])$$

* **Prefix Max Array:** Scans left-to-right to track the tallest wall seen so far from the start.
* **Suffix Max Array:** Scans right-to-left to track the tallest wall seen so far from the end.
* **Execution:** Combine both arrays in a final linear pass to calculate total trapped water in $O(N)$ time and $O(N)$ space.

---

### 3. Product of Array Except Self

For each index $i$, return the product of all array elements except $\text{arr}[i]$.

* **Why Division Fails:** Computing total product and dividing by $\text{arr}[i]$ breaks immediately if the array contains one or more zeroes (division by zero is undefined).
* **The Robust Solution:** Precompute a **Left Product Array** (products of all elements before $i$) and a **Right Product Array** (products of all elements after $i$).

$$\text{answer}[i] = \text{left\_product}[i] \times \text{right\_product}[i]$$

---

## Pattern Comparison Reference

| Problem | Precomputation Required | Core Formula / Logic | Time / Space |
| --- | --- | --- | --- |
| **Range Sum Query** | Prefix Sums | $\text{prefix}[R] - \text{prefix}[L - 1]$ | $O(1)$ query / $O(N)$ space |
| **Pivot Index** | Prefix Sums | $\text{left\_sum} == \text{right\_sum}$ | $O(N)$ time / $O(N)$ space |
| **Trapping Rain Water** | Prefix Max & Suffix Max | $\min(\text{left\_max}, \text{right\_max}) - \text{height}[i]$ | $O(N)$ time / $O(N)$ space |
| **Product Except Self** | Left & Right Products | $\text{left\_prod}[i] \times \text{right\_prod}[i]$ | $O(N)$ time / $O(N)$ space |

---

## Complexity & Geometric Series

### Halving Loops

When a loop variable starts at $N$ and is repeatedly halved ($N \rightarrow \frac{N}{2} \rightarrow \frac{N}{4} \dots \rightarrow 1$), the number of levels generated is logarithmic: **$O(\log N)$**.

### Geometric Progressions

When analyzing series where terms shrink or grow by a constant multiplier (e.g., $S_n = \frac{A(R^n - 1)}{R - 1}$), asymptotic analysis ignores lower-order additions and constants. **Only the dominant growth term dictates the Big-O complexity.**

---

## Developing Pattern Recognition

Algorithmic mastery relies on recognizing structural cues in problem statements rather than memorizing isolated code implementations:

* **"Top $K$" or "$K$ Frequent Elements"** $\rightarrow$ Strongly hints at **Heaps (Priority Queues)** or frequency bucket sorting.
* **"Minimize the Maximum" / "Maximize the Minimum"** $\rightarrow$ Strongly hints at **Binary Search on the Answer** or Greedy optimization.
* **Contiguous Subarrays / Cumulative Totals** $\rightarrow$ Point directly toward **Prefix Sums**, **Sliding Window**, or **Two Pointers**.

=================================== simple understanding ==================================

Imagine you are at a grocery store buying 5 items. As the cashier scans each item, the register screen doesn't just show the price of that one item—it shows the **Running Total** (the subtotal of everything scanned so far).

That **Running Total** is a **Prefix Sum**.

Instead of walking down your shelf and adding boxes from scratch every single time a query card asks for a sum (which is slow), we do the addition **once** and write down the running totals on a second shelf called `prefix`.

---

## 1. Building the Running Total Shelf

Let's use simple prices for 5 items:
`arr = [10, 20, 30, 40, 50]`

To build our `prefix` shelf, we just add the current box to whatever our running total was a second ago:

| Index (`i`) | Item Price (`arr[i]`) | Running Total Math | What goes in `prefix[i]` |
| --- | --- | --- | --- |
| **0** | 10 | Just the first item | **10** |
| **1** | 20 | 10 + 20 | **30** |
| **2** | 30 | 30 + 30 | **60** |
| **3** | 40 | 60 + 40 | **100** |
| **4** | 50 | 100 + 50 | **150** |

Now we have our cheat sheet: `prefix = [10, 30, 60, 100, 150]`

---

## 2. The Magic Formula: Why subtract `L - 1`?

Imagine someone gives you a query card: **"How much did items from Index 2 to Index 4 cost?"**
*(In real prices: 30 + 40 + 50 = 120)*

Instead of adding `30 + 40 + 50`, look at your `prefix` cheat sheet:

1. Look at the end of the range, **Index 4**. The running total there is **150**. That is the cost of *everything* from Box 0 all the way to Box 4.
2. But we only want boxes **2, 3, and 4**. That means we need to **throw away** the boxes we don't want: **Box 0 and Box 1**.
3. What was the running total of the boxes we want to throw away? Look at **Index 1** (`L - 1`). The running total there is **30**.

Subtract the part you don't want from the total:


$$\text{Total up to Index 4} - \text{Total up to Index 1} = 150 - 30 = 120$$

> **The Golden Rule:** To get the sum from index $L$ to $R$, take the running total at $R$, and subtract the running total of everything **just before** $L$ (which is index $L - 1$).

---

## 3. Tracing Your Exact Example

Let's use the exact array from your notes: `arr = [-2, 0, 3, -5, 2, -1]`

First, we build the `prefix` array by keeping a running total:

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| **`arr` (Box)** | `-2` | `0` | `3` | `-5` | `2` | `-1` |
| **`prefix` (Running Total)** | **`-2`** | **`-2`** | **`1`** | **`-4`** | **`-2`** | **`-3`** |

Now let's answer your three query cards instantly using **only** subtraction—no loops!

### Query 1: `[0, 2]` (Start at 0, Stop at 2)

* **Rule:** Because it starts at `0`, we don't need to throw anything away! We just grab the running total at index `2`.
* **Look at `prefix[2]`:** The answer is **`1`**.

### Query 2: `[2, 5]` (Start at 2, Stop at 5)

* **We want:** Everything up to index 5 (`prefix[5]`, which is **`-3`**).
* **We throw away:** Everything before index 2. That means index 1 (`prefix[1]`, which is **`-2`**).
* **Math:** `-3 - (-2) = -3 + 2 =` **`-1`**.

### Query 3: `[0, 5]` (Start at 0, Stop at 5)

* **Rule:** Starts at `0`, so no subtraction needed. Just look at the very last box of our running total!
* **Look at `prefix[5]`:** The answer is **`-3`**.

---

## Why this makes you pass the interview

If LeetCode gives you **100,000 query cards** on an array of **100,000 numbers**:

* **Brute Force** will try to do 10,000,000,000 additions and your code will freeze (Time Limit Exceeded).
* **Prefix Sum** does the addition once at the very beginning. After that, answering each of the 100,000 cards takes **one single subtraction** ($O(1)$ time). It finishes in milliseconds!