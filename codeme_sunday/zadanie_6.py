import random
# Napisz program, który wylosuje liczbę z zakresu 1-100, a następnie do zadania użytkownika będzie należało jej odgadnięcie:
#
#     program informuje, że podana liczba jest za duża lub za mała
#     program kończy się, gdy użytkownik zgadnie właściwą liczbę
#     program powinien w tym momencie pogratulować mu wygranej oraz poinformować o liczbie prób, które były potrzebne

wylosowana_liczba = random.randint(1, 101)
print(wylosowana_liczba)

#podaj_liczbe = int(input("Podaj liczbe ktora została wylosowana -->"))
liczba_prob = 1

while True:
    podaj_liczbe = int(input("Podaj liczbe ktora została wylosowana w zakresie od 1 do 100 -->"))
    if podaj_liczbe < wylosowana_liczba:
        print("Twoja liczba jest za mała")
        liczba_prob +=1
    elif podaj_liczbe > wylosowana_liczba:
        print("Twoja liczba jest za duża")
        liczba_prob += 1
    elif podaj_liczbe == wylosowana_liczba:
        print(f"Gratulacje, wykoanles {liczba_prob} prob")
        break

