from random import randint

class Matriz:
    coordenadas = []
    def geraMatriz(self, n):
        for x in range(n):
            for y in range(n):
                yield x,y

    def defineTamanhoMatriz(self):
        espacos=(self.navios[0]*5 + self.navios[1]*4 + self.navios[2]*3 + self.navios[3]*3 + self.navios[4]*2)/(1-self.pma)
        n=int(espacos**0.5) + 1  
        return n
    
    def getN(self):
        n=self.defineTamanhoMatriz()
        return n

    def __init__(self, pma, navios):
        self.pma=pma #percentual mínimo de espaços com água em relação ao total
        self.navios=navios  #lista contendo a qtde de cada navio
        self.MatrizPlayer = [[0 for i in range(self.getN())] for i in range(self.getN())] #retorna um valor de n conforme a qtde
        self.MatrizBot = [[0 for i in range(self.getN())] for i in range(self.getN())]    #de navios escolhida
        return
    #'''
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

    def checaTiro(self, coordenada, mat): #tentar substituir x e y por coordenada
        if mat[coordenada[0]][coordenada[1]] == 1: 
            print("navio")
        else:
            print("agua")

    def geraTiro(self):
        n=self.defineTamanhoMatriz()
        coordenada = (randint(0, n-1), randint(0, n-1))
        while(coordenada in self.coordenadas):
            coordenada = (randint(0, n-1), randint(0, n-1))
        self.coordenadas.append(coordenada)
        return coordenada

    

l=[4, 1, 1, 1, 1]
m=Matriz(0.6,l)

#print(m.checaTiro(1,1, m.MatrizPlayer))
coord = m.geraTiro()
print(coord)
m.checaTiro(coord, m.MatrizPlayer)
#m.alocaNavios(m)
#print(m.getN())
