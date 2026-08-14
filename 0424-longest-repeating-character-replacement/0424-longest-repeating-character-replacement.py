class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_frequency = 0
        ans = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            max_frequency = max(max_frequency, count[s[r]])

            window_length = r - l + 1
            replacements = window_length - max_frequency

            while replacements > k:
                count[s[l]] -= 1
                l += 1

                window_length = r - l + 1
                replacements = window_length - max_frequency

            ans = max(ans, window_length)

        return ans