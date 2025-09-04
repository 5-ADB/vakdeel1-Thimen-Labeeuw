nummer = int(input("geef een getal op"))

for x in range (0, 3):
    if nummer > 5:
        print("succes")
        break
else:    
    print("3x mislukt, probeer opnieuw")