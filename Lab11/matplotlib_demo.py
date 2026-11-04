import os
import matplotlib.pyplot as plt
import pandas as pd
duong_dan_csv = os.path.join(os.path.dirname(__file__), "diem_sinh_vien.csv")
df = pd.read_csv(duong_dan_csv)
#bai3.1
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
plt.figure(figsize=(6, 4))
plt.bar(diem_trung_binh_mon.index, diem_trung_binh_mon.values, color="skyblue")
plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")
plt.ylim(0, 10)
plt.savefig("bieu_do_cot.png")
plt.show()
#bai3.2
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]
plt.figure(figsize=(6, 4))
plt.plot(lan_kiem_tra, diem_qua_cac_lan, marker="o", color="green", label="Diem thuc te") 
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")
plt.ylim(0, 10)
plt.xticks(lan_kiem_tra, ["Lan 1", "Lan 2", "Lan 3"])
plt.savefig("bieu_do_duong.png")
plt.show()
