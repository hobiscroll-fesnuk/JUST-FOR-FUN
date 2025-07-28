import time
from typing import Optional


def simulate_ddos_attack() -> Optional[str]:
    """
    Simulate a DDoS attack (for educational purposes only).
    
    Returns:
        str or None: Status message of the simulation
    """
    print("SELAMAT DATANG CALON HACKER")
    print("---------------------------")
    
    try:
        target_url = input("Masukkan URL target: ").strip().lower()
        
        # Basic URL validation
        if not target_url.startswith(("http://", "https://")):
            print("Error: URL harus dimulai dengan http:// atau https://")
            return None
            
        print(f"\nMemulai simulasi DDoS ke {target_url}...\n")
        
        # Simulation loop
        for attempt in range(1, 21):
            print(f"Request #{attempt}: Mengirim paket ke {target_url}")
            time.sleep(0.5)  # Simulate delay
            
        return "Simulasi DDoS berhasil (20 requests dikirim)"
        
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan oleh pengguna")
        return None
    except Exception as e:
        print(f"Error teknis terjadi: {str(e)}")
        return None


if __name__ == "__main__":
    result = simulate_ddos_attack()
    if result:
        print(f"\nHasil: {result}")
