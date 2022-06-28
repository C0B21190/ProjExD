import tkinter as tk

def key_down(event):
    global key
    key = event.keysym
    print(f'{key}woshita')

if __name__ == "__main__":
    root = tk.Tk('迷えるこうかとん')
    canvas = tk.Canvas(root,
            width=500,
            height=600,
            bg='black' )
    canvas.pack()
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    cx ,cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag='tori')

    key = ''
    root.bind('<KeyPress>',key_down)
    root.mainloop()