**Binary search** is an efficient algorithm for finding a target value within a **sorted array**. Instead of scanning items one by one (linear search), binary search continually divides the search space in half.

---

## Key Mechanism

1. **Prerequisite:** The array **must** be sorted.
2. Find the element in the **middle** of the current range:

$$\text{mid} = \text{low} + \left\lfloor \frac{\text{high} - \text{low}}{2} \right\rfloor$$


3. Compare the middle element to your **target**:
* **If equal:** Search is complete.
* **If target is smaller:** Ignore the right half by setting $\text{high} = \text{mid} - 1$.
* **If target is larger:** Ignore the left half by setting $\text{low} = \text{mid} + 1$.


4. Repeat until the target is found or $\text{low} > \text{high}$.

---

## Step-by-Step Example

Search for **`23`** in sorted array: `[2, 5, 8, 12, 16, 23, 38, 56, 72]`

```text
Step 1:  [2, 5, 8, 12, 16, 23, 38, 56, 72]
          ^             ^              ^
         low           mid            high
         Mid value = 16. Target (23) > 16  --> Search right half.

Step 2:  [2, 5, 8, 12, 16, 23, 38, 56, 72]
                           ^    ^      ^
                          low  mid    high
         Mid value = 38. Target (23) < 38  --> Search left half.

Step 3:  [2, 5, 8, 12, 16, 23, 38, 56, 72]
                           ^
                      low/mid/high
         Mid value = 23. Target (23) == 23 --> Found at index 5!

```

---

## Code Implementation

```python
def binary_search(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1

    while low <= high:
        # Prevents integer overflow in lower-level languages
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found

```

---

## Complexity Analysis

| Measure | Complexity | Reason |
| --- | --- | --- |
| **Best Time** | $\mathcal{O}(1)$ | Target is at the exact middle on the first attempt. |
| **Average / Worst Time** | $\mathcal{O}(\log n)$ | Search space halves with every single comparison. |
| **Space (Iterative)** | $\mathcal{O}(1)$ | Uses only two pointers (`low`, `high`). |
| **Space (Recursive)** | $\mathcal{O}(\log n)$ | Call stack depth proportional to search steps. |



## Type of Binary Search

1. Sorted Array Binary Search: The classic binary search algorithm applied to a sorted array.
2. Binary Search on Rotated Array: A modified binary search to handle arrays that have been rotated.
3. Binary Search on Abstract Data Structures: Binary search can also be applied to data structures like trees (e.g., binary search trees) and graphs, where the search space is organized in a sorted manner.