# Importar las librerias necesarias
import markovify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Función para leer un archivo de texto
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

# Ruta al archivo de texto corpus
corpus_file_path = "corpus.txt"

# Leer el texto original
original_text = read_text_file(corpus_file_path)

# Generar y almacenar el texto sintético usando markovify
model = markovify.Text(original_text)
synthetic_text = ''
for i in range(20):
    sentence = model.make_sentence()
    if sentence is None:
        continue
    synthetic_text += str(sentence)

# Imprimir ambos textos
print("---------------")
print("Texto original:")
print(original_text)
print("---------------")
print("Texto generado:")
print(synthetic_text)
print("---------------")

# Almacenar ambos textos juntos
texts = [original_text, synthetic_text]

# Transformar ambos textos a una representación vectorial usando tf-idf
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# Calcular la similitud usando la distancia del coseno
similarity_matrix = cosine_similarity(tfidf_matrix)

# Similitud entre el texto original y el texto sintético
similarity_synthetic_original = similarity_matrix[0][1]
print(f"Similitud entre el texto original y el texto sintético: {similarity_synthetic_original}")