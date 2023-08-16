class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.disciplinas_cursadas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas_cursadas.append(disciplina)

    def mostar_disciplina_cursadas(self):
        return self.disciplinas_cursadas

aluno1 = Aluno("Lucas", 22)
print(f"Aluno: {aluno1.nome}\nIdade: {aluno1.idade}")

aluno1.adicionar_disciplina("História")
aluno1.adicionar_disciplina("Matemática")
aluno1.adicionar_disciplina("Geografia")
print(f"Disciplinas Adicionadas: {aluno1.mostar_disciplina_cursadas()}")