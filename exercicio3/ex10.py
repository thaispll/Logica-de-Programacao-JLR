'''Faça uma classe Relogio com métodos para mostrar o horário atual e ajustar o horário manualmente.
'''
from datetime import datetime, timedelta

class Relogio:
    def __init__(self):
        self.hora_atual = datetime.now()

    def mostrar_horario(self):
        print("Horário atual:", self.hora_atual.strftime("%H:%M:%S"))

    def ajustar_horario(self, horas=0, minutos=0, segundos=0):
        self.hora_atual = self.hora_atual.replace(hour=horas, minute=minutos, second=segundos)
        print("Horário ajustado para:", self.hora_atual.strftime("%H:%M:%S"))

relogio = Relogio()
relogio.mostrar_horario()
relogio.ajustar_horario(15, 30, 0)
relogio.mostrar_horario()
