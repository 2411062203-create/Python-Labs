import utils


def hien_thi_menu():
    print("\n========== QUẢN LÝ DANH BẠ ĐIỆN THOẠI ==========")
    print("1. Hiển thị danh sách toàn bộ danh bạ")
    print("2. Xem danh sách liên hệ theo nhóm")
    print("3. Thêm liên hệ mới")
    print("4. Tìm kiếm liên hệ (theo Tên hoặc SĐT)")
    print("5. Xóa liên hệ")
    print("6. Thống kê số lượng liên hệ")
    print("0. Thoát chương trình")
    print("================================================")


def main():
    while True:
        hien_thi_menu()
        chon = input("Nhập lựa chọn của bạn (0-6): ").strip()

        if chon == "1":
            utils.hien_thi_tat_ca_lien_he()

        elif chon == "2":
            nhom = (
                input(
                    "Nhập tên nhóm cần xem (Gia dinh / Cong viec / Ban be): "
                )
                .strip()
                .title()
            )
            utils.xem_theo_nhom(nhom)

        elif chon == "3":
            sdt = utils.nhap_sdt_an_toan("Nhập số điện thoại: ")
            ho_ten = input("Nhập Họ và Tên: ").strip().title()
            email = input("Nhập Email: ").strip()
            nhom = (
                input(
                    "Nhập Nhóm (Gia dinh / Cong viec / Ban be / Khac): "
                )
                .strip()
                .title()
            )

            success, msg = utils.them_lien_he_moi(sdt, ho_ten, email, nhom)
            print(f"\n[{'+' if success else '!'}] {msg}")

        elif chon == "4":
            tu_khoa = input("Nhập Tên hoặc SĐT cần tìm: ").strip()
            utils.tim_kiem_lien_he(tu_khoa)

        elif chon == "5":
            sdt = input("Nhập SĐT cần xóa: ").strip()
            success, msg = utils.xoa_lien_he(sdt)
            print(f"\n[{'+' if success else '!'}] {msg}")

        elif chon == "6":
            utils.thong_ke_danh_ba()

        elif chon == "0":
            print("\nCảm ơn bạn đã sử dụng phần mềm Quản lý danh bạ!")
            break

        else:
            print("\n[!] Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 6.")


if __name__ == "__main__":
    main()