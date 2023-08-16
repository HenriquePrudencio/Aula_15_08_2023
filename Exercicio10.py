class Passageiro:
    def __init__(self, nome, numero_passaporte):
        self.nome = nome
        self.numero_passaporte = numero_passaporte

class Voo:
    def __init__(self, numero_voo, origem, destino, capacidade_maxima):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.capacidade_maxima = capacidade_maxima
        self.reservas = []

    def verificar_lotacao(self):
        return len(self.reservas) >= self.capacidade_maxima

    def reservar_assento(self, passageiro):
        if not self.verificar_lotacao():
            nova_reserva = Reserva(passageiro, self)
            self.reservas.append(nova_reserva)
            return nova_reserva
        else:
            print("Desculpe, o voo está lotado.")

    def listar_reservas(self):
        print(f"Reservas para o Voo {self.numero_voo}:")
        for reserva in self.reservas:
            print(reserva)


class Reserva:
    def __init__(self, passageiro, voo):
        self.passageiro = passageiro
        self.voo = voo

    def __str__(self):
        return f"Passageiro: {self.passageiro.nome}, Voo: {self.voo.numero_voo}"

passageiro1 = Passageiro("Rogério", "14515")
voo1 = Voo("153", "Florianópolis", "São Paulo", 12)
voo2 = Voo("147", "Florianópolis", "Brasília", 24)

reserva1 = voo1.reservar_assento(passageiro1)
reserva2 = voo1.reservar_assento(Passageiro("Maya", "14522"))

voo2.reservar_assento(Passageiro("Alfredo", "45863"))

voo1.listar_reservas()
voo2.listar_reservas()