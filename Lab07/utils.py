# ====================================================
# BƯỚC 2: CẤU TRÚC DỮ LIỆU LƯU TRỮ
# ====================================================

# Danh sách liên hệ (list các dict)
danh_sach_danh_ba = [
    {
        "sdt": "0987654321",
        "ho_ten": "Nguyen Van A",
        "email": "a.nguyen@gmail.com",
        "nhom": "Cong viec",
    },
    {
        "sdt": "0912345678",
        "ho_ten": "Tran Thi B",
        "email": "b.tran@gmail.com",
        "nhom": "Gia dinh",
    },
    {
        "sdt": "0933445566",
        "ho_ten": "Le Van C",
        "email": "c.le@gmail.com",
        "nhom": "Ban be",
    },
]


# ====================================================
# BƯỚC 3: CÁC HÀM XỬ LÝ CHỨC NĂNG
# ====================================================


def nhap_sdt_an_toan(thong_bao):
    """Hàm hỗ trợ nhập số điện thoại an toàn bằng try-except / kiểm tra chữ số."""
    while True:
        sdt = input(thong_bao).strip()
        if sdt.isdigit() and len(sdt) >= 9:
            return sdt
        print(
            "[!] Lỗi: Số điện thoại phải chỉ chứa các chữ số và có ít nhất 9-10 chữ số. Thử lại!"
        )


# 1. Hiển thị danh sách toàn bộ danh bạ
def hien_thi_tat_ca_lien_he():
    if not danh_sach_danh_ba:
        print("\n[!] Danh bạ hiện tại đang trống.")
        return

    print("\n" + "=" * 70)
    print(
        f"{'Số điện thoại':<15} | {'Họ và Tên':<20} | {'Email':<20} | {'Nhóm':<10}"
    )
    print("-" * 70)
    for lh in danh_sach_danh_ba:
        print(
            f"{lh['sdt']:<15} | {lh['ho_ten']:<20} | {lh['email']:<20} | {lh['nhom']:<10}"
        )
    print("=" * 70)


# 2. Xem nhanh các liên hệ theo nhóm
def xem_theo_nhom(nhom_can_xem):
    lh_nhom = [
        lh
        for lh in danh_sach_danh_ba
        if lh["nhom"].lower() == nhom_can_xem.lower()
    ]
    if not lh_nhom:
        print(f"\n[!] Không tìm thấy liên hệ nào thuộc nhóm '{nhom_can_xem}'.")
        return

    print(f"\n--- DANH SÁCH LIÊN HỆ NHÓM {nhom_can_xem.upper()} ---")
    print(f"{'Số điện thoại':<15} | {'Họ và Tên':<20} | {'Email':<20}")
    print("-" * 60)
    for lh in lh_nhom:
        print(f"{lh['sdt']:<15} | {lh['ho_ten']:<20} | {lh['email']:<20}")


# 3. Thêm liên hệ mới
def them_lien_he_moi(sdt, ho_ten, email, nhom):
    for lh in danh_sach_danh_ba:
        if lh["sdt"] == sdt:
            return False, f"Số điện thoại '{sdt}' đã tồn tại trong danh bạ!"

    lien_he_moi = {
        "sdt": sdt,
        "ho_ten": ho_ten,
        "email": email,
        "nhom": nhom,
    }
    danh_sach_danh_ba.append(lien_he_moi)
    return True, "Thêm liên hệ mới thành công!"


# 4. Tìm kiếm liên hệ (theo tên hoặc SĐT)
def tim_kiem_lien_he(tu_khoa):
    tu_khoa_lower = tu_khoa.lower()
    ket_qua = [
        lh
        for lh in danh_sach_danh_ba
        if tu_khoa_lower in lh["sdt"] or tu_khoa_lower in lh["ho_ten"].lower()
    ]

    if not ket_qua:
        print(f"\n[!] Không tìm thấy liên hệ nào phù hợp với từ khóa '{tu_khoa}'.")
        return

    print(f"\n--- KẾT QUẢ TÌM KIẾM CHO '{tu_khoa}' ---")
    print(
        f"{'Số điện thoại':<15} | {'Họ và Tên':<20} | {'Email':<20} | {'Nhóm':<10}"
    )
    print("-" * 70)
    for lh in ket_qua:
        print(
            f"{lh['sdt']:<15} | {lh['ho_ten']:<20} | {lh['email']:<20} | {lh['nhom']:<10}"
        )


# 5. Xóa liên hệ
def xoa_lien_he(sdt):
    for lh in danh_sach_danh_ba:
        if lh["sdt"] == sdt:
            danh_sach_danh_ba.remove(lh)
            return True, f"Đã xóa liên hệ có SĐT '{sdt}' thành công!"
    return False, f"Không tìm thấy liên hệ có SĐT '{sdt}'!"


# 6. Thống kê tổng số lượng liên hệ theo từng nhóm
def thong_ke_danh_ba():
    if not danh_sach_danh_ba:
        print("\n[!] Danh bạ trống.")
        return

    thong_ke = {}
    for lh in danh_sach_danh_ba:
        nhom = lh["nhom"]
        thong_ke[nhom] = thong_ke.get(nhom, 0) + 1

    print("\n" + "=" * 50)
    print("--- THỐNG KÊ SỐ LƯỢNG LIÊN HỆ THEO NHÓM ---")
    for nhom, so_luong in thong_ke.items():
        print(f"- Nhóm {nhom:<15}: {so_luong} liên hệ")
    print("-" * 50)
    print(f"==> TỔNG CỘNG: {len(danh_sach_danh_ba)} liên hệ trong danh bạ.")
    print("=" * 50)