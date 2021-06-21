import socket
# import socket module / liberary to create
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#          socket type ipv4,       UDP
# what is my receiver address:- it is bind address
recv_addr=("127.0.0.1",9999)
#  now i want to send the message
user_data=input("enter your message :- ")
#converting data into ascii code or UTF or UNICODE string
newdata=user_data.encode('ascii')
#now you can send data
s.sendto(newdata, recv_addr)
print("your message has been send ..")