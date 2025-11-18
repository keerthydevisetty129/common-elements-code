def word_frequency(sentence):
    # Convert to lowercase
    sentence = sentence.lower()

    # Split into words
    words = sentence.split()

    # Dictionary to store word counts
    freq = {}

    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    return freq

# Example
sentence = "the cat and the hat"
result = word_frequency(sentence)
print(result)
