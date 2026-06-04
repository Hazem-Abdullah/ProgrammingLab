# Scrivete una classe denominata Veicolo che disponga di questi attributi dati:
# ● modello (per il modello del veicolo);
# ● marca (per la marca del veicolo);
# ● anno (per l'anno del veicolo).
# ● speed (per la velocità del veicolo)
# E di questi metodi:
# ● __init__ che accetti come argomenti l’anno, il modello, e la marca. Il metodo dovrebbe inoltre
# assegnare 0 all’attributo dati speed.
# ● __str__ che restituisce una stringa con i dettagli del veicolo (marca, modello, anno e velocità)
# ● accellerare che aggiunge 5 all’attributo dati speed ogni volta che viene chiamato.
# ● frenare che sottrae 5 dall’attributo dati speed ogni volta che viene chiamato.
# ● get_speed che restituisce la velocità corrente.


class Veicolo():

    def __init__(self, anno, marca, modello):

        self.anno = anno 
        self.modello = modello
        self.marca = marca
        self.speed = 0

    def __str__(self):
        return (f'Veicolo : ["{self.marca}", "{self.modello}", "{self.anno}", "{self.speed}"]')

    def accellerare(self):
        self.speed += 5

    def frenare(self):
        if self.speed != 0 :
            self.speed -= 5

    def get_speed(self):
        return (self.speed)
    

veicolo1 = Veicolo(2008, 'Mitsubishi', 'Lancer EX: Shark')

veicolo1.accellerare()
print(veicolo1.get_speed())
print(veicolo1)
        












