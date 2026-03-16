from dataclasses import dataclass

#Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

#Si modifichi la classe cliente in maniera tale che la proprietà categoria sia "protetta"
# e accetti solo ("Gold", "Silver", "Bronze")

categorie_valide = {"Gold", "Silver", "Bronze"}

class Cliente:
    def __init__(self, nome, mail, categoria):
        self.nome = nome
        self.mail = mail
        self._categoria = None
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. Scegliere fra Gold, Silver, Bronze")
        self._categoria = categoria

    def descrizione(self): #to_string
        # "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"

@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

    def __str__(self):
        return f"{self.nome} -- {self.mail} ({self.categoria})"


def _test_modulo():
    c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
    # c2 = Cliente("Carlo Masone", "carlo.masone@polito.it", "Platinum")
    print(c1.descrizione())

if __name__ == "__main__":
    _test_modulo()