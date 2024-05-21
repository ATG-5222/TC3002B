import re
import numpy as np
import math
import javalang

# Leer y almacenar el texto 1 
with open("example_1.java", 'r', encoding='utf-8') as f:
    text1 = f.read()

# Leer y almacenar el texto 2 
with open("example_2.java", 'r', encoding='utf-8') as f:
    text2 = f.read()

# Función para tokenizar utilizando javalang
def tokenize_with_javalang(text):
    tokens = []
    lexer = javalang.tokenizer.tokenize(text)
    for token in lexer:
        tokens.append(token.value)
    return tokens

# Tokenizar ambos textos
tokens_text1 = tokenize_with_javalang(text1)
tokens_text2 = tokenize_with_javalang(text2)

# Combinar los tokens de ambos textos
combined_text = tokens_text1 + tokens_text2

words1 = {}
words2 = {}

for word in combined_text:
    words1[word] = []
    words2[word] = []

# Crear grafo para text1
for i in range(1, len(tokens_text1)):
    origin_word = tokens_text1[i-1]
    destination_word = tokens_text1[i]
    words1[origin_word].append(destination_word)

# Crear grafo para text2
for i in range(1, len(tokens_text2)):
    origin_word = tokens_text2[i-1]
    destination_word = tokens_text2[i]
    words2[origin_word].append(destination_word)