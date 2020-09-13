import socket
import threading
clients_data = {}
def process_request(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data_split = data.decode("utf-8").split()
            try:
                if data_split[0] == 'put' and len(data_split) <= 4:
                    put_data(data_split, conn, clients_data)
                elif data_split[0] == 'get' and len(data_split) == 2:
                    get_data(data_split, conn, clients_data)
                else: conn.sendall("error\nwrong command\n\n".encode("utf-8"))
            except: 
                conn.sendall("error\nwrong command\n\n".encode("utf-8"))

def get_data(data, conn, clients_data):
    data_send = ""
    if data[1] == "*" and len(clients_data) != 0 :
        for key in clients_data:
            data_list = clients_data[key]
            for i in range(len(data_list)):
                if i % 2 == 0:
                    data_send += key + " " + ' '.join(map(str, data_list[i:i+2])) + "\n"
        data_send =  "ok\n" + data_send + "\n"      
        return conn.sendall(data_send.encode("utf-8"))
    elif data[1] in clients_data:
        data_list = clients_data[data[1]]
        for i in range(len(data_list)):
            if i % 2 == 0:
                data_send += data[1] + " " + ' '.join(map(str, data_list[i:i+2])) + "\n"
        data_send =  "ok\n" + data_send + "\n"
        return conn.sendall(data_send.encode("utf-8"))
    else:
        return conn.sendall("ok\n\n".encode("utf-8"))

def put_data(data, conn, clients_data):
    try:
        if data[1] not in clients_data:
            clients_data[data[1]] = [float(data[2]),int(data[3])]
        elif data[2] != str(next(iter(clients_data[data[1]]))):
            clients_data.setdefault(data[1], []).append(float(data[2]))
            clients_data.setdefault(data[1], []).append(int(data[3]))
        
        a = iter(clients_data[data[1]])
        b = next(a) ; b = next(a)
        if data[3] == str(b):
            clients_data[data[1]] = [float(data[2]),int(data[3])]
            
    except:
        return conn.sendall("error\nwrong command\n\n".encode("utf-8"))
    return conn.sendall("ok\n\n".encode("utf-8"))


    




def run_server(host, port):
    with socket.socket() as server:
        server.bind((host, port))
        server.listen()
        try:
            while True:
                conn, addr = server.accept()
                th = threading.Thread(target=process_request, args=(conn, addr))
                th.start()
        except:
            pass
#run_server("127.0.0.1", 10001)