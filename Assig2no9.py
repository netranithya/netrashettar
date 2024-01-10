def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Return the count of words
    return len(words)

# Example usage:
input_sentence = input("Enter a sentence: ")
word_count = count_words(input_sentence)
print("Number of words:", word_count)
