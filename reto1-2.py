"""
Realice una función que permita validar si una palabra es un palíndromo. 
Condición: No se vale hacer slicing para invertir la palabra y 
verificar que sea igual a la original.
"""


def is_palindrome(word: str):
    if len(word) < 2:
        return "Input is not valid"

    index = len(word)-1
    word = word.lower()
    for i in range(index,-1,-1):
        j = index - i # Search the opposite position
        if word[i] != word[j]:
            return False

    return True



# unit test
r = is_palindrome("aa")
print(r) # True
r = is_palindrome("a")
print(r) # Error message
r = is_palindrome("fox")
print(r) # False
r = is_palindrome("mama")
print(r) # False
r = is_palindrome("maam")
print(r) # True


"""
So, comparing one to one char allows to function 
shows false earlier without validating all chars 
"""