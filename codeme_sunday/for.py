for i in range(3):
    print(f"to jest iteracja numer {i}")
    i += 1


film = "Matrix"
licznik = 0
for i in film:
    if licznik % 2:
        print(i)
    if i == "i":
        continue
        #break#
    print(i)


for index, literka in enumerate(film):
    print(index, literka)

for krotka in enumerate(film, start=12):
    print(krotka)