import time
import socket
import threading
import requests



def TXThread():
	while True:
		MESSAGE = bytes(username + " : "+ input("type: "),encoding='utf8')

		UDP_IP = "144.202.94.205"
		UDP_PORT = 28015

		#print("message: %s" % MESSAGE)

		sock = socket.socket(socket.AF_INET, # Internet
							socket.SOCK_DGRAM) # UDP
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))



def RXThread():
	a = ""
	while True:

		url = "http://144.202.94.205:8080/text"

		resp = requests.get(url)

		if (resp.content != a):
			print("\n\n")
			print("______________________")
			#print ("MSG: " + str(MESSAGE))
			print (resp.content)
			print("______________________")
			print("\n\n")
			a = resp.content
		time.sleep(1)




# try:

username = input("Name : ")

threading.Thread(target=TXThread).start()
threading.Thread(target=RXThread).start()

# except:
#    print("Error: unable to start thread")
























#####


