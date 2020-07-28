from random import randint

class Matriz:
    coordenadas = []
    def geraMatriz(self, n):
        for x in range(n):
            for y in range(n):
                yield x,y

    def defineTamanhoMatriz(self):
        espacos=(self.navios[0]*5+self.navios[1]*4+self.navios[2]*3+self.navios[3]*3+self.navios[4]*2)/(1-self.pma)
        if(self.navios[0]!=0 and espacos<25):
            n=5
        elif(self.navios[1]!=0 and espacos<16):
            n=4
        elif((self.navios[2]!=0 or self.navios[3]!=0) and espacos<9):
            n=3
        else:
            n=int(espacos**0.5)+1
        return n
    
    def getN(self):
        n=self.defineTamanhoMatriz()
        return n

    def __init__(self, pma, navios, n = None):
        self.pma=pma #percentual mínimo de espaços com água em relação ao total
        self.navios=navios  #lista contendo a qtde de cada navio
        self.n = n
        if(n == None):
            self.n = self.getN()

        self.MatrizPlayer=self.alocaNavios()
        self.MatrizBot=self.alocaNavios()
        #self.MatrizPlayer = [[0 for i in range(self.getN())] for i in range(self.getN())] #retorna um valor de n conforme a qtde
        #self.MatrizBot = [[0 for i in range(self.getN())] for i in range(self.getN())]    #de navios escolhida
        return
    
    def alocaNavios(self): #gustavo e marcos
        #carrier = 5 espaços
        #battleship = 4 espaços
        #cruiser = 3 espaços
        #submarine = 3 espaços
        #destroyer = 2 espaços
        espaco_navio=(5, 4, 3, 3, 2)  #espaço que cada navio ocupa idx 0:carrier 1:battleship 2:cruiser 3:submarine 4:destroyer
        n = self.n
        matriz_navios=[[0 for i in range(n)] for i in range(n)]
        i=0 #Tipo de navio
        qtde_navios=sum(self.navios) #quantidade total de navios
        tipo=self.navios[i] #quantidade de um tipo de navio
        while(qtde_navios>0):
            while(tipo==0):
                i+=1  
                tipo=self.navios[i]
            verifica=0 
            pos=randint(0,1)   #posição 1:horizontal 0:vertical
            c_i=[randint(0,n-1),randint(0,n-1)] #coordenada inicial e final inicializadas
            c_f=c_i.copy()
            step=1 #define o sentido da busca
            espacos_alocados=0 
            while(verifica!=2 and espacos_alocados<espaco_navio[i]): 
                if(matriz_navios[c_f[0]][c_f[1]]==0 and c_f[pos]!=-1):
                    espacos_alocados+=1
                    c_f[pos]= c_f[pos]+step if((c_f[pos]+step)<n and (c_f[pos]+step)>=0) else -1                                                                                                
                else:
                    verifica+=1 
                    espacos_alocados=0
                    c_f=c_i.copy()  #isso pode fazer a alocação ficar bem mais demorada
                    #c_i=c_f.copy()
                    step*=-1 #inverte o sentido
            if(verifica<2): #Caso verifica <2 há a possiblidade de alocar o navio no sentido determinado pelo step
                qtde_navios-=1
                tipo-=1
                for x in range(espaco_navio[i]):
                    matriz_navios[c_i[0]+step*abs(pos-1)*x][c_i[1]+step*pos*x]=1  #alocando o navio 
        return matriz_navios #retorna uma matriz com os navios alocados para poder ser atribuida a matriz do bot/player

    def checaTiro(self, x, y, mat): 
        return mat[x][y]

    def geraTiro(self):
        n=self.defineTamanhoMatriz()
        coordenada = (randint(0, n-1), randint(0, n-1))
        while(coordenada in self.coordenadas):
            coordenada = (randint(0, n-1), randint(0, n-1))
        self.coordenadas.append(coordenada)
        return coordenada

    

""" l=[1, 1, 0, 0, 1]
m=Matriz(0,l)
print(m.MatrizPlayer) """
#print(m.checaTiro(1,1, m.MatrizPlayer))
#coord = m.geraTiro()
#print(coord)
#m.checaTiro(coord, m.MatrizPlayer)

