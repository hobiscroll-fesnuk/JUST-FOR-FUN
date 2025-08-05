import random

def main():
    print("SELAMAT DATANG SEPUH")
    print("SEKEDAR UNTUK HIBURAN")
    print("JANGAN DIBAWA SERIUS")

    # Mengatur warna latar belakang dan teks (hanya untuk referensi, tidak berfungsi di terminal)
    background_color = "#87CEEB"
    text_color = "#8BC34A"

    user_input = input("Masukkan waifu favorit Anda di Naruto: ").lower()

    if user_input == "sakura":
        print("DIH, SUKA KOK SAMA BEBAN")
    elif user_input in ["hinata", "tsunade"]:
        print("SELERAMU BAGUS, KAWAN")
    elif user_input in ["jiraya", "sasuke", "rock lee", "guy"]:
        print("KELUAR KAU KAUM LAGIBETE, SEMOGA NERAKA TEMPATMU")
    else:
        print("INPUT TIDAK VALID, ERROR")

if __name__ == "__main__":
    main()
