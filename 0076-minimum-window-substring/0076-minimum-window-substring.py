class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        l = 0
        formed = 0
        min_len = float("inf")
        start = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == len(need):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                left = s[l]
                window[left] -= 1

                if left in need and window[left] < need[left]:
                    formed -= 1

                l += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]