"""
   Tento zdrojový kód pochází z IT sociální sítě WWW.ITNETWORK.CZ v rámci závěrečného projektu

   odkaz na http://www.itnetwork.cz
"""

from pojisteny import Pojisteny

evidovany = []

run = "ano"

while run == "ano":
    try:
        volba = int(
            input("\n---------------------------- \n\n"
                  "Evidence pojistenych\n"
                  "---------------------------- \n\n"
                  "Vyberte si akci: \n"
                  "1 - Pridat noveho pojisteneho\n"
                  "2 - Vypsat vsechny pojistene\n"
                  "3 - Vyhledat pojistence\n"
                  "4 - Konec\n"))

        if volba == 1:
            jmeno = input("Zadejte jmeno pojisteneho:")
            prijmeni = input("Zadejte prijmeni pojisteneho:")
            vek = int(input("Zadejte vek:"))
            while vek < 0:
                print("Špatně zadaný věk.")
                vek = int(input("Zadejte vek:"))
            else:
                pass
            telefonni_cislo = int(input("Zadejte telefonni cislo:"))
            while len(str(telefonni_cislo)) != 9:
                print("Špatně zadané telefonní číslo.")
                telefonni_cislo = int(input("Zadejte telefonni cislo: "))
            else:
               pass
            novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, telefonni_cislo)
            print(f"Pojištěnec {jmeno} {prijmeni} byl nahran.")
            # založení objektu novy_pojisteny - ktery je pridany na konec seznamu
            evidovany.append(novy_pojisteny)
            run = input("Přejete si pokračovat? ano/ne")

        elif volba == 2:
            for pojisteny in evidovany:
                print(pojisteny)
            run = input("Přejete si pokračovat? ano/ne")

        elif volba == 3:
            zaznam = False
            zadane_jmeno = input("Zadejte jméno:")
            zadane_prijmeni = input('Zadejte přijmení:')
            for pojisteny in evidovany:
                if pojisteny.jmeno == zadane_jmeno and pojisteny.prijmeni == zadane_prijmeni:
                    print(pojisteny)
                    print("Pojištěnec existuje")
                    zaznam = True
            if zaznam is False:
                print("Pojištěnec nebyl nalezen")
            run = input("Přejete si pokračovat? ano/ne")

        elif volba == 4:
            run = "Ne"

        else:
            print("Zadali jste nesprávnou volbu.")
            run = input("Přejete si pokračovat? ano/ne")

    except ValueError as error:
        print("Zadali jste nesprávnou volbu.")

konec = input("Aplikace se uzavře stiskem klávesy")
