class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)

        left = 0

        for right in range(len(s) + 1):
            if right == len(s) or s[right] == ' ':

                l = left
                r = right - 1

                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1

                left = right +1

        return ''.join(s)