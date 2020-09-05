# обработка нескольких соединений одновременно, процессы и потоки
import socket
import threading
import multiprocessing

with socket.socket() as sock:
    sock.bind(("", 10002))
    sock.listen()
    
    workers_count = 3
    workers_list = [multiprocessing.Process(target=worker,args=(sock,))for _ in range(workers_count)]
    for w in workers_list:
        w.start()
    for w in workers_list:
        w.join()
        
# обработка нескольких соединений одновременно, процессы и потоки
def worker(sock):
    while True:
        conn, addr = sock.accept()
        print("pid", os.getpid())
        th = threading.Thread(target=process_request,args=(conn, addr))
        th.start()

def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
        print(data.decode("utf8"))
