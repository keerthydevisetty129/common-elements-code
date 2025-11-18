def reverse_words(sentence):
    # Split sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join back into a string
    return " ".join(reversed_words)

# Example
sentence = "hello world python"
result = reverse_words(sentence)
print(result)
