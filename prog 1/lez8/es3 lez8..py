#Date due liste, crrea una lista con il prodotto x*y solo se il prodotto è maggiore di 10.

#input:
lista_a = [1,3,5,7]
lista_b = [2,4,6]

output = [x*y for x in lista_a for y in lista_b if x*y > 10]

print(output)