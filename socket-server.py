import subprocess
import socket

HOST = '127.0.0.1'  
PORT = 65432        
t = True
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while t:
            data = conn.recv(1024)
            if not data:
                break
            command = data.decode()
            if command == "exit":
                t = False
            else:
                res = subprocess.run(command, shell=True, capture_output=True, text=True)
            n = res.stdout
            n = str(n)
            m = n.encode()
            conn.sendall(m)
