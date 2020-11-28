import socket

server_ip = '192.168.2.127'
port = 5000

while True:
    data = input('Send Message :')

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # เป็นคำสั้งที่ใช้ในการรียูตพอร์ตทำให้ใช้พอร์ตซำ้ได้

    server.connect((server_ip,port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Data from Server :', data_server)
    server.close()