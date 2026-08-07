## Binary Search

- Binary search is an efficient search algorithm that finds the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half. If the value of the target is less than the item in the middle of the interval, it narrows the interval to the lower half. Otherwise, it narrows it to the upper half. The process continues until the target value is found or the interval is empty.

- It is always applied to sorted arrays or lists, and it has a time complexity of O(log n), making it much faster than linear search for large datasets.

## Binary Search Foundation:-

- Binary search is divide and conquer algorithm. It works on the principle of reducing the search space by half in each iteration. The key steps involved in binary search are:
  1. Start with the middle element of the array.
  2. If the middle element is equal to the target value, return its index.
  3. If the middle element is greater than the target value, narrow the search to the left half.
  4. If the middle element is less than the target value, narrow the search to the right half.
  5. Repeat the process until the target value is found or the search space is empty.

### Key insights of Binary Search:
- Binary search requires a sorted array or list.
- It has a time complexity of O(log n), making it efficient for large datasets.
- The search space is halved in each iteration, leading to faster search times compared to linear search.

`Key Insights of Binary Search`:
- Binary search is a divide-and-conquer algorithm that efficiently finds the position of a target value within a sorted array or list.
- It has a time complexity of O(log n), making it much faster than linear search for large datasets.
- The search space is halved in each iteration, leading to faster search times compared to linear search.
- Binary search is not "looking everywhere". It repeatedly divides the search space in half, focusing only on the relevant portion of the array or list.


## The basic setup uses two boundaries.
- S = start / left boundary
- E = end / right boundary
- mid = middle index

mid = S + (E - S) // 2

<!-- The logic is straightforward: -->
1. If the target value is equal to the middle element, return the middle index.
2. If the target value is less than the middle element, narrow the search to the left half by updating the end boundary to mid - 1.
3. If the target value is greater than the middle element, narrow the search to the right half by updating the start boundary to mid + 1.
4. Repeat the process until the target value is found or the search space is empty (i.e., start boundary exceeds end boundary).

`
if arr[mid] == target:
    return mid  # Target found, return index
elif arr[mid] < target:
    S = mid + 1  # Target is in the right half
else:
    E = mid - 1  # Target is in the left half
`

The loop countinues while S <= E. If the loop ends without finding the target, return -1 to indicate that the target is not present in the array.

`Key Insights:` Compare the value of mid with target, not the index.

`Watch Out:` if you stop early, you may miss the target. Always check the mid value against the target before adjusting the boundaries.


## Why the safe midpoint matters
- A common midpoint formula is `mid = (S + E) // 2`. However, this can lead to integer overflow in some programming languages when S and E are large. To avoid this, use the safer formula: `mid = S + (E - S) // 2`. This prevents overflow by calculating the difference first before adding it to S.

<!-- ======================= Binary ======================= -->
```python
# Verify algebraic equivalence and edge cases
s, e = 10, 20

# Standard midpoint formula
mid1 = (s + e) // 2

# Overflow-safe midpoint formula
mid2 = s + (e - s) // 2

# The user's literal formula mid = s + (s - e) // 2
mid3 = s + (s - e) // 2

print(f"s={s}, e={e}")
print(f"(s+e)//2 = {mid1}")
print(f"s + (e-s)//2 = {mid2}")
print(f"s + (s-e)//2 = {mid3}")

# Integer overflow demo in 32-bit signed int bounds (2,147,483,647)
import ctypes
INT_MAX = 2147483647
s_large = 2000000000
e_large = 2000000000

# 32-bit addition overflow simulation
overflow_sum = ctypes.c_int32(s_large + e_large).value
print(f"32-bit signed overflow sum: {overflow_sum}")
print(f"Overflow mid: {overflow_sum // 2}")
print(f"Safe mid: {s_large + (e_large - s_large) // 2}")


```

```text
s=10, e=20
(s+e)//2 = 15
s + (e-s)//2 = 15
s + (s-e)//2 = 5
32-bit signed overflow sum: -294967296
Overflow mid: -147483648
Safe mid: 2000000000


```

There are two distinct differences to highlight here: a likely **formula typo** in the second expression, and a critical **integer overflow issue** in programming.

---

## 1. Mathematical Logic & Typo Check

If you write `mid = s + (s - e) / 2`:

$$\text{mid} = s + \frac{s - e}{2} = \frac{2s + s - e}{2} = \frac{3s - e}{2}$$

This moves **left** (away from `e`) instead of finding the center point.

* **Example ($s = 10, e = 20$):**
* `(s + e) / 2` $\rightarrow (10 + 20) / 2 =$ **`15`** *(Correct midpoint)*
* `s + (s - e) / 2` $\rightarrow 10 + (10 - 20) / 2 =$ **`5`** *(Incorrect)*



### The Intended Formula: `mid = s + (e - s) / 2`

The intended alternative in binary search is `mid = s + (e - s) / 2`. Algebraically, it is identical to `(s + e) / 2`:

$$s + \frac{e - s}{2} = \frac{2s + e - s}{2} = \frac{s + e}{2}$$

---

## 2. Why use `s + (e - s) / 2` instead of `(s + e) / 2`?

The primary reason to use `mid = s + (e - s) / 2` is to prevent **Integer Overflow**.

### The Integer Overflow Problem

In languages with fixed-size integer types like **C, C++, Java, C#, or Rust** (where standard 32-bit signed integers range from $-2,147,483,648$ to $2,147,483,647$):

* If $s$ and $e$ are both large numbers (e.g., $s = 1,500,000,000$ and $e = 2,000,000,000$):
* `s + e = 3,500,000,000`
* Since $3,500,000,000 > 2,147,483,647$, the sum **overflows into negative numbers** (wrapping around to approximately $-794,967,296$).
* `mid = (s + e) / 2` yields a **negative index**, causing an `ArrayIndexOutOfBoundsException` or memory crash.

### How `s + (e - s) / 2` Fixes It

By subtracting $s$ from $e$ first:

1. $e - s = 500,000,000$ (well within 32-bit limits).
2. $(e - s) / 2 = 250,000,000$.
3. $s + 250,000,000 = 1,750,000,000$ (never exceeds $2,147,483,647$).

---

## Comparison Summary

| Expression | Mathematical Output | Overflow Safe? | Correct Use Case |
| --- | --- | --- | --- |
| **`mid = (s + e) / 2`** | $\frac{s + e}{2}$ | ❌ No | Python (arbitrary precision) or small array bounds. |
| **`mid = s + (e - s) / 2`** | $\frac{s + e}{2}$ | ✅ Yes | Safe standard in C, C++, Java, Rust, Go, etc. |
| **`mid = s + (s - e) / 2`** | $\frac{3s - e}{2}$ | ❌ Incorrect math | Never used for midpoint calculation. |