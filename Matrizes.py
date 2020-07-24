from random import randint

class Matriz:
    coordenadas = []
    def geraMatriz(self, n):
        for x in range(n):
            for y in range(n):
                yield x,y

    def defineTamanhoMatriz(self):
        espacos=(self.navios[0]*5+self.navios[1]*4+self.navios[2]*3+self.navios[3]*3+self.navios[4]*2)/(1-self.pma)
        n=int(espacos**0.5) + 1  
        return n
    
    def getN(self):
        n=self.defineTamanhoMatriz()
        return n

    def __init__(self, pma, navios):#navios idx 0:carrier 1:battleship 2:cruiser 3:submarine 4:destroyer
        self.pma=pma #percentual mínimo de espaços com água em relação ao total
        self.navios=navios  #lista contendo a qtde de cada navio
        self.MatrizPlayer = [[x, y, 0] for x, y in self.geraMatriz(self.defineTamanhoMatriz())] #retorna um valor de n conforme a qtde
        self.MatrizBot = [[x, y, 0] for x, y in self.geraMatriz(self.defineTamanhoMatriz())]    #de navios escolhida
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
        n=self.defineTamanhoMatriz()
        coordenada = (randint(0, n-1), randint(0, n-1))
        while(coordenada in self.coordenadas):
            coordenada = (randint(0, n-1), randint(0, n-1))
        self.coordenadas.append(coordenada)
        return coordenada

    

l=[4, 1, 1, 1, 1]
m=Matriz(0.6,l)
#m.alocaNavios(m)
print(m.getN())




