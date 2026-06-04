#date due liste una di interi e una di lettere crea le copie (x,y) solo dove x è pari e l'indice di y è dispari

lista_a = [0,1,3,4]
lista_b = ['a','b','c']

output = [(x,y) for x in lista_a for ind,y in enumerate(lista_b) if (x%2==0)and(ind%2==1)]

print(output)