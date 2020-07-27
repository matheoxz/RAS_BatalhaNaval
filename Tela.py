from tkinter import Tk, LabelFrame, Button, PhotoImage, Label, BOTH, Toplevel, DISABLED, HORIZONTAL, W, E, Entry, Scale
from Matrizes import Matriz
from functools import partial

class Tela(Tk):
    #pencertual medio de agua desejado 
    pma = 0.5
    #numero de navios que devem se inicializar a matriz, por padrão é apenas 1
    navios = [1 for i in range(5)]

    def __init__(self):
        super().__init__()
        self.title("Batalha Naval")
        self.iconphoto(True, PhotoImage(file = "./icons/Battleship.png"))
        self.state("normal")
        self.criaTelaMenu()
        self.mainloop()

    def checaTiro(self, x, y, jogador):
        if(jogador == 'Player'):
            mat = self.tabuleiro.MatrizBot
            print('Player', x,y)
            self.tiros_dados_player += 1
            self.tiros_dados_player_lbl.configure(text = str(self.tiros_dados_player))

            if(self.tabuleiro.checaTiro(x, y, mat) == 0):
                self.matriz_inimiga[x][y].configure(bg = "#5151B8", state = DISABLED)
                self.tiros_errados_player += 1
                self.tiros_errados_player_lbl.configure(text = str(self.tiros_errados_player))

            elif(self.tabuleiro.checaTiro(x, y, mat) == 1):
                self.matriz_inimiga[x][y].configure(bg = "#FF415A", state = DISABLED)
                self.tiros_acertados_player += 1
                self.tiros_acertados_player_lbl.configure(text = str(self.tiros_acertados_player))
            
            if (self.tiros_acertados_player== (self.navios[0]*5 + self.navios[1]*4 + self.navios[2]*3 + self.navios[3]*3 + self.navios[4]*2)):
                print("ganhou!")

        else:
            mat = self.tabuleiro.MatrizPlayer
            self.matriz_amiga[x][y].configure(bg = "#5151B8", state = DISABLED)

            if(self.tabuleiro.checaTiro(x, y, mat) == 0):
                self.matriz_amiga[x][y].configure(bg = "#5151B8", state = DISABLED)
                #self.tiros_errados_bot +=1

            elif(self.tabuleiro.checaTiro(x, y, mat) == 1):
                self.matriz_amiga[x][y].configure(bg = "#FF415A", state = DISABLED)
                #self.tiros_acertados_bot +=1

            #if (self.tiros_acertados_bot== (navios[0]*5 + navios[1]*4 + navios[2]*3 + navios[3]*3 + navios[4]*2)):
                #print("perdeu!")


        
    def criaMatrizDeBotao(self, frame, matriz_botoes, jogador):
        #pega o valor de n que for dado na tela de menu
        #cria uma matriz de botoes nxn para o player "player" ou "bot"
        #de acordo com a matriz gerada após a alocação de navios
        n = self.tabuleiro.getN()
        if jogador == 'Player':
            for i, j in Matriz.geraMatriz(Matriz, n):
                checaTiro_xy = partial(self.checaTiro, i, j, 'Player')
                matriz_botoes[i][j] = Button(frame, text = '~', height = 5, width = 10, bg = "#BFBFF2", command = checaTiro_xy)
                matriz_botoes[i][j].grid(row = i+1, column = j+1)
        
        else:
            for i, j in Matriz.geraMatriz(Matriz, n):
                matriz_botoes[i][j] = Button(frame, text = '~', height = 5, width = 10, bg = "#BFBFF2")
                self.checaTiro(i, j, 'Bot')
                matriz_botoes[i][j].grid(row = i+1, column = j+1)

    def getNumeros(self):
        self.navios[0] = int(self.carrier_entry.get())
        self.navios[1] = int(self.battleship_entry.get())
        self.navios[2] = int(self.cruiser_entry.get())
        self.navios[3] = int(self.submarine_entry.get())
        self.navios[4] = int(self.destroyer_entry.get())
        self.pma = int(self.pma_slider.get())/100
        self.config_window.destroy()
        
    def criaTelaConfigurações(self):
        self.config_window = Toplevel(self)
        #cria o frame
        frame = LabelFrame(self.config_window, text = "Configurações")
        #poe imagem de configurações
        img = PhotoImage(file = './icons/gear.png')
        img = img.subsample(8, 8)
        img_lbl = Label(frame, image = img)
        img_lbl.image = img
        img_lbl.grid(row = 0, column = 0, columnspan = 2, pady = 20)
        #insere labels
        Label(frame, text = 'Carrier (5 espaços): ').grid(row = 1, column = 0, sticky = W)
        Label(frame, text = 'Battleship (4 espaços): ').grid(row = 2, column = 0, sticky = W)
        Label(frame, text = 'Cruiser (3 espaços): ').grid(row = 3, column = 0, sticky = W)
        Label(frame, text = 'Submarine (3 espaços): ').grid(row = 4, column = 0, sticky = W)
        Label(frame, text = 'Destroyer (2 espaços): ').grid(row = 5, column = 0, sticky = W)
        Label(frame, text = 'Percentual de água: ').grid(row = 6, column = 0, sticky = W)
        #insere entradas
        self.carrier_entry = Entry(frame)
        self.carrier_entry.insert(0,str(self.navios[0]))
        self.carrier_entry.grid(row = 1, column = 1)
        self.battleship_entry = Entry(frame)
        self.battleship_entry.insert(0,str(self.navios[1]))
        self.battleship_entry.grid(row = 2, column = 1)
        self.cruiser_entry = Entry(frame)
        self.cruiser_entry.insert(0,str(self.navios[2]))
        self.cruiser_entry.grid(row = 3, column = 1)
        self.submarine_entry = Entry(frame)
        self.submarine_entry.insert(0,str(self.navios[3]))
        self.submarine_entry.grid(row = 4, column = 1)
        self.destroyer_entry = Entry(frame)
        self.destroyer_entry.insert(0,str(self.navios[4]))
        self.destroyer_entry.grid(row = 5, column = 1)
        #insere slider de pma
        self.pma_slider = Scale(frame, from_ = 10, to = 60, orient = HORIZONTAL)
        self.pma_slider.set(self.pma*100)
        self.pma_slider.grid(row = 6, column = 1)

        #insere botao de ok
        ok_button = Button(frame, text = "Salvar", command = self.getNumeros)
        ok_button.grid(row = 7, column = 0, columnspan = 2, sticky = W+E)
        #poe o frame na tela
        frame.pack(padx = 5, pady = 5)
        pass

    def Sandbox(self):
        #cria janela toplevel
        self.sandbox_window = Toplevel(self)
        self.sandbox_window.title("Sandbox")
        self.tabuleiro = Matriz(self.pma, self.navios)
        #cria o tabuleiro
        frame_tabuleiro = LabelFrame(self.sandbox_window, text = "Campo Inimigo")
        #coloca labels de coordenadas
        for i in range(self.tabuleiro.getN()):
            Label(frame_tabuleiro, text = str(i+1)).grid(row = 0, column = i+1)
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i, j in zip(alfabeto, range(self.tabuleiro.getN())):
            Label(frame_tabuleiro, text = i).grid(row = j+1, column = 0)
        #cria matriz de botoes
        self.matriz_inimiga = [[None for i in range(self.tabuleiro.getN())] for i in range(self.tabuleiro.getN())]
        #self.matriz_inimiga = self.tabuleiro.alocaNavios()
        self.criaMatrizDeBotao(frame_tabuleiro, self.matriz_inimiga, 'Player')
        frame_tabuleiro.pack()
        #cria labels de pontuação
        frame_pontuacao = LabelFrame(self.sandbox_window, text = 'Pontuação')
        #label de tiros dados
        Label(frame_pontuacao, text = 'Tiros dados: ').grid(row = 0, column = 0, sticky = W)
        self.tiros_dados_player = 0
        self.tiros_dados_player_lbl = Label(frame_pontuacao, text = str(self.tiros_dados_player))
        self.tiros_dados_player_lbl.grid(row = 0, column = 1, sticky = E)
        #label de tiros acertados
        Label(frame_pontuacao, text = 'Tiros acertados: ').grid(row = 0, column = 2, sticky = W)
        self.tiros_acertados_player = 0
        self.tiros_acertados_player_lbl = Label(frame_pontuacao, text = str(self.tiros_acertados_player))
        self.tiros_acertados_player_lbl.grid(row = 0, column = 3, sticky = E)
        #label de tiros errados
        Label(frame_pontuacao, text = 'Tiros errados: ').grid(row = 0, column = 4, sticky = W)
        self.tiros_errados_player = 0
        self.tiros_errados_player_lbl = Label(frame_pontuacao, text = str(self.tiros_errados_player))
        self.tiros_errados_player_lbl.grid(row = 0, column = 5, sticky = E)

        frame_pontuacao.pack(fill = BOTH)

    def PvE(self):
        #cria janela toplevel
        self.sandbox_window = Toplevel(self)
        self.sandbox_window.title("PvE")
        self.tabuleiro = Matriz(self.pma, self.navios)
        self.tabuleiro_amigo = Matriz(self.pma, self.navios)
        #cria o tabuleiro
        frame_tabuleiro = LabelFrame(self.sandbox_window, text = "Campo Inimigo")
        #coloca labels de coordenadas
        for i in range(self.tabuleiro.getN()):
            Label(frame_tabuleiro, text = str(i+1)).grid(row = 0, column = i+1)
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i, j in zip(alfabeto, range(self.tabuleiro.getN())):
            Label(frame_tabuleiro, text = i).grid(row = j+1, column = 0)
        #cria matriz inimiga
        self.matriz_inimiga = [[None for i in range(self.tabuleiro.getN())] for i in range(self.tabuleiro.getN())]
        #self.matriz_inimiga = self.tabuleiro.alocaNavios()
        self.criaMatrizDeBotao(frame_tabuleiro, self.matriz_inimiga, 'Player')
        frame_tabuleiro.grid(row = 0, column = 0)
        #cria labels de pontuação
        frame_pontuacao = LabelFrame(self.sandbox_window, text = 'Pontuação')
        #label de tiros dados
        Label(frame_pontuacao, text = 'Tiros dados: ').grid(row = 0, column = 0, sticky = W)
        self.tiros_dados_player = 0
        self.tiros_dados_player_lbl = Label(frame_pontuacao, text = str(self.tiros_dados_player))
        self.tiros_dados_player_lbl.grid(row = 0, column = 1, sticky = E, padx = 10)
        #label de tiros acertados
        Label(frame_pontuacao, text = 'Tiros acertados: ').grid(row = 0, column = 2, sticky = W)
        self.tiros_acertados_player = 0
        self.tiros_acertados_player_lbl = Label(frame_pontuacao, text = str(self.tiros_acertados_player))
        self.tiros_acertados_player_lbl.grid(row = 0, column = 3, sticky = E)
        #label de tiros errados
        Label(frame_pontuacao, text = 'Tiros errados: ').grid(row = 0, column = 4, sticky = W)
        self.tiros_errados_player = 0
        self.tiros_errados_player_lbl = Label(frame_pontuacao, text = str(self.tiros_errados_player))
        self.tiros_errados_player_lbl.grid(row = 0, column = 5, sticky = E)
        #poe labels na tela
        frame_pontuacao.grid(row =1, column = 0, sticky = W+E, padx = 10)

        #cria o tabuleiro
        frame_tabuleiro_amigo = LabelFrame(self.sandbox_window, text = "Campo Amigo")
        #coloca labels de coordenadas
        for i in range(self.tabuleiro.getN()):
            Label(frame_tabuleiro_amigo, text = str(i+1)).grid(row = 0, column = i+1)
        for i, j in zip(alfabeto, range(self.tabuleiro.getN())):
            Label(frame_tabuleiro_amigo, text = i).grid(row = j+1, column = 0)
        #cria matriz amiga
        self.matriz_amiga = [[None for i in range(self.tabuleiro.getN())] for i in range(self.tabuleiro.getN())]
        #self.matriz_amiga = self.tabuleiro.alocaNavios()
        self.criaMatrizDeBotao(frame_tabuleiro_amigo, self.matriz_amiga, 'Bot')
        frame_tabuleiro_amigo.grid(row = 0, column = 1, padx = 10)
        #cria labels de pontuação
        frame_pontuacao_inimigo = LabelFrame(self.sandbox_window, text = 'Pontuação do Inimigo')
        #label de tiros dados
        Label(frame_pontuacao_inimigo, text = 'Tiros dados: ').grid(row = 0, column = 0, sticky = W)
        self.tiros_dados_bot = 0
        self.tiros_dados_bot_lbl = Label(frame_pontuacao_inimigo, text = str(self.tiros_dados_bot))
        self.tiros_dados_bot_lbl.grid(row = 0, column = 1, sticky = E)
        #label de tiros acertados
        Label(frame_pontuacao_inimigo, text = 'Tiros acertados: ').grid(row = 0, column = 2, sticky = W)
        self.tiros_acertados_bot = 0
        self.tiros_acertados_bot_lbl = Label(frame_pontuacao_inimigo, text = str(self.tiros_acertados_bot))
        self.tiros_acertados_bot_lbl.grid(row = 0, column = 3, sticky = E)
        #label de tiros errados
        Label(frame_pontuacao_inimigo, text = 'Tiros errados: ').grid(row = 0, column = 4, sticky = W)
        self.tiros_errados_bot = 0
        self.tiros_errados_bot_lbl = Label(frame_pontuacao_inimigo, text = str(self.tiros_errados_bot))
        self.tiros_errados_bot_lbl.grid(row = 0, column = 5, sticky = E)
        #poe labels na tela
        frame_pontuacao_inimigo.grid(row =1, column = 1, sticky = W+E, padx = 10)
        pass

    def TelaFinal(self):
        pass

    def criaTelaMenu(self):
        #cria o frame
        frame = LabelFrame(self, text = "Batlha Naval Atlas")
        #poe imagem do navio
        img = PhotoImage(file = './icons/Battleship.png')
        img_lbl = Label(frame, image = img)
        img_lbl.image = img
        img_lbl.pack()
        #insere botao de sandbox
        sandbox_button = Button(frame, text = "Sandbox", command = self.Sandbox)
        sandbox_button.pack(padx = 5, pady = 5, fill = BOTH)
        #insere botao de pve
        pve_button = Button(frame, text = "PvE", command = self.PvE)
        pve_button.pack(padx = 5, pady = 5, fill = BOTH)
        #insere botao de configuracoes
        config_button = Button(frame, text = "Configurações", command = self.criaTelaConfigurações)
        config_button.pack(padx = 5, pady = 5, fill = BOTH)
        #insere botao de sair
        exit_button = Button(frame, text = "Sair", command = self.quit).pack(padx = 5, pady = 5, fill = BOTH)
        #poe o frame na tela
        frame.pack(padx = 5, pady = 5)


tela = Tela()