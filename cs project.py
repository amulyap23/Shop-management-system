import tkcalendar
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import sqlite3 as db
from PIL import ImageTk,Image

def connection():
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()
    sql = '''
    create table if not exists sellings (
        date string,
        product string,
        price number,
        quantity number,
        total number
        )
    '''
    cur.execute(sql)
    connectObj.commit()   
connection()     
window=Tk()                     
window.title("H-MART BILLING MANAGEMENT SYSTEM")
tabs = ttk.Notebook(window)
root= ttk.Frame(tabs)
root2=ttk.Frame(tabs)
tabs.add(root, text ='Sell')            
tabs.add(root2, text ='Stock')          
tabs.pack(expand = 1, fill ="both") 
bg=ImageTk.PhotoImage(Image.open("C:/Users/AMULYA/Desktop/bag.jpg"))
my_label=Label(root,image=bg)
my_label.place(x=0,y=0)
pic=Label(root2,image=bg)
pic.place(x=0,y=0)
def clear():
    p1quantity.set(0)
    p2quantity.set(0)
    p3quantity.set(0)
    p4quantity.set(0)
    p4quantity.set(0)
    p5quantity.set(0)
    p6quantity.set(0)
    p7quantity.set(0)
    p8quantity.set(0)
    p9quantity.set(0)
    p10quantity.set(0)
    p11quantity.set(0)
    p12quantity.set(0)
    p13quantity.set(0)
    p14quantity.set(0)
    p15quantity.set(0)
    p16quantity.set(0)
    p17quantity.set(0)
    p18quantity.set(0)
    p19quantity.set(0)
    p20quantity.set(0)
    p21quantity.set(0)   
    p22quantity.set(0)   
    p23quantity.set(0)   
    p24quantity.set(0)   
    p25quantity.set(0)   
    p26quantity.set(0)       
    billarea.delete('1.0',END)
#----------------------------------------------tab1 ----------------------------------
def GenerateBill():
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()  
    global billarea
    if (p1quantity.get()==0 and p2quantity.get()==0 and p3quantity.get()==0 and p4quantity.get()==0 and p5quantity.get()==0
        and p6quantity.get()==0  and p7quantity.get()==0  and p8quantity.get()==0  and p9quantity.get()==0  and p10quantity.get()==0
        and p11quantity.get()==0 and p12quantity.get()==0 and p13quantity.get()==0 and p14quantity.get()==0 and p15quantity.get()==0
        and p16quantity.get()==0 and p17quantity.get()==0 and p18quantity.get()==0 and p19quantity.get()==0 and p20quantity.get()==0
        and p21quantity.get()==0 and p22quantity.get()==0 and p23quantity.get()==0 and p24quantity.get()==0 and p25quantity.get()==0
        and p26quantity.get()==0):
        messagebox.showerror("Error","No product purchased")
    else:
        billarea.delete('1.0',END)
        billarea.insert(END,"\t|| H-MART SUPERMARKET ||")
        billarea.insert(END,"\n_______________\n")
        billarea.insert(END,"\nDate\t Products\tPrice\t QTY\t Total")
        billarea.insert(END,"\n==========================================")
        price= IntVar()
        price2=IntVar()
        price3=IntVar()
        price4=IntVar()
        price5=IntVar()
        price6=IntVar()
        price7=IntVar()
        price8=IntVar()
        price9=IntVar()
        price10=IntVar()
        price11=IntVar()
        price12=IntVar()
        price13=IntVar()
        price14=IntVar()
        price15=IntVar()
        price16=IntVar()
        price17=IntVar()
        price18=IntVar() 
        price19=IntVar()
        price20=IntVar()
        price21=IntVar()
        price22=IntVar()
        price23=IntVar()
        price24=IntVar()
        price25=IntVar()
        price26=IntVar()
        print(dateE.get())
        price=price2=price3=price4=price5=price6=price7=price8=price9=price10=price11=price12=price13=price14=price15=price16=price17=price18=price19=price20=price21=price22=price23=price24=price25=price26=0
        if p1quantity.get()>0:
            price=p1quantity.get()*p1price.get()
            print(price)
            billarea.insert(END,f"\n{dateE.get()}\t Tomato \t{p1price.get()}\t {p1quantity.get()}\t {price}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Tomato',p1price.get(),p1quantity.get(),price))
            connectObj.commit() 

        if p2quantity.get()>0:
            price2=p2quantity.get()*p2price.get()
            print(price2)
            billarea.insert(END,f"\n{dateE.get()}\t Britannia \t{p2price.get()}\t {p2quantity.get()}\t {price2}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            print(dateE.get(),'Britannia',p2price.get(),p2quantity.get(),price2)
            cur.execute(sql,(dateE.get(),'Britannia',p2price.get(),p2quantity.get(),price2))
            connectObj.commit() 
        if p3quantity.get()>0:
            price3=p3quantity.get()*p3price.get()
            print(price3)
            billarea.insert(END,f"\n{dateE.get()}\t Oreo \t{p3price.get()}\t {p3quantity.get()}\t {price3}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Oreo',p3price.get(),p3quantity.get(),price3))
            connectObj.commit() 
        if p4quantity.get()>0:
            price4=p4quantity.get()*p4price.get()
            print(price4)
            billarea.insert(END,f"\n{dateE.get()}\tHide&Seek \t{p4price.get()}\t {p4quantity.get()}\t {price4}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Hide&Seek',p4price.get(),p4quantity.get(),price4))
            connectObj.commit()
        if p5quantity.get()>0:
            price5=p5quantity.get()*p5price.get()
            print(price5)
            billarea.insert(END,f"\n{dateE.get()}\t Potato \t{p5price.get()}\t {p5quantity.get()}\t {price5}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Potato',p5price.get(),p5quantity.get(),price5))
            connectObj.commit()
        if p6quantity.get()>0:
            price6=p6quantity.get()*p6price.get()
            print(price6)
            billarea.insert(END,f"\n{dateE.get()}\t Oil \t{p6price.get()}\t {p6quantity.get()}\t {price6}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Oil',p6price.get(),p6quantity.get(),price6))
            connectObj.commit()
        if p7quantity.get()>0:
            price7=p7quantity.get()*p7price.get()
            print(price7)
            billarea.insert(END,f"\n{dateE.get()}\t Sugar \t{p7price.get()}\t {p7quantity.get()}\t {price7}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Sugar',p7price.get(),p7quantity.get(),price7))
            connectObj.commit()
        if p8quantity.get()>0:
            price8=p8quantity.get()*p8price.get()
            print(price8)
            billarea.insert(END,f"\n{dateE.get()}\t Salt \t{p8price.get()}\t {p8quantity.get()}\t {price8}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Salt',p8price.get(),p8quantity.get(),price8))
            connectObj.commit()
        if p9quantity.get()>0:
            price9=p9quantity.get()*p9price.get()
            print(price9)
            billarea.insert(END,f"\n{dateE.get()}\t Rice \t{p9price.get()}\t {p9quantity.get()}\t {price9}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Rice',p9price.get(),p9quantity.get(),price9))
            connectObj.commit()
        if p10quantity.get()>0:
            price10=p10quantity.get()*p10price.get()
            print(price10)
            billarea.insert(END,f"\n{dateE.get()}\t Wheat \t{p10price.get()}\t {p10quantity.get()}\t {price10}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Wheat',p10price.get(),p10quantity.get(),price10))
            connectObj.commit()
        if p11quantity.get()>0:
            price11=p11quantity.get()*p11price.get()
            print(price11)
            billarea.insert(END,f"\n{dateE.get()}\t Pepsi \t{p11price.get()}\t {p11quantity.get()}\t {price11}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Pepsi',p11price.get(),p11quantity.get(),price11))
            connectObj.commit()
        if p12quantity.get()>0:
            price12=p12quantity.get()*p12price.get()
            print(price12)
            billarea.insert(END,f"\n{dateE.get()}\t Coke \t{p12price.get()}\t {p12quantity.get()}\t {price12}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Coke',p12price.get(),p12quantity.get(),price12))
            connectObj.commit()
        if p13quantity.get()>0:
            price13=p13quantity.get()*p13price.get()
            print(price13)
            billarea.insert(END,f"\n{dateE.get()}\t Maggie \t{p13price.get()}\t {p13quantity.get()}\t {price13}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Maggie',p13price.get(),p13quantity.get(),price13))
            connectObj.commit()
        if p14quantity.get()>0:
            price14=p14quantity.get()*p14price.get()
            print(price14)
            billarea.insert(END,f"\n{dateE.get()}\t Dal \t{p14price.get()}\t {p14quantity.get()}\t {price14}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Dal',p14price.get(),p14quantity.get(),price14))
            connectObj.commit()
        if p15quantity.get()>0:
            price15=p15quantity.get()*p15price.get()
            print(price15)
            billarea.insert(END,f"\n{dateE.get()}\t Brinjal \t{p15price.get()}\t {p15quantity.get()}\t {price15}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Brinjal',p15price.get(),p15quantity.get(),price15))
            connectObj.commit()
        if p16quantity.get()>0:
            price16=p16quantity.get()*p16price.get()
            print(price16)
            billarea.insert(END,f"\n{dateE.get()}\t Maida \t{p16price.get()}\t {p16quantity.get()}\t {price16}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Maida ',p16price.get(),p16quantity.get(),price16))
            connectObj.commit()
        if p17quantity.get()>0:
            price17=p17quantity.get()*p17price.get()
            print(price17)
            billarea.insert(END,f"\n{dateE.get()}\t Munch \t{p17price.get()}\t {p17quantity.get()}\t {price17}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Munch',p17price.get(),p17quantity.get(),price17))
            connectObj.commit()
        if p18quantity.get()>0:
            price18=p18quantity.get()*p18price.get()
            print(price18)
            billarea.insert(END,f"\n{dateE.get()}\t Bread \t{p18price.get()}\t {p18quantity.get()}\t {price18}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Bread',p18price.get(),p18quantity.get(),price18))
            connectObj.commit()
        if p19quantity.get()>0:
            price19=p19quantity.get()*p19price.get()
            print(price19)
            billarea.insert(END,f"\n{dateE.get()}\t Capisicum \t{p19price.get()}\t {p19quantity.get()}\t {price19}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Capisicum',p19price.get(),p19quantity.get(),price19))
            connectObj.commit()
        if p20quantity.get()>0:
            price20=p20quantity.get()*p20price.get()
            print(price20)
            billarea.insert(END,f"\n{dateE.get()}\t Monacco \t{p20price.get()}\t {p20quantity.get()}\t {price20}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Monacco',p20price.get(),p20quantity.get(),price20))
            connectObj.commit()
        if p21quantity.get()>0:
            price21=p21quantity.get()*p21price.get()
            print(price21)
            billarea.insert(END,f"\n{dateE.get()}\t Milk \t{p21price.get()}\t {p21quantity.get()}\t {price21}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Milk',p21price.get(),p21quantity.get(),price21))
            connectObj.commit()
        if p22quantity.get()>0:
            price22=p22quantity.get()*p22price.get()
            print(price22)
            billarea.insert(END,f"\n{dateE.get()}\t Frooti \t{p22price.get()}\t {p22quantity.get()}\t {price22}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Frooti',p22price.get(),p22quantity.get(),price22))
            connectObj.commit()
        if p23quantity.get()>0:
            price23=p23quantity.get()*p23price.get()
            print(price23)
            billarea.insert(END,f"\n{dateE.get()}\t Appy Fiz \t{p23price.get()}\t {p23quantity.get()}\t {price23}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Appy Fiz',p23price.get(),p23quantity.get(),price23))
            connectObj.commit()
        if p24quantity.get()>0:
            price24=p24quantity.get()*p24price.get()
            print(price24)
            billarea.insert(END,f"\n{dateE.get()}\t Choco Pie \t{p24price.get()}\t {p24quantity.get()}\t {price24}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Choco Pie ',p24price.get(),p24quantity.get(),price24))
            connectObj.commit()
        if p25quantity.get()>0:
            price25=p25quantity.get()*p25price.get()
            print(price25)
            billarea.insert(END,f"\n{dateE.get()}\t Apples \t{p25price.get()}\t {p25quantity.get()}\t {price25}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Apples',p25price.get(),p25quantity.get(),price25))
            connectObj.commit()
        if p26quantity.get()>0:
            price26=p26quantity.get()*p26price.get()
            print(price26)
            billarea.insert(END,f"\n{dateE.get()}\t Carrots \t{p26price.get()}\t {p26quantity.get()}\t {price26}")
            sql ='''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql,(dateE.get(),'Carrots',p26price.get(),p26quantity.get(),price26))
            connectObj.commit()
            Totalprice=IntVar()
        Totalprice=price+price2+price3+price4+price5+price6+price7+price8+price9+price10+price11+price12+price13+price14+price15+price16+price17+price18+price19+price20+price21++price22+price23+price24+price25+price26
        if Totalprice>0:
         Totalquantity=IntVar()
         Totalquantity=p1quantity.get()+p2quantity.get()+p3quantity.get()+p4quantity.get()+p5quantity.get()+p6quantity.get()+p7quantity.get()+p8quantity.get()+p9quantity.get()+p10quantity.get()+p11quantity.get()+p12quantity.get()+p13quantity.get()+p14quantity.get()+p15quantity.get()+p16quantity.get()+p17quantity.get()+p18quantity.get()+p19quantity.get()+p20quantity.get()+p21quantity.get()+p22quantity.get()+p23quantity.get()+p24quantity.get()+p25quantity.get()+p26quantity.get()
         billarea.insert(END,f"\nTotal \t \t \t{Totalquantity}\t {Totalprice}")
        else:
          billarea.insert(END,f"\n\n  negative data, please check entries")
def view():
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()  
    sql = 'Select * from Sellings'
    cur.execute(sql)
    rows=cur.fetchall()
    viewarea.insert(END,f"Date\t Product\t Price of 1\t Quantity\t Price\n")
    for i in rows:
        allrows=""
        for j in i:
            allrows+=str(j)+'\t'
        allrows+='\n'
        viewarea.insert(END,allrows)
#-------------------------------------------------------------------------------------------------------------------------------
dateL=Label(root,text="Date",bg="orange",width=12,font=('arial',15,'bold'),borderwidth=5,relief="groove")
dateL.grid(row=0,column=0,padx=7,pady=7)
dateE=DateEntry(root,width=12,bg="orange",font=('arial',15,'bold'))
dateE.grid(row=0,column=1,padx=7,pady=7)
l=Label(root, text="Product",font=('arial',15,'bold'),bg="orange",width=12,borderwidth=5,relief="groove")
l.grid(row=1,column=0,padx=2,pady=2)
l=Label(root, text="Price",font=('arial',15,'bold'),bg="orange",width=7,borderwidth=5,relief="groove")
l.grid(row=1,column=1,padx=7,pady=7)
l=Label(root, text="Quantity",font=('arial',15,'bold'),bg="orange",width=7,borderwidth=5,relief="groove")
l.grid(row=1,column=2,padx=7,pady=7)
h=Label(root,text="H-MART SUPERMARKET",bg="yellowgreen",width=30,font=('kristen itc',15,'bold'),borderwidth=5,relief="groove")
h.place(x=500,y=0)
#----product 1----------------------------------------------------
p1name=StringVar()
p1name.set('Tomato')
p1price=IntVar()
p1price.set(60)
p1quantity=IntVar()
p1quantity.set(0)
l=Label(root, text=p1name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=4,column=0,padx=7,pady=7)
l=Label(root, text=p1price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=4,column=1,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=280,y=107)
t=Entry(root,textvariable=p1quantity,font=('arial',15,'bold'),width=3)
t.grid(row=4,column=2,padx=7,pady=7)
#----product 2-------------------------------------------------------------
p2name=StringVar()
p2name.set('Britannia')
p2price=IntVar()
p2price.set(30)
p2quantity=IntVar()
p2quantity.set(0)
l=Label(root, text=p2name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=5,column=0,padx=7,pady=7)
l=Label(root, text=p2price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=5,column=1,padx=7,pady=7)
l=Label(root, text="/pc",font=('arial',15,'bold'),width=3)
l.place(x=280,y=151)
t=Entry(root,textvariable=p2quantity,font=('arial',15,'bold'),width=3)
t.grid(row=5,column=2,padx=7,pady=7)
#----product 3------------------------------------
p3name=StringVar()
p3name.set('Oreo')
p3price=IntVar()
p3price.set(70)
p3quantity=IntVar()
p3quantity.set(0)
l=Label(root, text=p3name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=6,column=0,padx=7,pady=7)
l=Label(root, text=p3price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=6,column=1,padx=7,pady=7)
l=Label(root, text="/pc",font=('arial',15,'bold'),width=3)
l.place(x=280,y=195)
t=Entry(root,textvariable=p3quantity,font=('arial',15,'bold'),width=3)
t.grid(row=6,column=2,padx=7,pady=7)
#----product 4------------------------------------------
p4name=StringVar()
p4name.set('Hide&Seek')
p4price=IntVar()
p4price.set(20)
p4quantity=IntVar()
p4quantity.set(0)
l=Label(root, text=p4name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=7,column=0,padx=7,pady=7)
l=Label(root, text=p4price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=7,column=1,padx=7,pady=7)
l=Label(root, text="/pc",font=('arial',15,'bold'),width=3)
l.place(x=280,y=239)
t=Entry(root,textvariable=p4quantity,font=('arial',15,'bold'),width=3)
t.grid(row=7,column=2,padx=7,pady=7)
#----product 5-------------------------------------------------
p5name=StringVar()
p5name.set('Potato')
p5price=IntVar()
p5price.set(20)
p5quantity=IntVar()
p5quantity.set(0)
l=Label(root, text=p5name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=8,column=0,padx=7,pady=7)
l=Label(root, text=p5price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=8,column=1,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=280,y=283)
t=Entry(root,textvariable=p5quantity,font=('arial',15,'bold'),width=3)
t.grid(row=8,column=2,padx=7,pady=7)
#----product 6------------------------------------------------------
p6name=StringVar()
p6name.set('Oil')
p6price=IntVar()
p6price.set(165)
p6quantity=IntVar()
p6quantity.set(0)
l=Label(root, text=p6name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=9,column=0,padx=7,pady=7)
l=Label(root, text=p6price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=9,column=1,padx=7,pady=7)
l=Label(root, text="/l",font=('arial',15,'bold'),width=3)
l.place(x=280,y=327)
t=Entry(root,textvariable=p6quantity,font=('arial',15,'bold'),width=3)
t.grid(row=9,column=2,padx=7,pady=7)
#----product 7----
p7name=StringVar()
p7name.set('Sugar')
p7price=IntVar()
p7price.set(50)
p7quantity=IntVar()
p7quantity.set(0)
l=Label(root, text=p7name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=10,column=0,padx=7,pady=7)
l=Label(root, text=p7price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=10,column=1,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=280,y=371)
t=Entry(root,textvariable=p7quantity,font=('arial',15,'bold'),width=3)
t.grid(row=10,column=2,padx=7,pady=7)
#----product 8-------------------------------------------------------------------
p8name=StringVar()
p8name.set('Salt')
p8price=IntVar()
p8price.set(23)
p8quantity=IntVar()
p8quantity.set(0)
l=Label(root, text=p8name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=11,column=0,padx=7,pady=7)
l=Label(root, text=p8price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=11,column=1,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=280,y=415)
t=Entry(root,textvariable=p8quantity,font=('arial',15,'bold'),width=3)
t.grid(row=11,column=2,padx=7,pady=7)
#----product 9----------------------------------------------------------------
p9name=StringVar()
p9name.set('Rice')
p9price=IntVar()
p9price.set(70)
p9quantity=IntVar()
p9quantity.set(0)
l=Label(root, text=p9name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=12,column=0,padx=7,pady=7)
l=Label(root, text=p9price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=12,column=1,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=280,y=459)
t=Entry(root,textvariable=p9quantity,font=('arial',15,'bold'),width=3)
t.grid(row=12,column=2,padx=7,pady=7)
#----product 10----------------------------------------------------------------
p10name=StringVar()
p10name.set('Wheat')
p10price=IntVar()
p10price.set(55)
p10quantity=IntVar()
p10quantity.set(0)
l=Label(root, text=p10name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=13,column=0,padx=7,pady=7)
l=Label(root, text=p10price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=13,column=1,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=280,y=503)
t=Entry(root,textvariable=p10quantity,font=('arial',15,'bold'),width=3)
t.grid(row=13,column=2,padx=7,pady=7)
#----product 11----------------------------------------------------------------
p11name=StringVar()
p11name.set('Pepsi')
p11price=IntVar()
p11price.set(50)
p11quantity=IntVar()
p11quantity.set(0)
l=Label(root, text=p11name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=14,column=0,padx=7,pady=7)
l=Label(root, text=p11price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=14,column=1,padx=7,pady=7)
l=Label(root, text="/l",font=('arial',15,'bold'),width=3)
l.place(x=280,y=547)
t=Entry(root,textvariable=p11quantity,font=('arial',15,'bold'),width=3)
t.grid(row=14,column=2,padx=7,pady=7)
#----product 12----------------------------------------------------------------
p12name=StringVar()
p12name.set('Coke')
p12price=IntVar()
p12price.set(60)
p12quantity=IntVar()
p12quantity.set(0)
l=Label(root, text=p12name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=15,column=0,padx=7,pady=7)
l=Label(root, text=p12price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=15,column=1,padx=7,pady=7)
l=Label(root, text="/l",font=('arial',15,'bold'),width=3)
l.place(x=280,y=591)
t=Entry(root,textvariable=p12quantity,font=('arial',15,'bold'),width=3)
t.grid(row=15,column=2,padx=7,pady=7)
#----product 13----------------------------------------------------------------
p13name=StringVar()
p13name.set('Maggie')
p13price=IntVar()
p13price.set(6)
p13quantity=IntVar()
p13quantity.set(0)
l=Label(root, text=p13name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=16,column=0,padx=7,pady=7)
l=Label(root, text=p13price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=16,column=1,padx=7,pady=7)
l=Label(root, text="/pc",font=('arial',15,'bold'),width=3)
l.place(x=280,y=635)
t=Entry(root,textvariable=p13quantity,font=('arial',15,'bold'),width=3)
t.grid(row=16,column=2,padx=7,pady=7)#
#---------------------------------------------------------------------------
l=Label(root, text="Product",font=('arial',15,'bold'),bg="orange",width=12,borderwidth=5,relief="groove")
l.grid(row=1,column=4,padx=2,pady=2)
l=Label(root, text="Price",font=('arial',15,'bold'),bg="orange",width=7,borderwidth=5,relief="groove")
l.grid(row=1,column=5,padx=7,pady=7)
l=Label(root, text="Quantity",font=('arial',15,'bold'),bg="orange",width=7,borderwidth=5,relief="groove")
l.grid(row=1,column=6,padx=7,pady=7)
#-------------------------------------------------------------------
#----product 14----
p14name=StringVar()
p14name.set('Dal')
p14price=IntVar()
p14price.set(80)
p14quantity=IntVar()
p14quantity.set(0)
l=Label(root, text=p14name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=4,column=4,padx=7,pady=7)
l=Label(root, text=p14price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=4,column=5,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=690,y=107)
t=Entry(root,textvariable=p14quantity,font=('arial',15,'bold'),width=3)
t.grid(row=4,column=6,padx=7,pady=7)
#----product 15-------------------------------------------------------------
p15name=StringVar()
p15name.set('Brinjal')
p15price=IntVar()
p15price.set(30)
p15quantity=IntVar()
p15quantity.set(0)
l=Label(root, text=p15name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=5,column=4,padx=7,pady=7)
l=Label(root, text=p15price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=5,column=5,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=690,y=151)
t=Entry(root,textvariable=p15quantity,font=('arial',15,'bold'),width=3)
t.grid(row=5,column=6,padx=7,pady=7)
#----product 16-------------------------------------------------------------
p16name=StringVar()
p16name.set('Maida')
p16price=IntVar()
p16price.set(80)
p16quantity=IntVar()
p16quantity.set(0)
l=Label(root, text=p16name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=6,column=4,padx=7,pady=7)
l=Label(root, text=p16price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=6,column=5,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=690,y=195)
t=Entry(root,textvariable=p16quantity,font=('arial',15,'bold'),width=3)
t.grid(row=6,column=6,padx=7,pady=7)
#----product 17-------------------------------------------------------------
p17name=StringVar()
p17name.set('Munch')
p17price=IntVar()
p17price.set(10)
p17quantity=IntVar()
p17quantity.set(0)
l=Label(root, text=p17name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=7,column=4,padx=7,pady=7)
l=Label(root, text=p17price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=7,column=5,padx=7,pady=7)
l=Label(root, text="/pc",font=('arial',15,'bold'),width=3)
l.place(x=690,y=239)
t=Entry(root,textvariable=p17quantity,font=('arial',15,'bold'),width=3)
t.grid(row=7,column=6,padx=7,pady=7)
#----product 18-------------------------------------------------------------
p18name=StringVar()
p18name.set('Bread')
p18price=IntVar()
p18price.set(30)
p18quantity=IntVar()
p18quantity.set(0)
l=Label(root, text=p18name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=8,column=4,padx=7,pady=7)
l=Label(root, text=p18price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=8,column=5,padx=7,pady=7)
l=Label(root, text="/pc",font=('arial',15,'bold'),width=3)
l.place(x=690,y=283)
t=Entry(root,textvariable=p18quantity,font=('arial',15,'bold'),width=3)
t.grid(row=8,column=6,padx=7,pady=7)
#----product 19-------------------------------------------------------------
p19name=StringVar()
p19name.set('Capsicum')
p19price=IntVar()
p19price.set(48)
p19quantity=IntVar()
p19quantity.set(0)
l=Label(root, text=p19name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=9,column=4,padx=7,pady=7)
l=Label(root, text=p19price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=9,column=5,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=690,y=327)
t=Entry(root,textvariable=p19quantity,font=('arial',15,'bold'),width=3)
t.grid(row=9,column=6,padx=7,pady=7)
#----product 20-------------------------------------------------------------
p20name=StringVar()
p20name.set('Monacco')
p20price=IntVar()
p20price.set(120)
p20quantity=IntVar()
p20quantity.set(0)
l=Label(root, text=p20name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=10,column=4,padx=7,pady=7)
l=Label(root, text=p20price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=10,column=5,padx=7,pady=7)
l=Label(root, text="/pc",font=('arial',15,'bold'),width=3)
l.place(x=690,y=371)
t=Entry(root,textvariable=p20quantity,font=('arial',15,'bold'),width=3)
t.grid(row=10,column=6,padx=7,pady=7)
#----product 21-------------------------------------------------------------
p21name=StringVar()
p21name.set('Milk')
p21price=IntVar()
p21price.set(19)
p21quantity=IntVar()
p21quantity.set(0)
l=Label(root, text=p21name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=11,column=4,padx=7,pady=7)
l=Label(root, text=p21price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=11,column=5,padx=7,pady=7)
l=Label(root, text="/(1/2)l",font=('arial',15,'bold'),width=5)
l.place(x=690,y=415)
t=Entry(root,textvariable=p21quantity,font=('arial',15,'bold'),width=3)
t.grid(row=11,column=6,padx=7,pady=7)
#----product 22-------------------------------------------------------------
p22name=StringVar()
p22name.set('Frooti')
p22price=IntVar()
p22price.set(60)
p22quantity=IntVar()
p22quantity.set(0)
l=Label(root, text=p22name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=12,column=4,padx=7,pady=7)
l=Label(root, text=p22price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=12,column=5,padx=7,pady=7)
l=Label(root, text="/l",font=('arial',15,'bold'),width=3)
l.place(x=690,y=459)
t=Entry(root,textvariable=p22quantity,font=('arial',15,'bold'),width=3)
t.grid(row=12,column=6,padx=7,pady=7)
#----product 23-------------------------------------------------------------
p23name=StringVar()
p23name.set('Appy Fiz')
p23price=IntVar()
p23price.set(100)
p23quantity=IntVar()
p23quantity.set(0)
l=Label(root, text=p23name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=13,column=4,padx=7,pady=7)
l=Label(root, text=p23price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=13,column=5,padx=7,pady=7)
l=Label(root, text="/l",font=('arial',15,'bold'),width=3)
l.place(x=690,y=503)
t=Entry(root,textvariable=p23quantity,font=('arial',15,'bold'),width=3)
t.grid(row=13,column=6,padx=7,pady=7)
#----product 24-------------------------------------------------------------
p24name=StringVar()
p24name.set('Choco Pie')
p24price=IntVar()
p24price.set(50)
p24quantity=IntVar()
p24quantity.set(0)
l=Label(root, text=p24name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=14,column=4,padx=7,pady=7)
l=Label(root, text=p24price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=14,column=5,padx=7,pady=7)
l=Label(root, text="/pc",font=('arial',15,'bold'),width=3)
l.place(x=690,y=547)
t=Entry(root,textvariable=p24quantity,font=('arial',15,'bold'),width=3)
t.grid(row=14,column=6,padx=7,pady=7)
#----product 25-------------------------------------------------------------
p25name=StringVar()
p25name.set('Apples')
p25price=IntVar()
p25price.set(190)
p25quantity=IntVar()
p25quantity.set(0)
l=Label(root, text=p25name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=15,column=4,padx=7,pady=7)
l=Label(root, text=p25price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=15,column=5,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=690,y=591)
t=Entry(root,textvariable=p25quantity,font=('arial',15,'bold'),width=3)
t.grid(row=15,column=6,padx=7,pady=7)
#----product 26-------------------------------------------------------------
p26name=StringVar()
p26name.set('Carrots')
p26price=IntVar()
p26price.set(50)
p26quantity=IntVar()
p26quantity.set(0)
l=Label(root, text=p26name.get(),font=('arial',15,'bold'),width=10)
l.grid(row=16,column=4,padx=7,pady=7)
l=Label(root, text=p26price.get(),font=('arial',15,'bold'),width=3)
l.grid(row=16,column=5,padx=7,pady=7)
l=Label(root, text="/kg",font=('arial',15,'bold'),width=3)
l.place(x=690,y=635)
t=Entry(root,textvariable=p26quantity,font=('arial',15,'bold'),width=3)
t.grid(row=16,column=6,padx=7,pady=7)
#----------------------------------------------------------------------------------------------------------------------------------
billarea=Text(root)
billarea.place(x=900,y=50)
submitbtn=Button(root,command=GenerateBill,text="Bill",
          font=('arial',15,'bold'),bg="orange",width=7 )
submitbtn.place(x=1150,y=0)
#----------------------------------------------tab2 ----------------------------------
def connection2():
    connectObj2 = db.connect("shopManagement.db")
    cur = connectObj2.cursor()
    sql = '''
    create table if not exists stocks (
        date string,
        product string,
        price number,
        quantity number
        )
    '''
    cur.execute(sql)
    connectObj2.commit()   
connection2() 
def addStock():
    global dateE2,qty,name,price
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()  
    sql = '''
            INSERT INTO stocks VALUES 
            (?, ?, ?, ?)
            '''
    cur.execute(sql,(dateE2.get(),name.get(),price.get(),qty.get()))
    connectObj.commit() 
def viewStock():
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()  
    sql = 'Select * from stocks'
    cur.execute(sql)
    rows=cur.fetchall()
    viewarea2.insert(END,f"Date \tProduct\t Price\t Quantity\t \n")
    
    for i in rows:
        allrows=""
        for j in i:
            allrows+=str(j)+'\t'
        allrows+='\n'
        viewarea2.insert(END,allrows)
dateL=Label(root2,text="Date",bg="orange",width=12,font=('arial',15,'bold'))
dateL.grid(row=0,column=0,padx=7,pady=7)
dateE2=DateEntry(root2,width=12,font=('arial',15,'bold'))
dateE2.grid(row=0,column=1,padx=7,pady=7)
l=Label(root2, text="Product",font=('arial',15,'bold'),bg="orange",width=12)
l.grid(row=1,column=0,padx=7,pady=7)
l=Label(root2, text="Price",font=('arial',15,'bold'),bg="orange",width=12)
l.grid(row=2,column=0,padx=7,pady=7)
l=Label(root2, text="Quantity",font=('arial',15,'bold'),bg="orange",width=12)
l.grid(row=3,column=0,padx=7,pady=7)
name=StringVar()
price=IntVar()
qty=IntVar()
Name=Entry(root2,textvariable=name,font=('arial',15,'bold'),width=12)
Name.grid(row=1,column=1,padx=7,pady=7)
Price=Entry(root2,textvariable=price,font=('arial',15,'bold'),width=12)
Price.grid(row=2,column=1,padx=7,pady=7)
Qty=Entry(root2,textvariable=qty,font=('arial',15,'bold'),width=12)
Qty.grid(row=3,column=1,padx=7,pady=7)
addbtn=Button(root2,command=addStock,text="Add",
font=('arial',15,'bold'),bg="orange",width=20)
addbtn.grid(row=4,column=1,padx=7,pady=7)
viewarea2=Text(root2)
viewarea2.grid(row=5,column=0,columnspan=2)
viewbtn2=Button(root2,command=viewStock,text="View Stock",
font=('arial',15,'bold'),bg="orange",width=20 )
viewbtn2.grid(row=4,column=0,padx=7,pady=7)
viewarea=Text(root2)
viewbtn=Button(root2,command=view,text="View All Sellings",
font=('arial',15,'bold'),bg="orange",width=20 )
viewbtn.place(x=1000,y=0)
viewarea.place(x=800,y=50)
clear=Button(root,command=clear,text='Clear',font=('arial',15,'bold'),bg='yellowgreen',width=10)
clear.place(x=1100,y=450)
Print=Button(root,command=clear,text='PRINT',font=('arial',15,'bold'),bg='yellowgreen',width=10)
Print.place(x=1100,y=700)
mainloop() 
