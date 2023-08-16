class Tarefa:
    def __init__(self, descricao, data_criacao):
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def exibir_detalhes(self):
        status = "Concluída" if self.concluida else "Não concluída"
        print("Detalhes da Tarefa:")
        print(f"Descrição: {self.descricao}")
        print(f"Data de Criação: {self.data_criacao}")
        print(f"Status: {status}")

tarefa = Tarefa("Fazer Faxina", "15/08/2023")
tarefa.exibir_detalhes()
print("\n")
tarefa.marcar_concluida()
tarefa.exibir_detalhes()