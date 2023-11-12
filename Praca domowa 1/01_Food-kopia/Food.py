class Składnik:
    def __init__(self, jedzenie, białko, węglowodany, tłuszcze):
        self.jedzenie = jedzenie
        self.białko = białko
        self.węglowodany = węglowodany
        self.tłuszcze = tłuszcze

    def kcal(self):
        return self.białko * 4 + self.węglowodany * 4 + self.tłuszcze * 9.4


class Posiłki:
    def __init__(self, posiłek):
        self.posiłek = posiłek
        self.składniki = {}

    def dodajemy_składniki(self, ilość: int, Składnik):
        if Składnik not in self.składniki:
            self.składniki[Składnik] = 0
        self.składniki[Składnik] += ilość

    def wartości_odżwycze(self):
        wartości = {}
        for składniki, ilość in self.składniki.items():
            wartości[składniki.nazwa] = {
                "białko":  Składnik.białko * ilość / 100,
                "węglowodany": Składnik.węglowodany * ilość / 100,
                "tłuszcze": Składnik.tłuszcze * ilość / 100,
                "kalorie": Składnik.kcal * ilość / 100,
            }
        return wartości

class Plan_dnia:
    def __init__(self, nazwa,):
        self.nazwa = nazwa
        self.posiłki = []

    def nowy_posiłek(self, posiłek):
        self.posiłki.append(posiłek)

    def wartości_odżywcze(self):
        wartości = {
            "białko": 0,
            "węglowodany": 0,
            "tłuszcze": 0,
            "kcal": 0,
        }

        for posilek in self.posilki:
            wartosci_odzywcze = {
                k: wartosci_odzywcze[k] + posilek.oblicz_wartosci_odzywcze()[k]
                for k in wartosci_odzywcze
            }
        return wartosci_odzywcze

egg = Składnik("Jajko", 13, 1.1, 11)
tomato = Składnik("Pomidor", 0.9, 3.9, 0.2)
bread = Składnik("Chleb", 9, 49, 3.2)

scrambled_eggs = Posiłki("Jajecznica")
scrambled_eggs.dodajemy_składniki(egg, 200)
scrambled_eggs.dodajemy_składniki(tomato, 50)

sandwich = Posiłki("Kanapka")
sandwich.dodajemy_składniki(bread, 25)
sandwich.dodajemy_składniki(tomato, 50)

very_minimalistic_menu = Plan_dnia("Oszczędny")
very_minimalistic_menu.dodaj_posilek(scrambled_eggs)
very_minimalistic_menu.dodaj_posilek(sandwich)

print(very_minimalistic_menu.oblicz_wartosci_odzywcze())



