# Importar las librerias necesarias
import markovify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Función para leer un archivo de texto
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

# Función para calcular la similitud del coseno
def cosineSimilarity(text1, text2):
    # Almacenar ambos textos juntos
    texts = [text1, text2]
    # Transformar ambos textos a una representación vectorial usando tf-idf
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    # Calcular la similitud usando la distancia del coseno
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

# Ruta al archivo del corpus de texto zaratustras
corpus_file_path = "zaratustra.txt"

# Leer el texto original
zaratustra = read_text_file(corpus_file_path)

# Generar y almacenar el texto sintético usando markovify
model = markovify.Text(zaratustra)
synthetic_text = ''
for i in range(20):
    sentence = model.make_sentence()
    if sentence is None:
        continue
    synthetic_text += str(sentence)

# Imprimir ambos textos
print("\n")
print("---------------")
print("Texto original:")
print(zaratustra)
print("---------------")
print("Texto generado:")
print(synthetic_text)
print("---------------")

# Similitud entre el texto original y el texto sintético
similarity_matrix_1 = cosineSimilarity(zaratustra, synthetic_text)
similarity_synthetic_original = similarity_matrix_1[0][1]
print(f"Similitud entre el texto original (Extracto de : 'Así hablaba zaratustra') y el texto sintético: {similarity_synthetic_original}")
print("\n")

# Comparar textos identicos (fragmento de "La llamada de Cthulhu")

# Ruta al archivo del corpus de texto llamada_de_cthulhu
corpus_file_path_2 = "llamada_de_cthulhu.txt"

# Leer el texto original
cthulhu = read_text_file(corpus_file_path_2)

# Similitud entre ambos textos
similarity_matrix_2 = cosineSimilarity(cthulhu, cthulhu)
similarity_equals = similarity_matrix_2[0][1]
print(f"Similitud entre el texto (Extracto de : 'La llamada de Cthulhu') y el mismo: {similarity_equals}")
print("\n")

# Comparar textos diferentes "La llamada de Cthulhu" y "La llave de plata"

# Ruta al archivo del corpus de texto llamada_de_cthulhu
corpus_file_path_3 = "llamada_de_cthulhu.txt"

# Ruta al archivo del corpus de texto llave_de_plata
corpus_file_path_4 = "llave_de_plata.txt"

# Leer texto 1 
cthulhu = read_text_file(corpus_file_path_3)

# Leer texto 2
llave = read_text_file(corpus_file_path_4)

# Similitud entre ambos textos
similarity_matrix_3 = cosineSimilarity(cthulhu, llave)
similarity_differents = similarity_matrix_3[0][1]
print(f"Similitud entre el texto 1 (Extracto de : 'La llamada de Cthulhu') y el texto 2 (Extracto de : 'La lave de plata'): {similarity_differents}")
print("\n")