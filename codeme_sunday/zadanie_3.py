wynik_proc= input("Podaj wynik testu w procentach [%]-->")

wynik_proc = float(wynik_proc)
if wynik_proc >= 0.91:
    print("Otrzymujesz ocecnę 5")
elif wynik_proc <= 0.90 and wynik_proc >= 0.75:
    print("Otrzymujesz ocencę 4")
elif wynik_proc <=0.74 and wynik_proc >= 0.51:
    print("otrzymujesz ocene 3")
elif wynik_proc <=0.50 and wynik_proc >= 0.30:
    print("Otrzymujesz ocene 2")
else:
    print("otrzymujesz ocenę 1")
