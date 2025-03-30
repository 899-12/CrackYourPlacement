"""
Print all the duplicate characters in a string
"""
from collections import Counter

def find_duplicates(s):
    char_count = Counter(s)  # O(n) time

    for char, count in char_count.items():
        if count > 1:
            print(f"{char}: {count} times")

# Example Usage
s = "hello world"
find_duplicates(s)

"""
Without using counter"""
def find_duplicates(s):
    char_count = {}  # O(n) space
    
    for char in s:  # O(n) time
        char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():  # O(n) time
        if count > 1:
            print(f"{char}: {count} times")

# Example Usage
s = "hello world"
find_duplicates(s)
