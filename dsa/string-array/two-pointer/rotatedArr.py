class Solution:

    def reverse(self, arr, i, j):
        """Helper to reverse array in-place from index i to j."""
        while i < j:
            self.swap(arr, i, j)
            i += 1
            j -= 1

    def swap(self, arr, i, j):
        """Helper to swap two elements in an array."""
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def rotate(self, arr, k):
        """Rotates array right by k steps in-place."""
        n = len(arr)
        if n == 0:
            return

        k = k % n  # Handle k > n

        if k == 0:
            return

        # 1. Reverse entire array
        self.reverse(arr, 0, n - 1)

        # 2. Reverse first k elements
        self.reverse(arr, 0, k - 1)

        # 3. Reverse remaining n - k elements
        self.reverse(arr, k, n - 1)


# --- Execution ---
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

obj = Solution()
obj.rotate(arr, k)

print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]