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
#        if self.isValidSymbol(symbol):
#            return self.transitionFunction(currentState , symbol)
#        else:
#            return ["Se", "Símbolo não pertence ao alfabeto (externo)"]
        return self.transitionFunction(currentState , symbol)


        
class LexicalAnalyzer:
    def __init__(self):
        self.symbleTable = SymbolTable()
        self.DFA = DeterministicFiniteAutomaton( alphabet, estados, funcao_de_transicao , "s0" , valid_states)


    def lexicon(self, lexeme):
        return self.symbleTable.symbol[lexeme]

#Caso a leitura finalize no estado s8 as aspas não foram fechadas
#Caso termine no estado s12 a chave não foi fechada

    def readFile(self , fileName):
        state = "s0"
        lexema = ""
        erro = ""
        listaLexemas = []
        listaErros = []
        file = open(fileName,"r")
        for line in file:
            for character in line:
                currentState = self.DFA.nextState(state,character)[0]
                #print(currentState)
                if currentState == "Se":
#                    if character not in alphabet or character == " ":
                    if character == " " or character == EOFError or character == "\n":
                        if currentState == "s8" or currentState == "s12":
                            print("Erro")
                            return "Erro"
                        elif erro != "":
                            listaErros.append(erro)
                            erro = ""
                        elif self.DFA.isValidFinalState(state):
                            listaLexemas.append([lexema, state])
                        state = "s0"
                        lexema = ""
                    else:
                        state = currentState
                        erro = lexema + erro + character
                        lexema = ""
                else:
                    state = currentState
                    lexema = lexema + character
        else:
            if self.DFA.isValidFinalState(state):
                listaLexemas.append([lexema, state])


        print("Lista de lexemas: ")
        print(listaLexemas)
        print("\nLista de Erros: ")
        print(listaErros)


def teste():

    c = DeterministicFiniteAutomaton(alphabet, estados, funcao_de_transicao , "s0" , ["s1", "s3", "s6", "s9", "s10", "s13", "s14", "s15", "s16", "s17", "s18", "s20", "s21", "s22","s23", "s24"])

    simbolo = input("Insira um símbolo\n")
    estado = "s0"

    for symbol in simbolo:
        vetor = c.nextState(estado, symbol)
        estado = vetor[0]

    print("\nestado: " + estado + "\nidentificação: " + vetor[1] + "\n")





if __name__ == "__main__":

    testeLexicalAnalyzer = LexicalAnalyzer()
    testeLexicalAnalyzer.readFile("programa_fonte.txt")




