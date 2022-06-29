import tkinter as tk


class Test(tk.Tk):

    ile = 0

    def __init__(self):
        super().__init__()
        self.title("TEST z informatyki!")
        self.geometry("500x200")
        self.pytanie_1()

    def run(self):
        self.mainloop()

    def pytanie_1(self):
        self.r = 1
        self.typ_1 = tk.StringVar()
        self.typ_2 = tk.StringVar()
        self.typ_3 = tk.StringVar()
        self.typ_1.set(0)
        self.typ_2.set(0)
        self.typ_3.set(0)

        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 1: Oznaczenie typu całkowitego to: ")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "int", variable = self.typ_1, onvalue = 1)
        self.b1.grid(row = 1, column = 0)
        self.b2 = tk.Checkbutton(self.frame, text = "string", variable = self.typ_2, onvalue = 2)
        self.b2.grid(row = 2, column = 0)
        self.b3 = tk.Checkbutton(self.frame, text = "float", variable = self.typ_3, onvalue = 3)
        self.b3.grid(row = 3, column = 0)

        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)

    def pytanie_2(self):
        self.r = 2
        self.typ_4 = tk.StringVar()
        self.typ_5 = tk.StringVar()
        self.typ_6 = tk.StringVar()
        self.typ_4.set(0)
        self.typ_5.set(0)
        self.typ_6.set(0)
        
        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 2: W którym języku programowania można wykorzystywać krotkę: ")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "C#", variable = self.typ_4, onvalue = 1).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "JavaScript", variable = self.typ_5, onvalue = 2).grid(row = 2, column = 0, sticky = "W")
        self.b3 = tk.Checkbutton(self.frame, text = "Python", variable = self.typ_6, onvalue = 3).grid(row = 3, column = 0, sticky = "W")
        
        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)
        
    def pytanie_3(self):
        self.r = 3
        self.typ_7 = tk.StringVar()
        self.typ_8 = tk.StringVar()
        self.typ_9= tk.StringVar()
        self.typ_7.set(0)
        self.typ_8.set(0)
        self.typ_9.set(0)
        
        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 3: Jakie komendy można spotkać w pythonie? ")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "static", variable = self.typ_7, onvalue = 1).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "self", variable = self.typ_8, onvalue = 2).grid(row = 2, column = 0, sticky = "W")
        self.b3 = tk.Checkbutton(self.frame, text = "def", variable = self.typ_9, onvalue = 3).grid(row = 3, column = 0, sticky = "W")
        
        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)
    
    def pytanie_4(self):
        self.r = 4
        self.typ_10 = tk.StringVar()
        self.typ_11 = tk.StringVar()
        self.typ_12 = tk.StringVar()
        self.typ_10.set(0)
        self.typ_11.set(0)
        self.typ_12.set(0)
        
        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 4: Do czego służy funkcja print w pythonie? ")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "Do wyświetlania", variable = self.typ_10, onvalue = 1).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "Do przypisywania wartości", variable = self.typ_11, onvalue = 2).grid(row = 2, column = 0, sticky = "W")
        self.b3 = tk.Checkbutton(self.frame, text = "Do zapisywania w pliku", variable = self.typ_12, onvalue = 3).grid(row = 3, column = 0, sticky = "W")
        
        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)

    def pytanie_5(self):
        self.r = 5
        self.typ_13 = tk.StringVar()
        self.typ_14 = tk.StringVar()
        self.typ_13.set(0)
        self.typ_14.set(0)
  

        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 5: Czy krotka jest strukturą mutowalną?")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "Tak", variable = self.typ_13, onvalue = 1).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "Nie", variable = self.typ_14, onvalue = 2).grid(row = 2, column = 0, sticky = "W")

        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)

    def pytanie_6(self):
        self.r = 6
        self.typ_15 = tk.StringVar()
        self.typ_16 = tk.StringVar()
        self.typ_17 = tk.StringVar()
        self.typ_15.set(0)
        self.typ_16.set(0)
        self.typ_17.set(0)

        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 6: Za pomocą jakiej komendy deklaruje się konstruktor w klasach?")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "__str__", variable = self.typ_15, onvalue = 1).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "__init__", variable = self.typ_16, onvalue = 2).grid(row = 2, column = 0, sticky = "W")
        self.b3 = tk.Checkbutton(self.frame, text = "__main__", variable = self.typ_17, onvalue = 3).grid(row = 3, column = 0, sticky = "W")

        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)

    def pytanie_7(self):
        self.r = 7
        self.typ_18 = tk.StringVar()
        self.typ_19 = tk.StringVar()
        self.typ_20 = tk.StringVar()
        self.typ_18.set(0)
        self.typ_19.set(0)
        self.typ_20.set(0)

        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 7: Która instrukcja nie istnieje w pythonie?")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "switch", variable = self.typ_18, onvalue = 1,).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "do while", variable = self.typ_19, onvalue = 2).grid(row = 2, column = 0, sticky = "W")
        self.b3 = tk.Checkbutton(self.frame, text = "for", variable = self.typ_20, onvalue = 3).grid(row = 3, column = 0, sticky = "W")

        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)
        

    def pytanie_8(self):
        self.r = 8
        self.typ_21 = tk.StringVar()
        self.typ_22 = tk.StringVar()
        self.typ_23 = tk.StringVar()
        self.typ_21.set(0)
        self.typ_22.set(0)
        self.typ_23.set(0)

        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 8: Która metoda służy od zaimplementowania dziedziczonej metody? ")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "main()", variable = self.typ_21, onvalue = 1).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "super()", variable = self.typ_22, onvalue = 2).grid(row = 2, column = 0, sticky = "W")
        self.b3 = tk.Checkbutton(self.frame, text = "object()", variable = self.typ_23, onvalue = 3).grid(row = 3, column = 0, sticky = "W")

        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)

    def pytanie_9(self):
        self.r = 9
        self.typ_24 = tk.StringVar()
        self.typ_25 = tk.StringVar()
        self.typ_26 = tk.StringVar()
        self.typ_24.set(0)
        self.typ_25.set(0)
        self.typ_26.set(0)

        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 9: Wskaż zdanie/a prawdziwe: ")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "Python nie jest językiem obiektowym", variable = self.typ_24, onvalue = 1).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "Przy deklaracji nowej zmiennej możemy nie przypisywać typu, lecz tylko samą wartość", variable = self.typ_25, onvalue = 2).grid(row = 2, column = 0, sticky = "W")
        self.b3 = tk.Checkbutton(self.frame, text = "Wcięcia są kluczowe w pisaniu skryptu", variable = self.typ_26, onvalue = 3).grid(row = 3, column = 0, sticky = "W")

        self.akceptuj = tk.Button(self, text = "Następne pytanie", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)

    def pytanie_10(self):
        self.r = 10
        self.typ_27 = tk.StringVar()
        self.typ_28 = tk.StringVar()
        self.typ_29 = tk.StringVar()
        self.typ_27.set(0)
        self.typ_28.set(0)
        self.typ_29.set(0)

        self.frame = tk.Frame(self)
        self.frame.grid(row = 2, column = 0)

        self.myLabel = tk.Label(self, text = "Pytanie 10: Moduł służący do budowania okien graficznych to: ")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")

        self.b1 = tk.Checkbutton(self.frame, text = "Tuple", variable = self.typ_27, onvalue = 1).grid(row = 1, column = 0, sticky = "W")
        self.b2 = tk.Checkbutton(self.frame, text = "Tkinter", variable = self.typ_28, onvalue = 2).grid(row = 2, column = 0, sticky = "W")
        self.b3 = tk.Checkbutton(self.frame, text = "Math", variable = self.typ_29, onvalue = 3).grid(row = 3, column = 0, sticky = "W")

        self.akceptuj = tk.Button(self, text = "Zakończ test", command = self.usun_buttony)
        self.akceptuj.grid(row = 6, column = 0)

    def wybor_1(self):
        self.wyborx1= self.typ_1.get()
        self.wyborx2 = self.typ_2.get()
        self.wyborx3 = self.typ_3.get()
        if int(self.wyborx1) == 1 and int(self.wyborx2) == 0 and int(self.wyborx3) == 0:
            self.ile += 1
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)

    def wybor_2(self):
        self.wyborx1 = int(self.typ_4.get())
        self.wyborx2 = int(self.typ_5.get())
        self.wyborx3 = int(self.typ_6.get())
        if self.wyborx1 == 0 and self.wyborx2 == 0 and self.wyborx3 == 3:
            self.ile += 1
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)

    def wybor_3(self):
        self.wyborx1 = int(self.typ_7.get())
        self.wyborx2 = int(self.typ_8.get())
        self.wyborx3 = int(self.typ_9.get())
        if self.wyborx1 == 0 and self.wyborx2 == 2 and self.wyborx3 == 3:
            self.ile += 1
        elif (self.wyborx1 == 0 and self.wyborx2 == 2 and self.wyborx3 == 0) or (self.wyborx1 == 0 and self.wyborx2 == 0 and self.wyborx3 == 3):
            self.ile += 0.5
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)

    def wybor_4(self):
        self.wyborx1 = int(self.typ_10.get())
        self.wyborx2 = int(self.typ_11.get())
        self.wyborx3 = int(self.typ_12.get())
        if self.wyborx1 == 1 and self.wyborx2 == 0 and self.wyborx3 == 0:
            self.ile += 1
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)

    def wybor_5(self):
        self.wyborx1 = int(self.typ_13.get())
        self.wyborx2 = int(self.typ_14.get())
        if self.wyborx1 == 0 and self.wyborx2 == 2:
            self.ile += 1
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)

    def wybor_6(self):
        self.wyborx1 = int(self.typ_15.get())
        self.wyborx2 = int(self.typ_16.get())
        self.wyborx3 = int(self.typ_17.get())
        if self.wyborx1 == 0 and self.wyborx2 == 2 and self.wyborx3 == 0:
            self.ile += 1
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)

    def wybor_7(self):
        self.wyborx1 = int(self.typ_18.get())
        self.wyborx2 = int(self.typ_19.get())
        self.wyborx3 = int(self.typ_20.get())
        if self.wyborx1 == 1 and self.wyborx2 == 2 and self.wyborx3 == 0:
            self.ile += 1
        elif (self.wyborx1 == 1 and self.wyborx2 == 0 and self.wyborx3 == 0) or (self.wyborx1 == 0 and self.wyborx2 == 2 and self.wyborx3 == 0):
            self.ile += 0.5
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)

    def wybor_8(self):
        self.wyborx1 = int(self.typ_21.get())
        self.wyborx2 = int(self.typ_22.get())
        self.wyborx3 = int(self.typ_23.get())
        if self.wyborx1 == 0 and self.wyborx2 == 2 and self.wyborx3 == 0:
            self.ile += 1
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)

    def wybor_9(self):
        self.wyborx1 = int(self.typ_24.get())
        self.wyborx2 = int(self.typ_25.get())
        self.wyborx3 = int(self.typ_26.get())
        if self.wyborx1 == 0 and self.wyborx2 == 2 and self.wyborx3 == 3:
            self.ile += 1
        elif (self.wyborx1 == 0 and self.wyborx2 == 2 and self.wyborx3 == 0) or (self.wyborx1 == 0 and self.wyborx2 == 0 and self.wyborx3 == 3):
            self.ile += 0.5
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)


    def wybor_10(self):
        self.wyborx1 = int(self.typ_27.get())
        self.wyborx2 = int(self.typ_28.get())
        self.wyborx3 = int(self.typ_29.get())
        if self.wyborx1 == 0 and self.wyborx2 == 2 and self.wyborx3 == 0:
            self.ile += 1
        ##print("Punkty: ",self.ile)
        ##print(self.wyborx1)
        ##print(self.wyborx2)
        ##print(self.wyborx3)


    def usun_buttony(self):
        self.myLabel.grid_forget()
        self.frame.grid_remove()
        self.akceptuj.destroy()
        if self.r == 1:
            self.wybor_1()
            self.pytanie_2()
        elif self.r == 2:
            self.wybor_2()
            self.pytanie_3()
        elif self.r == 3:
            self.wybor_3()
            self.pytanie_4()
        elif self.r == 4:
            self.wybor_4()
            self.pytanie_5()
        elif self.r == 5:
            self.wybor_5()
            self.pytanie_6()
        elif self.r == 6:
            self.wybor_6()
            self.pytanie_7()
        elif self.r == 7:
            self.wybor_7()
            self.pytanie_8()
        elif self.r == 8:
            self.wybor_8()
            self.pytanie_9()
        elif self.r == 9:
            self.wybor_9()
            self.pytanie_10()
        elif self.r == 10:
            self.wybor_10()
            self.wynik()
    
    def wynik(self):
        self.myLabel.grid_forget()
        self.frame.grid_remove()
        self.akceptuj.destroy()

        self.myLabel = tk.Label(self, text = "Twój wynik to: ")
        self.myLabel.grid(row = 0, column= 0, sticky = "W")
        self.myLabel2 = tk.Label(self,text = self.ile)
        self.myLabel2.grid(row = 0, column = 1, sticky = "W")
        self.myLabel4 = tk.Label(self, text = "/10")
        self.myLabel4.grid(row = 0, column = 2, sticky = "W")
        self.ocena()

    def ocena(self):
        if self.ile < 5:
            self.myLabel3 = tk.Label(self,text = "Ocena niedostateczna")
            self.myLabel3.grid(row = 1,column = 0,sticky = "W")
        elif self.ile < 6:
            self.myLabel3 = tk.Label(self,text = "Ocena dopuszczająca")
            self.myLabel3.grid(row = 1,column = 0,sticky = "W")
        elif self.ile < 8:
            self.myLabel3 = tk.Label(self,text = "Ocena dostateczna")
            self.myLabel3.grid(row = 1,column = 0,sticky = "W")
        elif self.ile < 9:
            self.myLabel3 = tk.Label(self,text = "Ocena dobra")
            self.myLabel3.grid(row = 1,column = 0,sticky = "W")
        else:
            self.myLabel3 = tk.Label(self,text = "Ocena bardzo dobra")
            self.myLabel3.grid(row = 1,column = 0,sticky = "W")



t1 = Test()
t1.run()
