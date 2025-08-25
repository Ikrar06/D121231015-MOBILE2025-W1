def hitung_faktorial(n: int) -> int:
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def main():
    try:
        n = int(input("Masukkan bilangan bulat: ").strip())
        if n < 0:
            print("Bilangan harus lebih dari 0!")
            return
    except ValueError:
        print("Harus bilangan bulat!")
        return
    
    print(f"Faktorial dari {n} adalah {hitung_faktorial(n)}")

if __name__ == "__main__":
    main()