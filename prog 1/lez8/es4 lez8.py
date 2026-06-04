#usa una list comprehension per trovare tutte le triplette pitagoriche (a,b,c), con valori di (a,b,c) tra 1 e 20

input = [n for n in range(1,21)]

tri_pita = [(a,b,c) for a in input for b in input for c in input if a**2+b**2==c**2]

print(tri_pita)