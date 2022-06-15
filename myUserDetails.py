from tkinter import *
from tkinter import ttk
import mySQLConnection as database, adminMainPage


class UserTable:
    def __init__(self):
        frame = Tk()

        frame.geometry("1286x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)

        myTitle = Label(frame, text="USER'S TABLE", font=("Times New Roman", 24, "bold"))
        myTitle.place(x=0, y=0, width=1266, height=50)
        myTitle.config(bg="midnightblue", fg="white")
        database.myQuery.execute("select * from myuser")

        def toMoveBack():
            frame.destroy()
            adminMainPage.AdminMainPage()

        Back = Button(myTitle, text="<<", font=("Times New Roman", 16, "bold"))
        Back.place(x=10, y=4)
        Back.config(bg="midnightblue", fg="white", activeforeground="white", activebackground="midnightblue",
                    borderwidth=0, command=toMoveBack)

        tree = ttk.Treeview(frame)
        tree['show'] = "headings"
        # jitna headings mein chahta hoon utna he dikhaaye aur apna blank space add na kareee.

        # to get the styles
        styles = ttk.Style()
        styles.theme_use("clam")
        styles.configure(".", font=("Helvetica", 14))
        styles.configure("Treeview.Heading", foreground="midnightblue", font=('Helvetica', 11, "bold"), background="white",
                         borderwidth=0)

        tree["columns"] = ("ID", "NAME", "PASSWORD", "GENDER", "ADDRESS", "DATE OF BIRTH", "CONTACT NO")
        tree.column("ID", width=10, minwidth=50, anchor=CENTER)
        tree.column("NAME", width=50, minwidth=50, anchor=CENTER)
        tree.column("PASSWORD", width=50, minwidth=50, anchor=CENTER)
        tree.column("GENDER", width=50, minwidth=50, anchor=CENTER)
        tree.column("ADDRESS", width=50, minwidth=50, anchor=CENTER)
        tree.column("DATE OF BIRTH", width=50, minwidth=50, anchor=CENTER)
        tree.column("CONTACT NO", width=50, minwidth=50, anchor=CENTER)

        tree.heading("ID", text="ID", anchor=CENTER)
        tree.heading("NAME", text="NAME", anchor=CENTER)
        tree.heading("PASSWORD", text="PASSWORD", anchor=CENTER)
        tree.heading("GENDER", text="GENDER", anchor=CENTER)
        tree.heading("ADDRESS", text="ADDRESS", anchor=CENTER)
        tree.heading("DATE OF BIRTH", text="DATE OF BIRTH", anchor=CENTER)
        tree.heading("CONTACT NO", text="CONTACT NO", anchor=CENTER)

        i = 0
        for row in database.myQuery:
            if row[0] % 2 == 0:
                tree.insert('', i, text="",
                            values=(
                                row[0], row[1], row[2], row[3], row[4], row[5], row[6]),
                            tags=("even",))
            else:
                tree.insert('', i, text="",
                            values=(
                                row[0], row[1], row[2], row[3], row[4], row[5], row[6]),
                            tags=("odd",))
            i = i + 1

        tree.tag_configure("even", background="midnightblue", foreground="white")
        tree.tag_configure("odd", background="white", foreground="midnightblue")

        horiScrollBar = ttk.Scrollbar(frame, orient="horizontal")
        tree.configure(xscrollcommand=horiScrollBar.set)
        horiScrollBar.pack(fill=X, side="bottom")

        veriScrollBar = ttk.Scrollbar(frame, orient="vertical")
        tree.configure(xscrollcommand=horiScrollBar.set)
        veriScrollBar.pack(fill=Y, side="right")

        tree.place(x=0, y=50, width=1286, height=668)
        frame.mainloop()


if __name__ == "__main__":
    newPage = UserTable()
