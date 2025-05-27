class Biblioteca:
    def __init__(self):
        self._colecao_livros = ()
        self.lista_livros = []

    def adicionar_livro(self, titulo, autor, ano):
        novo_livro = (titulo, autor, ano)
        self._colecao_livros += (novo_livro,)  # Atualiza a tupla imutável
        self.lista_livros.append(novo_livro)  # Atualiza a lista mutável

    def consultar_colecao(self):
        return self._colecao_livros

    def consultar_lista(self):
        return self.lista_livros


# Criando uma biblioteca e adicionando livros
biblioteca = Biblioteca()
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
biblioteca.adicionar_livro("O Cortiço", "Aluísio Azevedo", 1890)

# Consultando os dados
print("Tupla (coleção de livros):", biblioteca.consultar_colecao())
print("Lista (livros cadastrados):", biblioteca.consultar_lista())
