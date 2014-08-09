import socket
import sys
import re
wordlist = []
def main():  
  wordlist = []
  jumbled_word= None
 
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server_address = ('10.0.0.13',5050)
  sock.connect(server_address)
  #while True: 
  done = 0
  #50 for getting the annagramss
  while done<51:
    msgs = 0
    data = ''
    while msgs < 3:
      data+=sock.recv(4096)
      msgs+=1
    jumbled_word = None
    print data
    try:
      wordlist = re.search("'.*'",data).group().replace("'","").split(",")
      jumbled_word = re.search("[\n\r].*Jumbled word:\s*([^\n\r]*)",data).group(1)
    except:
      break
    #jumbled_word_list = jumbled_word.split()
    solution = unjumble(jumbled_word,wordlist)
    print solution
    sock.send(solution)
    done+=1

def unjumble(jumbled_word,wordlist):
  jumbled_sorted = ''.join(sorted(jumbled_word))
  for word in wordlist:
    word_stripped = ''.join(sorted(word.strip()))
    if jumbled_sorted == word_stripped:
      return word.strip()
  return None
    
if __name__ == "__main__":
  main()
