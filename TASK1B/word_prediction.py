import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from collections import defaultdict
import random

# Load and preprocess text data
nltk.download('gutenberg')
corpus = gutenberg.raw('shakespeare-hamlet.txt')
tokens = word_tokenize(corpus.lower())
words = [word for word in tokens if word.isalnum()]  # Filter out non-alphanumeric tokens

# Create n-grams
def create_ngrams(words, n=3):
    ngrams = defaultdict(list)
    for i in range(len(words) - n):
        context = tuple(words[i:i + n - 1])
        next_word = words[i + n - 1]
        ngrams[context].append(next_word)
    return ngrams

ngrams = create_ngrams(words)

# Predict next word based on context
def predict_next_word(context, ngrams):
    if context in ngrams:
        # Count occurrences of each word
        word_counts = defaultdict(int)
        for word in ngrams[context]:
            word_counts[word] += 1
        
        # Sort words by frequency (most common first)
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        
        # Return the most common word
        return sorted_words[0][0]  # Return the word with highest frequency
    else:
        return None

# Take user input and predict next word
user_input = input("Enter a phrase to predict the next word: ").lower()
input_words = user_input.split()
context = tuple(input_words[-2:])  # Use the last two words as context
predicted_word = predict_next_word(context, ngrams)
print("Predicted next word:", predicted_word)
