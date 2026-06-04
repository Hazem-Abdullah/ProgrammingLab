#1. Scrivete una funzione che sommi tutti gli elementi di una lista
# def sum_list(mylist):
#     sum = 0
#     for i in mylist:
#         sum += i
#     return sum

# mylist = [5,3,6,9]
# sum = sum_list(mylist)
# print(f"la somma della lista : {sum}")



#2. Scrivere una funzione che prende in input una stringa e ritorna True se è un palindromo, False altrimenti.
# def palindrome(stn):
#     pal = False
#     if stn == stn[-1::-1]:
#         pal = True
#     return pal

# stn = input("inserisci una stringa : ")
# print(palindrome(stn))



# 3. Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di A[i] con A[j].
# def scambio_indici(A,i,j):
#     temp = A[i] 
#     A[i] = A[j]
#     A[j] = temp

# A = ['a','b','c','d','e']
# i = 0
# j = 3
# print(A)
# scambio_indici(A,i,j)
# print(A)


# 4. Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno almeno un elemento in comune
# def OneInCommon(a,b):
#     for i in a :
#         if i in b :
#             return True
#     return False
# a = [11,5,9,3]
# b = [0,3,9,20,7]
# print(OneInCommon(a,b))


# 5. Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una lista di stringhe, corrispondenti ai numeri scritti in Italiano.
# def NumToStrng (lis):
#     Strng = ['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
#     rtrn = [] #la lista che ritorna alla fine 
#     for item in lis:
#         rtrn.append(Strng[item])
#     return rtrn
# a = [3,1,9,0,6]
# print(NumToStrng(a))
# print(a)


# 6. Scrivere una funzione che prende una lista di parole e restituisce un dizionario con il conteggio delle occorrenze.
# def occorrenza(lis):
#     diz = {}
#     for item in lis :
#         if item in diz :
#             x = diz[item]
#             diz[item] = x+1
#         else:
#             diz[item] = 1
#     return diz
# lista = ['a','b','f','a','b','b','c']
# print(occorrenza(lista))


# 7. Definire una funzione che sommi tutti i valori delle vendite degli shampoo del file passato come argomento
# def sum_sales(myfile):
#     somma = 0
#     for line in myfile :
#         elems = line.split(',')
#         if elems[0] != 'Date' :
#             somma += float(elems[1])
#     return somma
# myfile = open('shampoo_sales.csv','r')
# somma = sum_sales(myfile)
# myfile.close()
# print(f"la somma dei valori delle vendite : {somma}")


# 8. Definire una funzione che prende in input un file ed una parola e conta quante volte quella parola è presente sul file
# def Occurrenza_parola(myfile,parola):
#     occur = 0 #quante volte è presente la parola
#     for line in myfile:
#         elems = line.split(',')
#         if elems[2] == parola :
#             occur += 1
#     return occur
# myfile = open('appartamenti.csv','r')
# parola = 'affitto'
# occuranza = Occurrenza_parola(myfile,parola)
# myfile.close
# print(f"la parola : {parola} é presente {occuranza} volte nel file.")  


# 9. Definire una funzione conteggio che prende come input un file e ritorna un dizionario con chiave le parole e valore il numero di volte che la parola è presente nel file.
# def conteggio(myfile):
#     cont = {'affitto':0,'vendita':0}
#     for line in myfile:
#         elems = line.split(',')
#         if(elems[0] != 'id'):
#             cont[elems[2]] +=1
#     return cont
# myfile = open('appartamenti.csv','r')
# cont = conteggio(myfile)
# myfile.close()
# print(cont)


# 10. Definire una funzione che prende come input un file, rimuove tutte le righe duplicate, scrive il risultato in un nuovo file chiamato unique.txt.
# def remove_duplicate(myfile):
#     unqset = set()
#     for line in myfile:
#         unqset.add(line)
#     unique = open('unique.txt','w')
#     for item in unqset:
#         unique.write(item)
#     unique.close
# myfile = open('city_cap.csv','r')
# remove_duplicate(myfile)
