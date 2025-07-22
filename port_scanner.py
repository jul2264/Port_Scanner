import socket
import threading
from queue import Queue
import datetime

# ONLY FOR EDUCATIONAL PURPOSES ON AUTHORIZED NETWORKS

target = "127.0.0.1"  # localhost or target IP address
queue = Queue()
open_ports = []
lock = threading.Lock()

# Port Scanner using multithreading

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        sock.close()
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            with lock:
                print(f"Port {port} is open")
                open_ports.append(port)

port_list = range(1, 1024)  # Scans ports from 1 to 1024 on the target IP address
fill_queue(port_list)

thread_list = []

# Create 100 threads to scan ports concurrently
for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# Start all threads
for thread in thread_list:
    thread.start()

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print("Open ports: ", open_ports)

x = datetime.datetime.now()
print(x) 

# Saves results to a file
with open("results.txt", "a") as f:
    f.write(f"Scan conducted on: {x}\n")
    f.write("Open ports:\n")
    for port in open_ports:
        f.write(f"{port}\n")
print("Results saved to results.txt")