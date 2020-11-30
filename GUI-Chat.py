
from tkinter import * 
from tkinter import ttk


def send(event=None):
    text = v_message.get()
    print("mesage : ", text)
    v_result.set(text)
    

Gui = Tk()
Gui.geometry('500x500')
Gui.title('Chating for love')

FONT = ('Angsana New', 20)



v_message = StringVar()
Emessage = ttk.Entry(Gui, textvariable= v_message , font=FONT ,width=45)
Emessage.place(x=50,y=150)

v_result = StringVar()
v_result.set('----------Result----------')
Eresult = ttk.Label(Gui, textvariable= v_result , font=FONT ,width=45)
Eresult.place(x=50,y=300)

Bsend = ttk.Button(Gui, text = 'send message' , command = send) 
#Bsend.pack()
Bsend.place(x=200,y=250)

Gui.bind('<Return>',send)  ###เป็นการกด enter เพื่อใช้ def send #### 

Gui.mainloop()