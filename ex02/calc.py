from cmath import sqrt
from distutils.command.build import build
import tkinter as tk
import tkinter.messagebox as tkm
import math


def button_click(event):
    btn = event.widget
    num = btn['text']
    if num == '=':
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    elif num == 'C':
        entry.delete(0,tk.END)
    elif num == 'B':
        moji = len(entry.get())-1
        entry.delete(moji,tk.END)
    elif num == 'x^2':
        nijyo = entry.get()
        a = int(nijyo)*int(nijyo)
        entry.delete(0,tk.END)
        entry.insert(tk.END,a)
    
    elif num == 'sqrt':
        heiho = entry.get()
        a = math.sqrt(int(heiho))
        entry.delete(0,tk.END)
        entry.insert(tk.END,a)
    elif num == '+/-':
        gyaku = entry.get()
        a=int(gyaku)*-1
        entry.delete(0,tk.END)
        entry.insert(tk.END,a)
    elif num == '1/x':
        gyaku = entry.get()
        a=1/int(gyaku)
        entry.delete(0,tk.END)
        entry.insert(tk.END,a)
    elif num == '%':
        gyaku = entry.get()
        a=int(gyaku)/100
        entry.delete(0,tk.END)
        entry.insert(tk.END,a)
    elif num == 'x^3':
        sanjyo = entry.get()
        a = int(sanjyo)*int(sanjyo)*int(sanjyo)
        entry.delete(0,tk.END)
        entry.insert(tk.END,a)


    
    else:
        #tkm.showinfo('',f'{num}押しました') #警告メッセージ
        entry.insert(tk.END,num)



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('360x590') #設定しないと、自動的にサイズマッチ
    root.title('denntaku')

    entry = tk.Entry(root,width=12,justify='right',font=('Times New Roman',40))
    entry.grid(row=0,column=0,columnspan=5)
    

    r,c = 1,0
    #l=['9','8','7','6','5','4','3','2','1','0','+','=']
    for i,num in enumerate(['sqrt','x^2','B','C','1/x','x^3','%','/',7,8,9,'*',4,5,6,'-',1,2,3,"+",'+/-',0,'.','=']):
        btn = tk.Button(root,
                        text=f'{num}',
                        width=5,
                        height=2,
                        font=('Arial',20)
                        )
        btn.bind('<1>',button_click)
        btn.grid(row=r,column=c)
        c += 1
        #d=l[num]
        if (i+1)%4 == 0:
            r+=1
            c=0
        if num == '=':
            btn['bg']= '#ffd803'
        if num == '*':
            btn['bg']= '#bae8e8'
        if num == '-':
            btn['bg']= '#bae8e8'
        if num == '+':
            btn['bg']= '#bae8e8'
        if num == '/':
            btn['bg']= '#bae8e8'
        if num == 'C':
            btn['bg']= '#e3f6f5'
        if num == 'B':
            btn['bg']= '#e3f6f5'
        if num == '%':
            btn['bg']= '#e3f6f5'
        if num == 'x^2':
            btn['bg']= '#e3f6f5'
        if num == 'x^3':
            btn['bg']= '#e3f6f5'
        if num == 'sqrt':
            btn['bg']= '#e3f6f5'
        if num == '1/x':
            btn['bg']= '#e3f6f5'
        if num == '+/-':
            btn['bg']= '#e3f6f5'

            
    root.mainloop()

