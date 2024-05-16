# Generar diagrama de transiciones
def transition_diagram(text):
    transitions = {}
    for i in range(len(text) - 1):
        current_transition = (text[i], text[i + 1])
        if current_transition in transitions:
            transitions[current_transition] += 1
        else:
            transitions[current_transition] = 1
    return transitions

# Comparar las similitudes entre los diagramas de transición
def similarity_transition_diagram(text1, text2):
    diagram1 = transition_diagram(text1)
    diagram2 = transition_diagram(text2)
    intersection = set(diagram1.keys()) & set(diagram2.keys())
    total_transitions1 = sum(diagram1.values())
    total_transitions2 = sum(diagram2.values())
    similarity = sum(min(diagram1.get(t, 0), diagram2.get(t, 0)) for t in intersection) / max(total_transitions1, total_transitions2)
    return similarity

# Ejemplo de uso
text1 = "hola"
text2 = "hola"
similarity = similarity_transition_diagram(text1, text2)
print("Similitud entre los textos:", similarity)
