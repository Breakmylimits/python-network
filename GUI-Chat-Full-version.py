
from tkinter import * 
from tkinter import ttk
import socket
import threading

allmsg = []

def server():
    my_ip = '192.168.2.127'
    port = 5000

    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # เป็นคำสั้งที่ใช้ในการรียูตพอร์ตทำให้ใช้พอร์ตซำ้ได้

        server.bind((my_ip,port))
        server.listen(1)

        print('Witing for cleint...')
        client, addr = server.accept()
        print('Connect from :', str(addr))

        data = client.recv(1024).decode('utf-8')
        print('Message from Client :', data)

        allmsg.append(data)

        try:
            textshow = ''
            if len(allmsg) >= 5:
                for m in allmsg[-5:]:
                    textshow += m+ '\n'
            else:
                for m in allmsg:
                    textshow += m+ '\n'
                
            v_result2.set(textshow)
        except:
            print('With client')

        resp_text = '---send done!----' 

        client.send(resp_text.encode('utf-8'))
        client.close()

def ThreadRunserver():
    task1 = threading.Thread(target=server)
    task1.start()


def Sendmessage():
    server_ip = '192.168.2.127'
    port = 5000

    data =  v_message.get()

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # เป็นคำสั้งที่ใช้ในการรียูตพอร์ตทำให้ใช้พอร์ตซำ้ได้

    server.connect((server_ip,port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Data from Server :', data_server)
    server.close()

def send(event=None):
    text = v_message.get()
    v_result.set(text)
    task2 = threading.Thread(target=Sendmessage)
    task2.start()

ThreadRunserver()    

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



v_result2 = StringVar()
v_result2.set('----------Result2----------')
Eresult2 = ttk.Label(Gui, textvariable= v_result2 , font=FONT ,width=45)
Eresult2.place(x=260,y=300)


Bsend = ttk.Button(Gui, text = 'send message' , command = send) 
#Bsend.pack()
Bsend.place(x=200,y=250)

Gui.bind('<Return>',send)  ###เป็นการกด enter เพื่อใช้ def send #### 

Gui.mainloop()