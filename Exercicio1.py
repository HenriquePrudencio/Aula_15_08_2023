class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
        else:
            print("Quantidade de estoque insuficiente")

    def valor_total_estoque(self):
        return self.preco * self.estoque

produto1 = Produto("Mouse", 59.99, 35)
print(f"Produto: {produto1.nome}\nPreço: R$ {produto1.preco:.2f}\nQuantidade em estoque: {produto1.estoque}")

produto1.adicionar_estoque(15)
print(f"Quantidade em estoque após adicionar: {produto1.estoque}")

produto1.remover_estoque(12)
print(f"Quantidade em estoque após remover: {produto1.estoque}")

valor_total = produto1.valor_total_estoque()
print(f"Valor total em estoque: R$ {valor_total:.2f}")
