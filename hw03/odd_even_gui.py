import tkinter as tk
from def_source import is_even


def encoding():
    try:
        num = int(ent_input.get())
        encoding = is_even(num)
        if num >= 0:
            if encoding == True:
                lbl_result["text"] = f"정수 {num}는 짝수입니다"
            else:
                lbl_result["text"] = f"정수 {num}는 홀수입니다"
        else:
            lbl_result["text"] = f"0보다 큰 정수를 입력하세요"
    except ValueError:
        lbl_result["text"] = f"정수를 입력해주세요"


window = tk.Tk()
window.title("홀짝")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_input = tk.Entry(master=frm_entry, width=20)
lbl_input = tk.Label(master=frm_entry, text="정수입력")

ent_input.grid(row=0, column=0, sticky="e")
lbl_input.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="SUBMIT", command=encoding)

lbl_result = tk.Label(master=window, text="")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
