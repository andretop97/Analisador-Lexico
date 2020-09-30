import re
class DeterministicFiniteAutomaton:

    def __init__ (self , alphabet , states , transitionFunction , initialState , validStates):
        self.alphabet = alphabet
        self.states = states
        self.transitionFunction = transitionFunction
        self.initialState = initialState
        self.validStates = validStates
        self.currentState = self.initialState

    # Função que verifica se o estado atual é final valido
    def isValidFinalState(self , currentState) :
        return currentState in self.validStates

    # Função que verifica se o simbolo pertecen ao alfabeto do nosso DFA
    def isValidSymbol(self , symbol):
        return symbol in self.alphabet

    # Função que verifica se é o final do lexema
    def isEndLexeme(self , currentState , symbol):
        return self.transitionFunction(currentState , symbol) == "Se"


    # Função que recebe estado e o simbolo , para a paritr dele e da função de transição retornar o proximo estado
    def nextState(self , currentState, symbol):
        if self.isValidSymbol(symbol):
            nextState = self.transitionFunction(currentState , symbol)
            print("nextState", nextState)
            if self.isValidFinalState(nextState):
                if self.isEndLexeme :
                    return nextState
                else:
                    return "Se"
            else:
                return nextState
        else:
            return "Se"


