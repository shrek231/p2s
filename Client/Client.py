#will add encryption later
import time
import socket
import threading
import requests
def TXThread():
	while True:
		try:
			MESSAGE = bytes(username + " : "+ input("type: "),encoding='utf8')


			#UDP_IP = "144.202.94.205"
			UDP_PORT = 28015

			#print("message: %s" % MESSAGE)

			sock = socket.socket(socket.AF_INET, # Internet
								socket.SOCK_DGRAM) # UDP
			sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
		except:
			print("cant connect to server, its probubly off")
def RXThread():
	a = ""
	while True:
		#try:

		url = "http://" + (UDP_IP.decode('utf8')) + ":8080/text"
		#print(url)

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
		#except:
			#print("cant connect to server api, its probubly off")
# try:
UDP_IP = bytes(input("IP (default: 144.202.94.205): "),encoding='utf8')
username = input("Name : ")
threading.Thread(target=TXThread).start()
threading.Thread(target=RXThread).start()
# except:
#    print("Error: unable to start thread")
