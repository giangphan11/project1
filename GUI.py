from tkinter import *
from tkinter import messagebox
from center import makecenter
from XulyFile import *

def addFunction():
    ma=strMa.get()
    ten=strTen.get()
    nam=strNam.get()
    GhiFile("database.txt",ma+";"+ten+";"+nam)
    strMa.set("")
    strTen.set("")
    strNam.set("")
    ShowItem()
def ShowItem():
    arr=DocFile("database.txt")
    print(arr)
    listbox.delete(0,END)
    for item in arr:
        listbox.insert(END,item)
def SapXep():
    arr=DocFile("database.txt")
    for i in range(len(arr)):
        for j in range(len(arr)):
            a=arr[i]
            b=arr[j]
            if a[2]>b[2]:
                arr[i]=b
                arr[j]=a
    print(arr)
    listbox.delete(0,END)
    for item in arr:
        listbox.insert(END,item)
def TimKiem():
    arr=DocFile("database.txt")
    ma=strMa.get()
    flag=False
    listbox.delete(0, END)
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col]==ma:
                listbox.insert(END,arr[row])
                flag=True
    if flag==False:
        messagebox.showinfo('Thông báo','Không tìm thấy mã '+ma)
root=Tk()

strMa= StringVar()
strTen=StringVar()
strNam=StringVar()

root.title("Phần mềm quản lý sách")
root.minsize(width=340,height=320)
root.resizable(width=True,height=True)
makecenter(root)

Label(root,text="Quản lý sách",fg='blue', font=("Arial",16),justify=CENTER).grid(row=0,columnspan=2)
listbox=Listbox(root,width=50)
listbox.grid(row=1,columnspan=2)
ShowItem()

Label(root,text="Mã sách",fg='orange', font=("Arial",14)).grid(row=2,column=0)
Entry(root,width=30,textvariable=strMa).grid(row=2,column=1)

Label(root,text="Tên sách",fg='orange', font=("Arial",14)).grid(row=3,column=0)
Entry(root,width=30,textvariable=strTen).grid(row=3,column=1)

Label(root,text="Năm xuất bản",fg='orange', font=("Arial",14)).grid(row=4,column=0)
Entry(root,width=30,textvariable=strNam).grid(row=4,column=1)

btnChoose=Frame()
Button(btnChoose,text="Thêm",command=addFunction).pack(side=LEFT)
Button(btnChoose,text="Tìm",command=TimKiem).pack(side=LEFT)
Button(btnChoose,text="Sắp xếp",command=SapXep).pack(side=LEFT)
Button(btnChoose,text="Thoát",command=root.quit).pack(side=LEFT)

btnChoose.grid(row=5,column=1)
root.mainloop()

