class automato_finito_deterministico:

    def __init__ (self , alphabet , states , transition_function , initial_state , valid_states):
        self.alphabet = alphabet
        self.states = states
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.valid_states = valid_states

    def isFinal(self , state) :
        if state in self.valid_states:
            return True
        else:
            return False

    def isValidsymbol(self , letter):
        if letter in self.alphabet:
            return True
        else:
            return False

    def nextState(self , state, letter):
       return self.transition_function(state , letter)

def funcao_de_transicao(state , letter):
    if state == "s0":
        if letter == "a" or letter == "c":
            return "s1"
        elif letter == "b":
            return "s2"
        else:
            return "err"
    if state =="s2":
        if letter == "a":
            return "s0"
        if letter == "b":
            return "s2"
        else:
            return "err"


if __name__ == "__main__":
    c = automato_finito_deterministico(["a","b","c","d","e"],["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9"] , funcao_de_transicao , "s0" , ["s2"])


    print(c.transition_function("s0","c"))


