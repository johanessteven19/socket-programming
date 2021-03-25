#!/usr/bin/env python

import socket
from queue import Queue

SERVER_IP = "127.0.0.1"
SERVER_PORT = 4322
BUFFER_SIZE = 1024

format = "UTF-8"

def main():
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to Server([IP:{SERVER_IP}],[PORT:{SERVER_PORT}]")
    status = True
    task = Queue()
    
    while status:
        print(". . .")
        command = sc.recv(BUFFER_SIZE)
        command_bytes = command.decode(format)
        if command_bytes == "check":
            print("Server is checking your status")
            size = str(task.qsize())
            send_message = size.encode(format)
            sc.send(send_message)
        elif command_bytes == "wait":
            print("Server is waiting for your input")
            # DO TASK HERE
            tStatus = True
            while tStatus:
                command = input(">")
                if command == "do":
                    # STILL EXAMPLE MIGHT CHANGE LATER
                    # parameter = task.get()
                    # send_message = doTask(parameter.split(","))
                    param = pArr(task.get())
                    send_message = doTask(param)
                    sc.send(send_message.encode(format))
                    print(f"1 task done, remaining task: {str(task.qsize())}")
                elif command == "done":
                    ans = input("Want to quit?")
                    if ans == "y" or ans == "yes":
                        send_message = "dc"
                        sc.send(send_message.encode(format))
                        status = False
                        tStatus = False
                    elif ans == "n" or ans == "no":
                        send_message = "done"
                        sc.send(send_message.encode(format))
                        tStatus = False
        else:
            print("Server has sent you something")
            task.put(command_bytes)
    sc.close()

def doTask(num_list):
    e = mean(num_list)
    o = modus(num_list)
    s = bubbleSort(num_list)
    result = f'mean: {e}, modus: {o}, sorted: {s}'
    return result

def pArr(param):
    li = param.split(",")
    for i in range(len(li)): 
        li[i] = int(li[i])
    return li

def mean(array):
    s, counter, m = 0, 0, 0
    for i in range(len(array)):
        s += array[i]
        counter += 1
    m = s / counter
    return str(m)

def modus(array):
    max_value = array[0]
    for element in array:
        if element > max_value:
            max_value = element
    return str(max_value)

def bubbleSort(num_list):
    n = len(num_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return str(num_list)

def quickSort(num_list, first_index, last_index):
    quickSortRecursion(num_list, first_index, last_index)
    return str(num_list)

def quickSortRecursion(num_list, first_index, last_index):
    if first_index < last_index:
        partition_index = partition(num_list, first_index, last_index)
        quickSortRecursion(num_list, first_index, partition_index-1)
        quickSortRecursion(num_list, partition_index+1, last_index)
    return num_list

def partition(num_list, first_index, last_index):
    pivot = num_list[-1]
    i = first_index-1
    for j in range(first_index, last_index):
        if num_list[j] <= pivot:
            i += 1
            num_list[i], num_list[j] = num_list[j], num_list[i]
    i += 1
    num_list[i], num_list[last_index] = num_list[last_index], num_list[i]
    return i

    # TODO:
    # MAKE doTask(array):
    # mean = mean(array) 
    # median = median(array)
    # modus = modus(array)
    # sort = bubleSort(array)
    # result = """
    # return f" Mean :{mean}; median :{median}; Modus :{modus}; Sorted :{Sort}
    #           

    # TODO:
    # Make mean(array):
    # return string

    # TODO:
    # Make median(array):
    #  return string

    # TODO:
    # Make modus(array):
    # return string

    # TODO:
    # make bubbleSort(array):
    # return string


    # NOTES
    # print("Example Socket Client Program")

    # input_value = input("Enter a string to send to the server: ")
    # input_value_bytes = input_value.encode("UTF-8")
    # sc.send(input_value_bytes)

    # output_value_bytes = sc.recv(BUFFER_SIZE)
    # output_value = output_value_bytes.decode("UTF-8")
    # print(output_value)

    # sc.close()

if __name__ == "__main__":
    main()