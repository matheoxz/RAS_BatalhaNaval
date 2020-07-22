from tkinter import Tk, PhotoImage
import Matrizes

class Tela(Tk):
    def __init__(self):
        super().__init__()
        self.title("Batalha Naval")
        self.iconphoto(True, PhotoImage("icons/Battleship.ico"))
        self.state("normal")
        self.mainloop()

    def criaMatrizDeBotao(self, player):
        #pega o valor de n que for dado na tela de menu
        #cria uma matriz de botoes nxn para o player "player" ou "bot"
        #de acordo com a matriz gerada após a alocação de navios

        pass

    def criaTelaMenu(self):
        pass

    def criaTelaConfigurações(self):
        pass
    
    def Sandbox(self):
        pass

    def PvE(self):
        pass

    def TelaFinal(self):
        pass


tela = Tela()
    