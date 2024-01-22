import socket
def run_server():
    #create socket object, AF_INET is an ip ADDRESS family FOR IPV4 , socket_stream means TCP connection 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #ip of host machine and the port number
    server_ip = "127.0.0.1"
    port = 8000
    #create a socket to send info
    server.bind((server_ip, port))
    #the socket is now listening, 0 is size of the queue.
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")
    #accept incoming connections, client_socket is a socket which receives info from the client, client address is the ip address and portnumber
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    while True:
        #looks for incoming info from socket and stores it in request
        request = client_socket.recv(1024)
        #converts from binary
        request = request.decode("utf-8")
        if request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break
        response = "accepted".encode("utf-8") # convert string to bytes
        # convert and send accept response to the client
        client_socket.send(response)
    print(f"Received: {request}")
    #close sockets to free up ports and system 
    client_socket.close()
    print("Connection to client closed")
    server.close()
run_server()
