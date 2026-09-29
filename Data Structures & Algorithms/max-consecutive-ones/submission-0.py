class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0
        
        for num in nums:
            if num == 1:
                current_ones += 1
                # Update the maximum seen so far
                if current_ones > max_ones:
                    max_ones = current_ones
            else:
                # Reset the counter when we hit a 0
                current_ones = 0
                
        return max_ones