#1. Mereverse setiap kata dalam kalimat
def reverse_per_kata(kalimat):
    return ' '.join([kata[::-1] for kata in kalimat.split()])
    #' '.join() -> untuk menggabungkan seluruh kata yang sudah dibalik dan dipisahkan dengan spasi
    #kata[::-1] -> untuk membalikkan urutan karakter pada setiap kata
    #for kata in kalimat.split() -> melakukan perulangan melalui setiap kata yang dihasilkan kalimat.split()
    #kalimat.split() -> untuk memisahkan string kalimat menjadi list-list kata berdasarkan spasi.
    #return -> adalah cara fungsi mengembalikan hasil yang sudah diproses supaya bisa dipakai di luar fungsi tersebut.

#2 Mengurutkan kata berdasarkan indeks list
def urutkan_kalimat(kalimat,urutan):
    kata = kalimat.split()
    urutan = [kata[i-1] for i in urutan]
    return ' '.join(urutan)
    #kata = kalimat.split() -> Untuk memisahkan string kalimat menjadi list-list kata berdasarkan spasi, dan "kata" sebagai variabel.
    #urutan (sebelah kiri) -> Sebagai variabel yang menyimpan list baru hasil dari list comprehension.
    #kata[i-1] -> Mengambil elemen dari list "kata" pada posisi i-1.
    #for i in urutan -> Melakukan perulangan untuk setiap elemen "i" didalam list urutan.
    #i -> variabel perulangan yang mewakili setiap elemen (indeks) dari list urutan.
    #urutan (sebelah kanan) -> list yang berisi indeks-indeks (angka).
    #return -> adalah cara fungsi mengembalikan hasil yang sudah diproses supaya bisa dipakai di luar fungsi tersebut.

#3 Mengganti huruf vokal dengan simbol tertentu
def ganti_vokal(kalimat,opsi):
    if opsi==1:
        kalimat = kalimat.replace('a','4').replace('i','1').replace('u','|_|').replace('e','3').replace('o','0')
    elif opsi==2:
        kalimat = kalimat.replace('A','4').replace('I','1').replace('U','|_|').replace('E','3').replace('O','0')
    return kalimat
    #if opsi==1 -> Mengecek apakah nilai variabel opsi sama dengan 1. Jika ya, maka fungsi akan mengganti huruf vokal kecil (a, i, u, e, o) dalam string kalimat dengan karakter pengganti yang sudah ditentukan.
    #if opsi==2 -> Mengecek apakah nilai variabel opsi sama dengan 2. Jika ya, maka fungsi akan mengganti huruf vokal besar (A, I, U, E, O) dalam string kalimat dengan karakter pengganti yang sudah ditentukan.
    #kalimat.replace(old,new) -> Menggantikan semua kemunculan substring "old" dengan substring "new" dalam string kalimat.
    #return kalimat -> Mengembalikan string kalimat yang sudah dimodifikasi sebagai hasil fungsi agar bisa digunakan di luar fungsi tersebut.

#Output
#1. Output mereverse dari setiap kata dalam kalimat
print(reverse_per_kata("AKU CINTA KAMU"))

#2. Output mengurutkan kata berdasarkan indeks list
print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON",[5,1,4,3,2]))

#3. Output mengganti huruf vokal dengan simbol tertentu
print(ganti_vokal("Aku Cinta Kamu", 1))
print(ganti_vokal("Aku Cinta Kamu", 2))