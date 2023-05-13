import threading
import time

def print_numbers():
    for i in range(1, 6):
        print("Thread 1 - ", i)
        time.sleep(1)

def print_letters():
    for char in 'ABCDE':
        print("Thread 2 - ", char)
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Selesai")
