import tkinter as tk
from def_source import is_prime


def prime_sum(n):
    
    prime_list = [i for i in range(1, n+1) if is_prime(i)]

    return prime_list

def encoding():
    try:
        num = int(ent_input.get())
        encoding = prime_sum(num)
        encoding_str = ", ".join(map(str, encoding)) #괄호 없이 표현하기 위해서 문자열로 변경함
        lbl_result["text"] = f"0부터 {num}까지의 모든 소수들은 {encoding_str}입니다"
        
    except ValueError:
        lbl_result["text"] = f"정수를 입력해주세요"

    

window = tk.Tk()
window.title("소수들의 모음")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_input = tk.Entry(master=frm_entry, width=20)
lbl_input = tk.Label(master=frm_entry, text="정수입력")

ent_input.grid(row=0, column=0, sticky="e")
lbl_input.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
    master = window,
    text = "SUBMIT",
    command = encoding
)

lbl_result = tk.Label(master=window, text="")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()