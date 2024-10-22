import tkinter as tk
from def_source import is_even


def sum_even(n):
    num_list = [i for i in range(1, n + 1) if is_even(i)]
    return sum(num_list)


def encoding():
    try:
        num = int(ent_input.get())
        encoding = sum_even(num)
        if num > 0:
            lbl_result["text"] = f"1부터 {num}까지의 짝수의합은 {encoding}입니다"
        else:
            lbl_result["text"] = f"0보다 큰 정수를 입력하세요"

    except ValueError:
        lbl_result["text"] = f"정수를 입력해주세요"


window = tk.Tk()
window.title("짝수의 합")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_input = tk.Entry(master=frm_entry, width=20)
lbl_input = tk.Label(master=frm_entry, text="정수입력")

ent_input.grid(row=0, column=0, sticky="e")
lbl_input.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="SUBMIT", command=encoding)

lbl_result = tk.Label(master=window, text="총합")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
