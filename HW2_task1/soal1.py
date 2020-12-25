arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    arrBerat.sort()
    bMax = arrBerat[0]
    arrBerat.reverse()
    bMin = arrBerat[0]



def rerata(arrBerat):
    total = 0
    for berat in arrBerat:
        total = total + berat
    return total

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    berat = float(input())
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(berat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)
rata = rerata(arrBerat)/n
# Print Data Minimum, Maximum, dan Rerata Berat
print('Berat balita minimum: %.2f'%bMin)
print('Berat balita maksimum: %.2f'%bMax)
print('Rerata berat balita: %.2f'%rata)
