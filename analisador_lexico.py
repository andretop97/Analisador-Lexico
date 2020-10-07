from funcao_de_transicao import *

class SymbolTable():
    def __init__(self):
        self.symbol = {}

    def addSymbol(self , lexeme , token , tipo):
        if not self.checkSymbolExistence(lexeme):
            self.symbol[lexeme] = {"lexema": lexeme , "token": token , "tipo": tipo }

    def checkSymbolExistence(self , lexeme):
        return lexeme in self.symbol


class DeterministicFiniteAutomaton:
    def __init__ (self , alphabet , states , transitionFunction , initialState , validStates):
        self.alphabet = alphabet
        self.states = states
        self.transitionFunction = transitionFunction
        self.initialState = initialState
        self.validStates = validStates

    # Função que verifica se o estado atual é final valido
    def isValidFinalState(self , currentState) :
        return currentState in self.validStates

    # Função que verifica se o simbolo pertecen ao alfabeto do nosso DFA
    def isValidSymbol(self , symbol):
        return symbol in self.alphabet

    # Função que recebe estado e o simbolo , para a paritr dele e da função de transição retornar o proximo estado
    def nextState(self , currentState, symbol):
        if self.isValidSymbol(symbol) or currentState =="s8":
            return self.transitionFunction(currentState , symbol)
        else:
            return ["SE", "1"]




class LexicalAnalyzer:
    def __init__(self):
        self.symbleTable = SymbolTable()
        self.DFA = DeterministicFiniteAutomaton( alphabet, estados, funcao_de_transicao , "s0" , valid_states)
        self.errors = []
        self.initSymbleTable()

    def initSymbleTable(self):
        self.symbleTable.addSymbol("inicio","inicio","")
        self.symbleTable.addSymbol("varinicio","varinicio","")
        self.symbleTable.addSymbol("varfim","varfim","")
        self.symbleTable.addSymbol("escreva","escreva","")
        self.symbleTable.addSymbol("leia","leia","")
        self.symbleTable.addSymbol("se","se","")
        self.symbleTable.addSymbol("entao","entao","")
        self.symbleTable.addSymbol("fimse","fimse","")
        self.symbleTable.addSymbol("fim","fim","")
        self.symbleTable.addSymbol("inteiro","inteiro","")
        self.symbleTable.addSymbol("lit","lit","")
        self.symbleTable.addSymbol("real","real","")

    def lexicon(self, lexeme):
        if self.symbleTable.checkSymbolExistence(lexeme):
            return self.symbleTable.symbol[lexeme]
        else:
            print("Lexema não encontrado")
            return []

    def readFile(self , fileName):
        state = ["s0","Estado inicial"]
        lexema = ""
        erro = ""
        lineNumber = 1
        columnNumber = 0
        file = open(fileName,"r") #Lê o arquivo indicado
        for line in file:
            for character in line: #Passa por todos os símbolos do arquivo um a um
                currentState = self.DFA.nextState(state[0],character)
                if currentState[0] == "Se" or currentState[0] == "SE":
                    specialState = self.DFA.nextState("s0",character)
                    if character == " "  or character == "\n": #Determinando as condições para para de ler um lexema e registrar ele
                        if state[0] == "s8": #Os estados descritos aqui são os q indicam estar dentro de aspas ou chaves
                            self.errors.append([erro,lineNumber, columnNumber, "3"])
                        elif state[0] == "s12":
                            self.errors.append([erro,lineNumber, columnNumber, "4"])
                        elif erro != "": #Caso já esteja registrando um falso lexema continua até ele terminar
                            self.errors.append([erro,lineNumber, columnNumber, "2"])
                            erro = ""
                        elif self.DFA.isValidFinalState(state[0]): #Registra os lexemas
                            self.symbleTable.addSymbol(lexema, state[1], "")
                        state = ["s0","Estado inicial"]
                        lexema = ""

                    elif specialState[0] != "Se" and currentState[0] != "SE":
                        self.symbleTable.addSymbol(lexema, state[1], "") #######
                        state = specialState
                        lexema = character
                       

                    else: #Não para de registrar qdo encontra um simbolo inválido, mas guarda ele separadamente
                        state = currentState
                        erro = lexema + erro + character
                        lexema = ""

                else: #Continua a contruir um lexema
                    state = currentState
                    lexema = lexema + character

                columnNumber +=1
            columnNumber = 0
            lineNumber += 1
        else: #Registra o último lexema do arquivo
            if self.DFA.isValidFinalState(state[0]):
                self.symbleTable.addSymbol(lexema, state[1], "") ##################


if __name__ == "__main__":

    testeLexicalAnalyzer = LexicalAnalyzer()
    testeLexicalAnalyzer.readFile("programa_fonte.txt")
    # testeLexicalAnalyzer.readFile("text.txt")

    a = testeLexicalAnalyzer.lexicon("batata")
    print(a)
    
    print("\nTabela de símbolos")
    for item in testeLexicalAnalyzer.symbleTable.symbol:
        print(testeLexicalAnalyzer.symbleTable.symbol[item])

    print("\nErros")
    for erro in testeLexicalAnalyzer.errors:
        print("Erro: " , erro[0] , " na linha: " , erro[1] , " e coluna: " , erro[2], Dicionario_de_erros[erro[3]])




