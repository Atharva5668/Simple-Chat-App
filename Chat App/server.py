import socket
import threading

HEADER = 64
PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECTED!"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

def manage_client(conne, addr):
    print(f"[New Connection found] {addr} is connected!")
    connected = True
    while connected:
        msg_len = conne.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conne.recv(HEADER).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conne.send("Message has been sent!".encode(FORMAT))

    conne.close()

def start():
    server.listen()
    print(f"[Listening!] Server is listening on {SERVER}!")
    while True:
        conne, addr = server.accept()
        thread = threading.Thread(target=manage_client, args=(conne, addr))
        thread.start()
        print(f"[Active Connections!] {threading.activeCount() - 1}")

print(f"[Starting.....]Server is listening on {SERVER}")
start()