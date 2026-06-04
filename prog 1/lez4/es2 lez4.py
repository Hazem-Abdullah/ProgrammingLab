# Create un oggetto CSVFile che rappresenti un file CSV, e che:
# 1) venga inizializzato sul nome del file csv, e
# 2) abbia un attributo “name” che ne contenga il nome
# 3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, 

class CSV():

    def __init__(self,name):

        self.name = name

    def get_data(self):
        
        myfile = open(self.name,'r')
        copia = []
        for line in myfile:
            # line_pulita = line.strip()
            if 'Date' not in line :
                copia.append(line.strip().split(','))
        return copia

shampoo = CSV('shampoo_sales.csv')
print(*shampoo.get_data(), sep='\n')