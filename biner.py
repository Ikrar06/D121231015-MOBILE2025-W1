def angka_biner(n: int) -> str:
    if n < 0:
        raise ValueError("N harus >= 0")
    
    if n == 0:
        return "0"
    
    biner = ""
    while n > 0:
        biner = str(n % 2) + biner
        n = n // 2
    
    return biner

def tampilkan_proses_konversi(n: int):
    if n < 0:
        print("N harus >= 0")
        return
    
    if n == 0:
        print("0 dalam biner = 0")
        return
    
    print(f"Konversi {n} ke biner:")
    print("Langkah-langkah:")
    
    original_n = n
    langkah = 1
    hasil_biner = ""
    
    while n > 0:
        sisa = n % 2
        hasil_biner = str(sisa) + hasil_biner
        print(f"{langkah}. {n} ÷ 2 = {n // 2} sisa {sisa}")
        n = n // 2
        langkah += 1
    
    print(f"\nMembaca sisa dari bawah ke atas:")
    print(f"{original_n} dalam biner = {hasil_biner}")

def main():
    print("=== KONVERSI ANGKA BINER ===")
    
    try:
        n = int(input("Masukkan bilangan bulat untuk konversi ke biner: ").strip())
        
        if n < 0:
            print("Bilangan harus >= 0!")
            return
        
        hasil = angka_biner(n)
        print(f"\nHasil: {n} dalam biner = {hasil}")
        
        print("\n" + "=" * 40)
        tampilkan_proses_konversi(n)
        
        print(f"\nVerifikasi dengan bin(): {bin(n)[2:]}")

    except ValueError:
        print("Input harus berupa bilangan bulat!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


if __name__ == "__main__":
    print("\n" + "=" * 50 + "\n")
    main()