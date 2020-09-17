import automato_finito_deterministico as DFA,
import re
class SymbolTable():
    def __init__(self):
        self.symbol = {}

    def addSymbol(self , token , lexeme , tipo):
        self.symbol[lexeme] = {"lexema": lexeme , "token": token , "tipo": tipo }

    def checkSymbolExistence(self , lexeme):
        if lexeme in self.symbol:
            return True
        else: 
            return False

class lexicalAnalyzer:
    def __init__(self):
        self.symbleTable = SymbolTable()
        self.DFA = DFA.DeterministicFiniteAutomaton(["a" , "b" , "c"],["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9"] , funcao_de_transicao , "s0" , ["s2"])

    def readFile(self , fileName):
        file = open(fileName,"r")

        for line in file:
            lexemes = line.split()
            print(lexemes)


def funcao_de_transicao(state , letter):
    if state == "s0":
        if re.findall("\d", letter):
            return "s1"
        elif re.findall("\w", letter):
            return "s2"
        else:
            return "Serr"

    if state == "s1":
        if re.findall("\d", letter):
            return "s1"
        elif re.findall("\w", letter):
            return "s2"
        else:
            return "err"

    if state =="s2":
        if re.findall("\w", letter):
            return "s2"
        elif re.findall("\d", letter):
            return "s1"
        else:
            return "err"


if __name__ == "__main__":
    c = SymbolTable()
    c.addSymbol("int","int","int")

    print(c.simbolo)

    d = c.checkSymbolExistence("int")
    e = c.checkSymbolExistence("batata")
    print(d , "  " , e)


