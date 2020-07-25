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
        #carrier = 5 espaços
        #battleship = 4 espaços
        #cruiser = 3 espaços
        #submarine = 3 espaços
        #destroyer = 2 espaços
        espaco_navio=(5, 4, 3, 3, 2)  #espaço que cada navio ocupa idx 0:carrier 1:battleship 2:cruiser 3:submarine 4:destroyer
        n=self.defineTamanhoMatriz()
        i=0 #Tipo de navio
        qtde_navios=sum(self.navios) #quantidade total de navios
        tipo=self.navios[i] #quantidade de um tipo de navio
        while(qtde_navios>0):
            print("Quantidade de navios = {}".format(str(qtde_navios)))
            if(tipo==0): #verifica se foram alocados todos os navios de um tipo
                i+=1  
                tipo=self.navios[i]
                print("Passou para o próximo tipo") 
            verifica=0 #Variável para verificar se a posição contêm um 0 ou 1
            pos=randint(1,2)   #posição 1:horizontal 2:vertical
            print("Posição = {}".format(str(pos)))
            coordenada_i=randint(0,n**2-1) #coordenada inicial e final inicializadas
            print("Coordenada = {}".format(str(coordenada_i)))
            coordenada_f=coordenada_i
            linha=int(coordenada_i/n)+1 #determina a linha da coordenada aleatória
            coluna=int(coordenada_i%n)  #determina a coluna da coordenada aleatória
            if(pos==1):
                step=1 #percorre as colunas
            else:
                step=n #percorre as linhas
            while(verifica!=2 and (coordenada_f-coordenada_i)<=espaco_navio[i]): 
                if(pos==1): #procura na horizontal
                    if((player.MatrizPlayer[coordenada_f][2]==0) and (coordenada_f+step)<(linha*n) and (coordenada_f+step)>=((linha-1)*n)): #verifica se o proximo passo está dentro do limite 
                        coordenada_f+=step                                                                                                  #de linha
                    else:
                        verifica+=1 
                        coordenada_f=coordenada_i #repensar
                        step*=-1 #inverte o sentido
                else:  #procura na vertical
                    if((player.MatrizPlayer[coordenada_f][2]==0) and (coordenada_f+step)<(n**2-(n-coluna)) and (coordenada_f+step)>=coluna): #verifica se o proximo passo está dentro do limite 
                        coordenada_f+=step                                                                                                   #de coluna
                    else:
                        verifica+=1 
                        coordenada_f=coordenada_i
                        step*=-1
            if(verifica<2): 
                qtde_navios-=1
                tipo-=1
                x=0
                print("Espaços do navio = {}".format(str(espaco_navio[i])))
                print("Step = {}".format(str(step)))
                while(x<espaco_navio[i]):
                    player.MatrizPlayer[coordenada_i+(step*x)][2]=1  #alocando o navio 
                    x+=1
                print(player.MatrizPlayer)
        return

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
