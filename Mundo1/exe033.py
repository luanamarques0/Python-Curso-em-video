numero_1 = int(input("número um: "))
numero_2 = int(input("número dois: "))
numero_3 = int(input("número três: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("maior:", numero_1)
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("maior:", numero_2)
else:
    print("maior:", numero_3)

if numero_1 < numero_2 and numero_1 < numero_3:
    print("menor:", numero_1)
elif numero_2 < numero_1 and numero_2 < numero_3:
    print("menor:", numero_2)
else:
    print("menor:", numero_3)