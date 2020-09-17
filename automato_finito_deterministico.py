import re
class DeterministicFiniteAutomaton:

    def __init__ (self , alphabet , states , transitionFunction , initialState , validStates):
        self.alphabet = alphabet
        self.states = states
        self.transitionFunction = transitionFunction
        self.initialState = initialState
        self.validStates = validStates

    # Função que verifica se o estado atual é final valido
    def isValidFinalState(self , state) :
        if state in self.validStates:
            return True
        else:
            return False
    # Função que verifica se o simbolo pertecen ao alfabeto do nosso AFD
    def isValidSymbol(self , symbol):
        if symbol in self.alphabet:
            return True
        else:
            return False

    # Função que recebe estado e o simbolo , para a paritr dele e da função de transição retornar o proximo estado
    def nextState(self , state, symbol):
       return self.transitionFunction(state , symbol)

    # Função que analisa a palavra e retorna o estado final da mesma 
    def lexemeVerify(self , lexeme):
        state = self.initialState
        for symbol in lexeme:
            if self.isValidSymbol(symbol):
               state = self.nextState(state , symbol)
            else:
                return "err , invalid symbol"

        if self.isValidFinalState(state):
            return state
        else:
            return "err , lexema does not belong to the language" 

        

        

# def funcao_de_transicao(state , letter):
#     if state == "s0":
#         if re.findall("\d", letter):
#             return "s1"
#         elif re.findall("\w", letter):
#             return "s2"
#         else:
#             return "Serr"

#     if state == "s1":
#         if re.findall("\d", letter):
#             return "s1"
#         elif re.findall("\w", letter):
#             return "s2"
#         else:
#             return "err"

#     if state =="s2":
#         if re.findall("\w", letter):
#             return "s2"
#         elif re.findall("\d", letter):
#             return "s1"
#         else:
#             return "err"


# if __name__ == "__main__":
#     c = DeterministicFiniteAutomaton(["a" , "b" , "c"],["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9"] , funcao_de_transicao , "s0" , ["s2"])


#     # print(c.transition_function("s0","c"))
#     # print(c.transition_function("s0","9"))
#     print(c.lexemeVerify("abc"))

