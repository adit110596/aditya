import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


def balance(debet, kredit):
    sel = []
    for idx in range(0, len(debet)):
        if idx == 0: # idx pasti bernilai 0
            awal = debet[idx] - kredit[idx]
            sel.append(awal)
        else: # idx pasti lebih besar dari 0
            idx_before = idx - 1
            lanjutan =  debet[idx] - kredit[idx] + sel[idx_before]
            sel.append(lanjutan)
    return sel


# mengambil data dari data.csv dan di ubah menjadi
# panda DataFrame
df = pd.read_csv('pertemuan6/data.csv')
print(df.head())

# mengambil nilai berbentuk array dari tiap kolom
# yaitu kolom debet dan kredit dan menambah kolom
# selisih ke dalam DataFrame

debet = df.debet.values
kredit = df.kredit.values
df['selisih'] = balance(debet,kredit)


# mencetak DataFrame yang telah di ubah ke dalam
# File excel dengan nama data-olahan.xlsx

writer = ExcelWriter('pertemuan6/data-olahan.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()