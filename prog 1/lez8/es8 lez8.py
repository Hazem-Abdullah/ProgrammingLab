#data una frase, usa dict comprehension per contare quante volte ogni parola appare

input = "the cat sat on the mat the cat"


words = input.lower().split(" ")
output = {par: words.count(par) for par in words }

print(output)


