import tkinter as tk

# 1. Khởi tạo cửa sổ ứng dụng
cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

# Biến lưu trữ biểu thức toán học
bieu_thuc = ""


# 2. Các hàm xử lý sự kiện
def bam_nut(gia_tri):
    """Thêm số hoặc phép tính vào màn hình hiển thị."""
    global bieu_thuc
    bieu_thuc += str(gia_tri)
    man_hinh_var.set(bieu_thuc)


def xoa_man_hinh():
    """Xóa toàn bộ biểu thức trên màn hình (Nút C)."""
    global bieu_thuc
    bieu_thuc = ""
    man_hinh_var.set("")


def tinh_ket_qua():
    """Tính toán biểu thức toán học khi bấm nút `=`."""
    global bieu_thuc
    try:
        # eval() thực hiện tính toán biểu thức dạng chuỗi
        ket_qua = str(eval(bieu_thuc))
        man_hinh_var.set(ket_qua)
        bieu_thuc = ket_qua  # Lưu lại kết quả để tính tiếp
    except ZeroDivisionError:
        man_hinh_var.set("Lỗi: Chia cho 0")
        bieu_thuc = ""
    except Exception:
        man_hinh_var.set("Lỗi cú pháp")
        bieu_thuc = ""


# 3. Màn hình hiển thị (Entry)
man_hinh_var = tk.StringVar()
o_hien_thi = tk.Entry(
    cua_so,
    textvariable=man_hinh_var,
    font=("Arial", 20),
    bd=10,
    insertwidth=4,
    bg="powder blue",
    justify="right",
)
o_hien_thi.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# 4. Sắp xếp danh sách nút bấm (Nút, Hàng, Cột)
danh_sach_nut = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("C", 4, 2),
    ("+", 4, 3),
]

# Tạo các nút bấm 0-9 và +, -, *, /
for text, row, col in danh_sach_nut:
    if text == "C":
        nut = tk.Button(
            cua_so,
            text=text,
            padx=20,
            pady=15,
            font=("Arial", 12, "bold"),
            bg="#ff6666",
            command=xoa_man_hinh,
        )
    else:
        # Sử dụng lambda với tham số mặc định t=text để tránh đè giá trị
        nut = tk.Button(
            cua_so,
            text=text,
            padx=20,
            pady=15,
            font=("Arial", 12, "bold"),
            command=lambda t=text: bam_nut(t),
        )
    nut.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Nút bằng (=) nằm riêng ở hàng dưới cùng
nut_bang = tk.Button(
    cua_so,
    text="=",
    padx=20,
    pady=15,
    font=("Arial", 12, "bold"),
    bg="#66cc66",
    command=tinh_ket_qua,
)
nut_bang.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=5)

# Cấu hình các cột dãn đều nhau
for i in range(4):
    cua_so.grid_columnconfigure(i, weight=1)

# 5. Duy trì giao diện
if __name__ == "__main__":
    cua_so.mainloop()