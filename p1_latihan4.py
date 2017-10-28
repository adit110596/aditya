# File: p1_latihan3.py
w = input("nilai A:")
x = input("nilai B:")
y = input("nilai C:")
z = input("nilai D:")


# Pengisian Nilai ke variabel
a = bool(w)
b = bool(x)
c = int(y)
d = int(z)


#operasi logika variabel
ab1 = (a == b)
cd1 = (c >= d)
cd2 = (c > d)
cd3 = (c <= d)
cd4 = (c < d)
cd5 = (c != d)
cd6 = (c == d)


#mencetak hasil operasi variabel
out1 = "a == b adalah " + str(ab1)
print(out1)

out2 = "c >= d adalah " + str(cd1)
print(out2)

out3 = "c > d adalah " + str(cd2)
print(out3)

out4 = "c <= d adalah " + str(cd3)
print(out4)

out5 = "c < d adalah " + str(cd4)
print(out5)

out6 = "c != d adalah " + str(cd5)
print(out6)

out7 = "c == d adalah " + str(cd6)
print(out7)