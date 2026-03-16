import copy
from collections import Counter
from collections import deque

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello =[p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key = lambda x: x.prezzo_unitario, reverse=True)

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

#Aggiungere
carrello.append(ProdottoRecord("Propdo", 100.0))
carrello.extend([ProdottoRecord("aaa", 100.0), ProdottoRecord("bbb", 100.0)])
carrello.insert(2, ProdottoRecord("ccc", 100.0))

#Rimuovere
carrello.pop() # rimuove l'ultimo elemento
carrello.pop(2) # rimuove l'elemento in posizione 2
carrello.remove(p1) #elimino la prima occorrenza di p1
# carrello.clear() #svuoto la lista

#Sorting
# carrello.sort() #ordina seguendo ordinamento naturale -- questo non funziona se gli oggetti contenuti non definisco un metodo __lt__
# carrello.sort(reverse=True) #ordina al contrario
# carrello.sort(key = function)
# carrello_ordinato = sorted(carrello)

#Copie ed altro
carrello.reverse() # inverte l'ordine
carrello_copia = carrello.copy() # shallow copy
carrello_copia2 = copy.deepcopy(carrello) # deep copy, ovvero copio anche il contenuto

# TUPLE
sede_principale = (45, 8) #lat e long della sede di torino
sede_milano = (45, 9) #lat e long della sede di milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))


tot, media, max, min = calcola_statistiche_carrello(carrello)

# tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#SET
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie)
print(len(categorie))
categorie2 = {"Platinum", "Elite", "Gold"}
# categorie_all = categorie.union(categorie2)
categorie_all = categorie | categorie2 # unione
print(categorie_all)

categorie_comuni = categorie & categorie2 # solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie2 #solo gli elementi presenti in uno dei due set
print(categorie_esclusive)

categorie_esclusive_symm = categorie ^ categorie2 # differenza simmetrica
print(categorie_esclusive_symm)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200),
                     ProdottoRecord("Mouse", 20),
                     ProdottoRecord("Tablet", 700)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200),
                     ProdottoRecord("Mouse2", 20),
                     ProdottoRecord("Tablet", 700)}

#Metodi utili per i set
s = set()
s1 = set()

#aggiungere
s.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) #aggiungo più elementi

#togliere
# s.remove(elem) #rimuove un elemento. Raise KeyError se non esiste.
# s.discard(elem) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste.
s.pop() #rimuove e restituisce un elemento.
s.clear()

#operazioni insiemistiche
s.union(s1) # s | s1, ovvero genera un set che unisce i due set di partenza
s.intersection(s1) # s & s1, ovvero solo elementi comuni
s.difference(s1) # s-s1, ovvero elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #s ^s1, ovvero elementi di s non contenuti in s1 ed elementi di s1 non contenuti in s

s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi

#Dictionary
catalogo = {
    "LAP001": ProdottoRecord("Laptop", 1200),
    "LAP002": ProdottoRecord("Laptop Pro", 2300.0),
    "MAU001": ProdottoRecord("Mouse", 20.0),
    "AUR001": ProdottoRecord("Auricolari", 250.0)
}

cod = "LAP002"
prod = catalogo[cod]

print(f"Il prodotto con codice {cod} è {prod}")

# print(f"Cerco un altro oggetto: {catalogo["NonEsiste"]}")

prod1 = catalogo.get("NonEsiste")

if prod1 is None:
    print("Prodotto non trovato")

prod2 = catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0))

print(prod2)

#ciclare su un dizionario
keys = list(catalogo.keys())
values = list(catalogo.values())

for k in keys:
    print(k)

for v in values:
    print(v)

for key, val in catalogo.items():
    print(f"Cod {key} è associata a: {val}")

#rimuovere dal dizionario
rimosso = catalogo.pop("LAP002")
print(rimosso)

#dict comprehesion
prezzi = {codice: prod.prezzo_unitario for codice,prod in catalogo.items()}

#DA RICORDARE PER DICT
# d[key] = v # scrivo sul dizionbario
# v = d[key] # leggere -- restituisce key error se non esiste
# v = d.get(key, default) # legge senza rischiare keyerror. Se non esiste rende il default
# d.pop(key) # restiuisce un voalore e lo cancella dal diz
# d.clear() # elimina tutto.
# d.keys() # mi restituisce tutte le chiavi definite nel diz
# d.values() # mi resituisce tutti i valori salvati nel diz
# d.items() # restituisce le coppie.
# key in d # condizione che verifica se key è presente nel diz

"""Esercizio live
Per ciascuno dei seguenti casi, decidere quale struttura usare:"""

"""1) Memorizzare una elenco di ordini che dovranno poi essere processati in ordine di arrivo"""
# Collection? Lista

ordini_da_processare = []
o1 = Ordine([], ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"))
o2 = Ordine([], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"))
o3 = Ordine([], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"))
o4 = Ordine([], ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"))

ordini_da_processare.append((o1, 0))
ordini_da_processare.append((o2, 10))
ordini_da_processare.append((o3, 3))
ordini_da_processare.append((o4, 45))

"""2) Memorizzare i CF dei clienti (univoco)"""
# Collection?
codici_fiscali = {"ajnfkefioe231", "ajnsow241", "njknaskm1094", "ajnsow241"}
print(codici_fiscali)

"""3) Creare un database di prodotti che posso cercare con un codice univoco"""
# Collection?
listino_prodotti = {"LAP0001" : ProdottoRecord("Laptop", 1200.0),
                    "KEY001" : ProdottoRecord("Keyboard", 20.0)}

"""4) Memorizzare le coordinate gps della nuova sede di Roma"""
# Collection?
magazzino_roma = (45, 6)

"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale"""
# Collection?
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("=============================================================")

#COUNTER
lista_clienti = [
    ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "mario@polito.it", "Gold"),
    ClienteRecord("Giuseppe Averta", "bianchi@polito.it", "Silver"),
    ClienteRecord("Francesca Pistilli", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Fulvio Corno", "carlo@polito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print("Distribuzione categorie clienti")
print(categorie_counter)

print("2 Categorie più frequent1")
print(categorie_counter.most_common(2))

print("totale:")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop": 13, "Tablet": 15}
)

vendite_febbraio = Counter(
    {"Laptop": 3, "Stampante": 1}
)

vendite_bimestre = vendite_gennaio+vendite_febbraio

#Aggregare informazione
print(f"Vendite Gennaio: {vendite_gennaio}")
print(f"Vendite Febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")

# Fare la differenza
print(f"Differenza di vendite: {vendite_gennaio-vendite_febbraio}")


#modificare i valore in the fly

vendite_gennaio["Laptop"] += 4
print(f"Vendite Gennaio: {vendite_gennaio}")

# metodi da ricordare
#c.most_common(n) #restituisce gli n elementi più frequenti
#c.total() # somma dei conteggi

#Deque

coda_ordini = deque()

for i in range (1,10):
    cliente=ClienteRecord(f'Cliente{i}', f'cliente{i}@polito.it', 'Gold')
    prodotto=ProdottoRecord(f'Prodotto{i}',100*i)
    ordine=Ordine([RigaOrdine(prodotto,1)] , cliente)
    coda_ordini.append(ordine)

print(f'Ordini in coda:{len(coda_ordini)}')

while coda_ordini: #cicla finchè è pieno
    ordine_corrente = coda_ordini.popleft()
    print(f"Sto gestendo l'ordine del cliente: {ordine_corrente.cliente}")

print('Ho processato tutti gli ordini')
