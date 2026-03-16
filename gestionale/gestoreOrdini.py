from collections import deque, Counter, defaultdict

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

'''
Voglio creare un software gestionale che abbia le seguenti caratteristiche:
1) supportare l'arrivo e la gestione degli ordini
1bis) quanto arriva un nuovo ordine lo aggiungo alla coda, assicurandomi che sia servito solo dopo gli altri
2) avere delle funzionalità per avere statistiche sugli ordini
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente
'''

class GestoreOrdini:

    def __init__(self):
        self._ordiniProcessare = deque()
        self._ordiniProcessati = []
        self._statisticheProdotti = Counter()
        self._ordiniCategoria = defaultdict()

    def addOrdine(self, ordine: Ordine):
        #Aggiunge un nuovo ordine agli elementi da gestire

        self._ordiniProcessare.append(ordine)
        print(f'Ricevuto un nuovo ordine da parte di {ordine.cliente}')
        print(f'Ordini ancora da evadere: {len(self._ordiniProcessare)}')

    def processaProssimoOrdine(self):
        #Legge il prossimo ordine in coda e lo gestisce

        if not self._ordiniProcessare: #devo assicurarmi di avere ordini da gestire
            print('Non ci sono ordini in coda.')
            return False

        ordine = self._ordiniProcessare.popleft() #Logica FIFO
        print(f"Processo l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        #Aggiornare statistiche sui prodotti venduti
        for riga in ordine.righe:
            self._statisticheProdotti[riga.prodotto.name] += riga.quantita

        #Aggiornare gli ordini per categoria
        self._ordiniCategoria[ordine.cliente.categoria].append(ordine)

        #Archiviare l'ordine
        self._ordiniProcessati.append(ordine)

        print('Ordine correttamente processato')
        return True

    def processaTuttiOrdini(self):
        #Processa tutti gli ordini attualmente presenti in coda
        print('\n' + '=' * 60)
        print(f'Processando {len(self._ordiniProcessare)} ordini')

        while self._ordiniProcessare:
            self.processaProssimoOrdine() #delego al metodo di gestione del singolo ordine

        print(f'Tutti gli ordini sono stati processati')

    def getStatisticheProdotti(self, topN: int=5): #Se non viene dato è messo a 5 di default
        #Questo metodo restituisce info su quante unità sono state vendute di un certo prodotto
        #Non stampo, delego la stampa a chi chiama il metodo

        valori=[]
        for prodotto, quantita in self._statisticheProdotti.most_common(topN):
            valori.append((prodotto, quantita)) #Se non avessi fatto questo avrei ritornato direttamente una parte del Counter in una lista

        return valori

    def getStatisticheDistribuzione(self):
        #Questo metodo restituisce info su totale fatturato per ogni categoria presente

        valori=[]
        for cat in self._ordiniCategoria.keys():
            ordini = self._ordiniCategoria[cat]
            totaleFatturato = sum([ordini.totale_lordo(0.22) for o in ordini])
            valori.append((cat,totaleFatturato))
        return valori


    def stampaRiepilogo(self):
        #Stampa info di massimo

        print('\n'+'='*60)
        print(f'Stato attuale del business:')
        print(f'Ordini correttamente gestiti: {len(self._ordiniProcessati)}')
        print(f'Ordini in coda: {len(self._ordiniProcessare)}')

        print('Prodotti più venduti:')
        for prod,quantita in self._getStatisticheProdotti():
            print(f'{prod}: {quantita}')

        print('Fatturato per categoria:')
        for cat,fatturato in self.getStatisticheDistribuzione():
            print(f'{cat}: {fatturato}')

def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([
            RigaOrdine(ProdottoRecord('Laptot',1200.0),1),
            RigaOrdine(ProdottoRecord('Mouse',10.0),3)
        ], ClienteRecord('Mario Rossi', 'mario@gmail.com', 'Gold')),
        Ordine([
            RigaOrdine(ProdottoRecord('Laptot', 1200.0), 1),
            RigaOrdine(ProdottoRecord('Mouse', 10.0), 2),
            RigaOrdine(ProdottoRecord('Tablet', 500.0), 1),
            RigaOrdine(ProdottoRecord('Cuffie', 250.0), 3)
        ], ClienteRecord('Fulvio Bianchi', 'bianchi@gmail.com', 'Gold')),
        Ordine([
            RigaOrdine(ProdottoRecord('Laptot', 1200.0), 2),
            RigaOrdine(ProdottoRecord('Mouse', 10.0), 2)
        ], ClienteRecord('Giuseppe Averta', 'giuseppe.averta@polito.it', 'Silver')),
        Ordine([
            RigaOrdine(ProdottoRecord('Tablet', 900.0), 1),
            RigaOrdine(ProdottoRecord('Cuffie', 250.0), 3)
        ], ClienteRecord('Carlo Masone', 'carlo@mail.com', 'Gold')),
        Ordine([
            RigaOrdine(ProdottoRecord('Laptot', 1200.0), 1),
            RigaOrdine(ProdottoRecord('Mouse', 10.0), 3)
        ], ClienteRecord('Francesca Pistilli', 'francesca@gmail.com', 'Bronze'))
    ]

    for o in ordini:
        sistema.addOrdine(o)

    sistema.processaTuttiOrdini()

    sistema.stampaRiepilogo()

if __name__ == '__main__':
    test_modulo()