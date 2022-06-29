from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Kantor")
root.geometry("900x600")

label = Label(root,text = "Kursy wymiany walut!", font = 20, fg = "black", bg = "#ecfc03", pady = 20)
label.pack(side = TOP)

label2 = Label(root, text = "Wpisz wartość (PLN)", font = 15, pady = 10)
label2.pack(side = TOP)

e = Entry(root, width = 20, font = 20, justify = LEFT)
e.pack(side = "top")

label3 = Label(root, text = "Zaznacz waluty", font = 15,padx = 10, pady = 10)
label3.pack(side = TOP)


w1,w2,w3,w4,w5,w6,w7,w8 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()


def checkinput(inputValue):
    try:
        if(float(inputValue)>0):
            return True
    except:
        return False 

def currency_rate():
    inputValue = e.get()
    if(checkinput(inputValue)):
        cantor=Tk()
        cantor.title('Wymiana walut')
        value = float(e.get())
        if(w1.get()==1):
            exchange = round(value *0.2326,2)
            label = Label(cantor,text="Dolar amerykański\nKurs: 4,30zł\nWartość wymiany: "+str(exchange)+" USD",bg="#833ab4",pady=40,padx=5)
            label.pack(anchor=W,side=LEFT,fill='both')
        if(w2.get()==1):
            exchange = round(value *0.1852,2)
            label = Label(cantor,text="Funt brytyjski\nKurs: 5,40zł\nWartość wymiany: " + str(exchange)+" GBP",bg="#be2e9b",pady=40,padx=5)
            label.pack(anchor=W,side=LEFT,fill='both')
        if(w3.get()==1):
            exchange = round(value *0.2174,2)
            label = Label(cantor,text="Euro\nKurs: 4,60zł\nWartość wymiany: "+str(exchange) +" EUR",bg="#c52a62",pady=40,padx=5)
            label.pack(anchor=W,side=LEFT,fill='both')
        if(w4.get()==1):
            exchange = round(value *0.2237,2)
            label = Label(cantor,text="Frank szwajcarski\nKurs: 4,47zł\nWartość wymiany: "+str(exchange) +" CHF",bg="#fd1d1d",pady=40,padx=5)
            label.pack(anchor=W,side=LEFT,fill='both')
        if(w5.get()==1):
            exchange = round(value *15.1515,2)
            label = Label(cantor,text="Rubel\nKurs: 0,066zł\nWartość wymiany: "+str(exchange) +" RUB",bg="#fd4327",pady=40,padx=5)
            label.pack(anchor=W,side=LEFT,fill='both')
        if(w6.get()==1):
            exchange = round(value *29.4118,2)
            label = Label(cantor,text="Jen japoński\nKurs: 0,034zł\nWartość wymiany: "+str(exchange) +" JPY",bg="#b36f51",pady=40,padx=5)
            label.pack(anchor=W,side=LEFT,fill='both')
        if(w7.get()==1):
            exchange = round(value *2.2727,2)
            label = Label(cantor,text="Korona Szwedzka\nKurs 0,44zł\nWartość wymiany: "+str(exchange) +" SEK",bg="#5da281",pady=40,padx=5)
            label.pack(anchor=W,side=LEFT,fill='both')
        if(w8.get()==1):
            exchange = round(value *0.2899,2)
            label = Label(cantor,text="Dolar kanadyjski\nKurs 3,45zł\nWartość wymiany: "+str(exchange) +" CAD",bg="#2ac19e",pady=40,padx=5)
            label.pack(anchor=W,side=LEFT,fill='both')
        if(w1.get()==0 and w2.get()==0 and w3.get()==0 and w4.get()==0 and w5.get()==0 and w6.get()==0 and w7.get()==0 and w8.get()==0):
            cantor.destroy()
            messagebox.showerror('Uwaga!','Waluta nie została wybrana')
    else:
        messagebox.showerror('Błąd!','Podana wartość jest błędna')


v1 = Checkbutton(root,text="Dolar amerykański",font=12,variable=w1, onvalue="1",offvalue="0",bg="#833ab4")
v1.pack(anchor=W,fill='x')
v2 = Checkbutton(root,text="Funt brytyjski",font=12,variable=w2,bg='#be2e9b')
v2.pack(anchor=W,fill='x')
v3 = Checkbutton(root,text="Euro",font=12,variable=w3,bg='#c52a62')
v3.pack(anchor=W,fill='x')
v4 = Checkbutton(root,text="Frank szwajcarski",font=12,variable=w4,bg="#fd1d1d")
v4.pack(anchor=W,fill='x')
v5 = Checkbutton(root,text="Rubel",font=12,variable=w5,bg="#fd4327")
v5.pack(anchor=W,fill='x')
v6 = Checkbutton(root,text="Jen japoński",font=12,variable=w6,bg="#b36f51")
v6.pack(anchor=W,fill='x')
v7 = Checkbutton(root,text="Korona szwedzka",font=12,variable=w7,bg='#5da281')
v7.pack(anchor=W,fill='x')
v8 = Checkbutton(root,text="Dolar kanadyjski",font=12,variable=w8,bg='#2ac19e')
v8.pack(anchor=W,fill='x')

btn = Button(root,text="Sprawdź",width=8,font=4,justify=LEFT,command=currency_rate)
btn.pack(side='top',pady=15)


root.mainloop()