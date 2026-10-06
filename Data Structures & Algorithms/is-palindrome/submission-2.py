class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_list = list(s)
        reverse_list.reverse()
        reverse_s = "".join(reverse_list)
        final_s =""
        final_reverse_s = ""

        for char in reverse_s:
            if char.isalnum():
                final_s += char.lower()
        for char in s:
            if char.isalnum():
                final_reverse_s += char.lower()


        if final_s == final_reverse_s:
            return True
        else:
            return False
