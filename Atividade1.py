class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_dados(self):
        print(f"Carro marca: {self.marca}\nmodelo {self.modelo}")

carro_1 = Carro("Ford", "Edge").mostrar_dados()
carro_2 = Carro("Mercedes", "Amg").mostrar_dados()