# and, or, not
# and: True si los dos operandos son True
# or: True si al menos uno de los operandos es True
# not: True si el operando es False
# Una operacion de corto circuito es una operacion que no evalua el segundo operando si el resultado se puede determinar con el primer operando

gas = True
encendido = False
edad = 18

if not gas and encendido and edad > 17:
    print("Puede avanzar")
