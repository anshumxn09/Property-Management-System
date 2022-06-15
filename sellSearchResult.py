from tkinter import *
from PIL import ImageTk, Image
import sellSearch


class SellSearchResult:
    def __init__(self, myRow):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="midnightblue")

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="white")

        def toMoveBack():
            frame.destroy()
            sellSearch.SellSearch()

        headerLabel = Label(newWindow, text=f"Details About {myRow[1]}", font=("Times New Roman", 16, "bold"))
        headerLabel.place(x=0, y=0, width=1206, height=60)
        headerLabel.config(bg="slateblue", fg="#e2d7f2")

        back = Button(headerLabel, text="<<", font=("Times New Roman", 14, "bold"), command=toMoveBack)
        back.place(x=20, y=20, width=20, height=20)
        back.config(borderwidth=0, bg="slateblue", fg="#e2d7f2",
                    activebackground='slateblue',
                    activeforeground="#e2d7f2")

        Name = Label(newWindow, text="Seller's Name : ", font=("Times New Roman", 14))
        Name.place(x=70, y=70 + 20)
        Name.config(fg="darkmagenta", bg="white")
        pname = Label(newWindow, font=("Times New Roman", 14))
        pname.place(x=260, y=70 + 20)
        pname.config(bg="white", fg="darkmagenta")

        Address = Label(newWindow, text="Seller's Address : ", font=("Times New Roman", 14))
        Address.place(x=70, y=120 + 20)
        Address.config(fg="darkmagenta", bg="white")
        padd = Label(newWindow, font=("Times New Roman", 14))
        padd.place(x=260, y=120 + 20)
        padd.config(bg="white", fg="darkmagenta")

        BType = Label(newWindow, text="Building Type : ", font=("Times New Roman", 14))
        BType.place(x=70, y=170 + 20)
        BType.config(fg="darkmagenta", bg="white")
        pb = Label(newWindow, font=("Times New Roman", 14))
        pb.place(x=260, y=170 + 20)
        pb.config(bg="white", fg="darkmagenta")

        AType = Label(newWindow, text="Area Type: ", font=("Times New Roman", 14))
        AType.place(x=70, y=220 + 20)
        AType.config(fg="darkmagenta", bg="white")
        pa = Label(newWindow, font=("Times New Roman", 14))
        pa.place(x=260, y=220 + 20)
        pa.config(bg="white", fg="darkmagenta")

        ASqft = Label(newWindow, text="Area (SqFT) : ", font=("Times New Roman", 14))
        ASqft.place(x=70, y=270 + 20)
        ASqft.config(fg="darkmagenta", bg="white")
        pas = Label(newWindow, font=("Times New Roman", 14))
        pas.place(x=260, y=270 + 20)
        pas.config(bg="white", fg="darkmagenta")

        Location = Label(newWindow, text="Location: ", font=("Times New Roman", 14))
        Location.place(x=70, y=320 + 20)
        Location.config(fg="darkmagenta", bg="white")
        pl = Label(newWindow, font=("Times New Roman", 14))
        pl.place(x=260, y=320 + 20)
        pl.config(bg="white", fg="darkmagenta")

        Landamrk = Label(newWindow, text="Landmark : ", font=("Times New Roman", 14))
        Landamrk.place(x=70, y=370 + 20)
        Landamrk.config(fg="darkmagenta", bg="white")
        plm = Label(newWindow, font=("Times New Roman", 14))
        plm.place(x=260, y=370 + 20)
        plm.config(bg="white", fg="darkmagenta")

        Up = Label(newWindow, text="Upper Price : ", font=("Times New Roman", 14))
        Up.place(x=70, y=420 + 20)
        Up.config(fg="darkmagenta", bg="white")
        pu = Label(newWindow, font=("Times New Roman", 14))
        pu.place(x=260, y=420 + 20)
        pu.config(bg="white", fg="darkmagenta")

        Lp = Label(newWindow, text="Lower Price : ", font=("Times New Roman", 14))
        Lp.place(x=70, y=470 + 20)
        Lp.config(fg="darkmagenta", bg="white")
        plp = Label(newWindow, font=("Times New Roman", 14))
        plp.place(x=260, y=470 + 20)
        plp.config(bg="white", fg="darkmagenta")

        Cno = Label(newWindow, text="Contact No. : ", font=("Times New Roman", 14))
        Cno.place(x=70, y=520 + 20)
        Cno.config(fg="darkmagenta", bg="white")
        pcn = Label(newWindow, font=("Times New Roman", 14))
        pcn.place(x=260, y=520 + 20)
        pcn.config(bg="white", fg="darkmagenta")

        pname.config(text="", width=9)
        padd.config(text="", width=9)
        pb.config(text="", width=9)
        pa.config(text="", width=9)
        pas.config(text="", width=9)
        pl.config(text="", width=9)
        plm.config(text="", width=9)
        pu.config(text="", width=9)
        plp.config(text="", width=9)
        pcn.config(text="", width=9)

        pname.config(text=myRow[1])
        padd.config(text=myRow[2])
        pb.config(text=myRow[3])
        pa.config(text=myRow[4])
        pas.config(text=myRow[5])
        pl.config(text=myRow[6])
        plm.config(text=myRow[7])
        pu.config(text=myRow[8])
        plp.config(text=myRow[9])
        pcn.config(text=myRow[10])

        myWall2 = ImageTk.PhotoImage(Image.open("searchIcon.jpg"))
        wallLabel = Label(newWindow)
        wallLabel.place(x=500, y=60, width=706, height=568)
        wallLabel.config(image=myWall2)

        frame.mainloop()


if __name__ == "__main__":
    newPage = SellSearchResult((1,2,3,4,5,6,7,8,9,10,11))
