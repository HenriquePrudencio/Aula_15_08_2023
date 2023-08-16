class Carrinho_de_compras:
    def __init__(self):
        self.produtos = []
        self.precos = []

    def adicionar_produtos(self, produto, preco):
        self.produtos.append(produto)
        self.precos.append(preco)

    def valor_total_compra(self):
        total = sum(self.precos)
        return total

    def mostrar_produtos_carrinho(self):
        if self.produtos:
            print("Itens no carrinho:")
            for i, produto in enumerate(self.produtos):
                preco = self.precos[i]
                print(f"{produto} - R$ {preco:.2f}")
            print(f"Total da compra: R$ {self.valor_total_compra():.2f}")
        else:
            print("Carrinho vazio.")

carrinho = Carrinho_de_compras()
carrinho.adicionar_produtos("Abacate", 1.99)
carrinho.adicionar_produtos("Laranja", 0.99)
carrinho.adicionar_produtos("Abacaxi", 2.99)
carrinho.adicionar_produtos("Chocolate", 4.59)
carrinho.mostrar_produtos_carrinho()

