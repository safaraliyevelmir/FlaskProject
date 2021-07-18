from tkinter import *
from functools import partial
from tkinter import messagebox
#from PIL import Image, ImageTk



def validateLogin(username, password):
    if username.get()=="admin" and password.get()=="123456":

        newWindow = Toplevel(form)
        label1=Label(newWindow,text='Adınız:  Məmməd')
        label1.pack()
        label1.place(x=10, y=10)
        
        label2=Label(newWindow,text='Soyadınız:  Abdullayev')
        label2.pack()
        label2.place(x=10, y=30)
        
        label3=Label(newWindow,text='Fin kodunuz:  78QHKMH')
        label3.pack()
        label3.place(x=10, y=50)

        label4=Label(newWindow,text='Bölmə: Azərbaycan')
        label4.pack()
        label4.place(x=210, y=10)

        label5=Label(newWindow,text='Hazırlaşdığınız Qrup: 1')
        label5.pack()
        label5.place(x=210, y=30)
        
        label6=Label(newWindow,text='Xarici dil: İngilis dili')
        label6.pack() 
        label6.place(x=210, y=50)

        label7=Label(newWindow,text='Sizin ümumi göstəiciniz:  513 baldır', bg='Green', fg="White")
        label7.pack()
        label7.place(x=210, y=100)

        

        newWindow.title("Your Profile") 
        newWindow.geometry("500x300") 


    else:
        messagebox.showwarning(title='Warning', message='Kod Səhvdir')


    
form=Tk()
form.title('Giriş ekranı')
form.geometry("230x120")
form.resizable(False, False)

username_label=Label(form,text='Username')
username_label.pack()
username_label.place(x=10, y=10)

username=StringVar()

username_yazı=Entry(fg='black', textvariable=username)
username_yazı.pack()
username_yazı.place(x=80, y=10)

password_label=Label(form,text='Password')
password_label.pack()
password_label.place(x=10, y=40)

password=StringVar()

password_yazı=Entry(fg='black', textvariable=password, show="*")
password_yazı.pack()
password_yazı.place(x=80, y=40)

validateLogin = partial(validateLogin, username, password)
loginButton = Button(form, text="Login", command=validateLogin) 
loginButton.place(x=160, y=70)
form.mainloop()