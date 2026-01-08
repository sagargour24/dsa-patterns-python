from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks for duplicates in an integer array.
        
        Time Complexity: O(n) - We iterate through the list once.
        Space Complexity: O(n) - We store elements in a hash set.
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False

# Test case to verify logic locally
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))  # Expected: True