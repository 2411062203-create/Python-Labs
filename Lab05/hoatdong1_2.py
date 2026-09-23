#Hoạt động 1
#bài 1.1
print("bai tap 1.1")
tuoi = 20
if tuoi >= 18:
  print("Da du tuoi truong thanh")
if tuoi >= 18:
  print("Duoc phep dang ky xe may")
else:
  print("Chua du tuoi")

#bài 1.2
print("bai tap 1.2")
diem = 7.2
if diem >= 8.0:
  print("xep loai: gioi")
elif diem >= 6.5:
  print("xep loai: kha")
elif diem >= 5:
  print("xep loai: trung binh")
else:
  print("xep loai: yeu")

#bai 1.3
print("bai tap 1.3")
tuoi = 17
co_giay_phep = False
if tuoi >= 18:
  if co_giay_phep:
    print("duoc phep lai xe")
  else:
    print("du tuoi nhung chua có giay phep")
else:
  print("chua du tuoi lai xe")

#bai 1.4
print("bai tap 1.4")
diem = 4.5
ket_qua = "dat" if diem >= 5.0 else "khong dat"
print(ket_qua)
so = -7
tri_tuyet_doi = so if so >= 0 else -so
print(tri_tuyet_doi)

#hoạt động 2
#bai 2.1
print("bai tap 2.1")
ho_ten = "Nguyen Van A"
diem_toan, diem_ly, diem_hoa = 8.0, 7.5, 9.0
dtb = round((diem_toan + diem_ly + diem_hoa)/3, 2)
if dtb >= 8.0:
  xep_loai = "gioi"
elif dtb >= 6.5:
  xep_loai = "kha"
elif dtb >= 5.0:
  xep_loai = "trung binh"
else:
  xep_loai = "yeu"
print(f"{ho_ten} - DTB: {dtb} - Xep loai: {xep_loai}")

#bai 2.2
print("bai tap 2.2")
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
c = float(input("Nhap so thu ba: "))
if a >= b and a >= c:
 lon_nhat = a
elif b >= a and b >= c:
 lon_nhat = b
else:
 lon_nhat = c
print("So lon nhat la:", lon_nhat)