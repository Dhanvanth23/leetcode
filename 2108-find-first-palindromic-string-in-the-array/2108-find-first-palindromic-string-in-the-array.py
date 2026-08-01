class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:       

            l = 0
            r = len(word) - 1
            isPalindrome = True

            while l < r:
                if word[l] != word[r]:
                    isPalindrome = False
                    break

                l += 1
                r -= 1

            if isPalindrome:
                return word

        return ""