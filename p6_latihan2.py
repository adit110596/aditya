#mendefinisakan debet dan kredit sebagai fungsi yang akan di buat
def selisih(debet, kredit):
    #memasukkan rumus fungsi ke dalam variable hasil
    hasil = debet - kredit
    #mengembalikan/memanggil kembali variable hasil agar bisa di cetak nilainya
    return hasil

def sums(input_array):
    total = 0
    for idx in range(0, len(input_array)):
        total = total + input_array[idx]
    return total

def selisih_list(debet, kredit):
    debet_total = sums(debet)
    kredit_total = sums(kredit)
    
    hasil = selisih(debet_total, kredit_total)
    return hasil


debet = [1000000,0,0,50000]
kredit = [0,500000,25000,0]
print(selisih_list(debet, kredit))