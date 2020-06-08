import socket

UDP_IP = "192.168.4.1"
THIS_IP = "192.168.4.2"
UDP_PORT = 3333
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((THIS_IP, UDP_PORT))                     
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

#sock = socket.socket(socket.AF_INET, # Internet
#                     socket.SOCK_DGRAM) # UDP


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
