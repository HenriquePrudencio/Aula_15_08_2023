class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def atualizar_ano_publicacao(self, novo_ano):
        self.ano_publicacao = novo_ano

    def exibir_detalhes(self):
        print("Detalhes do Livro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Gênero: {self.genero}")

livro1 = Livro("Percy Jackson e o Mar de Monstros", "Rick Riordan", 2011, "Fantasia")
livro1.exibir_detalhes()

livro1.atualizar_ano_publicacao(2012)
print("\nAtualizado")
livro1.exibir_detalhes()