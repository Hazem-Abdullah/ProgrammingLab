# Scrivete una definizione di una classe di nome Canguro con i metodi
# seguenti:
# 1. Un metodo __init__ che inizializza un attributo lista contenuto_tasca con paramatro di default
# lista vuota.
# 2. Un metodo di nome intasca che prende un oggetto di qualsiasi tipo e lo inserisce in
# contenuto_tasca.
# 3. Un metodo __str__ che restituisce una stringa di rappresentazione dell’oggetto Canguro e dei
# contenuti della tasca. 
# ● Provate il codice creando due oggetti Canguro, assegnandoli a variabili di nome can e guro,
# e aggiungendo elementi a can. Cosa succede a guro?

class Canguro():

    def __init__(self,contenuto_tasca = []):
        self.contenuto_tasca = contenuto_tasca

    def intasca(self,oggetto):
        self.contenuto_tasca.append(oggetto)

    def __str__(self):
        return (f'Canguro : {self.contenuto_tasca}')
    
can = Canguro()
guro = Canguro()
can.intasca(6)
print(can)
print(guro)