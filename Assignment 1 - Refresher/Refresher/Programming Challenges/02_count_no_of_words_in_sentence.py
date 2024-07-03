
def count_words_in_sentence(sentence: str):
    return len(sentence.split())


sentence = input("Enter a sentence : ")

print(f"Number of words : {count_words_in_sentence(sentence)}")

# Output:
'''
Enter a sentence : The quick brown fox jumps over the lazy dog.
Number of words : 9
'''
