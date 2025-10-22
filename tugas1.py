# Program Hitung Gaji Karyawan
print("PROGRAM HITUNG GAJI KARYAWAN")

# Input
nama = input("Nama Karyawan: ")
gol = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ").upper()
jam = int(input("Jumlah jam kerja: "))

# Gaji pokok (tetap)
gaji = 300000

# Hitung tunjangan jabatan
if gol == 1:
    tj_jabatan = 0.05 * gaji
elif gol == 2:
    tj_jabatan = 0.10 * gaji
elif gol == 3:
    tj_jabatan = 0.15 * gaji
else:
    tj_jabatan = 0

# Hitung tunjangan pendidikan
if pendidikan == "SMA":
    tj_pendidikan = 0.025 * gaji
elif pendidikan == "D1":
    tj_pendidikan = 0.05 * gaji
elif pendidikan == "D3":
    tj_pendidikan = 0.20 * gaji
elif pendidikan == "S1":
    tj_pendidikan = 0.30 * gaji
else:
    tj_pendidikan = 0

# Hitung honor lembur
if jam > 8:
    lembur = (jam - 8) * 3500
else:
    lembur = 0

# Hitung total gaji
total = gaji + tj_jabatan + tj_pendidikan + lembur

# Output
print("-----------------------------")
print("Nama :", nama)
print("Golongan :", gol)
print("Pendidikan :", pendidikan)
print("Jumlah Jam Kerja :", jam)
print("-----------------------------")
print("Tunjangan Jabatan Rp", round(tj_jabatan))
print("Tunjangan Pendidikan Rp", round(tj_pendidikan))
print("Honor Lembur Rp", round(lembur))
print("-----------------------------")
print("Total Gaji = Rp", round(total))
