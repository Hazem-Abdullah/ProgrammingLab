# Si vogliono modificare le classi Studente e Docente precedentemente definite
# in modo che esse possano:
# ○ memorizzare una lista di corsi frequentata da uno studente
# ○ memorizzare una lista di corsi insegnati da un Docente
# ● Per semplicità le liste in questione non sono vuote. Si vuole quindi definire
# saluta per stampare a schermo la lista completa dei corsi.
# ● In pratica, si vuole permettere di scrivere il seguente codice:
# ○ corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]
# ○ obj_Irene = Studente("Irene", "Rossi", corsi)
# ● cosicché obj_Irene.saluta() stampi tutti i corsi frequentati da obj_Irene
# (variabile corsi, passata al costruttore).

# Si estendano ulteriormente le classi definite nell'esercizio 1 aggiungendo:
# ○ un algoritmo che calcoli se un docente insegna tutti i corsi frequentati da uno studente.
# ○ un algoritmo che verifichi che, per ogni studente iscritto ad un certo numero di corsi, esistano
# docenti che effettivamente insegnino quei corsi.
# ● Per risolvere il secondo punto si usi la soluzione del primo.

class Person():
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print(f'Ciao sono {self.ruolo}, {self.nome} {self.cognome}')


class Studente(Person):
    def __init__(self, nome, cognome, corsi):
        super().__init__('Studente UNITS', nome, cognome)
        self.corsi = corsi

    def saluta(self):
        super().saluta()
        print(f'Frequento i corsi di {self.corsi}')


class Docente(Person):
    def __init__(self, nome, cognome, corsi):
        super().__init__('Docente UNITS', nome, cognome)
        self.corsi = corsi

    def saluta(self):
        super().saluta()
        print(f'Docente del corsi di {self.corsi}')

# def controllo_corsi(doc = Docente, std = Studente):
#     for corso in doc.corsi :
#         if corso in std.corsi

corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]
obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Md7t = Docente('Md7t', 'Zakaria', corsi.copy())

obj_Irene.saluta()
obj_Md7t.saluta()
# print(controllo_corsi(obj_Md7t, obj_Irene))