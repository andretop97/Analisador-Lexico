import automato_finito_deterministico as DFA
import re

numeros = ["0","1","2","3","4","5","6","7","8","9"]
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
class SymbolTable():
    def __init__(self):
        self.symbol = {}

    def addSymbol(self , token , lexeme , tipo):
        self.symbol[lexeme] = {"lexema": lexeme , "token": token , "tipo": tipo }

    def checkSymbolExistence(self , lexeme):
        return lexeme in self.symbol
        
class LexicalAnalyzer:
    def __init__(self):
        self.symbleTable = SymbolTable()
        self.DFA = DFA.DeterministicFiniteAutomaton( numeros + letras ,["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9"] , funcao_de_transicao , "s0" , ["s2"])

    def readFile(self , fileName):
        state = "s0"
        lexema = ""
        listaLexemas = []
        file = open(fileName,"r")
        for line in file:
            for character in line:
                nextState = self.DFA.nextState(state,character)
                if nextState == "Se":
                    listaLexemas.append([lexema, state])
                    state = "s0"
                    lexema = ""
                else:
                    state = nextState
                    lexema = lexema + character

        print(listaLexemas)



def funcao_de_transicao(state , letter):
    if state == "s0":
        if re.findall("\d", letter):
            return "s1"
        elif re.findall("\w", letter):
            return "s2"
        else:
            return "Se"

    if state == "s1":
        if re.findall("\d", letter):
            return "s1"
        elif re.findall("\w", letter):
            return "s2"
        else:
            return "Se"

    if state =="s2":
        if re.findall("\w", letter):
            return "s2"
        elif re.findall("\d", letter):
            return "s1"
        else:
            return "Se"


if __name__ == "__main__":
    # testeSymbolTable = SymbolTable()
    # testeSymbolTable.addSymbol("int","int","int")
    # testeDFA = DFA.DeterministicFiniteAutomaton(["a" , "b" , "c"],["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9"] , funcao_de_transicao , "s0" , ["s2"])
    # print(testeSymbolTable.symbol)
    # d = testeSymbolTable.checkSymbolExistence("int")
    # e = testeSymbolTable.checkSymbolExistence("batata")
    # print(d , "  " , e)

    testeLexicalAnalyzer = LexicalAnalyzer()

    testeLexicalAnalyzer.readFile("text.txt")

