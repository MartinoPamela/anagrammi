import copy
from time import time
from functools import lru_cache


class Model:
    def __init__(self):
        self._anagrammi = set()  # nel set non ci sono ripetizioni
        self._anagrammi_list = []

    def calcola_anagrammi(self, parola):
        self._anagrammi = set()
        self.ricorsione("", "".join(sorted(parola)))  # a livello zero il mio input è una stringa vuota
        return self._anagrammi

    @lru_cache(maxsize=None)  # senza limiti
    def ricorsione(self, parziale, lettere_rimanenti):  # anche le lettere rimanenti sono stringhe
        # Caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi.add(parziale)
            # parziale è una stringa, le stringhe sono immutabili e hashable, quindi posso usare una cache
            return  # in realtà questo return non serve
        else:
            # Caso non terminale: dobbiamo provare ad aggiungere una lettera
            # per volta, ed andare avanti nella ricorsione
            for i in range(len(lettere_rimanenti)):  # ciclo for con l'indice
                parziale += lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]  # queste saranno le mie nuove
                # lettere rimanenti, la i-esima la salto perché l'ho già considerata,
                # l'ho già messa dentro il parziale, [:i] salto l'i-esimo, fino a i-1, [i+1:] da i+1 vado fino alla fine
                self.ricorsione(parziale, nuove_lettere_rimanenti)  # andrà avanti fino a raggiungere il fondo
                parziale = parziale[:-1]  # faccio back tracking, ovvero tolgo l'ultima lettera rimanente

    @lru_cache(maxsize=None)
    def calcola_anagrammi_list(self, parola):
        self._anagrammi_list = []
        self.ricorsione_list([], parola)  # la soluzione parziale iniziale sarà una lista vuota
        return self._anagrammi_list

    def ricorsione_list(self, parziale, lettere_rimanenti):  # assumo che parziale non sia più una stringa ma una lista
        # Caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi_list.append(copy.deepcopy(parziale))  # devo farne una copia perché non voglio il riferimento
            # che poi viene modificato dalle altre funzioni
            return
        else:
            # Caso non terminale: dobbiamo provare ad aggiungere una lettera
            # per volta, ed andare avanti nella ricorsione
            for i in range(len(lettere_rimanenti)):
                parziale.append(lettere_rimanenti[i])
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                self.ricorsione_list(parziale, nuove_lettere_rimanenti)
                parziale.pop()  # faccio back tracking


if __name__ == "__main__":

    model = Model()

    start_time = time()
    print(model.calcola_anagrammi_list(["c", "s", "a"]))
    end_time = time()
    print(end_time-start_time)

    # print(model.calcola_anagrammi_list("Dog"))
