import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.s = s
        self.s = self.s.lower()
        self.s = re.sub(r"[^A-Za-z0-9]","",self.s)
        if self.s == self.s[::-1]:
            return True
        else :
            return False
        
        