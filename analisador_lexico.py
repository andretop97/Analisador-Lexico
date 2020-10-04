from funcao_de_transicao import *

class SymbolTable():
    def __init__(self):
        self.symbol = {}

    def addSymbol(self , token , lexeme , tipo):
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
        if self.isValidSymbol(symbol):
            return self.transitionFunction(currentState , symbol)
        else:
            return ["SE", "Símbolo não pertence ao alfabeto (externo)"]

class LexicalAnalyzer:
    def __init__(self):
        self.symbleTable = SymbolTable()
        self.DFA = DeterministicFiniteAutomaton( alphabet, estados, funcao_de_transicao , "s0" , valid_states)


    def lexicon(self, lexeme):
        return self.symbleTable.symbol[lexeme]

#Caso a leitura finalize no estado s8 as aspas não foram fechadas
#Caso termine no estado s12 a chave não foi fechada

    def readFile(self , fileName):
        file = open(fileName,"r")
        self.analizer(file)

    def analizer(self , file):
        state = "s0"
        lexema = ""
        erro = ""
        listaLexemas = []
        listaErros = []
        for line in file:
            for character in line: #Passa por todos os símbolos do arquivo um a um
                currentState = self.DFA.nextState(state,character)[0]
                if currentState == "Se" or currentState == "SE":
                    specialState = self.DFA.nextState("s0",character)[0]
                    if character == " "  or character == "\n": #Determinando as condições para para de ler um lexema e registrar ele
                        if currentState == "s8" or currentState == "s12": #Os estados descritos aqui são os q indicam estar dentro de aspas ou chaves
                            return "Erro" #Ainda deve ser implementado
                        elif erro != "": #Caso já esteja registrando um falso lexema continua até ele terminar
                            listaErros.append(erro)
                            erro = ""
                        elif self.DFA.isValidFinalState(state): #Registra os lexemas
                            self.symbleTable.addSymbol(lexema, lexema, "")
                            listaLexemas.append([lexema, state])
                        state = "s0"
                        lexema = ""
                    elif specialState != "Se" and currentState != "SE":
                        self.symbleTable.addSymbol(lexema, lexema, "")
                        listaLexemas.append([lexema, state])
                        state = specialState
                        lexema = character
                    else: #Não para de registrar qdo encontra um simbolo inválido, mas guarda ele separadamente
                        state = currentState
                        erro = lexema + erro + character
                        lexema = ""
                else: #Continua a contruir um lexema
                    state = currentState
                    lexema = lexema + character
        else: #Registra o último lexema do arquivo
            if self.DFA.isValidFinalState(state):
                self.symbleTable.addSymbol(lexema, lexema, "") 
                listaLexemas.append([lexema, state])
            else:
                listaErros.append(erro)

        print("Lista de lexemas: ")
        print(listaLexemas)
        print("\nLista de Erros: ")
        print(listaErros)


if __name__ == "__main__":

    testeLexicalAnalyzer = LexicalAnalyzer()
    #testeLexicalAnalyzer.readFile("programa_fonte.txt")
    testeLexicalAnalyzer.readFile("text.txt")

    print("\nTabela de símbolos")
for item in testeLexicalAnalyzer.symbleTable.symbol:
    print(testeLexicalAnalyzer.symbleTable.symbol[item])




