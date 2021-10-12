'''
=======================================================
Gramática Original:
A -> A,,C
    |A..D
    |A.C
    |A,D
    |D
    |F
C -> x
D -> b
F -> m
========================================================
Primer Regla De Producción
A -> DA'
    |FA'

A' -> ,,,CA'
    | ..DA'
    | .CA'
    | ,DA'
    | Epsilon
C -> x
D -> b
F -> m
========================================================
Factorizar

En este caso no hay ambiguedad, por lo tanto se deja como está
A -> DA'
    |FA'
En A' si existía ambiguedad por lo tando se debe factorizar
A' -> ,U1
    | .U2
    | Epsilon

U1 -> ,,CA'
    | DA'

U2 -> .DA'
    | CA'

C -> x
D -> b
F -> m
Ahora ya tenemos la gramática recurisva por la derecha, factorizada.
Se define como inicio:
INICIO = A
========================================================
'''
token_actual=0
#ANALIZADOR LÉXICO QUE SIMULAMOS, YA QUE NO SE CREARON LOS OBJETOS DE UN ANALIZADOR LÉXICO REAL
lista_tokens=[]
lista_tokens.append({'lexema':'b','tipo':'letrab','linea':1,'columna':1})
lista_tokens.append({'lexema':',','tipo':'coma','linea':1,'columna':1})
lista_tokens.append({'lexema':',','tipo':'coma','linea':1,'columna':1})
lista_tokens.append({'lexema':',','tipo':'coma','linea':1,'columna':1})
lista_tokens.append({'lexema':'x','tipo':'letrax','linea':1,'columna':1})

def U1(indice_token):
    if indice_token<len(lista_tokens):
        if lista_tokens[indice_token]['tipo'] =='coma':
            indice_token+=1
            if lista_tokens[indice_token]['tipo']=='coma':
                indice_token+=1
                if lista_tokens[indice_token]['tipo']=='letrax':
                    indice_token+=1
                    a_prima(indice_token)
                else:
                    print("Error sintáctico, se esperaba: 'letrax' y se recibió:",lista_tokens[indice_token]['lexema'])
                    return False
            else:
                print("Error sintáctico, se esperaba: 'coma' y se recibió:",lista_tokens[indice_token]['lexema'])
                return False
        elif lista_tokens[indice_token]['tipo'] =='letrab':
            indice_token+=1
            a_prima(indice_token)
        else:
            print("Error sintáctico, se esperaba: 'coma' o 'letrab' y se recibió:",lista_tokens[indice_token]['lexema'])
        return False


def U2(indice_token):
    if indice_token<len(lista_tokens):
        if lista_tokens[indice_token]['tipo'] =='punto':
            indice_token+=1
            if lista_tokens[indice_token]['tipo']=='letrab':
                indice_token+=1
                a_prima(indice_token)
            else:
                print("Error sintáctico, se esperaba: 'coma' y se recibió:",lista_tokens[indice_token]['lexema'])
                return False
        elif lista_tokens[indice_token]['tipo'] =='letrax':
            indice_token+=1
            a_prima(indice_token)
        else:
            print("Error sintáctico, se esperaba: 'punto' o 'letrax' y se recibió:",lista_tokens[indice_token]['lexema'])
        return False


def A_no_terminal(indice_token):
    if indice_token<len(lista_tokens):
        if lista_tokens[indice_token]['tipo'] =='letrab':
            indice_token+=1
            a_prima(indice_token)
        elif lista_tokens[indice_token]['tipo'] =='letram':
            indice_token+=1
            a_prima(indice_token)

def C_no_terminal(indice_token):
    if indice_token<len(lista_tokens):
        if lista_tokens[indice_token]['tipo'] =='letrax':
            indice_token+=1
            return True
        else:
            print("Error sintáctico, se esperaba: 'letrax'  y se recibió:",lista_tokens[indice_token]['lexema'])
            return False
def D_no_terminal(indice_token):
    if indice_token<len(lista_tokens):
        if lista_tokens[indice_token]['tipo'] =='letrab':
            indice_token+=1
            return True
        else:
            print("Error sintáctico, se esperaba: 'letrab'  y se recibió:",lista_tokens[indice_token]['lexema'])
            return False
def F_no_terminal(indice_token):
    if indice_token<len(lista_tokens):
        if lista_tokens[indice_token]['tipo'] =='letram':
            indice_token+=1
            return True
        else:
            print("Error sintáctico, se esperaba: 'letram' y se recibió:",lista_tokens[indice_token]['lexema'])
            return False

def A_no_terminal(indice_token):
    if indice_token<len(lista_tokens):
        if lista_tokens[indice_token]['tipo'] =='letrab':
            indice_token+=1
            a_prima(indice_token)
        elif lista_tokens[indice_token]['tipo'] =='letram':
            indice_token+=1
            a_prima(indice_token)
        else:
            print("Error sintáctico, se esperaba: 'letram' y se recibió:",lista_tokens[indice_token]['lexema'])
            return False

def a_prima(indice_token):
    if indice_token<len(lista_tokens):
        if lista_tokens[indice_token]['tipo'] =='coma':
            indice_token+=1
            U1(indice_token)
        elif lista_tokens[indice_token]['tipo'] =='punto':
            indice_token+=1
            U2(indice_token)
        else:
            return False


def inicio(indice_token):
    A_no_terminal(indice_token)
    print("análisis Satisfactorio!!!")

inicio(token_actual)

