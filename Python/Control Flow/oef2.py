temperatuur = int(input("geef de temperatuur op"))

if temperatuur < 10:
    print("koud")
elif temperatuur >= 10 and temperatuur < 20:
    print("nice")
elif temperatuur >= 20 and temperatuur < 30:
    print("het word warm")
elif temperatuur >= 30:
    print("zeer warm")
    