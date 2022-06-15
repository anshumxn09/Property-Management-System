import mysql.connector as sql

myDatabase = sql.connect(host="localhost", user="root", passwd="anshuman@123", database="miniproject")
myQuery = myDatabase.cursor()

# query = "insert into mypurchase values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
# myData = [(9005, "Krishna", "Kings Circle", "Plot", "Commercial", "8500", "Lower Parel", "Worli Naka", "80000", "60000", "9892296515"),
#           (9006, "Falguni", "Thane", "Plot", "Commercial", "9000", "Airoli", "Gold Films", "75000", "65000", "9152561088"),
#           (9007, "Jeevan", "Mira Road", "Plot", "Residential", "8000", "Kurla", "Pheonix", "70000", "60000", "8879567070"),
#           (9008, "Anisha", "Matunga", "Plot", "Residential", "8500", "Dadar", "Dadar Fort", "90000", "85000", "8890567070")]
# myQuery.executemany(query, myData)
# myDatabase.commit()

# myNewId = 9001
# Name = "Anshuman"
# A = "Santa"
# bt = "plot"
# at = "comm"
# aq = 9000
# lo = "thane"
# ld = "thane"
# up = "50000"
# lp = "25000"
# c = "8779939269"
# my = f"insert into mypurchase values({myNewId}, \"Anshuman\", {A}, {bt}, {at}, {aq}, {lo}, {ld}, {up}, {lp}, {c})"
# # val = ("Anshuman", "Santacruz", "Plot", "Commercial", "9000", "Thane", "Thane", "90000", "50000", "8779939269")
# myQuery.execute(my)
# myDatabase.commit()

'''

dataBase.myQuery.execute(f"select * from myAdmin where admin_id={adminName}")
                if dataBase.myQuery:
                    print("finallyyy")
                else:
                    print("good night")
                
from tkinter import *

from PIL import ImageTk, Image
frame = Tk()

frame.geometry("1266x668+50+20")
frame.minsize(1266, 668)
frame.maxsize(1266, 668)
frame.title("Property Management System")
myicon = PhotoImage(file='myIcon.png')
frame.iconphoto(False, myicon)

frame.mainloop()

# try:
                    myId = int(adminName)
                    # try:
                    dataBase.myQuery.execute("select * from myAdmin where admin_id="+str(myId))
                    if dataBase.myQuery:
                            print("finallyyyyyyy")
                    # except:
                        # popup.showwarning("Property Management System", "Kindly Enter Valid ID And Password")
                # except:
                #     popup.showwarning("Property Management System", "Kindly Enter Valid ID")
'''