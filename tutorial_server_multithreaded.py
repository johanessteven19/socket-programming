#!/usr/bin/env python

import socket
import threading
import random
from typing import Tuple

SERVER_NAME = ""
SERVER_PORT = 4322
BUFFER_SIZE = 1024

format = "UTF-8"


def socket_handler(connection: socket.socket, address: Tuple[str, int]):
    print(f"Receive connection from [{address}]")
    status = True

    while status:   
        command = input("Input Command: ")
        if command == "send":
            send_message = input(">")
            if send_message == 'random':
                length = input('''>Enter length of list
>''')
                a = input('''>Enter least possible value
>''')
                b = input('''>Enter most possible value
>''')
                send_message = random_numbers(int(length), int(a), int(b))
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
        elif command == "revert":
            send_message = "revert"
            connection.send(send_message.encode(format))
            print("Worker's queue is cleared")

    
    print(f"Connection with [{address}] is lost")            
    connection.close()

def random_numbers(length, a, b):
    result = ''
    for i in range(length):
        result += str(random.randint(a,b)) + ','
    return result[:-1]
    


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