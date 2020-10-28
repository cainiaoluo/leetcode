class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(k//2-1, -1, -1):
            self.heapify(i, k, nums)
            
        for i in range(k-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(0, i, nums)
        
        nums[0], nums[k-1] = nums[k-1], nums[0]
        for i in range(k, n):
            if nums[i] > nums[k-1]:
                nums[i], nums[k-1] = nums[k-1], nums[i]
                self.heapify_small(0, k, nums)
                nums[k-1], nums[0] = nums[0], nums[k-1]
                
        return nums[k-1]
    
    def heapify_small(self, begin, end, nums):
        left, right = 2*begin + 1, 2*begin + 2
        smallest = begin
        if left < end and nums[left] <= nums[smallest]:
            smallest = left
        if right < end and nums[right] <= nums[smallest]:
            smallest = right
        if smallest != begin:
            nums[begin], nums[smallest] = nums[smallest], nums[begin]
            self.heapify_small(smallest, end, nums)
        
    def heapify(self, begin, end, nums):
        left, right = 2*begin + 1, 2*begin + 2
        largest = begin
        if left < end and nums[left] > nums[largest]:
            largest = left
        if right < end and nums[right] > nums[largest]:
            largest = right
        if largest != begin:
            nums[begin], nums[largest] = nums[largest], nums[begin]
            self.heapify(largest, end, nums)