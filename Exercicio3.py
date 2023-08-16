class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def atualizar_email(self, novo_email):
        self.email = novo_email

contato1 = Contato("Danilo", 21981415573, "danilo.mendes@alunos.sc.senac.br")
print(f"Nome: {contato1.nome}\nTelefone: {contato1.telefone}\nEmail: {contato1.email}")
contato1.atualizar_telefone(48981415573)
contato1.atualizar_email("danilomendes@hotmail.com")
print("\nContato Atualizado")
print(f"Nome: {contato1.nome}\nTelefone: {contato1.telefone}\nEmail: {contato1.email}")