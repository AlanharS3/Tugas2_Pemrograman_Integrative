def main():
    total = 0
    
    while True:
        num = input("Masukkan sebuah angka (-1 untuk berhenti): ")
        
        # Periksa apakah input adalah -1
        if num == '-1':
            break
        
        # Konversi input ke float dan tambahkan ke total
        total += float(num)
    
    # Cetak total jumlah dengan dua digit setelah titik desimal
    print(f"{total:.2f}")

if __name__ == "__main__":
    main()
