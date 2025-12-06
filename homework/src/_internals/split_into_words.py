def split_into_words(preprocessed_lines):
    words = []
    for line in preprocessed_lines:
        words.extend(words.strip(",.!?") for words in line.split())
    return words
