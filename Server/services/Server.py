import socket, ssl

bindsocket = socket.socket()
bindsocket.bind(('', 10026))
bindsocket.listen(0)



while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket,
                                 server_side=True,
                                 certfile="server.crt",
                                 keyfile="server.key")
    try:
        print connstream.read()
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
