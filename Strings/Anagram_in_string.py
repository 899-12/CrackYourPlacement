from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        p_len = len(p)
        p_count = Counter(p)
        s_count = Counter()

        for i in range(len(s)):
            # Add current character to the sliding window
            s_count[s[i]] += 1

            # Remove the character that's left behind as window slides
            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                else:
                    s_count[s[i - p_len]] -= 1

            # Compare counters
            if s_count == p_count:
                res.append(i - p_len + 1)

        return res
