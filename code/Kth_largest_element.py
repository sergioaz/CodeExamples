import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# Example usage
k = 3
nums = [4, 5, 8, 2]
kth_largest = KthLargest(k, nums)

print(kth_largest.add(3))  # Output: 4
print(kth_largest.add(5))  # Output: 5
print(kth_largest.add(10)) # Output: 5
print(kth_largest.add(9))  # Output: 8
print(kth_largest.add(4))  # Output: 8