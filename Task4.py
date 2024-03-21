def main():
    grades = []
    
    # Input nilai sampai -1 dimasukkan
    while True:
        nilai = input("Masukkan nilai (-1 untuk berhenti): ")
        
        # Periksa apakah input adalah -1
        if nilai == '-1':
            break
        
        # Tambahkan nilai ke dalam list
        grades.append(int(nilai))
    
    # Hitung rata-rata nilai
    rata_rata = int(sum(grades) / len(grades))
    
    # Output rata-rata
    print(rata_rata)
    
    # Output nilai secara berurutan sesuai dengan urutan masukan
    for nilai in grades:
        print(nilai)

if __name__ == "__main__":
    main()
