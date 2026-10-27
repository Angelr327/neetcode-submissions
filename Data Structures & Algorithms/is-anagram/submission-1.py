class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = []
        list_t = []

        for string in s:
            list_s.append(string)

        for string in t:
            list_t.append(string)

        list_s.sort()
        list_t.sort()
        
        if list_t == list_s:
            return True
        else:
            return False
