class HitungBmi:
    def __init__(self, berat_kg, tinggi_cm):
        self._berat_kg = berat_kg
        self._tinggi_m = tinggi_cm / 100  # konversi sentimeter ke meter
    
    @property
    def berat(self):
        return self._berat_kg
    
    @property
    def tinggi(self):
        return self._tinggi_m
    
    def nilai_BMI(self):
        if self._tinggi_m == 0:
            return "Error: Tinggi tidak boleh nol"
        else:
            return self._berat_kg / (self._tinggi_m ** 2)

# Input berat dan tinggi dari pengguna
berat = float(input("Masukkan berat dalam kilogram: "))
tinggi = float(input("Masukkan tinggi dalam sentimeter: "))

# Buat objek HitungBmi
orang = HitungBmi(berat, tinggi)

# Cetak informasi berat, tinggi, dan nilai BMI
print("Berat:", orang.berat, "kg")
print("Tinggi:", orang.tinggi, "m")
print("Nilai BMI:", f"{orang.nilai_BMI():.2f}")
