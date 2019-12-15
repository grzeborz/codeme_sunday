wiek = input("Podaj wiek -->")
wzrost = input("Podaj wzrost w centymetrach-->")
limit_wiek = 10
limit_wzrost = 140

if int(wiek) > limit_wiek:
    if int(wzrost) > limit_wzrost:
        print("mozesz wejsc na zjezdzalnie")
    else:
        print("Wzrost nie spełnia wymagań")
else:
    print("Wiek nie spełnia wymagań")
