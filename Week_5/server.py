# создание сокета, контекстный менеджер
# сервер
import socket, re
data_file = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
   
    while True:
        conn, addr = sock.accept()
        conn.settimeout(30) # timeout := None|0|gt 0
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                except socket.timeout:
                    print("close connection by timeout")
                    break
                    
                if not data:
                    break
                pattern = re.compile(r'\w+')
                get_put = pattern.findall(data.decode("utf8"))[0]
                metrics = pattern.findall(data.decode("utf8"))[1]
                try:
                    conn.settimeout(pattern.findall(data.decode("utf8"))[3])
                except:
                    pass
                if get_put == 'put':
                    data_file[pattern.findall(data.decode("utf8"))[1]] = pattern.findall(data.decode("utf8"))[2]
                elif get_put == 'get':
                    #if metrics == "*":
                    #    conn.send(str(data_file).encode("utf-8"))
                    conn.send(str(data_file[pattern.findall(data.decode("utf8"))[1]]).encode("utf-8"))
