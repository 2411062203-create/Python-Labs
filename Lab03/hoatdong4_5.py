import math

# Hoạt động 4: Tuple 

# Bài tập 4.1 
toa_do = (3, 5)
print(toa_do, type(toa_do))

# Thử gán lại (bỏ dấu # ở dòng dưới để quan sát lỗi TypeError nếu muốn)
# toa_do[0] = 10  # Lỗi vì Tuple là kiểu dữ liệu bất biến (không sửa được)

print("-" * 50)

# Bài tập 4.2 
x, y = toa_do
print("x =", x, "- y =", y)

# Đổi giá trị 2 biến bằng unpacking (không cần biến tạm)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

print("-" * 50)

# Bài tập 4.3 
c, d = 17, 5
thuong_du = divmod(c, d)  # divmod trả về một tuple (thuong, du)
thuong, du = thuong_du    # unpacking kết quả
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

print("=" * 50)

# Hoạt động 5: Vận dụng Tuple - Tọa độ điểm & khoảng cách

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

# Yêu cầu: Tính khoảng cách của từng điểm so với gốc tọa độ (0, 0)
print("\n--- Khoang cach cua cac diem so voi goc toa do (0, 0) ---")

cac_diem = [(0, 0), (3, 4), (6, 8)]

for x, y in cac_diem:
    # Khoảng cách tới (0,0) áp dụng công thức: sqrt((x - 0)^2 + (y - 0)^2) = sqrt(x^2 + y^2)
    kc_goc = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu điểm ({x}, {y}) den (0, 0) la: {round(kc_goc, 2)}")