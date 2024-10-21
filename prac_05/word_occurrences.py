"""
Word Occurrences
Estimate: 10 minutes
Actual:   14 min
"""
def main():
    text_input = input("Text: ")
    word_to_count = {}
    for word in text_input.split():
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
    words_list = list(word_to_count.keys())
    words_list.sort()
    word_to_count = {word: word_to_count[word] for word in words_list}
    for word, count in word_to_count.items():
        max_word_length = max(len(word) for word in word_to_count)
        print(f"{word:{max_word_length}} : {count}")
main()