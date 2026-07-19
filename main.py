from tkinter import*
from tkinter import messagebox
import os

class my_class:
    def __init__(self):
        self.root=Tk()
        self.root.resizable(False,False)
        self.root.geometry("830x600+400+100")
        self.root.config(bg="#36013f")
        self.img1=PhotoImage(file="11.png")#tittle
        self.txt1=Label(self.root,image=self.img1,borderwidth=0)
        self.txt1.pack()
        self.txt1.place(x=12,y=5)
        
        self.img2=PhotoImage(file="66.png")#attention
        self.txt2=Label(self.root,image=self.img2,borderwidth=0)
        self.txt2.pack()
        self.txt2.place(x=245,y=100)

        self.b1 = Button(self.root, text="ساخت فرم جديد", font=("B Nazanin", 10 ,"bold"),fg="#4B0082",
                         activebackground="#ffffff")
        self.b1.pack()
        self.b1.place(x=380,y=116)
        self.b1.config(command=self.new_file)

        self.b2 = Button(self.root, text="حافظه", font=("B Nazanin", 10 ,"bold"),fg="#4B0082",
                         activebackground="#ffffff")
        self.b2.pack()
        self.b2.place(x=280,y=116)
        self.b2.config(command=self.memory) 

        self.img3=PhotoImage(file="33.png")#name
        self.txt3=Label(self.root,image=self.img3,borderwidth=0)
        self.txt3.pack()
        self.txt3.place(x=250,y=188)

        self.img4=PhotoImage(file="44.png")#kg
        self.txt4=Label(self.root,image=self.img4,borderwidth=0)
        self.txt4.pack()
        self.txt4.place(x=252,y=256)

        self.img5=PhotoImage(file="55.png")#tall
        self.txt5=Label(self.root,image=self.img5,borderwidth=0)
        self.txt5.pack()
        self.txt5.place(x=252,y=320)
        
        self.e1=Entry(self.root,width=20 ,font="calibre" ,justify="right")
        self.e1.pack()
        self.e1.place(x=290,y=210)
        

        self.e2=Entry(self.root,width=20 ,font="calibre" ,justify="right")##########
        self.e2.pack()
        self.e2.place(x=290,y=280)
        

        self.e3=Entry(self.root,width=20 ,font="calibre" ,justify="right" )
        self.e3.pack()
        self.e3.place(x=290,y=350)
        
         
        self.b3 = Button(self.root, text="محاسبه کن", font=("B Nazanin", 10 ,"bold"),fg="#4B0082",
                          activebackground="#ffffff")
        self.b3.pack()
        self.b3.place(x=150,y=340)
        self.b3.config(command=self.calculate)
        
        
        
        self.img10=PhotoImage(file="4444.png")#vector
        self.txt10=Label(self.root,image=self.img10,borderwidth=0)
        self.txt10.pack()
        self.txt10.place(x=0,y=420)
        
        
        self.root.mainloop()

    def new_file(self):
        answer=messagebox.showinfo("information","لطفا،اطلاعات زير را تکميل کنيد ")
        print(answer)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        
        self.img15=PhotoImage(file="10.png")#BMI
        self.txt19=Label(self.root,image=self.img15,borderwidth=0)
        self.txt19.pack()
        self.txt19.place(x=300,y=430)
    def memory(self):
        self.new_window=Toplevel(self.root)
        self.new_window.resizable(False,False)
        self.new_window.geometry("700x200+500+300")
        self.new_window.config(bg="#9975b9")

        self.new_window.img33=PhotoImage(file="99.png")#name
        self.new_window.txt33=Label(self.new_window,image=self.new_window.img33,borderwidth=0)
        self.new_window.txt33.pack()
        self.new_window.txt33.place(x=140,y=5)

        

        self.new_window.e1=Entry(self.new_window,width=20 ,font="calibre" ,justify="right")
        self.new_window.e1.pack()
        self.new_window.e1.place(x=170,y=50)

        self.new_window.b1 = Button(self.new_window, text="جستجو در حافظه",
                                    font=("B Nazanin", 10 ,"bold"),fg="#4B0082",
                                    activebackground="#ffffff")
        self.new_window.b1.pack()
        self.new_window.b1.place(x=50,y=50)
        self.new_window.b1.config(command=self.search)
        
    def search(self):
        self.new_window.img44=PhotoImage(file="18.png")#block
        self.new_window.txt44=Label(self.new_window,image=self.new_window.img44,borderwidth=0)
        self.new_window.txt44.pack()
        self.new_window.txt44.place(x=300,y=115)
        s1=self.new_window.e1.get()#name
        f=open("bmi.txt","r")
        for line in f:
            if s1 in line:
                self.new_window.txt17=Label(self.new_window,text=line ,fg="#36013f",
                                            font=("B Nazanin", 18,"bold") )
                self.new_window.txt17.config(bg="#9975b9")
                self.new_window.txt17.pack()
                self.new_window.txt17.place(x=300,y=110)
            
        f.close()        
    def calculate(self):
        s1=self.e1.get()#name
        s2=float(self.e2.get())#kg
        s3=float(self.e3.get())#tall
        result=s2/(s3*s3)
        r="%0.2f" %(result)
        #print("%0.2f" %(result))
        
        self.img9=PhotoImage(file="888.png")#BMI
        self.txt9=Label(self.root,image=self.img9,borderwidth=0)
        self.txt9.pack()
        self.txt9.place(x=250,y=410)
        
        self.img7=PhotoImage(file="77.png")#memory
        self.txt7=Label(self.root,image=self.img7,borderwidth=0)
        self.txt7.pack()
        self.txt7.place(x=250,y=490)

        self.b4 = Button(self.root, text="بله", font=("B Nazanin", 10 ,"bold"),fg="#4B0082",
                         activebackground="#ffffff")
        self.b4.pack()
        self.b4.place(x=380,y=500)
        self.b4.config(command=self.yes_button)

        self.b5 = Button(self.root,text="خير",font=("B Nazanin", 10 ,"bold"),fg="#4B0082" ,
                         activebackground="#ffffff")
        self.b5.pack()
        self.b5.place(x=280,y=500)
        self.b5.config(command=self.no_button)
        
        self.txt3=Label(self.root,text=r ,fg="#ffffff",font=("calibre", 18 ,"bold") )
        self.txt3.config(bg="#36013f")
        self.txt3.pack()
        self.txt3.place(x=300,y=430)
        
    def yes_button(self):
         data=""
         s1=self.e1.get()#name
         s2=float(self.e2.get())#kg
         s3=float(self.e3.get())#tall
         result=s2/(s3*s3)
         r="%0.2f" %(result)
         f=open("bmi.txt","a")
         data=s1+" عزيز، " +"شاخص توده بدني شما " + r + " است " +"\n"
         f.write(data)
         f.close()
         answer=messagebox.showinfo("information"," اطلاعات شما با موفقيت در حافظه ذخيره شد  ")
         print(answer)
         
    def no_button(self):
         answer=messagebox.showinfo("information"," اطلاعات شما ذخيره نشد  ")
         print(answer)    
        
def main():
    
    x=my_class()
    

if __name__=="__main__":main()   

