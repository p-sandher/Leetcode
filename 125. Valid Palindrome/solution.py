class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in st:
            if c.isalnum():
                st += c.lower()

        print(st)
        return st == st[::-1]

