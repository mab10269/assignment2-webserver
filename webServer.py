from socket import *
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(("", port))
  serverSocket.listen(1)
  
  while True:
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recv(10240).decode() 
      filename = message.split()[1]
      
      f = open(filename[1:], 'rb')
    
      outputdata = b"http/1.1 200 ok\r\n"
      outputdata += b"server: mypythonserver/1.0\r\n"
      outputdata += b"content-type: text/html; charset=UTF-8\r\n"
      outputdata += b"connection: close\r\n"
      outputdata += b"content-length: " + str(os.path.getsize(filename[1:])).encode() + b"\r\n"
      outputdata += b"r\n" 
         
      for i in f:
        outputdata += i 
        
      f.close()
      connectionSocket.send(outputdata)  
      connectionSocket.close()
      
    except Exception as e:
      body = b"<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>\r\n"
      outputdata = b"http/1.1 404 Not Found\r\n"
      outputdata += b"server: mypythonserver/1.0\r\n"
      outputdata += b"content-type: text/html; charset=UTF-8\r\n"
      outputdata += b"content-length: " + str(len(body)).encode() + b"\r\n"
      outputdata += b"\r\n"
      outputdata += bodyg
      
      connectionsocket.send(outputdata)
      connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)

