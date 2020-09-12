# создание сокета, клиент
import socket
sock = socket.socket()
sock.connect(("127.0.0.5", 10001))
sock.sendall("ping".encode("utf8"))
sock.close()
