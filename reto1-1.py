"""
Crear una función que realice operaciones básicas 
(suma, resta, multiplicación, división) entre dos números, 
según la elección del usuario, la forma de entrada de la función 
será los dos operandos y el caracter usado para la operación. 
entrada: (1,2,"+"), salida (3).
"""

type number = int | float


def calc(a: number, b: number, op: str):
    if op != "+" and op != "-" and op != "*" and op != "/":
        return "Operation selected is not defined."

    if op == "+":
        return a+b
    
    if op == "-":
        return a-b

    if op == "*":
        return a*b
    
    if op == "/":
        if b == 0:
            return "Operation is not possible to do"
        return a/b

# unit test
r = calc(1,2,"+")
print(r) # Expected output: 3

r = calc(0,0,"/")
print(r) # Error message

r = calc(0,0,"8")
print(r) # Error message 

r = calc(0,0,"*")
print(r) # Expected output: 0

r = calc(10,9.99, "*")
print(r) # Expected output: 99.9


"""
This solution provides a simple error handling and
allows user to compute operations using floats and integers
I do not want to use complex structures so I use if to 
compute every operation for each operator. Also, i use
the operation as a return in order to allow the code use 
the result in other operation if it would be necessary 
"""