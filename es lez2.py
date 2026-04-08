#1. Stampare l’equivalente di 538 minuti nel formato 8h:58min.
# minuti = 538
# h = int(minuti / 60)
# minuti = minuti % 60
# print(f"{h}h:{minuti}min")



#2. Scrivere un programma che chiede all’utente un numero intero e stampa il suo quadrato e il suo cubo.
# num = int(input("inserisci un numero :"))
# print(f"Il quadrato : {num**2}, il cubo : {num**3}")



#3. Scrivere un programma che verifica se un numero inserito dall’utente è pari o dispari.
# num = int(input("inserisci un numero :"))
# if(num%2):
#     print("dispari")
# else :
#     print("pari")



# 4. Definire una funzione che prende come argomento una parola e una lettera e ritorna quante volte quella lettera è contenuta nella parola.
# def LetInPar(parola,lettera):
#     num = 0
#     for item in parola:
#         if(item == lettera):
#             num+=1
#     return num

# parola = "hello every body :l"
# lettera = "o"
# num = LetInPar(parola,lettera) #il numero di volte quella lettera è contenuta nella parola
# print(f"la lettera \"{lettera}\" è stata repetuta {num} volte nella parola \"{parola}\"")



# 5. Scrivere un programma che verifica se un numero inserito dall’utente è primo.
# num = 1
# sq = int(num**0.5)+1
# if(num>1):
#     for i in range(2,sq) :
#         if(num % i == 0) :
#             print(f"not prime : {num} / {i} = {num/i}")
#             break
#     else:
#         print("prime")
# else:
#     print("not prime")


# 6. Scrivere un programma che fa la somma di n numeri inseriti dall’utente. Di all'utente di scrivere 0 per fermarsi.
# num = 2
# somma = 0
# while num != 0 :
#     num = int(input("inserisci i numeri che vuoi sommare: (scrivi 0 per fermarsi!)"))
#     somma+=num
# print(f"la somma : {somma}")


# 7. Definire la funzione fattoriale (versione iterativa).
# num = int(input("inserisci un numero : "))
# fat = 1
# while num != 1 :
#     fat*= num
#     num-=1
# print(f"il fattoriale del numero {num} è : {fat}")


# 8. Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un triangolo e, se sì, di che tipo di triangolo
# a = int(input("inserisci il primo lato : "))
# b = int(input("inserisci il secondo lato : "))
# c = int(input("inserisci il terzo lato : "))
# ab = a+b>c ; ac = a+c>b ; bc = b+c>a
# a_b = a==b ; a_c = a==c ; b_c = b==c
# if(ab and ac and bc):
#     print("Questi lati forniscono un triangolo di tipo : ",end=" ")
#     if (a_b or a_c or b_c):
#         if a_b and b_c :
#             print("Equilatero")
#         else:
#             print("Isoscele")
#     else:
#         print("Scaleno")
# else:
#     print("Questi lati non forniscono un triangolo ")


# 9. Definire una funzione che conta quante vocali sono presenti in una stringa.
def ContaVocali(stri):
    cont = 0
    vocali = "aeiou"
    for i in stri:
        if i.lower() in vocali:
            cont+=1
    print(f"la stringa \"{stri}\" contiene {cont} vocali.")


stri = input("inserisci una stringa : ")
ContaVocali(stri)
