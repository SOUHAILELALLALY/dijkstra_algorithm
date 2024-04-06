from tkinter import *
from Dijkstra import *

fn=Tk()


fn.title("App")
fn.geometry("1200x600")
fn.minsize(600 ,300)
fn.config(background="white")
window1=Frame(fn,bg="white")
window2=Frame(fn,bg="white")

def calcul(t,d,s,fin):
    for widget in window2.winfo_children():
        widget.grid_forget()

    v=[]
    e={}
    for i in range(0,len(t)):
        v.append(str(t[i].get()))
    for i,j in d.items():
        l=[]
        for k in range(0,len(j)):
            l.append((int(j[k].get())))
        e[i]=l
    e2 = {}
    for i in range(0, len(v)):
        t1 = e[v[i]]
        t2 = []
        for j in range(0, len(v)):
            if t1[j] != 0:
                t2.append((v[j], t1[j]))
        e2[v[i]] = t2

    res = graf(s.get(), v, e2, fin.get())
    Label(window2, text=res, bg="#FFFFFF", fg="black", font=("Arial", 15)).grid(row=0, column=0,padx=10, pady=5)
    window2.pack()

def veri_point(t,d,s,fin):
    t1=[]
    for i in range(0,len(t)):
        t1.append(t[i].get())
    if s.get() in t1 and fin.get() in t1:
        calcul(t, d, s, fin)
    else:
        Label(window1, text=f"*verifier les points que vous avez entrer", bg="#FFFFFF", fg="red", font=("Arial", 10)).grid(row=4, column=2,padx=10,pady=5)

def point_chercher(t, d):
    for widget in window1.winfo_children():
        #widget.destroy()
        widget.grid_forget()

    Label(window1, text=f"entrer le point de départ:", bg="#FFFFFF", fg="black", font=("Arial", 15)).grid(row=4 , column=0,padx=10, pady=5)
    s = StringVar()
    Entry(window1, textvariable=s, bg="#FAF9F6", fg="black", font=("Arial", 15), width=3).grid(row=4 ,column=1, padx=10, pady=5)
    Label(window1, text=f"entrer le point d'arrivée", bg="#FFFFFF", fg="black", font=("Arial", 15)).grid(row=5 , column=0,padx=40, pady=5)
    fin= StringVar()
    Entry(window1, textvariable=fin, bg="#FAF9F6", fg="black", font=("Arial", 15), width=3).grid(row=5,column=1, pady=5)
    Button(window1, text="OK", bg="#D3D3D3", font=("Arial", 15), command=lambda: veri_point(t, d,s,fin)).grid(row=6, column=0, padx=15, pady=5)


def verifier1(e,t,t1,lb):
    a=len(e)-1
    c=0
    i=len(t)
    for j in range(0,len((t1))):
        if t1[j].get()=='':
            c=c+1
    if c==0:
        ligne_suivant(e,t,lb)
    else:
        Label(window1, text=f"entrer les deux champs", bg="#FFFFFF", fg="red", font=("Arial", 10)).grid(row=5 + a,column=4 + j,padx=15, pady=5)


def ligne_suivant(e,t,lb):
    if len(e)==0:
        for widget in window1.winfo_children():
            # widget.destroy()
            widget.grid_forget()
        e={}
        for i in range(0, len(t)):
            Label(window1, text=t[i].get(), bg="#D3D3D3", fg="black", font=("Arial", 15), width=3).grid(row=4,column=1 + i, padx=15, pady=5)
    a = len(e)
    if a!=0:
        lb.destroy()
    Label(window1, text=t[a].get(), bg="#D3D3D3", fg="black", font=("Arial", 15), width=3).grid(row=5 + a, column=0,padx=15, pady=5)
    t3=[]
    t4=[]
    for i in range(0,len(e)):
        h=e[t[i].get()]
        for j in range(0,len(t)):
            if j==a:
                t3.append(i)
                t4.append(h[j].get())
    t3.append(a)
    t4.append(0)
    t1 = []
    for j in range(0, len(t)):
        var2 = StringVar()
        if j in t3:
            id=t3.index(j)
            if j==a:
                t1.append(StringVar(window1, '0'))
            else:
                t1.append(StringVar(window1,t4[id]))
            Label(window1,text=f"{t4[id]}", bg="#FAF9F6", fg="black", font=("Arial", 15), width=3).grid(row=5 + a,column=1 + j,padx=10, pady=5)

        else:
            Entry(window1, textvariable=var2, bg="#FAF9F6", fg="black", font=("Arial", 15), width=3).grid(row=5 + a,column=1 + j,padx=10,pady=5)
            t1.append(var2)
    e[t[a].get()] = t1
    if a < len(t) - 1:
        lb=Button(window1, text="next", bg="#D3D3D3", font=("Arial", 15), command=lambda: verifier1(e,t,t1,lb))
        lb.grid(row=5 + a, column=2 + j, padx=15, pady=5)
    else:
        Button(window1, text="ok", bg="#D3D3D3", font=("Arial", 15), command=lambda: point_chercher(t, e)).grid(row=7 + len(t), column=0, padx=15, pady=5)



def verifier(t):
    c=0
    for j in range(0,len(t)):
        if len(t[j].get()) == 0:
            c=c+1
            Label(window1, text=f"entrer les deux champs ", bg="#FFFFFF", fg="red", font=("Arial", 10)).grid(row=2 +j,column=4, padx=10,pady=5)
    if c==0:
        e={}
        ligne_suivant(e,t,2)



def next():
    a=int(var1.get())
    t=[]
    for i in range(0,a):
        Label(window1, text=f"entrer nom de sommet{i+1}:", bg="#FFFFFF", fg="black", font=("Arial", 15)).grid(row=2+i, column=0, padx=10, pady=5)
        var2 = StringVar()
        Entry(window1, textvariable=var2, bg="#FAF9F6", fg="black", font=("Arial", 15), width=3).grid(row=2+i,column=1,padx=10,pady=5)
        t.append(var2)
    Button(window1, text="suivant", bg="#D3D3D3", font=("Arial", 15), command=lambda :verifier(t)).grid(row=2+a, column=0, padx=15,pady=5)



Label(window1,text="entrer nb des sommet:",bg="#FFFFFF",fg="black",font=("Arial",15)).grid(row=0,column=0,padx=10,pady=5)
var1=StringVar()
in1=Entry(window1,textvariable=var1,bg="#FAF9F6",fg="black",font=("Arial",15),width=5).grid(row=0,column=1,padx=10,pady=5)
bt1=Button(window1,text="next",bg="#D3D3D3",font=("Arial",15),command=next).grid(row=1,column=0,padx=15,pady=5)



window1.pack()
fn.mainloop()