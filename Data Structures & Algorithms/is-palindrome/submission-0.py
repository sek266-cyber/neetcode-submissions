class Solution:
    def isPalindrome(self, s: str) -> bool:

        def is_ascii_alphanumeric(char):
            return "a"<=char<="z" or "A"<=char<="Z" or "0"<=char<="9"

        left, right = 0, len(s) - 1
        while left<right:
            if not is_ascii_alphanumeric(s[left]):
                left+=1
            elif not is_ascii_alphanumeric(s[right]):
                right -=1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left +=1
                right -= 1
        return True
        


        