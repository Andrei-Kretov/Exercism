def is_pangram(sentence: str) -> bool:
    return set('abcdefghijklmnopqrstuvwxyz').issubset(sentence.lower())