livros = [
    "Dom Casmurro",
    "Cem Anos de Solidão",
    "O Pequeno Príncipe",
    "1984",
    "A Revolução dos Bichos",
    "Orgulho e Preconceito",
    "Harry Potter e a Pedra Filosofal",
    "O Senhor dos Anéis: A Sociedade do Anel",
    "Capitães da Areia",
    "A Menina que Roubava Livros"
]

palavra_chave = input("Digite uma palavra-chave ou sequência de caracteres para buscar na lista de livros: ")

# Filtra os títulos com base na palavra-chave, ignorando maiúsculas/minúsculas
resultados = [titulo for titulo in livros if palavra_chave.lower() in titulo.lower()]

if resultados:
    print("\nTítulos encontrados:")
    for titulo in resultados:
        print("-", titulo)
else:
    print("\nNenhum título corresponde ao critério de busca.")
