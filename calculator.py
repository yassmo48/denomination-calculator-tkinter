from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root=Tk()
root.title("Denomination calculator")
root.configure(bg="light Blue")
root.geometry("650x400")


upload=Image.open("app.png")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root, image=image, bg="light blue")
label.place(x=180,y=20)


label1=Label(root,text="hey user, welcome to the denomination counter application", bg="light blue",)
label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
    MSGBOX= messagebox.showinfo(" do you want to calculate the denomination count")
    if MSGBOX == "ok":
        topwin()

button1=Button(root, text="lets get started", command=msg, bg="brown", fg="white")
button1.place(x=260, y=360)



def topwin():
    top=Toplevel()
    top.title("denominations calculations")
    top.configure(bg="light grey")
    top.geometry("600x300+50+50")

    label=Label(top,text="enter total amount", bg="light grey")
    entry=Entry(top)
    lbl=Label(top,text="here are the number of notes for each denomination", bg="light grey")



    l1=Label(top,text="5", bg="light grey")
    l2=Label(top,text="10", bg="light grey")
    l3=Label(top, text="20", bg="light grey")
    l4=Label(top, text="50", bg="light grey")

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    t4=Entry(top)

    def calculator():
        try:
            global amount
            amount=int(entry.get())
            note5=amount // 5
            amount %= 5
            note10=amount // 10
            amount %= 10
            note20=amount // 20
            amount %= 20
            note50=amount // 50
            amount %= 50


            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)

            t1.insert(END,str(note5))
            t2.insert(END,str(note10))
            t3.insert(END,str(note20))
            t4.insert(END,str(note50))
        except ValueError:
            messagebox.showerror("error", "please enter a valid number")

    btn=Button(top, text="calculate",comand=calculator,bg="brown", fg="white")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)


    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    l4.place(x=180,y=290)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    t4.place(x=270,y=290)
    top.mainloop()


root.mainloop()



        









            


