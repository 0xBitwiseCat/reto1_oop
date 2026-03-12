"""
Escribir una función que reciba una lista de números enteros y 
retorne la mayor suma entre dos elementos consecutivos
"""

type vector = list[int]
def max_consecutive_sum(v: vector):
    if len(v) < 2:
        return "There is no way to calculate consecutive sums"

    output = None
    for i in range(len(v)-1): #-1 discards the n-1 and n-2 elements
        z = v[i] + v[i+1]

        if output is None or z > output:
            output = z

    return output


# unit test
r = max_consecutive_sum([1,2,3,4,5,6,7])
print(r) # 6+7 = 13
r = max_consecutive_sum([-1,-2,-3,-4])
print(r) # -1 -2 = -3
r = max_consecutive_sum([])
print(r) # Error message
r = max_consecutive_sum([99,-100,440, 99, -10000, -1, 40])
print(r) # 440 + 99 = 539

"""
'cause requeriment is ambiguous i think that 
the way to do is sum pos + (pos+1) and take the max of that

another option could be order by asc and then search numbers
in the way n, n+1 and then take the max of that but anyways
"""