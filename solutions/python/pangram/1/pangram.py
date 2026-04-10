def is_pangram(sentence):
    new_sentence = filter(str.isalpha, sentence.lower())
    new_set = set(new_sentence)
    print(len(new_set))
    if len(new_set) == 26:
        return True
    return False

