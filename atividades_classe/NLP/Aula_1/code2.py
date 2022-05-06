from nltk.tokenize import sent_tokenize, word_tokenize
import nlp_utils
import re

# Split scene_one into sentences: sentences
scene_one = nlp_utils.get_sample_Santo_Graal()
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(scene_one)

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(tokenized_sent)

# Print the unique tokens result
print(unique_tokens)