"""
1385. Find the Distance Value Between Two Arrays

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
"""
# class Solution:
#     def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
#         count = 0
#         for num1 in arr1:
#             for num2 in arr2:
#                 if abs(num1 - num2) <= d:
#                     break
#             else: count += 1
#         return count

"""

Space complexity is O(1), just needs an int variable to count. Time complexity is a O(n x m) where n = len(arr1) and m=len (arr2). 

This could be optimised with binary search, I'll use bisect_left instead of writing it. I found out about bisect with a GOOGLE SEARCH on how to make my solution optimal

"""
from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # sort arr2 to prep for the bisect
        arr2.sort()
        count = 0
        for num1 in arr1:
            # bisect to find the index where num1 would fit into arr2
            i = bisect_left(arr2, num1)
            # check element i, which shoudl be the smallest element >= num1
            if i < len(arr2) and abs(arr2[i] - num1) <= d:
                continue
            # check element i-1 which would be the largest element < num1
            if i > 0 and abs(arr2[i-1] - num1) <= d:
                continue
            count += 1
        return count

"""

The optimisation brings time complexity to O(log m) because the bisect reduces the work to just two checks to cover the whole list.

First if statement is confirms the smallest above num, that confirms all right elements
Second does the same for the left side. Two searches instead of len(arr2)

"""
