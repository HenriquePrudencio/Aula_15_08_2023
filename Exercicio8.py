class Sensor:
    def __init__(self, identificador, unidade_medida, valor_temperatura_atual):
        self.identificador = identificador
        self.unidade_medida = unidade_medida
        self.valor_temperatura_atual = valor_temperatura_atual

    def atualizadar_temperatura(self, nova_temperatura):
        self.valor_temperatura_atual = nova_temperatura

    def exibir_leitura(self):
        print(f"Leitura Atual: {self.valor_temperatura_atual}")

sensor = Sensor("KQI8795", "Celcius", 29.2)
print(f"Identificador: {sensor.identificador}\nUnidade de Medida: {sensor.unidade_medida}"
      f"\nValor Temperatura Atual: {sensor.valor_temperatura_atual}")
sensor.atualizadar_temperatura(22.8)
print("\nAtualização de Temperatura")
print(f"Identificador: {sensor.identificador}\nUnidade de Medida: {sensor.unidade_medida}"
      f"\nValor Temperatura Atual: {sensor.valor_temperatura_atual}")