import re
import string
from collections import Counter

def preprocess_text(text):
    """
    Preprocess the given text by removing punctuation, converting to lowercase, and tokenizing.
    """
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    tokens = text.split()
    return tokens

def calculate_similarity(text1, text2):
    """
    Calculate the similarity between two texts using the Jaccard similarity coefficient.
    """
    tokens1 = preprocess_text(text1)
    tokens2 = preprocess_text(text2)

    # Calculate the Jaccard similarity coefficient
    intersection = set(tokens1) & set(tokens2)
    union = set(tokens1) | set(tokens2)
    similarity = len(intersection) / len(union)

    return similarity

# Example usage
text1 = "we are software engineers."
text2 = "we are software engineers."
similarity = calculate_similarity(text1, text2)
print(f"Similarity between the two texts: {similarity:.2f}")

# Example of plagiarism detection
original_text = "we are unique."
plagiarized_text = "Python is a high-level programming language known for its simplicity and readability. It is widely used in various domains, including web development, data analysis, machine learning, and scientific computing."

similarity = calculate_similarity(original_text, plagiarized_text)
if similarity > 0.8:
    print("Potential plagiarism detected!")
else:
    print("No plagiarism detected.")