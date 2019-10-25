import socket
def get_IP():
   try:
        ip_address=socket.gethostbyname(socket.gethostname())
        print("Your IP Address is:" , ip_address)
   except:
        print("Please check your Network connection")
get_IP()