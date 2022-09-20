"""
   Tento zdrojový kód pochází z IT sociální sítě WWW.ITNETWORK.CZ v rámci závěrečného projektu

   odkaz na http://www.itnetwork.cz
"""

class Pojisteny:

 def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
    self.jmeno = jmeno
    self.prijmeni = prijmeni
    self.vek = vek
    self.telefonni_cislo = telefonni_cislo

 def __str__(self):
     return f'{self.jmeno} \t {self.prijmeni} \t {self.vek} \t {self.telefonni_cislo}'