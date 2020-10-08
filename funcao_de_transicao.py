numeros = ["0","1","2","3","4","5","6","7","8","9"]
letras = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","x","X","y","Y","z","Z"]
outros_simbolos = [".", '"', "*", "{", "}", "<", ">", "=", "+", "-", "/", "\\", "(", ")", ";", ":", "_"," "]
alphabet = numeros + letras + outros_simbolos
estados =["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13","s14","s15","s16","s17","s18","s19"]
Dicionario_de_erros = {"1":"Simbolo não pertence ao alfabeto", "2":"Estado invalido", "3":"Nao fechou aspas", "4":"Não fechou a chave"}
valid_states = ["s1", "s3", "s6", "s9", "s10", "s13", "s14", "s15", "s16", "s17", "s18", "s19", "s20", "s21", "s22","s23", "s24"]
initialState = ["s0","Estado inicial"]
def funcao_de_transicao(state, symbol):
    if state[0] == "s0":
        if symbol in numeros:
            return ["s1", "Num"]
        elif symbol == '"':
            return ["s7", "3"]
        elif symbol in letras:
            return ["s10", "id"]
        elif symbol == "{":
            return ["s11", "4"]
        elif symbol == "=":
            return ["s14", "OPR"]
        elif symbol == "<":
            return ["s15", "OPR"]
        elif symbol == ">":
            return ["s16", "OPR"]
        elif symbol == "(":
            return ["s17", "AB_P"]
        elif symbol == ")":
            return ["s18", "FC_P"]
        elif symbol == ";":
            return ["s19", "PT_V"]
        elif symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
            return ["s20", "OPM"]
        else:
            return ["Se", "2"]

    if state[0] =="s1":
        if symbol in numeros:
            return ["s1", "Num"]
        elif symbol == ".":
            return ["s2", "Num"]
        elif symbol == "e" or symbol == "E":
            return ["s4", "Num"]
        else:
            return ["Se", "2"]

    if state[0] =="s2":
        if symbol in numeros:
            return ["s3", "Num"]
        else:
            return ["Se", "2"]

    if state[0] == "s3":
        if symbol in numeros:
            return ["s3", "Num"]
        elif symbol == "e" or symbol == "E":
            return ["s4", "Num"] 
        else:
            return ["Se", "2"]

    if state[0] == "s4":
        if symbol == "+" or symbol == "-":
            return ["s5", "Num"]
        if symbol in numeros:
            return["s6", "Num"]
        else:
            return ["Se", "2"]

    if state[0] == "s5":
        if symbol in numeros:
            return["s6", "Num"]
        else:
            return ["Se", "2"]

    if state[0] == "s6":
        if symbol in numeros:
            return ["s6", "Num"]
        else:
            return ["Se", "2"]

    if state[0] == "s7":
        if symbol == '"':
            return ["s9", "Literal"]
        else:
            return ["s8", "3"]

    if state[0] == "s8":
        if symbol == '"':
            return ["s9", "Literal"]
        else:
            return ["s8", "3"]

    if state[0] ==  "Se" and state[1] == "1":
        return ["Se", "1"]

    if  state[0] == "Se" and state[1] == "2":
        return ["Se", "2"]

    if state[0] ==  "s9" or state[0] ==  "s13" or state[0] ==  "s14" or state[0] ==  "s17" or state[0] ==  "s18" or state[0] ==  "s19" or state[0] ==  "s20" or state[0] ==  "s21" or state[0] ==  "s22" or state[0] ==  "s23" or state[0] ==  "s24":
        return ["Se", "2"]

    if state[0] == "s10":
        if symbol in letras+numeros or symbol == "_":
            return ["s10", "id"]
        else:
            return ["Se", "2"]

    if state[0] == "s11":
        if symbol == "}":
            return ["s13", "Comentário"]
        else:
            return ["s12", "4"]

    if state[0] == "s12":
        if symbol == "}":
            return ["s13", "Comentário"]
        else:
            return ["s12", "4"]

    if state[0] == "s15":
        if symbol == "=":
            return ["s21", "OPR"]
        elif symbol == ">":
            return ["s22", "OPR"]
        if symbol == "-":
            return ["s23", "RCB"]
        else:
            return ["Se", "2"]

    if state[0] == "s16":
        if symbol == "=":
            return ["s24", "OPR"]
        else:
            return ["Se", "2"]