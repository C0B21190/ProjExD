from cProfile import label
from http.client import TOO_MANY_REQUESTS
import tkinter as tk
import maze_maker as mm

# def count_up():
#     global tmr 
#     tmr = tmr+1
#     label['text'] = tmr 
#     root.after(1000,count_up)

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ''

def main_proc():
    global cx, cy, mx, my,is_g
    delta = {
        'Up': [0, -1],
        'Down': [0, +1],
        'Left': [-1, 0],
        'Right': [+1, 0],
    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my,mx = my+delta[key][1],mx+delta[key][0]
    except:
        pass

    cx ,cy = mx*70+35, my*70+35
    canvas.create_rectangle(cx+35,cy+35,cx-35,cy-35,fill='white')
    canvas.create_image(cx,cy,image=tori,tag='tori')
    canvas.coords('tori', cx, cy,)



    if cx==gcx and cy==gcy:
        is_g = True
        canvas.create_text(750,450,text='Congratulation!',font=('Arial',50))
    if not is_g:
        root.after(100, main_proc)


    

if __name__ == "__main__":
    root = tk.Tk('迷えるこうかとん')
    canvas = tk.Canvas(root,
            width=1500,
            height=900,
            bg='black' )
    canvas.pack()

    # label = tk.Label(root,font=("times New Roman", 89))
    # label.pack()
    # tmr = 0
    # root.after(1000,count_up)

    maze_bg = mm.make_maze(15, 9) 
    mm.show_maze(canvas, maze_bg)

    tori = tk.PhotoImage(file="ex03/fig/3.png")
    mx, my =1,1
    cx ,cy = mx*70+35, my*70+35



    canvas.create_rectangle(cx+35,cy+35,cx-35,cy-35,fill='white')
    #canvas.create_image(cx,cy,image=tori,tag='tori')

    g = tk.PhotoImage(file="ex03/fig/5.png")
    gmx,gmy=13,7
    gcx,gcy = gmx*70+35,gmy*70+35
    canvas.create_rectangle(gcx+35,gcy+35,gcx-35,gcy-35,fill='yellow')
    #canvas.create_image(gcx,gcy,image=g,tag='g')

    is_g = False






    canvas.create_image(cx, cy, image=tori, tag='tori')

    key = ''
    root.bind('<KeyPress>',key_down)
    root.bind('<KeyRelease>',key_up)

    # root.title(f'{tmr}')
    main_proc()
    root.mainloop()