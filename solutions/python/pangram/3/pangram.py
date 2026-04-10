"""Function to quickly determine is the str is pangram.
    Meaning if it has all letters of alphabet.
"""
def is_pangram(sentence: str) -> bool:
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(sentence.lower())