class Pedido:
    def __init__(self, numero, data):
        self.numero = numero
        self.data = data
        self.itens = []

    def adicionar_itens(self, iten):
        self.itens.append(iten)

    def mostar_itens(self):
        return self.itens

pedido = Pedido(458, "15/08/2023")
pedido.adicionar_itens("Milho")
pedido.adicionar_itens("Ervilha")
pedido.adicionar_itens("Salsicha")
pedido.adicionar_itens("Batata Palha")
pedido.adicionar_itens("Pão de Cachorro Quente")
pedido.adicionar_itens("Molho de Tomate")
pedido.adicionar_itens("Cebola")
pedido.adicionar_itens("Alho")
pedido.adicionar_itens("Ketchup")
pedido.adicionar_itens("Maionese")
pedido.adicionar_itens("Mostarda")
pedido.adicionar_itens("Queijo Ralado")
print(f"Numero: {pedido.numero}\nData: {pedido.data}\nItens: {pedido.itens}")
