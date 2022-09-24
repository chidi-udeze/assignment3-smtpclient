from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    # recv = clientSocket.recv(1024).decode()
    # to cmnt
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')
    # end

    # Send HELO command and print server response.
    heloCommand = 'HELO Chidi\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    # to cmnt
    # print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # end

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = 'MAIL FROM: <ctu212@nyu.edu>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpt = 'RCPT TO: <ogasampikin@gmail.com>\r\n'##Reciepient email
    clientSocket.send(rcpt.encode())
    recv3 = clientSocket.recv(1024).decode()
    # if recv3[:3] != '250':
    #     print('250 reply not received from server, Recipient was not deemed okay.')
    # print(recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    # if recv4[:3] != '250':
    #     print('250 reply not received from server, data not received.')
    # print(recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(bytes((msg + endmsg).encode()))
    recv5 = clientSocket.recv(1024)
    # print(recv5)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    recv6 = clientSocket.recv(1024).decode()
    # print(recv6)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv7 = clientSocket.recv(1024).decode()
    # print(recv7)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')