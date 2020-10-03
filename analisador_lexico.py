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
            return ["Se", "Símbolo não pertence ao alfabeto (externo)"]


        
class LexicalAnalyzer:
    def __init__(self):
        self.symbleTable = SymbolTable()
        self.DFA = DeterministicFiniteAutomaton( alphabet, estados, funcao_de_transicao , "s0" , valid_states)


    def lexicon(self, lexeme):
        return self.symbleTable.symbol[lexeme]

    def readFile(self , fileName):
        state = "s0"
        lexema = ""
        listaLexemas = []
        file = open(fileName,"r")
        for line in file:
            for character in line:
                currentState = self.DFA.nextState(state,character)[0]
                if currentState == "Se":
                    if character not in alphabet:
                        if self.DFA.isValidFinalState(state):
                            self.symbleTable.addSymbol(lexema, lexema, "")
                            listaLexemas.append([lexema, state])
                    state = "s0"
                    lexema = ""
                else:
                    state = currentState
                    lexema = lexema + character
        else:
            if self.DFA.isValidFinalState(state):
                listaLexemas.append([lexema, state])



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
    testeLexicalAnalyzer.readFile("text.txt")


for item in testeLexicalAnalyzer.symbleTable.symbol:
    print(testeLexicalAnalyzer.symbleTable.symbol[item])




