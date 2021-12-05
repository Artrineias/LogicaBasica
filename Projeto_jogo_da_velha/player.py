class player:
    def __init__(self,nome,jogada):
        self.player = nome 
        self.jogada = jogada
    
    def joga(self,jogada):
        self.posiçoes = []
        self.posiçoes.append(jogada)
        return self.posiçoes
