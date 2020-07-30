from tkinter import Tk, LabelFrame, Button, PhotoImage, Label, BOTH, Toplevel, DISABLED, HORIZONTAL, W, E, Entry, Scale, messagebox
from Matrizes import Matriz
from functools import partial

class Tela(Tk):
    #pencertual medio de agua desejado 
    pma = 0.5
    #numero de navios que devem se inicializar a matriz, por padrão é apenas 1
    navios = [1 for i in range(4)]

    def __init__(self):
        super().__init__()
        self.title("Batalha Naval")
        self.iconphoto(True, PhotoImage(file = "./icons/Battleship.png"))
        self.state("normal")

        self.tabuleiro = Matriz(self.pma, self.navios)
        self.n = self.tabuleiro.getN()

        self.criaTelaMenu()
        self.mainloop()

    def checaTiro(self, x, y, jogador, modo = 'Sandbox', ganhou = False, incrementa = True):
        if(jogador == 'Player'):
            mat = self.tabuleiro.MatrizBot
            print('Player', x,y)
            self.tiros_dados_player += 1
            self.tiros_dados_player_lbl.configure(text = str(self.tiros_dados_player))

            tiro, afundados = self.tabuleiro.checaTiro(x, y, mat)
            print('Player', afundados)
            if(tiro == 0):
                self.matriz_inimiga[x][y].configure(bg = "#5151B8", state = DISABLED)
                if incrementa:
                    self.tiros_errados_player += 1
                    self.tiros_errados_player_lbl.configure(text = str(self.tiros_errados_player))
                

            elif(tiro[0] == 2):
                self.matriz_inimiga[x][y].configure(bg = "#2A9D8F", text = str(tiro[1]+1), fg = 'black', state = DISABLED)
                if incrementa:
                    self.tiros_acertados_player += 1
                    self.tiros_acertados_player_lbl.configure(text = str(self.tiros_acertados_player))
                    self.destroyer_acertados_lbl.configure(text = str(afundados[3])+'/'+str(self.navios[3]))

            elif(tiro[0] == 3):
                self.matriz_inimiga[x][y].configure(bg = "#E9C46A", text = str(tiro[1]+1), fg = 'black', state = DISABLED)
                if incrementa:
                    self.tiros_acertados_player += 1
                    self.tiros_acertados_player_lbl.configure(text = str(self.tiros_acertados_player))
                    self.submarine_acertados_lbl.configure(text = str(afundados[2])+'/'+str(self.navios[2]))

            elif(tiro[0] == 4):
                self.matriz_inimiga[x][y].configure(bg = "#F4A261", text = str(tiro[1]+1), fg = 'black', state = DISABLED)
                if incrementa:
                    self.tiros_acertados_player += 1
                    self.tiros_acertados_player_lbl.configure(text = str(self.tiros_acertados_player))
                    self.battleship_acertados_lbl.configure(text = str(afundados[1])+'/'+str(self.navios[1]))

            elif(tiro[0] == 5):
                self.matriz_inimiga[x][y].configure(bg = "#E76F51", text = str(tiro[1]+1), fg = 'black', state = DISABLED)
                if incrementa:
                    self.tiros_acertados_player += 1
                    self.tiros_acertados_player_lbl.configure(text = str(self.tiros_acertados_player))
                    self.carrier_acertados_lbl.configure(text = str(afundados[0])+'/'+str(self.navios[0]))
                
            
            if (self.tiros_acertados_player== (self.navios[0]*5 + self.navios[1]*4 + self.navios[2]*3 + self.navios[3]*2) and ganhou == False):
                messagebox.showinfo('VOCÊ VENCEU!', 'Parabéns!!!')
                for i, j in Matriz.geraMatriz(Matriz, self.n):
                    self.checaTiro(i, j, 'Player', ganhou = True, incrementa = False)
                for i, j in Matriz.geraMatriz(Matriz, self.n):
                    self.checaTiro(i, j, 'Bot', ganhou = True, incrementa = False)
                return

        else:
            mat = self.tabuleiro.MatrizPlayer
            self.tiros_dados_bot += 1
            self.tiros_dados_bot_lbl.configure(text = str(self.tiros_dados_bot))
            print('Bot', x,y)
            tiro, afundados = self.tabuleiro.checaTiro(x, y, mat, player= False)
            print('Bot', afundados)
            if(tiro == 0):
                self.matriz_amiga[x][y].configure(bg = "#5151B8", state = DISABLED)
                if incrementa:
                    self.tiros_errados_bot += 1
                    self.tiros_errados_bot_lbl.configure(text = str(self.tiros_errados_bot))

            elif(tiro[0] == 2):
                self.matriz_amiga[x][y].configure(bg = "#2A9D8F", text = str(tiro[1]+1), fg = 'black', state = DISABLED)
                if incrementa:
                    self.tiros_acertados_bot += 1
                    self.tiros_acertados_bot_lbl.configure(text = str(self.tiros_acertados_bot))
                    self.destroyer_acertados_bot_lbl.configure(text = str(afundados[3])+'/'+str(self.navios[3]))

            elif(tiro[0] == 3):
                self.matriz_amiga[x][y].configure(bg = "#E9C46A", text = str(tiro[1]+1), fg = 'black', state = DISABLED)
                if incrementa:
                    self.tiros_acertados_bot += 1
                    self.tiros_acertados_bot_lbl.configure(text = str(self.tiros_acertados_bot))
                    self.submarine_acertados_bot_lbl.configure(text = str(afundados[2])+'/'+str(self.navios[2]))

            elif(tiro[0] == 4):
                self.matriz_amiga[x][y].configure(bg = "#F4A261", text = str(tiro[1]+1), fg = 'black', state = DISABLED)
                if incrementa:
                    self.tiros_acertados_bot += 1
                    self.tiros_acertados_bot_lbl.configure(text = str(self.tiros_acertados_bot))
                    self.battleship_acertados_bot_lbl.configure(text = str(afundados[1])+'/'+str(self.navios[1]))

            elif(tiro[0] == 5):
                self.matriz_amiga[x][y].configure(bg = "#E76F51", text = str(tiro[1]+1), fg = 'black', state = DISABLED)
                if incrementa:
                    self.tiros_acertados_bot += 1
                    self.tiros_acertados_bot_lbl.configure(text = str(self.tiros_acertados_bot))
                    self.carrier_acertados_bot_lbl.configure(text = str(afundados[0])+'/'+str(self.navios[0]))

            if (self.tiros_acertados_bot== (self.navios[0]*5 + self.navios[1]*4 + self.navios[2]*3 + self.navios[3]*2) and ganhou == False):
                messagebox.showinfo('VOCÊ PERDEU!', 'Que pena!!!')
                for i, j in Matriz.geraMatriz(Matriz, self.n):
                    self.checaTiro(i, j, 'Player', ganhou = True, incrementa = False)
                for i, j in Matriz.geraMatriz(Matriz, self.n):
                    self.checaTiro(i, j, 'Bot', ganhou = True, incrementa = False)
                
                
            #if (self.tiros_acertados_bot== (navios[0]*5 + navios[1]*4 + navios[2]*3 + navios[3]*3 + navios[4]*2)):
                #print("perdeu!")
        
        if modo == 'PvE' and not ganhou:
            i, j = self.tabuleiro_amigo.geraTiro(self.tabuleiro.MatrizPlayer)
            self.checaTiro(i, j, 'Bot')

        
    def criaMatrizDeBotao(self, frame, matriz_botoes, jogador, modo = 'Sandbox'):
        #pega o valor de n que for dado na tela de menu
        #cria uma matriz de botoes nxn para o player "player" ou "bot"
        #de acordo com a matriz gerada após a alocação de navios
        if self.n < 8:
            x = 5
            y = 10
        else:
            x = 3
            y = 5
        if jogador == 'Player':
            for i, j in Matriz.geraMatriz(Matriz, self.n):
                checaTiro_xy = partial(self.checaTiro, i, j, 'Player', modo = modo)
                matriz_botoes[i][j] = Button(frame, text = '~', height = x, width = y, bg = "#BFBFF2", command = checaTiro_xy)
                matriz_botoes[i][j].grid(row = i+1, column = j+1)
        
        else:
            for i, j in Matriz.geraMatriz(Matriz, self.n):
                matriz_botoes[i][j] = Button(frame, text = '~', height = x, width = y, bg = "#BFBFF2", state = DISABLED)
                checaTiro_xy = partial(self.checaTiro, i, j, 'Bot')
                matriz_botoes[i][j].grid(row = i+1, column = j+1)

    def getNumeros(self):
        try:
            self.navios[0] = int(self.carrier_entry.get())
            self.navios[1] = int(self.battleship_entry.get())
            self.navios[2] = int(self.submarine_entry.get())
            self.navios[3] = int(self.destroyer_entry.get())
            self.pma = int(self.pma_slider.get())/100
            self.n_user = int(self.n_entry.get())
            self.n = self.tabuleiro.getN()
            assert self.n_user >= self.n, 'O tamanho da matriz deve ser no mínimo {}'.format(self.n)
            if(self.n_user > self.n):
                self.n = self.n_user
            assert self.n > 0 and self.n <= 13, 'O tamanho da matriz deve ser no máximo 13'
            
        except Exception as e:
            messagebox.showwarning('Tamanho da matriz demasiado grande', e)
        else:
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
        Label(frame, text = 'Submarine (3 espaços): ').grid(row = 3, column = 0, sticky = W)
        Label(frame, text = 'Destroyer (2 espaços): ').grid(row = 4, column = 0, sticky = W)
        Label(frame, text = 'Percentual de água: ').grid(row = 5, column = 0, sticky = W)
        Label(frame, text = 'Tamanho do tabuleiro').grid(row = 6, column = 0, sticky = W)
        #insere entradas
        self.carrier_entry = Entry(frame)
        self.carrier_entry.insert(0,str(self.navios[0]))
        self.carrier_entry.grid(row = 1, column = 1)
        self.battleship_entry = Entry(frame)
        self.battleship_entry.insert(0,str(self.navios[1]))
        self.battleship_entry.grid(row = 2, column = 1)
        self.submarine_entry = Entry(frame)
        self.submarine_entry.insert(0,str(self.navios[2]))
        self.submarine_entry.grid(row = 3, column = 1)
        self.destroyer_entry = Entry(frame)
        self.destroyer_entry.insert(0,str(self.navios[3]))
        self.destroyer_entry.grid(row = 4, column = 1)
        self.n_entry = Entry(frame)
        self.n_entry.insert(0, str(self.n))
        self.n_entry.grid(row = 6, column = 1)
        #insere slider de pma
        self.pma_slider = Scale(frame, from_ = 10, to = 60, orient = HORIZONTAL)
        self.pma_slider.set(self.pma*100)
        self.pma_slider.grid(row = 5, column = 1)

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
        self.tabuleiro = Matriz(self.pma, self.navios, n = self.n)
        #cria o tabuleiro
        frame_tabuleiro = LabelFrame(self.sandbox_window, text = "Campo Inimigo")
        #coloca labels de coordenadas
        for i in range(self.n):
            Label(frame_tabuleiro, text = str(i+1)).grid(row = 0, column = i+1)
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i, j in zip(alfabeto, range(self.n)):
            Label(frame_tabuleiro, text = i).grid(row = j+1, column = 0)
        #cria matriz de botoes
        self.matriz_inimiga = [[None for i in range(self.n)] for i in range(self.n)]
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
        #labels navios
        #carrier
        Label(frame_pontuacao, text = 'Carrier: ').grid(row = 1, column = 0, sticky = W)
        self.carrier_acertados_lbl = Label(frame_pontuacao, text = '0/'+str(self.navios[0]))
        self.carrier_acertados_lbl.grid(row = 1, column = 1, sticky = E)
        #battleship
        Label(frame_pontuacao, text = 'Battleship: ').grid(row = 2, column = 0, sticky = W)
        self.battleship_acertados_lbl = Label(frame_pontuacao, text = '0/'+str(self.navios[1]))
        self.battleship_acertados_lbl.grid(row = 2, column = 1, sticky = E)
        #submarine
        Label(frame_pontuacao, text = 'Submarine: ').grid(row = 3, column = 0, sticky = W)
        self.submarine_acertados_lbl = Label(frame_pontuacao, text = '0/'+str(self.navios[2]))
        self.submarine_acertados_lbl.grid(row = 3, column = 1, sticky = E)
        #destroyer
        Label(frame_pontuacao, text = 'Destroyer: ').grid(row = 4, column = 0, sticky = W)
        self.destroyer_acertados_lbl = Label(frame_pontuacao, text = '0/'+str(self.navios[3]))
        self.destroyer_acertados_lbl.grid(row = 4, column = 1, sticky = E)
        
        frame_pontuacao.pack(fill = BOTH)

    def PvE(self):
        #cria janela toplevel
        self.sandbox_window = Toplevel(self)
        self.sandbox_window.title("PvE")
        self.tabuleiro = Matriz(self.pma, self.navios, n = self.n)
        self.tabuleiro_amigo = Matriz(self.pma, self.navios, n = self.n)
        #cria o tabuleiro
        frame_tabuleiro = LabelFrame(self.sandbox_window, text = "Campo Inimigo")
        #coloca labels de coordenadas
        for i in range(self.n):
            Label(frame_tabuleiro, text = str(i+1)).grid(row = 0, column = i+1)
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i, j in zip(alfabeto, range(self.n)):
            Label(frame_tabuleiro, text = i).grid(row = j+1, column = 0)
        #cria matriz inimiga
        self.matriz_inimiga = [[None for i in range(self.n)] for i in range(self.n)]
        #self.matriz_inimiga = self.tabuleiro.alocaNavios()
        self.criaMatrizDeBotao(frame_tabuleiro, self.matriz_inimiga, 'Player', modo = 'PvE')
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
        #labels navios
        #carrier
        Label(frame_pontuacao, text = 'Carrier: ').grid(row = 1, column = 0, sticky = W)
        self.carrier_acertados_lbl = Label(frame_pontuacao, text = '0/'+str(self.navios[0]))
        self.carrier_acertados_lbl.grid(row = 1, column = 1, sticky = E)
        #battleship
        Label(frame_pontuacao, text = 'Battleship: ').grid(row = 2, column = 0, sticky = W)
        self.battleship_acertados_lbl = Label(frame_pontuacao, text = '0/'+str(self.navios[1]))
        self.battleship_acertados_lbl.grid(row = 2, column = 1, sticky = E)
        #submarine
        Label(frame_pontuacao, text = 'Submarine: ').grid(row = 3, column = 0, sticky = W)
        self.submarine_acertados_lbl = Label(frame_pontuacao, text = '0/'+str(self.navios[2]))
        self.submarine_acertados_lbl.grid(row = 3, column = 1, sticky = E)
        #destroyer
        Label(frame_pontuacao, text = 'Destroyer: ').grid(row = 4, column = 0, sticky = W)
        self.destroyer_acertados_lbl = Label(frame_pontuacao, text = '0/'+str(self.navios[3]))
        self.destroyer_acertados_lbl.grid(row = 4, column = 1, sticky = E)
        #poe labels na tela
        frame_pontuacao.grid(row =1, column = 0, sticky = W+E, padx = 10)

        #cria o tabuleiro
        frame_tabuleiro_amigo = LabelFrame(self.sandbox_window, text = "Campo Amigo")
        #coloca labels de coordenadas
        for i in range(self.n):
            Label(frame_tabuleiro_amigo, text = str(i+1)).grid(row = 0, column = i+1)
        for i, j in zip(alfabeto, range(self.n)):
            Label(frame_tabuleiro_amigo, text = i).grid(row = j+1, column = 0)
        #cria matriz amiga
        self.matriz_amiga = [[None for i in range(self.n)] for i in range(self.n)]
        #self.matriz_amiga = self.tabuleiro.alocaNavios()
        self.criaMatrizDeBotao(frame_tabuleiro_amigo, self.matriz_amiga, 'Bot', modo= 'PvE')
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
        #labels navios
        #carrier
        Label(frame_pontuacao_inimigo, text = 'Carrier: ').grid(row = 1, column = 0, sticky = W)
        self.carrier_acertados_bot_lbl = Label(frame_pontuacao_inimigo, text = '0/'+str(self.navios[0]))
        self.carrier_acertados_bot_lbl.grid(row = 1, column = 1, sticky = E)
        #battleship
        Label(frame_pontuacao_inimigo, text = 'Battleship: ').grid(row = 2, column = 0, sticky = W)
        self.battleship_acertados_bot_lbl = Label(frame_pontuacao_inimigo, text = '0/'+str(self.navios[1]))
        self.battleship_acertados_bot_lbl.grid(row = 2, column = 1, sticky = E)
        #submarine
        Label(frame_pontuacao_inimigo, text = 'Submarine: ').grid(row = 3, column = 0, sticky = W)
        self.submarine_acertados_bot_lbl = Label(frame_pontuacao_inimigo, text = '0/'+str(self.navios[2]))
        self.submarine_acertados_bot_lbl.grid(row = 3, column = 1, sticky = E)
        #destroyer
        Label(frame_pontuacao_inimigo, text = 'Destroyer: ').grid(row = 4, column = 0, sticky = W)
        self.destroyer_acertados_bot_lbl = Label(frame_pontuacao_inimigo, text = '0/'+str(self.navios[3]))
        self.destroyer_acertados_bot_lbl.grid(row = 4, column = 1, sticky = E)
        #poe labels na tela
        frame_pontuacao_inimigo.grid(row =1, column = 1, sticky = W+E, padx = 10)

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