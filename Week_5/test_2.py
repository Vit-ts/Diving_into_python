


import socket

with socket.create_connection(("127.0.0.1", 9888), 5) as sock:
    # set socket read timeout
    sock.settimeout(2)
    try:
        sock.sendall("put PC 125 434543\n".encode("utf8"))
        data = sock.recv(1024)
        data = data.decode("utf-8")
        print(str(data))
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print("send data error:", ex)