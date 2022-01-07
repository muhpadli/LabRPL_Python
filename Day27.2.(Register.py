from tkinter import *
import tkinter.font

root = Tk()
root.geometry("300x600")

changefont = tkinter.font.Font(size =20)

register = Label(root, text = "REGISTER")
nama_depan  =  Label(root,text = "Nama depan")
nama_belakang =  Label(root,text = "Nama belakang")
username =  Label(root,text = "Username")
jenis_kelamin = Label(root, text = "Jenis Kelamin")
email =  Label(root,text = "Email")
password =  Label(root,text = "Password")
daftar = Label(root, text = "Daftar")

e1 = Entry(root, width = 40)
e2 = Entry(root, width = 40)
e3 = Entry(root, width = 40)
e4 = Entry(root, width = 40)
e5 = Entry(root, width = 40)

register.place(x = 20, y = 20)
nama_depan.place(x = 20, y=50)
nama_belakang.place(x = 20, y=100)
jenis_kelamin.place(x = 20, y = 150)
username.place(x = 20, y=200)
email.place(x = 20, y=250)
password.place(x = 20, y=300)
daftar.place(x =220, y = 360)

e1.place(x = 20, y = 70)
e2.place(x = 20, y = 120)
e3.place(x = 20, y = 220)
e4.place(x = 20, y = 270)
e5.place(x = 20, y = 320)

r = StringVar()
r.set("Laki-laki")

r1 = Radiobutton(root, text = "Laki-laki", variable =r, value = "Laki-laki").place(x = 20, y = 170)
r2 = Radiobutton(root, text = "Perempuan", variable =r, value = "Perempuan").place(x = 80, y = 170)

root.mainloop()
