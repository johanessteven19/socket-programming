#!/usr/bin/env python

import socket
import threading
from typing import Tuple

SERVER_NAME = ""
SERVER_PORT = 4321
BUFFER_SIZE = 1024

format = "UTF-8"


def socket_handler(connection: socket.socket, address: Tuple[str, int]):
    print(f"Receive connection from [{address}]")
    status = True

    while status:   
        command = input("Input Command: ")
        if command == "send":
            send_message = input(">")
            connection.send(send_message.encode(format))
        elif command == "check":
            send_message = "check"
            connection.send(send_message.encode(format))
            input_message = connection.recv(BUFFER_SIZE)
            print(f"Receive message: {input_message.decode(format)}")
        elif command == "wait":
            send_message = "wait"
            connection.send(send_message.encode(format))
            wStatus = True
            while wStatus:
                input_message = connection.recv(BUFFER_SIZE)  
                input_decode = input_message.decode(format)          
                if input_decode == "dc":
                    status = False
                    wStatus = False
                elif input_decode == "done":
                    print("Worker waiting for your command")
                    wStatus = False
                else:
                    print(f"Output receive: {input_decode}")
    
    print(f"Connection with [{address}] is lost")            
    connection.close()




def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.bind((SERVER_NAME, SERVER_PORT))
        sc.listen(0)

        print("Example Socket Server Program")
        print("Hit Ctrl+C to terminate the program")

        while True:
            connection, address = sc.accept()

            thread = threading.Thread(target=socket_handler,args=(connection,address))
            thread.start()

if __name__ == "__main__":
    main()