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
        if self.isValidSymbol(symbol) or currentState[0] =="s8" or currentState[0] =="s12":
            return self.transitionFunction(currentState , symbol)
        else:
            return ["Se", "1"]


class LexicalAnalyzer:
    def __init__(self):
        self.symbleTable = SymbolTable()
        self.DFA = DeterministicFiniteAutomaton( alphabet, estados, funcao_de_transicao , initialState , valid_states)
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
        return open(fileName,"r") #Lê o arquivo indicado

    def analyzer(self , fileName):
        state = initialState
        lexema = ""
        erro = ""
        lineNumber = 1
        columnNumber = 0
        file = self.readFile(fileName)
        for line in file:
            for character in line: #Passa por todos os símbolos do arquivo um a um
                currentState = self.DFA.nextState(state, character)
                if currentState[0] == "Se":
                    specialState = self.DFA.nextState(initialState, character)
                    if character == " "  or character == "\n": #Determinando as condições para para de ler um lexema e registrar ele
                        if erro != "": #Caso já esteja registrando um falso lexema continua até ele terminar
                            self.errors.append([erro,lineNumber, columnNumber, currentState[1]])
                            erro = ""
                        elif self.DFA.isValidFinalState(state[0]): #Registra os lexemas
                            self.symbleTable.addSymbol(lexema, state[1], "")
                        state = initialState
                        lexema = ""
                    elif specialState[0] != "Se" and currentState[1] != "1":#Permite que seja salvo um lexema logo após outro sem um espaço em branco
                        self.symbleTable.addSymbol(lexema, state[1], "")
                        state = specialState
                        lexema = character
                    else: #Não para de registrar qdo encontra um simbolo inválido, mas guarda ele separadamente
                        state = currentState
                        erro = lexema + erro + character
                        lexema = ""
                elif state[0] == "s8" or state[0] == "s12": #O estado descrito aqui adiciona um erro caso a linha termine sem fechar aspas
                    if state[0] == "s8" and character == '"':
                        lexema =  lexema + character
                        self.symbleTable.addSymbol(lexema, currentState[1], "")
                        state = initialState
                        lexema = ""
                    elif state[0] == "s12" and character == "}":
                        state = initialState
                        lexema = ""
                    elif character == "\n" or character == EOFError:
                        self.errors.append([lexema,lineNumber, columnNumber, currentState[1]])
                        lexema = ""
                        state = initialState
                    else:
                        lexema = lexema + character


                else: #Continua a contruir um lexema
                    state = currentState
                    lexema = lexema + character

                columnNumber +=1
            columnNumber = 0
            lineNumber += 1
        else: #Registra o último lexema do arquivo
            if self.DFA.isValidFinalState(state[0]):
                self.symbleTable.addSymbol(lexema, state[1], "")
            else:
                if state[0] == "s8" or state[0] == "s12":
                    self.errors.append([lexema,lineNumber, columnNumber, currentState[1]])
                else:
                    self.errors.append([erro,lineNumber, columnNumber, currentState[1]])               


if __name__ == "__main__":

    testeLexicalAnalyzer = LexicalAnalyzer()
    testeLexicalAnalyzer.analyzer("programa_fonte.txt")
    #testeLexicalAnalyzer.analyzer("text.txt")

    print("\nTabela de símbolos")
    for item in testeLexicalAnalyzer.symbleTable.symbol:
        print(testeLexicalAnalyzer.symbleTable.symbol[item])

    print("\nErros")
    for erro in testeLexicalAnalyzer.errors:
        print("Erro: " , erro[0] , " na linha: " , erro[1] , " e coluna: " , erro[2], Dicionario_de_erros[erro[3]])




