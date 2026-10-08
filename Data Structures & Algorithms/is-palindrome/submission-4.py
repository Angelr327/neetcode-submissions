class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = ""
        for char in s:
            if char.isalnum():
                valid_s += char.lower()


        if valid_s == valid_s[::-1]:
            return True
        else:
            return False