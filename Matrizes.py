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
    
    def alocaNavios(self): #gustavo e marcos
        #carrier = 5 espaços
        #battleship = 4 espaços
        #cruiser = 3 espaços
        #submarine = 3 espaços
        #destroyer = 2 espaços
        espaco_navio=(5, 4, 3, 3, 2)  #espaço que cada navio ocupa idx 0:carrier 1:battleship 2:cruiser 3:submarine 4:destroyer
        n=self.defineTamanhoMatriz()
        matriz_navios=[[0 for i in range(self.getN())] for i in range(n)]
        print("n= {}".format(str(n)))
        i=0 #Tipo de navio
        qtde_navios=sum(self.navios) #quantidade total de navios
        tipo=self.navios[i] #quantidade de um tipo de navio
        while(qtde_navios>0):
            print("Quantidade de navios = {}".format(str(qtde_navios)))
            if(tipo==0): #verifica se foram alocados todos os navios de um tipo
                i+=1  
                tipo=self.navios[i]
                print("Passou para o próximo tipo") 
            verifica=0 
            pos=randint(0,1)   #posição 1:horizontal 0:vertical
            print("Posição = {}".format(str(pos)))
            c_i=[randint(0,n-1),randint(0,n-1)] #coordenada inicial e final inicializadas
            print("Coordenada_i = {}".format(str(c_i)))
            c_f=c_i.copy()
            step=1 
            c=0 #Corrige o calculo do espaço do navio para o caso de a coordenada ser 0
            while(verifica!=2 and (abs(c_f[pos]-c_i[pos])+c)<espaco_navio[i]): 
                if((matriz_navios[c_f[0]][c_f[1]]==0) and (c_f[pos]+step)<n and (c_f[pos]+step)>=0): 
                    c_f[pos]+=step                                                                                               
                else:
                    verifica+=1 
                    c_f=c_i.copy()  #isso pode fazer a alocação de barcos ficar bem mais demorada
                    #c_i=c_f.copy()
                    step*=-1 #inverte o sentido
                c= 1 if(c_f[pos]==0 or c_i[pos]==0) else 0
            if(verifica<2): 
                qtde_navios-=1
                tipo-=1
                print("Espaços do navio = {}".format(str(espaco_navio[i])))
                for x in range(espaco_navio[i]):
                    matriz_navios[c_i[0]+step*abs(pos-1)*x][c_i[1]+step*pos*x]=1  #alocando o navio 
        return matriz_navios

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
print(m.alocaNavios())
#print(m.checaTiro(1,1, m.MatrizPlayer))
#coord = m.geraTiro()
#print(coord)
#m.checaTiro(coord, m.MatrizPlayer)

