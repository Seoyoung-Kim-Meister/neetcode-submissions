class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s=s.replace("?","")
        s= ''.join(char for char in s if char.isalnum())
        s=s.lower()
        print(s)
        t=s[::-1]
        if t==s:
            return True
        else:
            return False