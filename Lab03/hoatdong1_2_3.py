#=====HOẠT ĐỘNG 1=====

#Bài 1.1
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
print(diem_so[0]) # phan tu dau tien
print(diem_so[-1]) # phan tu cuoi cung
print(diem_so[1:4]) # cat tu vi tri 1 den truoc 4
print(diem_so[::2]) # lay cach 1 phan tu (step = 2)
print(diem_so[::-1]) # dao nguoc danh sach
#Bai 1.2
ten_sv = ["An", "Binh", "Chi"]
ten_sv.append("Dung") # them vao cuoi
ten_sv.insert(1, "Em") # chen vao vi tri 1
print(ten_sv)
ten_sv.remove("Chi") # xoa theo gia tri
pop_ra = ten_sv.pop() # xoa va lay ra phan tu cuoi
print(ten_sv, "- da xoa:", pop_ra)
ten_sv.sort() # sap xep tang dan (theo bang chu cai)
print(ten_sv)
ten_sv.reverse() # dao nguoc thu tu hien tai
print(ten_sv)
ten_sv.extend(["Giang", "Hoa"]) # noi them mot list khac vao

#=====HOẠT ĐỘNG 2=====

# Bài tập 2.1 

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0

for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))

print("-" * 50)
# Bài tập 2.2 

ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. In ra theo từng hàng
print("--- In ra theo tung hang ---")
for hang in ma_tran:
    print(hang)

# 2. In ra từng phần tử, duyệt theo hàng rồi theo cột
print("\n--- In ra tung phan tu dạng ma tran ---")
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()

tong_ma_tran = 0

for hang in ma_tran:            # Vòng for 1: lấy ra từng hàng (list con)
    for phan_tu in hang:        # Vòng for 2: lấy ra từng số trong hàng
        tong_ma_tran += phan_tu # Cộng dồn từng phần tử vào biến tổng

print("\nTong tat ca phan tu trong ma tran la:", tong_ma_tran)

#=====HOẠT ĐỘNG 3=====

# Bài tập 3.1 

day_so = list(range(1, 21))  # Tạo dãy số từ 1 đến 20

# Dùng list comprehension kết hợp điều kiện if để lọc
so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("So chan:", so_chan)
print("So le:", so_le)

print("-" * 50)
# Bài tập 3.2 

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

# Dùng list comprehension để cộng thêm 0.5 điểm cho từng sinh viên và làm tròn 2 chữ số
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]

print("Diem sau khi cộng:", diem_cong)
# Kết quả xuất ra sẽ là: [9.0, 7.5, 9.7, 7.0, 6.0]