import socket #เป็นการดึงฟังชั่นเน็ตเวิคของไพทอน
from uncleengineer import thaistock 
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

    try:
        mystock = thaistock(data)
        resp_text = 'Stock : {} Price : {}'.format(mystock[0],mystock[1])
        
    except:
        resp_text = 'No Stock data' 
        

    '''

    if data== 'Can I have the WIFI code?':
        resp_text = 'yes,  I L O V E  I love you'
    elif data == 'Sorry, it can not connect.':
        resp_text='TT'
    else:
        resp_text='don!'  '''

    client.send(resp_text.encode('utf-8'))
    client.close()