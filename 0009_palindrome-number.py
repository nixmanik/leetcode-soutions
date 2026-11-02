# 0009. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringed = str(x)
        return stringed == stringed[::-1]
