import tkinter as tk

def f2c(temp: float) -> float:
    return (temp - 32) * 5 / 9 
def c2f(temp: float) -> float:
    return (temp + 32) * 9 / 5

def f2c_encoding():
    try:
        temp = int(ent_input.get())
        encoding = f2c(temp)
        lbl_result["text"] = f"섭씨: {encoding:.1f}℃"
    except ValueError:
        lbl_result["text"] = f"정수를 입력하세요"
    

def c2f_encoding():
    try:
        temp = int(ent_input.get())
        encoding = c2f(temp)
        lbl_result["text"] = f"화씨: {encoding:.1f}℉"
    except ValueError:
        lbl_result["text"] = f"정수를 입력하세요"

window = tk.Tk()
window.title("온도단위 변환")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_input = tk.Entry(master=frm_entry, width=20)
lbl_input = tk.Label(master=frm_entry, text="입력온도")

ent_input.grid(row=0, column=0, sticky="e")
lbl_input.grid(row=0, column=1, sticky="w")


btn_convert = tk.Button(
    master=window,
    text="F2C",
    command=f2c_encoding
)

btn_convert_2 = tk.Button(
    master=window,
    text="C2F",
    command=c2f_encoding
)


lbl_result = tk.Label(master=window, text="전환온도")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
btn_convert_2.grid(row=0, column=2, pady=10)
lbl_result.grid(row=0, column=3, padx=10)


window.mainloop()