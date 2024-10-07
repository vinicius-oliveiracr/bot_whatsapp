import random

class jogador():
    def __init__(self, nome, funcao):
        self.nome = nome
        self.função = funcao

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
        return self.nome
    
    def get_funcao(self):
        return self.funcao
    
    def set_funcao(self, funcao):
        self.funcao = funcao
        return self.funcao

class times(jogador):

    def __init__(self, lista_participantes, valor):
        self.nome = jogador.get_nome
        self.funcao = jogador.get_funcao
        self.lista_participantes = lista_participantes
        self.valor = valor


    def get_valor(self):
        return self.valor

    def set_valor (self, valor):
        self.valor = valor
        return self.valor
    
    def get_participantes(self):
        jogadores = []
        goleiros = []
        for i in range(len(self.lista_participantess)):
            print(self.lista_participantes[i])
            if jogador.funcao == 'goleiro':
                goleiros.append(self.lista_participantes[i])
            else:
                jogadores.append(self.lista_participantes[i])

        return jogadores, goleiros
            


    def randomizer(self):
        time = []
        for i in range(0,5):
            time.append(random.choice(self.lista_participantes))

        return time
    
    def divide_valor(self):
        goleiros = 0
        for i in range(len(self.participantes)):
            if jogador.funcao == 'goleiro':
                goleiros += 1
        self.valor = self.valor / (len(self.participantes) - goleiros)


        return self.valor


