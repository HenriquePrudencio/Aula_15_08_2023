class Conta_bancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def realizar_depositos(self, deposito):
        self.saldo += deposito

conta1 = Conta_bancaria(548965, "Fernando", 2442.00)
conta1.realizar_depositos(50.00)
print(f"Número: {conta1.numero}\nTitular: {conta1.titular}\nSaldo: {conta1.saldo}")