imie = input("Podaj imie -->")
dlugosc = len(imie)
if len(imie)> 9:
    print(f"Twoje imie jest bardzo długie i jest dlugosci {dlugosc}")
else:
    print(f"Twoje imie jest krotkie i jest dlugosci {dlugosc} znakow")