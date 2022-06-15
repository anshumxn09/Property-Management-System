from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as popup
import adminMainPage, mySQLConnection as database


class SellDelete:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="white")

        myLayout = Label(frame)
        myLayout.place(x=0, y=0, width=1266, height=434.2)
        myLayout.config(bg="mintcream")

        myLayout2 = Label(frame)
        myLayout2.place(x=0, y=434.2, width=1266, height=668 - 434.2)
        myLayout2.config(bg="midnightblue")

        newWindow = Frame(frame)
        newWindow.place(x=233, y=84, width=800, height=500)
        newWindow.config(bg="white")

        def toMoveBack():
            frame.destroy()
            adminMainPage.AdminMainPage()

        def toDelete():
            getID = IdEntry.get().strip()
            if getID in "":
                popup.showwarning("Property Management System", "Kindly Enter ID First!!!!")
                return
            try :
                toMakeInt = int(getID)
                try:
                    database.myQuery.execute(f"select * from mysell where s_id={toMakeInt}")
                    myResult = database.myQuery.fetchone()
                    print(myResult)
                    if myResult is not None:
                        database.myQuery.execute(f"delete from mysell where s_id={toMakeInt}")
                        database.myDatabase.commit()
                        popup.showwarning("Property Management System", f"{toMakeInt} deleted succesfully!")
                        frame.destroy()
                        adminMainPage.AdminMainPage()
                    else:
                        popup.showwarning("Property Management System", "Kindly Enter Valid ID!!!!")
                except:
                    popup.showwarning("Property Management System", "Kindly Enter Valid ID!!!!")
            except:
                popup.showwarning("Property Management System","Oops ID Must In Integer!!")

        myBlock = Label(newWindow)
        myBlock.place(x=0, y=0, width=300, height=500)
        myBlock.config(bg="mediumslateblue")
        warn = Label(myBlock, text="Note: Deleting ID Will Delete\nAll Data Of The Seller's\nFrom The Database",
                                  font=("Times New Roman", 13, "bold"))
        warn.place(x=40, y=205)
        warn.config(bg="mediumslateblue", fg="white")

        IdLabel = Label(newWindow, text="Enter Seller's ID",
                        font=("Times New Roman", 16, "bold"))
        IdLabel.place(x=305+80+40+20, y=100+20)
        IdLabel.config(bg="white", fg="Slateblue")

        IdEntry = Entry(newWindow, font=("Times New Roman", 16))
        IdEntry.place(x=290+80+40+20, y=140+20)
        IdEntry.config(fg="slateblue", highlightcolor="slateblue",
                       highlightthickness=1,
                       highlightbackground="slateblue")

        deleteButton = Button(newWindow, text="Delete", font=("Times New Roman", 14))
        deleteButton.place(x=350+80+40+20, y=190+20, width=100, height=40)
        deleteButton.config(bg="slateblue", fg="white",
                            activebackground="slateblue",
                            activeforeground="white",
                            borderwidth=0, command=toDelete)

        back = Button(newWindow, text="🢘", font=("Times New Roman", 30), command=toMoveBack)
        back.place(x=350+80+40+20, y=240+20, width=100, height=40)
        back.config(bg="slateblue", fg="white",
                    activebackground="slateblue",
                    activeforeground="white",
                    borderwidth=0)

        frame.mainloop()


if __name__ == '__main__':
    newPage = SellDelete()
