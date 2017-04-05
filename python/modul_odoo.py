#/
#-*- coding: utf-8 -*-

class Calculadora:

    def __init__(self):

        # Variables de clase
        self.capital_inicial = 100000
        self.capital_final = None
        self.interes = 0.0865
        self.temps = 15
        self.retencio = None
        self.interesos = 0;

    def cap_final(self):
        self.capital_final = self.capital_inicial * ((1 + self.interes) ** self.temps)
        print self.capital_final

    def int_generats(self):
        interesos = self.capital_final - self.capital_inicial
        print interesos

    #def ret_aplicada(selfself):


if __name__ == '__main__':

    # Creacio de l'objecte
    calc = Calculadora()
    calc.cap_final()
    calc.int_generats()
	
