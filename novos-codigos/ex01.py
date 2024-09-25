# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.

# Variável que armazena uma string
nome = "João"

# Lista que armazena várias strings
nomes = ["João", "Maria", "José", "Ana"]

# Exibindo o conteúdo da variável nome

print(nome)

# Exibindo o conteúdo da lista nomes

print(nomes)

# Exibindo o conteúdo da lista nomes, utilizando um laço de repetição

for nome in nomes:
    print(nome)

# Exibindo o conteúdo da lista nomes, utilizando um laço de repetição e a função enumerate

for i, nome in enumerate(nomes):
    print(i, nome)

# Exibindo o conteúdo da lista nomes, utilizando um laço de repetição e a função enumerate, com um índice inicial

for i, nome in enumerate(nomes, 1):
    print(i, nome)

# Exibindo o conteúdo da lista nomes, utilizando um laço de repetição e a função enumerate, com um índice inicial e um índice final

for i, nome in enumerate(nomes, 1):
    if i == 3:
        break
    print(i, nome)

# Exibindo o conteúdo da lista nomes, utilizando um laço de repetição e a função enumerate, com um índice inicial e um índice final, e a função range

for i in range(1, 3):
    print(i, nomes[i])


