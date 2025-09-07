def barisan_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("N harus >= 0")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    
    return b

def main():
    print("=== BARISAN FIBONACCI ===")
    
    try:
        n = int(input("Masukkan bilangan bulat untuk Fibonacci: ").strip())
        
        if n < 0:
            print("Bilangan harus >= 0!")
            return
        
        hasil = barisan_fibonacci(n)
        print(f"Fibonacci ke-{n} adalah {hasil}")
        
        print(f"\nDeret Fibonacci hingga F({n}):")
        for i in range(min(n + 1, 15)): 
            print(f"F({i}) = {barisan_fibonacci(i)}")
        
        if n > 14:
            print("...")
            print(f"F({n}) = {hasil}")
            
    except ValueError:
        print("Input harus berupa bilangan bulat!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    print("\n" + "=" * 30 + "\n")
    main()