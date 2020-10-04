numeros = ["0","1","2","3","4","5","6","7","8","9"]
letras = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","x","X","y","Y","z","Z"]
outros_simbolos = [".", '"', "*", "{", "}", "<", ">", "=", "+", "-", "/", "\\", "(", ")", ";", ":", "_"," "]
alphabet = numeros + letras + outros_simbolos
estados =["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13","s14","s15","s16","s17","s18","s19"]
valid_states = ["s1", "s3", "s6", "s9", "s10", "s13", "s14", "s15", "s16", "s17", "s18", "s19", "s20", "s21", "s22","s23", "s24"]
def funcao_de_transicao(state , symbol):
#    print(state)
    if state == "s0":
        if symbol in numeros:
            return ["s1", "numero"]
        elif symbol == '"':
            return ["s7", "Abre aspas"]
        elif symbol in letras:
            return ["s10", "letra"]
        elif symbol == "{":
            return ["s11", "Abre chaves"]
        elif symbol == "=":
            return ["s14", "Igual"]
        elif symbol == "<":
            return ["s15", "Menor"]
        elif symbol == ">":
            return ["s16", "Maior"]
        elif symbol == "(":
            return ["s17", "Abre Parênteses"]
        elif symbol == ")":
            return ["s18", "Fecha Parênteses"]
        elif symbol == ";":
            return ["s19", "Ponto e vírgula"]
        elif symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
            return ["s20", "Operador matemático"]
        else:
            return ["Se", "simbolo inválido"]

    if state =="s1":
        if symbol in numeros:
            return ["s1", "numero"]
        elif symbol == ".":
            return ["s2", "Número seguido de ponto (Ex: 2.)"]
        elif symbol == "e" or symbol == "E":
            return ["s4", "Número seguido de símbolo exponencial"]
        else:
            return ["Se", "simbolo inválido"]

    if state =="s2":
        if symbol in numeros:
            return ["s3", "Número seguido de ponto e outro número"]
        else:
            return ["Se", "simbolo inválido"]

    if state == "s3":
        if symbol in numeros:
            return ["s3", "Número seguido de ponto e outros números"]
        elif symbol == "e" or symbol == "E":
            return ["s4", "Número seguido de símbolo exponencial"] 
        else:
            return ["Se", "simbolo inválido"]

    if state == "s4":
        if symbol == "+" or symbol == "-":
            return ["s5", "Número elevado a um sinal"]
        if symbol in numeros:
            return["s6", "Número elevado a um número positivo"]
        else:
            return ["Se", "simbolo inválido"]

    if state == "s5":
        if symbol in numeros:
            return["s6", "Número elevado a um número positivo ou negativo"]
        else:
            return ["Se", "simbolo inválido"]

    if state == "s6":
        if symbol in numeros:
            return ["s6", "Número elevado a um número positivo ou negativo"]
        else:
            return ["Se", "simbolo inválido"]

    if state == "s7":
        if symbol == '"':
            return ["s9", "Constante literal vazia finalizado"]
        else:
            return ["s8", "Constante literal não finalizada"]

    if state == "s8":
        if symbol == '"':
            return ["s9", "Constante literal finalizada"]
        else:
            return ["s8", "Constante literal não finalizada"]

    if  state ==  "Se" or state ==  "s9" or state ==  "s13" or state ==  "s14" or state ==  "s17" or state ==  "s18" or state ==  "s19" or state ==  "s20" or state ==  "s21" or state ==  "s22" or state ==  "s23" or state ==  "s24":
        return ["Se", "simbolo inválido"]

    if state ==  "SE":
        return ["SE", "Símbolo não pertence ao alfabeto (externo)"]


    if state == "s10":
        if symbol in letras+numeros or symbol == "_":
            return ["s10", "Identificador"]
        else:
            return ["Se", "simbolo inválido"]

    if state == "s11":
        if symbol == "}":
            return ["s13", "Comentário vazio finalizado"]
        else:
            return ["s12", "Comentário não finalizado"]

    if state == "s12":
        if symbol == "}":
            return ["s13", "Comentário finalizado"]
        else:
            return ["s12", "Comentário não finalizado"]

    if state == "s15":
        if symbol == "=":
            return ["s21", "Menor igual"]
        elif symbol == ">":
            return ["s22", "Menor maior"]
        if symbol == "-":
            return ["s23", "Atribuição"]
        else:
            return ["Se", "simbolo inválido"]

    if state == "s16":
        if symbol == "=":
            return ["s24", "Maior igual"]
        else:
            return ["Se", "simbolo inválido"]
