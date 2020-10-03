numeros = ["0","1","2","3","4","5","6","7","8","9"]
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
outros_simbolos = [".", '"', "*", "{", "}", "<", ">", "=", "+", "-", "/", "(", ")", ";"]
alphabet = numeros + letras + outros_simbolos
estados =["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13","s14","s15","s16","s17","s18","s19"]
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
        self.currentState = self.initialState

    # Função que verifica se o estado atual é final valido
    def isValidFinalState(self , currentState) :
        return currentState in self.validStates

    # Função que verifica se o simbolo pertecen ao alfabeto do nosso DFA
    def isValidSymbol(self , symbol):
        return symbol in self.alphabet

    # Função que verifica se é o final do lexema
    def isEndLexeme(self , currentState , symbol):
        return self.transitionFunction(currentState , symbol)[0] == "Se"


    # Função que recebe estado e o simbolo , para a paritr dele e da função de transição retornar o proximo estado
    def nextState(self , currentState, symbol):
        if self.isValidSymbol(symbol):
            nextState = self.transitionFunction(currentState , symbol)
            #print("nextState", nextState)
            if self.isValidFinalState(nextState):
                if self.isEndLexeme :
                    return nextState
                else:
                    return ["Se", "Não é um estado válido"]
            else:
                return nextState
        else:
            return ["Se", "Símbolo não pertence ao alfabeto"]


        
class LexicalAnalyzer:
    def __init__(self):
        self.symbleTable = SymbolTable()
        self.DFA = DeterministicFiniteAutomaton( alphabet, estados, funcao_de_transicao , "s0" , ["s2"])


    def lexicon(self, lexeme):
        return self.symbleTable.symbol[lexeme]

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
        if letter in numeros:
            return ["s1", "numero"]
        elif letter == '"':
            return ["s7", "Abre aspas"]
        elif letter in letras:
            return ["s10", "letra"]
        elif letter == "{":
            return ["s11", "Abre chaves"]
        elif letter == "<" or letter == ">" or letter == "=":
            return ["s20", "Maior, menor ou igual"]
        elif letter == "+" or letter == "-" or letter == "*" or letter == "/":
            return ["s16", "Operador matemático"]
        elif letter == "(":
            return ["s17", "Abre Parênteses"]
        elif letter == ")":
            return ["s18", "Fecha Parênteses"]
        elif letter == ";":
            return ["s19", "Ponto e vírgula"]
        else:
            return ["Se", "Símbolo não pertence ao alfabeto"]

    if state =="s1":
        if letter in numeros:
            return ["s1", "numero"]
        else:
            return "err"
    if state =="s2":
        if letter.isalpha() == True:
            return "s2"
        else:
            return "err"



if __name__ == "__main__":
    # testeSymbolTable = SymbolTable()
    # testeSymbolTable.addSymbol("int","int","int")
    # testeDFA = DFA.DeterministicFiniteAutomaton(["a" , "b" , "c"],["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9"] , funcao_de_transicao , "s0" , ["s2"])
    # print(testeSymbolTable.symbol)
    # d = testeSymbolTable.checkSymbolExistence("int")
    # e = testeSymbolTable.checkSymbolExistence("batata")
    # print(d , "  " , e)

#    testeLexicalAnalyzer = LexicalAnalyzer()

#    testeLexicalAnalyzer.readFile("text.txt")

    c = DeterministicFiniteAutomaton(alphabet, estados, funcao_de_transicao , "s0" , ["s2"])

    simbolo = input("Insira um símbolo\n")

    print("\nestado: " + c.nextState("s0",simbolo)[0] + "\nidentificação: " + c.nextState("s0",simbolo)[1] + "\n")

