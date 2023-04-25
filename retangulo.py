print("Este algoritmo calcula área e perimetro de um retângulo conhecendo seu lado e sua altura")
l = int(input("Insira o lado do retângulo:"))
h = int(input("Insira a altura do retângulo:"))
p = l + l + h + h
s = l * h
d = (l ** 2 + h ** 2) ** 0.5
print("Perimetro =", p, "e", "Área =", s, "Diagonal =", d)
