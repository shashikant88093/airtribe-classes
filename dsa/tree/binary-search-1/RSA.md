# RSA (Rotating Search Algorithm):

## Overview
The Rotating Search Algorithm (RSA) is an efficient search algorithm designed to find a target value in a rotated sorted array. A rotated sorted array is an array that has been rotated at some pivot point, resulting in two sorted subarrays.

## How RSA Works
1. **Identify the Pivot**: The algorithm first identifies the pivot point where the rotation occurred. This is done using a modified binary search.
2. **Determine the Search Range**: Once the pivot is found, the algorithm determines which of the two subarrays (left or right of the pivot) the target value may reside in.
3. **Perform Binary Search**: Finally, a standard binary search is performed on the identified subarray to locate the target value.

## Time Complexity
- The time complexity of RSA is O(log n) in the average and best cases, making it more efficient than a linear search.

## Use Cases
- RSA is particularly useful in scenarios where the dataset is large, and the search operation needs to be optimized for speed.

## Example Implementation in Python
```python
def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # Check if the left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, the right half must be sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1  # Target not found
```

## Algorithm Steps
1. Initialize two pointers, `left` and `right`, to the start and end of the array.
2. While `left` is less than or equal to `right`, calculate the middle index `mid`.
3. If the element at `mid` is equal to the target, return `mid`.
4. Check if the left half of the array is sorted:
   - If it is, check if the target lies within this range. If it does, adjust the `right` pointer to `mid - 1`. Otherwise, adjust the `left` pointer to `mid + 1`.
5. If the left half is not sorted, then the right half must be sorted:
   - Check if the target lies within this range. If it does, adjust the `left` pointer to `mid + 1`. Otherwise, adjust the `right` pointer to `mid - 1`.
6. Repeat steps 2-5 until the target is found or the search space is exhausted.
7. If the target is not found, return -1.