import numpy as np
import math
import javalang

# Leer y almacenar el texto 1 
with open("example_1.java", 'r', encoding='utf-8') as file1:
    text1 = file1.read()

# Leer y almacenar el texto 2 
with open("example_2.java", 'r', encoding='utf-8') as file2:
    text2 = file2.read()

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

# Crear diccionarios para indexar las palabras en words1 y words2
words1_index = {}
words2_index = {}

# Indexar las palabras en words1
index = 0
for word in words1:
    words1_index[word] = index
    index += 1

# Indexar las palabras en words2
index2 = 0
for word in words2:
    words2_index[word] = index2
    index2 += 1

# Inicializar las matrices de transición
mat1 = []
mat2 = []

# Longitudes de los diccionarios de palabras
len1 = len(words1)
len2 = len(words2)

# Crear la matriz de transición para text1
for word in words1:
    list1 = [0 for i in range(len1)]
    val1 = 0
    if len(words1[word]) != 0:
        val1 = 1 / len(words1[word])
    for next_word in words1[word]:
        next_word_index = words1_index[next_word]
        list1[next_word_index] += val1        
    mat1.append(list1)

# Crear la matriz de transición para text2
for word in words2:
    list2 = [0 for i in range(len2)]
    val2 = 0
    if len(words2[word]) != 0:
        val2 = 1 / len(words2[word])
    for next_word in words2[word]:
        next_word_index = words2_index[next_word]
        list2[next_word_index] += val2        
    mat2.append(list2)

# Convertir las listas de matrices a arrays de numpy
mat1 = np.array(mat1)
mat2 = np.array(mat2)

# Calcular el producto de la matriz de transposición de mat2 con mat1
BT = mat2.transpose()
C = np.matmul(BT, mat1)
prod_int = np.trace(C)

# Calcular las normas de las matrices
norm_A = math.sqrt(np.trace(np.matmul(mat1.transpose(), mat1)))
norm_B = math.sqrt(np.trace(np.matmul(mat2.transpose(), mat2)))

# Calcular el ángulo del coseno entre las matrices de transición
cos_ang = prod_int / (norm_A * norm_B)

# Imprimir los resultados
print('Prod int = ' + str(round(prod_int, 4)) + '\n')
print('Norm A = ' + str(round(norm_A, 4)) + '\n')
print('Norm B = ' + str(round(norm_B, 4)) + '\n')
print('Cosine angle = ' + str(round(cos_ang, 4)) + '\n')
print('The similarity of both texts is ' + str(round(cos_ang, 4) * 100) + '%' + ', based on the cosine distance of transition matrices.')