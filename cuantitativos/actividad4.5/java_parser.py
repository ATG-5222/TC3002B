import javalang

# Definir el nombre del archivo de java
java_file = "example_1.java"
# Cargar el archivo Java
with open(java_file, 'r') as file:
    java_code = file.read()
# Analizar el código Java
tokens = javalang.tokenizer.tokenize(java_code)
# Imprimir los tokens
for token in tokens:
    print(f"Token: {token.value}, Tipo: {token.__class__.__name__}")