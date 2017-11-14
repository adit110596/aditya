import random
print("Daftar Pilihan")
print()
print("1.Batu")
print("2.gunting ")
print("3.kertas")
print()

def game_sederhana():
    kom= random.choice({"Batu","gunting","kertas"})
    pil = int(input("Masukan pilihan      :"))
    if pil==1:
        print("anda      :Batu")
        print("komputer   :",kom)
        if kom == "Batu":
            print("\tdraw")
        if kom == "kertas":
            print("\tkamu kalah")
        if kom == "gunting":
            print("\tkamu menang ")
    if pil==2:
        print("anda      :gunting")
        print("komputer   :",kom)
        if kom == "Batu":
            print("\tkamu kalah")
        if kom == "kertas":
            print("\tkamu menang")
        if kom == "gunting":
            print("\tdraw ")
    if pil==3:
        print("anda      :kertas")
        print("komputer   :",kom)
        if kom == "Batu":
            print("\tkamu menang")
        if kom == "kertas":
            print("\tdraw")
        if kom == "gunting":
            print("\tkamu kalah ")

    if pil==4:
        print("pilihan tidak ada")

    game_sederhana()