listy = [1,2,3,4,"kot", "pies", True, False]

for i in listy:
    print(i)

lista1 = [1,2]
lista2 = [3,99]

nowa = lista1 + lista2
print(nowa)

nowa.append("kon")
print(nowa)
zwierz = nowa.pop()
# moetoda pop wycina i przypisuje zmiennąą, przuciwieństwo append
print(zwierz)