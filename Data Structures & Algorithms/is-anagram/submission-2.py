class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_s= sorted(list(s))
        sorted_t= sorted(list(t))

        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_t[i] or len(sorted_s) !=len(sorted_t):
                return False
        return True
