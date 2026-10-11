from csv import reader
from strumento import Strumento
from operator import attrgetter
from prestito import Prestito


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile
        self.__strumentiGestiti = []
        self.__prestitiAttuali = []

    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self.__responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            infile = open(file_path, "r")
            csv_reader = reader(infile)
            for row in csv_reader:
                codice = row[0]
                tipo = row[1]
                marca = row[2]
                anno_acquisto = int(row[3])
                valore = float(row[4])
                s = Strumento(codice, tipo, marca, anno_acquisto, valore)
                self.__strumentiGestiti.append(s)
            infile.close()
            print("Strumenti gestiti dal deposito: ")
            for strumento in self.__strumentiGestiti:
                print(strumento)

        except FileNotFoundError:
            raise FileNotFoundError(f'il file "{file_path}" non è stato trovato!!')



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        carattere='S'

        #se nessuno strumento è ancora presente nella lista strumenti gestiti dal deposito, allo strumento aggiunto
        #verrà assegnato il codice "S1"
        if len(self.__strumentiGestiti) == 0:
            num_progressivo = 1
        else:
            #vado a recuperare il codice dell'ultimo strumento presente nella lista strumenti gestiti dal deposito
            #estraggo da esso il numero intero progressivo e ci sommo 1 per ottener il nuovo num intero progressivo
            ultimo_strumento = self.__strumentiGestiti[-1]
            ultimo_codice = ultimo_strumento.codice
            num_progressivo = int(ultimo_codice[1:]) + 1
        nuovo_codice = carattere + str(num_progressivo)
        nuovo_s = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        #aggiungo il nuovo strumento in fondo alla lista strumenti gestiti dal deposito
        self.__strumentiGestiti.append(nuovo_s)
        return nuovo_s


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        strumenti_ordinati_per_marca = sorted(self.__strumentiGestiti, key=attrgetter('marca'))
        return strumenti_ordinati_per_marca

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        for prestito in self.__prestitiAttuali:
            if prestito.id_strumento == id_strumento:
                raise Exception(f"Lo strumento {id_strumento} è già in prestito ad un altro allievo")
        #verifico se lo strumento è presente nella lista strumenti gestiti dal deposito
        trovato = False
        for strumento in self.__strumentiGestiti:
            if strumento.codice == id_strumento:
                trovato = True
                break
        if not trovato:
            raise Exception(f"Lo strumento {id_strumento} non è disponibile nel deposito")

        carattere = 'P'
        if len(self.__prestitiAttuali) == 0:
            num_progressivo = 1
        else:
            ultimo_prestito = self.__prestitiAttuali[-1]
            ultimo_codice = ultimo_prestito.id_prestito
            num_progressivo = int(ultimo_codice[1:]) + 1
        nuovo_codice = carattere + str(num_progressivo)
        nuovo_p = Prestito(nuovo_codice, data, id_strumento, cognome_allievo)
        #aggiungo il nuovo prestito in fondo alla lista dei prestiti in corso effettuati dal deposito
        self.__prestitiAttuali.append(nuovo_p)
        return nuovo_p


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        trovato = False
        for (indice,element) in enumerate(self.__prestitiAttuali):
            if element.id_prestito == id_prestito:
                trovato = True
                #rimuovo dalla lista dei prestiti in corso effettuati dal deposito il prestito da terminare
                self.__prestitiAttuali.pop(indice)
                break
        if not trovato:
            raise Exception(f"Non è in corso nessun prestito col codice {id_prestito}")
