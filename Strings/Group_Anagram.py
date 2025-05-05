#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort the word to use as a key
            anagrams[sorted_word].append(word)

        return list(anagrams.values())
