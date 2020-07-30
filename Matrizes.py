from random import randint

class Matriz:
    
    def geraMatriz(self, n):
        for x in range(n):
            for y in range(n):
                yield x,y

    def defineTamanhoMatriz(self):
        espacos=(self.navios[0]*5+self.navios[1]*4+self.navios[2]*3+self.navios[3]*2)/(1-self.pma)
        if(self.navios[0]!=0 and espacos<25):
            n=5
        elif(self.navios[1]!=0 and espacos<16):
            n=4
        elif((self.navios[2]!=0) and espacos<9):
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
        self.coordenadas = []
        self.partes_encontradas_player = []
        self.partes_encontradas_bot = []
        self.navios_afundados_player = [0,0,0,0]
        self.navios_afundados_bot = [0,0,0,0]
        self.MatrizPlayer=self.alocaNavios()
        self.MatrizBot=self.alocaNavios()

        print('Coordnadas bot: ', self.coordenadas)
        #self.MatrizPlayer = [[0 for i in range(self.getN())] for i in range(self.getN())] #retorna um valor de n conforme a qtde
        #self.MatrizBot = [[0 for i in range(self.getN())] for i in range(self.getN())]    #de navios escolhida
        return
    
    def alocaNavios(self): #gustavo e marcos
        #carrier = 5 espaços
        #battleship = 4 espaços
        #submarine = 3 espaços
        #destroyer = 2 espaços
        espaco_navio=(5, 4, 3, 2)  #espaço que cada navio ocupa idx 0:carrier 1:battleship 2:submarine 3:destroyer
        n = self.n
        matriz_navios=[[0 for i in range(n)] for i in range(n)]
        i=0 #Tipo de navio
        qtde_navios=sum(self.navios) #quantidade total de navios
        qtde_tipo=self.navios[i] #quantidade de um tipo de navio
        while(qtde_navios>0):
            while(qtde_tipo==0):
                i+=1  
                qtde_tipo=self.navios[i]
            tipo=espaco_navio[i]
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
                for x in range(espaco_navio[i]):
                    matriz_navios[c_i[0]+step*abs(pos-1)*x][c_i[1]+step*pos*x]=(tipo,x,qtde_tipo)  #alocando o navio 
                qtde_navios-=1
                qtde_tipo-=1
        return matriz_navios #retorna uma matriz com os navios alocados para poder ser atribuida a matriz do bot/player

    def checaTiro(self, x, y, mat, player = True): 
        if player:
            navios_afundados = self.navios_afundados_player
            partes_encontradas = self.partes_encontradas_player
        else:
            navios_afundados = self.navios_afundados_bot
            partes_encontradas = self.partes_encontradas_bot
        if(mat[x][y]!=0):
            partes_encontradas.append([mat[x][y][0]]+[mat[x][y][2]])
            qtde_tipo=0
            idx=abs(mat[x][y][0]-5)
            for i in range(self.navios[idx]):
                partes=partes_encontradas.count([mat[x][y][0]]+[i+1])
                qtde_tipo+=int(partes/mat[x][y][0])
            navios_afundados[idx]=qtde_tipo

        if player:
            self.navios_afundados_player = navios_afundados
            self.partes_encontradas_player = partes_encontradas
        else:
            self.navios_afundados_bot = navios_afundados
            self.partes_encontradas_bot = partes_encontradas

        return mat[x][y],navios_afundados

    def geraTiro(self):
        n = self.n
        coordenada = (randint(0, n-1), randint(0, n-1))
        while(coordenada in self.coordenadas):
            coordenada = (randint(0, n-1), randint(0, n-1))
        self.coordenadas.append(coordenada)
        return coordenada

    

""" l=[0, 0, 2, 7]
m=Matriz(0,l)
for i in range(m.getN()):
    for j in range(m.getN()):
        m.checaTiro(i,j,m.MatrizPlayer)
print(m.navios_afundados)
print(m.partes_encontradas) """
#print(m.checaTiro(1,1, m.MatrizPlayer))
#coord = m.geraTiro()
#print(coord)
#m.checaTiro(coord, m.MatrizPlayer)

