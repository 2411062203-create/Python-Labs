#HOẠT ĐỘNG 3 - Phạm Thị Minh Phương - 2411062203

#3.1
#Định dạng sai
#1diem - Bắt đầu bằng chữ số (Python không cho phép tên biến bắt đầu bằng số)
#gia-tri - Chứa ký tự gạch ngang - (Python hiểu nhầm là phép trừ)
#class - Trùng với từ khóa hệ thống (keyword) của Python.
#so luong - Chứa khoảng trắng giữa các từ
#2024_data - Bắt đầu bằng chữ số
#tong$ - Chứa ký tự đặc biệt $
#Định dạng hợp lệ
#_tam_thoi - Bắt đầu bằng dấu gạch dưới _ và chứa các chữ cái hợp lệ
#Diem_TB - Đúng cú pháp Python (chỉ bao gồm chữ cái và dấu gạch dưới)
#MAX_SPEED - Đúng cú pháp (thường dùng làm hằng số)
#diemTB - Đúng cú pháp Python (đặt theo kiểu camelCase)
#sinhVien1 - Đúng cú pháp (chứa chữ cái và chữ số ở cuối)

#3.2
# Đặt tên biến và hằng số chuẩn PEP8
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  # Hằng số

# Xuất toàn bộ thông tin
print("Ho va ten:", ten)
print("Diem Toan:", diem_toan)
print("Diem Van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUC_LUONG_TOI_THIEU)

#HOẠT ĐỘNG 5

#5.1
a = 17
b = 5
print("--- 5.1 ---")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)    
print("a // b =", a // b)  
print("a % b =", a % b)   
print("a ** b =", a ** b)

# - / trả về số thực (float), còn // trả về phần nguyên (int) lấy tròn xuống
# - % lấy phần dư của phép chia, còn // lấy phần nguyên

#5.2
diem = 6.5
tuoi = 20
print("\n--- 5.2 ---")
loai_kha = (diem >= 6.5) and (diem < 8.0)
print("Diem dat loai Kha (and):", loai_kha)
chua_du_18_hoac_tren_60 = (tuoi < 18) or (tuoi > 60)
print("Tuoi chua du 18 hoac tren 60 (or):", chua_du_18_hoac_tren_60)

print("Phu dinh dieu kien diem (not):", not loai_kha)
print("Phu dinh dieu kien tuoi (not):", not chua_du_18_hoac_tren_60)

#5.3
print("\n--- 5.3 ---")

# Thực hiện chuỗi toán tử gán và in giá trị x sau mỗi bước
x = 10

x += 5  # x = 10 + 5 = 15
print("Gia tri x sau x += 5 la:", x)
x -= 3  # x = 15 - 3 = 12
print("Gia tri x sau x -= 3 la:", x)
x *= 2  # x = 12 * 2 = 24
print("Gia tri x sau x *= 2 la:", x)
x /= 4  # x = 24 / 4 = 6.0
print("Gia tri x sau x /= 4 la:", x)
x //= 2 # x = 6.0 // 2 = 3.0
print("Gia tri x sau x //= 2 la:", x)
x **= 3 # x = 3.0 ** 3 = 27.0
print("Gia tri x sau x **= 3 la:", x)

# Sử dụng toán tử in
danh_sach = [1, 2, 3, "python"]
print("3 co nam trong danh_sach khong?:", 3 in danh_sach)

# Sử dụng toán tử is để so sánh 2 biến cùng tham chiếu tới 1 list
list1 = danh_sach
list2 = [1, 2, 3, "python"]

print("list1 is danh_sach (cung tham chieu):", list1 is danh_sach)
print("list2 is danh_sach (khac tham chieu):", list2 is danh_sach)

#5.4 
print("\n--- 5.4 ---")
# Dự đoán: 4 ** 2 = 16 -> 3 * 16 = 48 -> 2 + 48 = 50
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)

# Dự đoán: (2 + 3) = 5 -> 4 ** 2 = 16 -> 5 * 16 = 80
print("(2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)

# Dự đoán: 10 > 5 (True), 3 < 1 (False), not False (True)
print("10 > 5 and 3 < 1 or not False =", 10 > 5 and 3 < 1 or not False)

#HOẠT ĐỘNG 6
#6.1
print("\n--- 6.1 ---")

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

#6.2 
print("\n--- 6.2 ---")

ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))