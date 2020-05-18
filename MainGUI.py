import tkinter as tk
import sqlite3

HEIGHT = 300
WIDTH = 400


database = sqlite3.connect('YourPlan.db')
c = database.cursor()


c.execute('''create table if not exists list 
        (contain varchar(50) primary key)''')
database.commit()

#---------------------运行所需函数--------------------------------
def addMission():
    top = tk.Toplevel()
    top.title("添加")

    textEntry = tk.Entry(top, width=10)
    textEntry.grid(row=1, column=0, padx=1, pady=1)

    addButton2 = tk.Button(top, text="添加", command=lambda: addMissionComfire(textEntry.get(), top))
    addButton2.grid(row=1, column=1, padx=1, pady=1)


def addList():
    top = tk.Toplevel()
    top.title("添加")

    textEntry = tk.Entry(top, width=10)
    textEntry.grid(row=1, column=0, padx=1, pady=1)

    addButton2 = tk.Button(top, text="添加", command=lambda: addListComfire(textEntry.get(), top))
    addButton2.grid(row=1, column=1, padx=1, pady=1)


def addMissionComfire(text, top):
    missionBox.insert("end", text)
    top.destroy()

def addListComfire(text, top):
    contain = listBox.get(0, missionBox.size())
    if text in contain:
        tk.messagebox.showinfo('提示', '存在重复的计划单，请更换名字')
    else:
        listBox.insert("end", text)
        #c.execute("create table "+text+"/n"
         #        "(contain varchar(50) primary key);"
          #        )
        c.execute("insert into list(contain) values (?);", (text,))
        database.commit()
        top.destroy()



def exitAndSave():
    print("Escape")
    root.destroy()


def click():
    print("click")
    root.destroy()






#-------------------------图形化GUI布局--------------------------
root = tk.Tk()
root.resizable(0, 0)

mainCanvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='gray')
mainCanvas.pack()

listFrame = tk.Frame(mainCanvas)
listFrame.grid(row=0, column=0)

missionFrame = tk.Frame(mainCanvas, bg='green')
missionFrame.grid(row=0, column=1)

listBox = tk.Listbox(listFrame)
listBox.grid(row=0, column=0)

buttonFrame2 = tk.Frame(listFrame)
buttonFrame2.grid(row=1, column=0)

addListButton = tk.Button(buttonFrame2, text="add", command=addList)
addListButton.grid(row=0, column=0)

deleteListButton = tk.Button(buttonFrame2, text="delete", command=lambda x=listBox: x.delete("active"))
deleteListButton.grid(row=0, column=1)

missionBox = tk.Listbox(missionFrame)
missionBox.grid(row=0, column=0)

buttonFrame1 = tk.Frame(missionFrame)
buttonFrame1.grid(row=1, column=0)

addButton = tk.Button(buttonFrame1, text="添加", command=addMission)
addButton.grid(row=0, column=0)

deleteButton = tk.Button(buttonFrame1, text="删除", command=lambda x=missionBox: x.delete("active"))
deleteButton.grid(row=0, column=1)

for item in ["996", "ICU"]:
    missionBox.insert("end", item)
    listBox.insert("end", item)

root.protocol('WM_DELETE_WINDOW', exitAndSave)

root.mainloop()
