class Solution:
    def isPalindrome(self, s: str) -> bool:
        string1 = ""
        for i in s:
            if i.isalnum():
                string1 += i.lower()
        
        string2 = ""
        for j in reversed(s):
            if j.isalnum():
                string2 += j.lower()

        if string1 == string2:
            return True
        return False
