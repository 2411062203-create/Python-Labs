import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget


class CuaSoDangNhap(QWidget):

    def __init__(self):
        super().__init__()
        # Nạp giao diện từ file .ui
        uic.loadUi("Lab10/form_dang_nhap.ui", self)

        # Kết nối sự kiện bấm nút Đăng nhập
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text().strip()
        mat_khau = self.o_nhap_mat_khau.text().strip()

        # Kiểm tra nếu chưa nhập đủ thông tin
        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(
                self, "Lỗi", "Vui lòng nhập đầy đủ tài khoản và mật khẩu."
            )
            return

        # Hiển thị thông báo thành công
        QMessageBox.information(
            self, "Thành công", f"Xin chào {tai_khoan}, đăng nhập thành công!"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())