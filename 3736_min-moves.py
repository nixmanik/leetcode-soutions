# 3736. Minimum Moves to Equal Array Elements III

# You are given an integer array nums.
# In one move, you may increase the value of any single element nums[i] by 1.
# Return the minimum total number of moves required so that all elements in nums become equal.

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # find the biggest element, make everything equal it
        goal = max(nums)
        moves = 0
        for num in nums:
            moves += goal - num
        return moves

# This was my first solution, mildly worse because of the additional while loop per num:
#####
# for num in nums:
#     while num != goal:
#         moves += 1
#         num += 1
# return moves
#####