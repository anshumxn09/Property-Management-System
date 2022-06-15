from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as popup
import mySQLConnection as database, purchaseSearchResult, adminMainPage


class PurchaseSearch:
    def __init__(self):
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
            adminMainPage.AdminMainPage()

        headerLabel = Label(newWindow)
        headerLabel.place(x=0, y=0, width=1206, height=60)
        headerLabel.config(bg="slateblue")

        back = Button(headerLabel, text="<<", font=("Times New Roman", 14, "bold"), command=toMoveBack)
        back.place(x=20, y=20, width=20, height=20)
        back.config(borderwidth=0, bg="slateblue", fg="#e2d7f2",
                    activebackground='slateblue',
                    activeforeground="#e2d7f2")

        myWall = ImageTk.PhotoImage(Image.open("searchWall.jpg"))
        wallLabel = Label(newWindow, image=myWall)
        wallLabel.place(x=0, y=60, width=1206, height=568)
        wallLabel.config(bg="plum")

        def fetch():
            getID = searchEntry.get()
            if getID.strip() == "":
                popup.showwarning("Property Management System", "Kindly Enter ID First!!!!")
                return
            try:
                yup = int(getID)
                database.myQuery.execute(f"select * from mypurchase where p_id={yup}")

                if database.myQuery:
                    myRow = database.myQuery.fetchone()
                    if myRow is not None:
                        frame.destroy()
                        purchaseSearchResult.PurchaseSearchResult(myRow)
                    else:
                        popup.showwarning("Property Management System", "Please Type Correct ID!!!!")
                else:
                    popup.showwarning("Property Management System", "Please Type Correct ID!!!!")
            except:
                popup.showwarning("Property Management System", "Kindly Enter Valid ID!!!!")

        search = Label(headerLabel, text="Enter Purchaser's ID : ", font=("Times New Roman", 16, "bold"))
        search.place(x=363, y=15)
        search.config(bg="slateblue", fg="#e2d7f2")

        searchEntry = Entry(headerLabel, font=("Times New Roman", 16))
        searchEntry.place(x=580, y=15)
        searchEntry.config(fg="slateblue", highlightcolor="slateblue",
                           highlightbackground="slateblue",
                           highlightthickness=1)

        searchButton = Button(headerLabel, command=fetch, text="🢘", font=("Times New Roman", 30),)
        searchButton.place(x=810, y=16, width=50, height=27)
        searchButton.config(bg="#e2d7f2", fg="slateblue", borderwidth=0
                            , activeforeground="white",
                            activebackground="#e2d7f2")

        frame.mainloop()


if __name__ == "__main__":
    newPage = PurchaseSearch()
