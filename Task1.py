from datetime import datetime, timedelta

def cetak_tanggal_mendatang(hari):
    # Dapatkan tanggal saat ini
    tanggal_sekarang = datetime.now()

    # Hitung tanggal mendatang
    tanggal_mendatang = tanggal_sekarang + timedelta(days=hari)

    # Format tanggal di masa depan
    tanggal_terformat = tanggal_mendatang.strftime("%A, %d %B %Y")

    # Cetak tanggal mendatang yang telah diformat
    print(tanggal_terformat)

# Masukkan jumlah hari
hari = int(input("Masukkan jumlah hari dari sekarang: "))

# Cetak tanggal mendatang
cetak_tanggal_mendatang(hari)
