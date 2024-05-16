# Importar las librerias necesarias
import markovify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Almacenar el texto original en una variable
original_text = "Synthesizing knowledge of the connections between above-surface and below-surface biodiversity was considered a priority to be addressed at a second workshop , since it would help to yield information on keystone species and interactions in ecosystem processes assess the extent of species "
# Generar y almacenar el texto sintetico usando markovify
model = markovify.Text(open("corpus.txt", 'r', encoding = 'utf-8', errors = 'ignore').read(), state_size = 1)
synthetic_text = model.make_sentence()

# Almacenar ambos textos juntos
texts = [original_text,synthetic_text]

# Transformar ambos textos a una representación vectorial usando tf-idf
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)
tfidf_matrix_original = tfidf_matrix[0]
tfidf_matrix_synthetic = tfidf_matrix[1]

# Calcular la similitud usando la distancia del coseno
similarity_synthetic_original = cosine_similarity(tfidf_matrix_original, tfidf_matrix_synthetic)

# Imprimir los resultados
print(f"Similitud entre el texto original y el texto sintético: {similarity_synthetic_original[0][0]}")