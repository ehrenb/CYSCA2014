import socket
import sys
import re
def main():  
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server_address = ('10.0.0.13',9876)
  sock.connect(server_address)
  while True:
    data=''
    msgs=0
    while msgs < 2:
      print 'getting new msgs'
      data+=sock.recv(1024)
      msgs+=1
    length =''
    challenge=''
    try:
      length = re.search("[\n\r].*length:\s*([^\n\r]*)",data).group(1)
      challenge = re.search("[\n\r].*[\n\r].*Challenge:\s*([^\n\r]*)\s*([^\n\r]*)",data).group(1)
      print length
      print challenge
      break
    except:
      print 'error with parsing'
      break
      

    
if __name__ == "__main__":
  main()