""" Create a tokenizer for your own language (mother tongue you speak). 
The tokenizer should tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”, “3,22,243”, “313/77”), 
social media usernames/user handles. 
Use regular expressions to design this. 
[Hint: Use unicode blocks for your language, check wikipedia pages] """

import re

def tokenize_bengali(text):
    patterns = {'url': r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', 'email': r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b', 'date': r'\b\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}\b', 'number': r'\b\d{1,3}(?:,\d{2,3})*(?:\.\d+)?\b|\b\d+/\d+\b', 'punctuation': r"[।,?!—;:\"'()]", 'social_handle': r'@[\w]+', 'bengali_word': r'[\u0980-\u09FF]+'}

    tokenizer = re.compile('|'.join(f'(?P<{key}>{pattern})' for key, pattern in patterns.items()))
    tokens = [match.group() for match in tokenizer.finditer(text)]
    return tokens

text = input("Enter text in Bengali to tokenize : ")
tokens = tokenize_bengali(text)
print(tokens)
