class tabela_de_simbolos():
    def __init__(self):
        self.simbolo = {}

    def add_simbolo(self , token , lexema , tipo):
        self.simbolo[lexema] = {"lexema": lexema , "token": token , "tipo": tipo}

    def verificacao_existencia_simbolo(self , lexema):
        if lexema in self.simbolo:
            return True
        else: 
            return False



if __name__ == "__main__":
    c = tabela_de_simbolos()
    c.add_simbolo("int","int","int")

    print(c.simbolo)

    d = c.verificacao_existencia_simbolo("int")
    e = c.verificacao_existencia_simbolo("batata")
    print(d , "  " , e)


