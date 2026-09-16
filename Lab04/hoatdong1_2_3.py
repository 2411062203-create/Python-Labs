#HOẠT ĐỘNG 1:
#BÀI TẬP 1.1:

sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5,
}

print(sinh_vien["ho_ten"])
print(sinh_vien.get("diem_tb"))
print(sinh_vien.get("lop","chua co"))

print("-"*50)

#BAI TẬP 1.2:

sinh_vien["lop"] = "CNTT01"
sinh_vien["diem_tb"] = 9.0
print(sinh_vien)

diem_cu = sinh_vien.pop("diem_tb")
print(sinh_vien, "- diem da xoa:", diem_cu)

sinh_vien.update({"nam_sinh": 2003, "email": "phamthiminhphuong06@gmail.com"})
print(sinh_vien)

#HOẠT ĐỘNG 2:

diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
for mon in diem_mon_hoc.keys():
 print(mon)
print("-"*30)
for diem in diem_mon_hoc.values():
 print(diem)
print("-"*30)
for mon, diem in diem_mon_hoc.items():
 print(f"{mon}: {diem}")
print("-"*30)
tong_diem = 0
for diem in diem_mon_hoc.values():
 tong_diem = tong_diem + diem
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

#HOAT ĐỘNG 3:
#BÀI TẬP 3.1:

diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)
print("-"*50)

#BÀI TẬP 3.2:
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print(mon_hoc_ky1 & mon_hoc_ky2)  # giao: môn học chung 2 học kỳ
print(mon_hoc_ky1 | mon_hoc_ky2)  # hợp: tất cả môn học cả 2 học kỳ
print(mon_hoc_ky1 - mon_hoc_ky2)
