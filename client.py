import socket

HOST = '127.0.0.1'
PORT = 9999

def connSocket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            recvData = s.recv(1024).decode('utf-8')
            print(recvData)
            sendData = input("보내기 > ")
            s.send(sendData.encode('utf-8'))

if __name__ == '__main__':
    connSocket()