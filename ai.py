def handle_user_input():
    """
    Fungsi untuk menangani input pengguna dengan berbagai respons
    """
    print("Halo para sepuh!")
    
    try:
        user_input = input("Masukkan pesan Anda: ").strip().lower()
        
        response_mapping = {
            "i love you": "Maaf, kamu terlalu baik untukku",
            "halo dek": "Mas rahimku anget mas"
        }
        
        # Cek input pengguna terhadap mapping respons
        if user_input in response_mapping:
            print(response_mapping[user_input])
        else:
            print("Pesan tidak dikenali")
    
    except Exception as e:
        print(f"Terjadi error: {str(e)}")

# Panggil fungsi utama
if __name__ == "__main__":
    handle_user_input()
