# cara membuat list manual

a = [1,"pisang",2,"nanas"]

#print(type(a))
print(a)

# cara mengakses list

print(a[0])
print(a[1])
print(a[2])
print(a[3])

# cara menghapus isi dari list menggunakan remove

a.remove("pisang")

print(a)

# cara menghapus isi dari list menggunakan del

del a[2]
print(a)

# cara menambah isi/anggota list

a.append("jeruk")
print(a)

# cara menghapus isi dari list menggunakan pop

a.pop(2)
print(a)