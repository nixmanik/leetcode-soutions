"""
2914. Minimum Number of Changes to Make Binary String Beautiful

You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more substrings such that:

Each substring has an even length.
Each substring contains only 1's or only 0's.
You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.

Constraints:
2 <= s.length <= 105
s has an even length.
s[i] is either '0' or '1'.

"""

class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        # s is always even in constraints
        changes = 0
        i = 0
        while i != n:
            # substrings just need to be two, so check each pair if they are the same
            a, b = s[i], s[i+1]
            if a != b: changes += 1
            i += 2
        return changes

"""
This felt easy. At first I wondered if checking longer substrings would be needed, but it actually works fine in pairs because it would need the same number of changes in either case.
"""