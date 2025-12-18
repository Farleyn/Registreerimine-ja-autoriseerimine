import random
import string


def genereeri_parool(pikkus=12):
    margid = ".,:;!_*-+()/#¤%&"
    kõik = margid + string.digits + string.ascii_letters
    return ''.join(random.choice(kõik) for _ in range(pikkus))

def registreeri(users, passwords):
    while True:
        nimi = input("\nSisesta uus kasutajanimi: ")
        if nimi in users:
            print("Nimi juba võetud!")
            continue

        print("\n1 - Sisestan parooli ise")
        print("2 - Genereeri parool automaatselt")
        valik = input("Valik: ")

        if valik == "1":
            parool = input("Sisesta parool: ")
            if len(parool) < 4:
                print("\nNõrk parool!")
                continue
        elif valik == "2":
            parool = genereeri_parool()
            print(f"\nGenereeritud parool: {parool}")
        else:
            print("\nVale valik!")
            continue

        users.append(nimi)
        passwords.append(parool)
        print("\nRegistreerimine õnnestus!\n")
        return


def autoriseeri(users, passwords):
    while True:
        nimi = input("\nSisesta kasutajanimi: ")
        parool = input("Sisesta parool: ")

        if nimi not in users:
            print("\nSellist kasutajat pole!")
            continue

        i = users.index(nimi)
        if passwords[i] != parool:
            print("\nVale parool!")
            continue

        print("\nSisselogimine õnnestus!\n")
        return nimi


def muuda(users, passwords, current_user):
    i = users.index(current_user)
    print("\n1 - Muuda nime")
    print("2 - Muuda parooli\n")
    valik = input("Valik: ")

    if valik == "1":
        uus_nimi = input("\nUus nimi: ")
        if uus_nimi in users:
            print("\nNimi juba võetud!\n")
        else:
            users[i] = uus_nimi
            print("\nNimi muudetud!\n")
            return uus_nimi

    elif valik == "2":
        print("\n1 - Sisestan parooli ise")
        print("2 - Genereeri parool automaatselt")
        v = input("Valik: ")

        if v == "1":
            uus_parool = input("Sisesta uus parool: ")
        elif v == "2":
            uus_parool = genereeri_parool()
            print(f"\nUus parool: {uus_parool}")
        else:
            print("\nVale valik!")
            return current_user

        passwords[i] = uus_parool
        print("\nParool muudetud!\n")

    return current_user


def unustatud_parool(users, passwords):
    nimi = input("\nSisesta kasutajanimi: ")
    if nimi not in users:
        print("\nSellist kasutajat pole!\n")
        return

    i = users.index(nimi)
    print("\n1 - Sisestan uue parooli ise")
    print("2 - Genereeri parool automaatselt")
    valik = input("Valik: ")

    if valik == "1":
        uus = input("Sisesta uus parool: ")
    elif valik == "2":
        uus = genereeri_parool()
        print(f"\nUus parool: {uus}")
    else:
        print("\nVale valik!")
        return

    passwords[i] = uus
    print("\nParool taastatud!\n")
