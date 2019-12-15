stan_konta = 300 - 290
wyplata = 30
debet = 50

if stan_konta > wyplata:
    print("Możesz wypłacić")
elif wyplata < stan_konta + debet:
    print("Mozesz wyplacic, ale wejdziesz na debet")
else:
    print("Brak hajsiku")
