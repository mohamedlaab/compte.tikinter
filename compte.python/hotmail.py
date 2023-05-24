import tkinter as tk
from tkinter import messagebox

# إنشاء نافذة الواجهة الرئيسية
root = tk.Tk()

# تعيين عنوان النافذة والألوان
root.title("الحساب البنكي")
root.configure(bg="#f5f5f5")

# إضافة عنوان كبير في الأعلى
title_label = tk.Label(root, text="الحساب البنكي", font=("Helvetica", 24), bg="#f5f5f5")
title_label.pack(pady=20)

# إنشاء Label لعرض النص
text = tk.Label(root, text="Merci de saisir le code", font=("Helvetica", 14), bg="#f5f5f5")

# تخصيص الخط والحجم لعلبة النص
entry_font = ("Helvetica", 16)

# إنشاء Entry لإدخال الرمز
entry = tk.Entry(root, font=entry_font, show="*")

# إنشاء زر "تشغيل"
button = tk.Button(root, text="تشغيل", font=("Helvetica", 14), bg="#008CBA", fg="white",
                   activebackground="#005c8f", activeforeground="white",
                   command=lambda: check_code(entry.get()))

# وضع العناصر في الشاشة
text.pack()
entry.pack(ipady=10, padx=20, pady=10)
button.pack(ipadx=10, ipady=5, pady=20)

# إنشاء النافذة الثانوية
def create_second_window():
    second_window = tk.Toplevel(root)

    # تعيين عنوان النافذة والألوان
    second_window.title("سحب المال")
    second_window.configure(bg="#f5f5f5")

    # إنشاء Label لعرض المبلغ المتحصل عليه في الحساب
    account_balance = 5000 # تم تخيل قيمة الرصيد هنا
    balance_label = tk.Label(second_window, text=f"الرصيد الحالي: {account_balance} دولار", font=("Helvetica", 16), bg="#f5f5f5")
    balance_label.pack(pady=20)

    amounts_frame = tk.LabelFrame(second_window, text="المبالغ المتاحة", padx=50, pady=50, bd=2, relief="solid")
    amounts_frame.pack(pady=30)
    # إنشاء مجموعة من المبالغ المالية المتاحة للسحب
    amounts = ["50 دولار", "100 دولار", "200 دولار", "500 دولار", "1000 دولار"]

    # إنشاء متغير لتخزين المبلغ المحدد
    selected_amount = tk.StringVar()

    # إنشاء GroupBox لعرض المبالغ المالية المتاحة للسحب
    groupbox = tk.LabelFrame(second_window, text="المبالغ المتاحة", padx=100, pady=100)

    # إنشاء Radiobuttons لكل مبلغ مالي
    for amount in amounts:
        amount_button = tk.Radiobutton(groupbox, text=amount, variable=selected_amount, value=amount, padx=20, pady=10,
                                       indicatoron=False, font=("Arial", 12), bg="#ffffff", fg="#000000")
        amount_button.pack(anchor="w")
        

    # إنشاء زر "سحب" لسحب المال
    withdraw_button = tk.Button(second_window, text="سحب", bg="#007aff", fg="#ffffff", font=("Helvetica", 16), pady=10, command=lambda: withdraw_money(selected_amount.get()))

    # وضع العناصر في الشاشة
    groupbox.pack(fill="both", expand="yes")
    withdraw_button.pack(pady=20)

    # رفع النافذة الثانوية فوق النافذة

    # رفع النافذة الثانوية فوق النافذة الرئيسية
    second_window.lift()

# التحقق من الرمز المدخل
def check_code(code):
    # فحص صحة الرمز
    if code == "1234":
        # عرض النافذة الثانوية إذا كان الرمز صحيحًا
        create_second_window()
    else:
        # عرض رسالة تنبيه إذا كان الرمز خاطئًا
        messagebox.showwarning("رمز خاطئ", "الرجاء إدخال الرمز الصحيح")

# تشغيل الواجهة الرئيسية
root.mainloop()
class Compte:
    def init(self, nom, prenom, code, solde):
        self.nom = nom
        self.prenom = prenom
        self.code = code
        self.solde=solde
        # إنشاء الحسابات


# فتح الملف للكتابة
f = open("compte.txt", "w")

# كتابة معلومات الحسابات في الملف
f.write(f"{compte1.nom},{compte1.prenom},{compte1.code},{compte1.solde}\n")
f.write(f"{compte2.nom},{compte2.prenom},{compte2.code},{compte2.solde}\n")

# إغلاق الملف
f.close