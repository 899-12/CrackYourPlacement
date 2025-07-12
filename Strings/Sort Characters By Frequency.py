""" Given a string s, sort it in decreasing order based on the frequency of the
characters. The frequency of a character is the number of times it appears
in the string. Return the sorted string. If there are multiple answers, return
any of them."""
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)

        sorted_chars=sorted(freq.items(),key=lambda x:-x[1])

        # Step 3: Build final string
        result = ''.join([char * count for char, count in sorted_chars])

        return result
