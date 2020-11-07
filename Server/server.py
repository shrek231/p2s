##will add decryption later
import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 28015

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
        print(data)
        text = str(data, 'utf-8')
        file = open("Text.txt", "w")
        file.write(text + "\n")
        file.close()
    except:
        print("malformed packet")
