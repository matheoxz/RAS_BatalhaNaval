from random import randint

class Matriz:
    coordenadas = []
    def geraMatriz(self, n):
        for x in range(n):
            for y in range(n):
                yield x,y

    def __init__(self, n):
        self.n = n
        self.MatrizPlayer = [(x, y, 0) for x, y in self.geraMatriz(n)]
        self.MatrizBot = [(x, y, 0) for x, y in self.geraMatriz(n)]
        return

    def alocaNavios(self, player, carrier = 1, battleship = 1, cruiser = 1, submarine = 1, destroyer = 1): #gustavo e marcos
        #poe navios na matriz de maneira aleatoria
        #deve checar o tamanho do navio e a quantidade destes
        #por padrão tem-se um único navio de cada, pode-se mudar pelas configurações do jogo
        #tipos de navios e seus tamanhos
            #carrier = 5 espaços
            #battleship = 4 espaços
            #cruiser = 3 espaços
            #submarine = 3 espaços
            #destroyer = 2 espaços
        pass

    def checaTiro(self, coordenada): #lucas e iris, checar se o tiro sorteado acertou um navio ou a agua
        pass

    def geraTiro(self):
        coordenada = (randint(0, self.n-1), randint(0, self.n-1))
        while(coordenada in self.coordenadas):
            coordenada = (randint(0, self.n-1), randint(0, self.n-1))
        self.coordenadas.append(coordenada)
        return coordenada

    



