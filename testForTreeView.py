
from tkinter import *
from tkinter import ttk
import mySQLConnection as database
from PIL import ImageTk, Image


frame = Tk()

frame.geometry("1266x668+50+20")
frame.minsize(1266, 668)
frame.maxsize(1266, 668)
frame.title("Property Management System")
myicon = PhotoImage(file='myIcon.png')
frame.iconphoto(False, myicon)

database.myQuery.execute("select * from mypurchase")

tree = ttk.Treeview(frame)
tree['show'] = "headings"
# jitna headings mein chahta hoon utna he dikhaaye aur apna blank space add na kareee.

# to get the styles
styles = ttk.Style()
styles.theme_use("clam")
styles.configure(".", font=("Helvetica", 14))
styles.configure("Treeview.Heading", foreground="red", font=('Helvetica', 11, "bold"))

tree["columns"] = ("ID", "NAME", "ADDRESS", "BTYPE", "ATYPE", "LOC", "LANDMARK", "UP", "LP", "CONTACT")
tree.column("ID", width=50, minwidth=50, anchor=CENTER)
tree.column("NAME", width=50, minwidth=50, anchor=CENTER)
tree.column("ADDRESS", width=50, minwidth=50, anchor=CENTER)
tree.column("BTYPE", width=50, minwidth=50, anchor=CENTER)
tree.column("ATYPE", width=50, minwidth=50, anchor=CENTER)
tree.column("LOC", width=50, minwidth=50, anchor=CENTER)
tree.column("LANDMARK", width=50, minwidth=50, anchor=CENTER)
tree.column("UP", width=50, minwidth=50, anchor=CENTER)
tree.column("LP", width=50, minwidth=50, anchor=CENTER)
tree.column("CONTACT", width=50, minwidth=50, anchor=CENTER)

tree.heading("ID", text="ID" ,anchor=CENTER)
tree.heading("NAME", text="NAME" ,anchor=CENTER)
tree.heading("ADDRESS", text="ADDRESS" ,anchor=CENTER)
tree.heading("BTYPE",text="BTYPE", anchor=CENTER)
tree.heading("ATYPE", text="ATYPE" ,anchor=CENTER)
tree.heading("LOC", text="LOC" ,anchor=CENTER)
tree.heading("LANDMARK",text="LANDMARK", anchor=CENTER)
tree.heading("UP", text="UP" ,anchor=CENTER)
tree.heading("LP", text="LP" ,anchor=CENTER)
tree.heading("CONTACT", text="CONTACT", anchor=CENTER)

i = 0
for row in database.myQuery:
    if row[0]%2==0:
        tree.insert('', i, text="",
                    values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]), tags=("even",))
    else:
        tree.insert('', i, text="",
                    values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]), tags=("odd",))
    i = i + 1

tree.tag_configure("even", background="midnightblue", foreground="white")
tree.tag_configure("odd", background="white", foreground="midnightblue")

horiScrollBar = ttk.Scrollbar(frame, orient="vertical")
tree.configure(xscrollcommand=horiScrollBar.set)
horiScrollBar.pack(fill=Y, side="right")

tree.place(x=0, y=0, width=1266, height=668)
frame.mainloop()