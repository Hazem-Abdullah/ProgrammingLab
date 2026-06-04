#usa una list comprehension per fare flattening di una lista di liste e trasformarla in una lista unica

input = [[1,2,3],[4,5],[6,7,8,1]]

output = [n for l in input for n in l]

print(output)