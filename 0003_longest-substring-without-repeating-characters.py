# 0003. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = float('-inf')
        # store characters as character:index
        chars = {}
        left = 0
        # s can be an empty string
        if s == '':
            return 0
        # two pointers to create window
        for right, char in enumerate(s):
            # if char not seen before OR if it has, not seen in this substring:
            if char not in chars or chars[char] < left:
                # check if this is new longest substring
                longest = max(longest, right - left + 1)
            else:
                # move left pointer forward to shrink window
                left = chars[char] + 1
            # add the char to the dict for lookup
            chars[char] = right
        return longest
