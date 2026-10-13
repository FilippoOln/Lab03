class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.__codice = codice
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = anno_acquisto
        self.__valore = valore
        self.__disponibile = True

    @property
    def codice(self):
        return self.__codice

    @property
    def marca(self):
        return self.__marca

    @property
    def disponibile(self):
        return self.__disponibile

    @disponibile.setter
    def disponibile(self, disponibile):
        self.__disponibile = disponibile

    def __str__(self):
        return f"{self.__codice} {self.__tipo} {self.__marca} {self.__anno_acquisto} {self.__valore} {self.__disponibile}"

    def __repr__(self):
        return (f"{type(self).__name__} (codice={self.__codice}, tipo={self.__tipo}, marca={self.__marca},"
                f" anno d'acquisto={self.__anno_acquisto}, valore={self.__valore}, disponibile={self.__disponibile})")