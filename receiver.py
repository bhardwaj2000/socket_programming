import socket
# import socket module / liberary to create
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#          socket type ipv4,       UDP
s.bind(("127.0.0.1",9999))# bind function take input tuple
# ip unkown system "0.0.0.1"
#creating udp socket ipv4, port
# port greater 1005 is always free many times on system. so, use 9999
# so now code for receive data
while True:
    data_recv=s.recvfrom(100)
    print(data_recv) 

    # sending message
    rply="thanks for connecting ...."
    s.sendto(rply.encode('ascii'),data_recv[1])