import socket

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create link:
s.connect(('www.bilibili.com', 80))
#send message
s.send(b'GET / HTTP/1.1\r\nHost: www.bilibili.com\r\nConnection: close\r\n\r\n')
#recept data
buffer = []
while True:
    #max=1kb
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#close link
s.close()

header,html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('bilibili.html', 'wb') as f:
    f.write(html)
