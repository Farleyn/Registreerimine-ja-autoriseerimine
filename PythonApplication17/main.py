from moodul import *

users = []
passwords = []
current_user = None

while True:
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime/parooli muutmine")
    print("4 - Unustatud parooli taastamine")
    print("5 - Lõpetamine")

    valik = input("Valik: ")

    if valik == "1":
        registreeri(users, passwords)
    elif valik == "2":
        current_user = autoriseeri(users, passwords)
    elif valik == "3":
        if current_user is None:
            print("Pole sisse logitud!")
        else:
            current_user = muuda(users, passwords, current_user)
    elif valik == "4":
        unustatud_parool(users, passwords)
    elif valik == "5":
        break
