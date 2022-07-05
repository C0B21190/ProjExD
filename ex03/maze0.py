import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn['text']
    tkm.showinfo(txt,f'[{txt}]ボタンが押されました')

def key_down(event):
    key = event.keysym
    tkm.showinfo('start')
    root.after(1000,count_up)

def count_up():
    global tmr, jid #jidリアルタイム処理の中断
    tmr = tmr+1
    label['text'] = tmr
    root.after(1000, count_up)
    # key = event.keysym
    # tkm.showinfo('キー押下', f'{key}キーが押されました')
    # root.after(1000, count_up)

# tori = tk.PhotoImage(file="fig/5.png")
# cx ,cy = 300, 400
# canvas.create_image(cx, cy, image=tori, tag='tori')

# button = tk.Button(root,
#         text='押すな',
#         command=button_click)
# button.bind('<1>', button_click)
# button.pack()

if __name__ == "__main__":
    root = tk.Tk('迷えるこうかとん')
    label = tk.Label(root,
            text='hi',
            font=("times New Roman", 89)
            )
    label.pack()
    tmr = 0 #初期値 グローバル変数
    #root.after(2000,count_up) #とりあえずこっち実行あと
    #count_up() #初期値
    root.bind('<KeyPress>',key_down)
    root.mainloop()

