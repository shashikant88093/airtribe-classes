## Linear Search

- Linear search is a simple search algorithm that checks each element in a list sequentially until the target value is found or the end of the list is reached. It does not require the list to be sorted.

## Algorithm Steps
1. Start from the first element of the list.
2. Compare the current element with the target value.
   - If they are equal, return the index of the current element.
   - If they are not equal, move to the next element.
3. Repeat step 2 until the target value is found or the end of the list is reached.
4. If the end of the list is reached without finding the target, return -1.
5. Linear search has a time complexity of O(n), where n is the number of elements in the list.

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72]

arr[index] = target

