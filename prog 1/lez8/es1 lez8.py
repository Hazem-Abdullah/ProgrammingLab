#data una lista di numeri, usa list comprehension per restituire i numeri dispari


input = [n for n in range(0,9)]

n_dispari = [n for n in input if n%2==1]

print(n_dispari)