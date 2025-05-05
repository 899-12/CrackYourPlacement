from collections import Counter
import math

MOD = 10**9 + 7

def modinv(a, mod):
    # Modular inverse using Fermat's Little Theorem
    return pow(a, mod - 2, mod)

def word_anagrams(word):
    freq = Counter(word)
    numerator = math.factorial(len(word)) % MOD
    denominator = 1
    for count in freq.values():
        denominator = (denominator * math.factorial(count)) % MOD
    return (numerator * modinv(denominator, MOD)) % MOD

def countDistinctAnagrams(s: str) -> int:
    words = s.strip().split()
    result = 1
    for word in words:
        result = (result * word_anagrams(word)) % MOD
    return result
