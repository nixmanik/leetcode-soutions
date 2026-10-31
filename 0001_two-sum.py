# 0001. Two Sum

# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} # Key is the number, value is the index
        for i, num in enumerate(nums):
            need = target - num # num + need = target, therefore need = target - num
            if need in seen: return [i, seen[need]]
            seen[num] = i # num was SEEN at index i
        return [] # Should not reach here because each input has a solution
