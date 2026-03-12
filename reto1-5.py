"""
Escribir una función que reciba una lista 
de string y retorne unicamente aquellos elementos 
que tengan los mismos caracteres. 
e.g. entrada: ["amor", "roma", "perro"], 
salida ["amor", "roma"]
"""

type vector = list[str]
def reduce_by_same_characters(v: vector):
    output = []
    for s0 in v:
        s0 = s0.lower()
        s00 = s0.lower()
        s00 = "".join(sorted(s00))
        for s1 in v:
            s1 = s1.lower()
            # remove events that using the same word
            if s0 == s1:
                continue
            s11 = s1.lower()
            s11 = "".join(sorted(s11))
            s00 == s11 and s0 not in output and output.append(s0)
            s00 == s11 and s1 not in output and output.append(s1)
    return output

# unit test
r = reduce_by_same_characters(["amor", "roma", "perro"])
print(r) # ["amor", "roma"]
r = reduce_by_same_characters(["rosa", "Rosa", "sora", "wft", "xd"])
print(r) # ["rosa", "sora"]
r = reduce_by_same_characters(["AMOR", "Mora", "RomA", "cAse InsenSiTiv3"])
print(r) # ["amor", "mora", "roma"]


"""
I just compare every word with every word discarding same initial words
'cause i ordered alphabetically every char in the word to compare two words
"""