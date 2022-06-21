from distutils.command.build import build
import tkinter as tk
import tkinter.messagebox as tkm


# root = tk.Tk()
# #root.title("おためしか")
# root.geometry('300x500')

# # label = tk.Label(root,
# #                 text='ラベルです',
# #                 font=('Ricty Diminished',20)
# #                 )
# # label.pack()
# def button_click(event):
#     btn = event.widget
#     txt = btn['text']
#     tkm.showwarning('警告',f'[{txt}]押しました')

# button = tk.Button(root,text='押すな',command=button_click)


# button.bind('<1>',button_click)
# button.pack()

# root.mainloop()
def button_click(event):
    btn = event.widget
    num = btn['text']
    tkm.showinfo('',f'{num}押しました') 

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x500')
    root.title('denntaku')
    r,c = 0,0
    for num in range(9,-1,-1):
        btn = tk.Button(root,
                        text=f'{num}',
                        width=4,
                        height=2,
                        font=('Times New Roman',30)
                        )
        btn.bind('<1>',button_click)
        btn.grid(row=r,column=c)
        c += 1
        if (num-1)%3 == 0:
            r+=1
            c=0
        
        
    root.mainloop()

