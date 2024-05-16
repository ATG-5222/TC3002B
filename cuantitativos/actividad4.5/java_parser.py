import javalang

# Cargar el archivo Java
with open('HelloWorld.java', 'r') as file:
    codigo_java = file.read()
# Analizar el código Java
tokens = javalang.tokenizer.tokenize(codigo_java)
# Imprimir los tokens
for token in tokens:
    print(f"Token: {token.value}, Tipo: {token.__class__.__name__}")
