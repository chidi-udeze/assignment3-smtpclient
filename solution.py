from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))

    helo = 'HELO Chidi\r\n'
    clientSocket.send(helo.encode())
    recv1 = clientSocket.recv(1024)
   
    clientSocket.send("\r\n".encode())
    
    mail_from = 'MAIL FROM: <ctu212@nyu.edu>\r\n'
    clientSocket.sendall(mail_from.encode())
    recv2 = clientSocket.recv(1024).decode()
   
    rcpt_to = 'RCPT TO: <ctu212@nyu.edu>\r\n'##Reciepient email
    clientSocket.sendall(rcpt_to.encode())
    recv3 = clientSocket.recv(1024).decode()

    data = 'DATA\r\n'
    clientSocket.sendall(data.encode())
    recv4 = clientSocket.recv(1024).decode()

    clientSocket.send(bytes((msg + endmsg).encode()))
    recv5 = clientSocket.recv(1024)

    recv6 = clientSocket.recv(1024).decode()

    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv7 = clientSocket.recv(1024).decode()
 
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')