class Solution:
    def isPalindrome(self, s: str) -> bool:
#        s=s.replace(" ","")
        s= ''.join(char for char in s if char.isalnum())
        s=s.lower()
        t=s[::-1]
        return t==s