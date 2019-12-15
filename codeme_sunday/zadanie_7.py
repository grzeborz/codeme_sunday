lista = []

for i in range(5):
    elem = lista.append(input("Uzytkowniku wpisz nazwe zwierza --> : "))
lista_sort = sorted(lista)
print(lista_sort[0])
nadpisanie_pierwszego = input("Zamien zwierza na innego --> podaj nazwe nowego zwierza: ")
lista_sort[0] = nadpisanie_pierwszego
lista.sort()
print(lista_sort)
print(lista)

