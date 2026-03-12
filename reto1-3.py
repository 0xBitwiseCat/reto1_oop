"""
Escribir una función que reciba una lista de números 
y devuelva solo aquellos que son primos. 
La función debe recibir una lista de enteros y 
retornar solo aquellos que sean primos.
"""

type vector = list[int]

def is_prime(n: int):
    # only positive numbers count as prime
    if n <= 0:
        return False
    # "1" divides every number
    count = 1
    if n > 25:
        m = int(n ** 0.5)
    else: 
        m = n
    for i in range(2,m):
        if count > 1:
            return False
        if n % i == 0:
            count = count + 1
    return True

def reduce_to_primes(v: vector):
    if len(v) < 1:
        return "Empty list is not valid"
    
    output = []
    for i in v:
        is_prime(i) and output.append(i)
    return output


# unit test
r = reduce_to_primes([2,3,5,6,14])
print(r) # [2,3,5]
r = reduce_to_primes([4,6,8,10])
print(r) # []
r = reduce_to_primes([0,-1,-2,-3,9])
print(r) # []
r = reduce_to_primes([12345678909876543211121111, 999999907, 9, -1, 2147483647])
print(r) # ?

"""
I just create a function that divides a number n
for each number beetween [2, n] if the number
is n<= 25, but if n > 25 just compute division until sqrt(n)
to optimize computing
In the reduce_primes function i just use the function 
that i mentioned before in order to push or not a number 
if is prime
"""