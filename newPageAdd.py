from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import newAddPage0, purchasePage, mySQLConnection as database

class NewAddPage:
    def __init__(self, loginid):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="navy")

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="white")

        def backProp():
            frame.destroy()
            newAddPage0.NewAddPage0(loginid)

        def propp1():
            frame.destroy()
            purchasePage.Purchase(loginid, 4)

        def propp2():
            frame.destroy()
            purchasePage.Purchase(loginid, 5)

        def propp3():
            frame.destroy()
            purchasePage.Purchase(loginid, 6)

        query = "select s_s from myi where i_id=4"
        database.myQuery.execute(query)
        result = database.myQuery.fetchone()
        print(result)

        if result[0] == '0':
            p1 = ImageTk.PhotoImage(Image.open("prop1.jpg"))
            Prop1 = Button(newWindow, image=p1)
            Prop1.place(x=0, y=0, width=1206, height=196)
            Prop1.config(bg="white", command=propp1)
        else:
            p1 = ImageTk.PhotoImage(Image.open("sold.jpg"))
            Prop1 = Button(newWindow, image=p1)
            Prop1.place(x=0, y=0, width=1206, height=196)
            Prop1.config(bg="white", command=propp1)
            Prop1.config(state=DISABLED)

        query = "select s_s from myi where i_id=5"
        database.myQuery.execute(query)
        result = database.myQuery.fetchone()
        print(result)

        if result[0] == '0':
            p2 = ImageTk.PhotoImage(Image.open("prop2.jpg"))
            Prop2 = Button(newWindow, image=p2)
            Prop2.place(x=0, y=196, width=1206, height=196)
            Prop2.config(bg="white", command=propp2)
        else:
            p2 = ImageTk.PhotoImage(Image.open("sold.jpg"))
            Prop2 = Button(newWindow, image=p2)
            Prop2.place(x=0, y=196, width=1206, height=196)
            Prop2.config(bg="white", command=propp2)
            Prop2.config(state=DISABLED)

        query = "select s_s from myi where i_id=6"
        database.myQuery.execute(query)
        result = database.myQuery.fetchone()
        print(result)

        if result[0] == '0':
            p3 = ImageTk.PhotoImage(Image.open("prop3.jpg"))
            Prop3 = Button(newWindow, image=p3)
            Prop3.place(x=0, y=392, width=1206, height=196)
            Prop3.config(bg="white", command=propp3)
        else:
            p3 = ImageTk.PhotoImage(Image.open("sold.jpg"))
            Prop3 = Button(newWindow, image=p3)
            Prop3.place(x=0, y=392, width=1206, height=196)
            Prop3.config(bg="white", command=propp3)
            Prop3.config(state=DISABLED)

        back = Button(newWindow, text="BACK", font=("Cascadia Code", 16))
        back.place(x=0, y=588, width=1206, height=40)
        back.config(bg="black", fg="white",
                    activeforeground="white",
                    activebackground="black",
                    command=backProp)

        frame.mainloop()


if __name__ == '__main__':
    myPage = NewAddPage(900)
