import socket

HOST = '127.0.0.1'  
PORT = 65432        
t = True
print("booting...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("connecting...")
    try:
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("can't connect")
        print("exiting...")
        t = False
    while t:
        d = input("enter command : ")
        if d == "help":
            print("[any command that can be run on the target sytem]")
            print("exit [shut down external server as well as client(you)]")
            print("clear [the shell feeling too clutterd? you can get rid of that with this]")
            d = input("enter command : ")
        if d == "clear":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            d = input("enter command : ")
        if d == "exit":
            print("exiting...")
            t = False
            print("sending final data...")
        s.sendall(d.encode())
        data = s.recv(1024)
        d = data.decode()
        print('\n\n\nReceived', str(d))
        print("\n\n\n\n")
