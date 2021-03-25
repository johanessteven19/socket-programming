#!/usr/bin/env python

import socket
from queue import Queue

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8086
BUFFER_SIZE = 1024

format = "UTF-8"

def main():
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to Server([IP:{SERVER_IP}],[PORT:{SERVER_PORT}]")
    status = False
    task = Queue(maxsize=3)
    
    print('Enter password to continue')
    psw = input('>')
    send_message = psw
    sc.send(send_message.encode(format))
    command = sc.recv(BUFFER_SIZE)
    command_bytes = command.decode(format)
    if command_bytes == 'Wrong password':
        print('Wrong password')
        sc.close()
    else:
        status = True

    while status:
        print(". . .")
        command = sc.recv(BUFFER_SIZE)
        command_bytes = command.decode(format)
        if command_bytes == "check":
            print("Server is checking your status")
            send_message = checkStat(task)
            sc.send(send_message.encode(format))
        elif command_bytes == "wait":
            print("Server is waiting for your input")
            tStatus = True
            while tStatus:
                command = input(">")
                if command == "do":
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
        elif command_bytes == "revert":
            task.queue.clear()
            print("Queue is cleared by the server")
        else:
            print("Server has sent you something")
            if not task.full():
                task.put(command_bytes)
            else:
                send_message = "Queue is full"
                sc.send(send_message.encode(format))
    sc.close()

def doTask(num_list):
    a = mean(num_list)
    m = modus(num_list)
    o = bubbleSort(num_list)
    g = median(num_list)
    u = smallest(num_list)
    s = highest(num_list)
    result = f'mean: {a}, modus: {m}, sorted: {o}, median: {g}, smallest value: {u}, highest value: {s}'
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
    dic = {}

    for element in array:
        dic[element] = 0

    for element in array:
        dic[element] += 1

    max_freq = 0
    for key, value in dic.items():
        if value > max_freq:
            max_freq = value

    mode = []
    for key, value in dic.items():
        if value == max_freq:
            mode.append(key)

    result = ""
    for val in mode:
        result += str(val) + " "

    return result

def median(array):
    lstLen = len(array)
    if lstLen % 2 == 0:
        return (array[lstLen//2]+array[(lstLen//2)-1])/2
    else:
        return array[lstLen//2]

def bubbleSort(num_list):
    n = len(num_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return str(num_list)

def smallest(array):
    return str(array[0])

def highest(array):
    return str(array[-1])

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

def checkStat(que):
    x = que.qsize()
    if x < 1:
        return "Idle"
    elif x > 0:
        return f"Working on {x} task(s)"


if __name__ == "__main__":
    main()