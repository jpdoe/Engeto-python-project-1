#!/usr/bin/env python3

# Popis: 1. projekt 'Textový analyzátor' v Engeto Online Python Akademie
# Autor: Jan Polák

'''
author = Jan Polák
'''
TEXTS = [
    """
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.""",

    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",

    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."""
]
SEPARATOR = 42 * "-"
USERS = dict(bob="123", ann="pass123", mike="password123", liz="pass123")


# Pomocná datová struktura pro jednoduší manipulaci
class NumberStats:
    def __init__(self):
        self.titlecase = 0
        self.uppercase = 0
        self.lowercase = 0
        self.numeric = 0
        self.summed = 0
        self.words = 0


# Třída s metodami pro jednoduší manipulaci
class Stats:
    def __init__(self):
        self.numbers = NumberStats()
        self.histogram = dict()
        self.sorted_histogram = list()

    def print_histogram(self):
        print("Histogram délky slov:")
        for item in self.sorted_histogram:
            print(item, "*" * self.histogram[item], self.histogram[item])

    def print_stats(self):
        print(f"Ve zvoleném textu je celkem {self.numbers.words} slov:",
              f"    {self.numbers.titlecase}krát slovo začínající velkým písmenem",
              f"    {self.numbers.uppercase}krát slovo psané velkými písmeny",
              f"    {self.numbers.lowercase}krát slovo psané malými písmeny",
              f"    {self.numbers.numeric}krát číselný řetězec",
              f"Celkový součet hodnot číselných řetězců je {self.numbers.summed} ",
              sep='\n')

    def fill_stats(self, text_string):
        string_to_analyze = text_string.split()

        for word in string_to_analyze:

            word_clean = word.strip(',.')

            if word_clean.istitle():
                self.numbers.titlecase += 1

            elif word_clean.isupper():
                self.numbers.uppercase += 1

            elif word_clean.islower():
                self.numbers.lowercase += 1

            elif word_clean.isnumeric():
                self.numbers.numeric += 1

                self.numbers.summed += int(word_clean)

            self.histogram[len(word_clean)] = self.histogram.get(len(word_clean), 0) + 1

        # Celkový počet slov v textu
        self.numbers.words = len(string_to_analyze)

        # Seřazený histogram - klíče od nejmenšího po největší
        self.sorted_histogram = sorted(self.histogram)


def login(users_db):
    while True:
        username = input("Uživatelské jméno:").strip()
        password = input("Heslo:")

        # Test hesla
        if username in users_db.keys() and password == users_db.get(username, 0):
            # Heslo je správné -> vyskočit ze smyčky
            break

        else:
            print(f"Uživatel {username} nemá přístup nebo zadal špatné heslo")
            print("Zadejte údaje znovu")
            # Heslo je nesprávné -> pokračovat ve smyčce
            continue


def choose_text(text_string):
    # Počet dostupných textů
    text_count = len(text_string)
    print(f"Zvolte jeden z {text_count} textů k analýze")

    while True:

        selection = int(input(f"Zvolte číslo textu (1-{text_count}):"))

        # Test zadaného čísla výběru
        if selection > 0 and selection <= text_count:
            break
        else:
            print("Zadali jste číslo mimo rozsah")

    return text_string[selection - 1]


def main():
    # Uvítání a přihlášení
    print(SEPARATOR)
    print("Vítejte v aplikaci 'Textový analyzátor'. Přihlašte se:")
    login(USERS)

    # Výběr textu ke zpracování
    print(SEPARATOR)
    one_text = choose_text(TEXTS)

    # Výpočet statistik
    print(SEPARATOR)
    statistics = Stats()
    statistics.fill_stats(one_text)

    # Tisk statistik a histogramu
    statistics.print_stats()
    print(SEPARATOR)
    statistics.print_histogram()


if __name__ == '__main__':
    main()
