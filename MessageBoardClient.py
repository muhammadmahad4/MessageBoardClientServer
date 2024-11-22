import socket
import sys
import time

SENDING_COOLDOWN = 0.3
BUFFER_SIZE = 4096

class MessageBoardClient:

    #Construct the Client and Initialise TCP Socket
    def __init__(self, server_ip, server_port): 
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Initiate a TCP connection to the server on the socket
    def connect_to_server(self):
        try:
            self.sock.connect((self.server_ip, self.server_port))
            print("Connected to server.")
        except socket.error as e:
            print(f"Error connecting to server: {e}")
            sys.exit(1)

    #Basic function for sending a message to the server
    def send_command(self, command):
        try:
            self.sock.send(command.encode())
            time.sleep(SENDING_COOLDOWN)
        except socket.error as e:
            print(f"Error sending command to server: {e}")
            sys.exit(1)

    #Basic function to decode and return the server's response to a request/command/message from the client
    def receive_response(self):
        try:
            response = self.sock.recv(BUFFER_SIZE).decode()
            return response
        except socket.error as e:
            print(f"Error receiving response from server: {e}")
            sys.exit(1)

    #POST Command
    def post_message(self):
        self.send_command("POST")
        message = input("Client: ")
        #continue to accept the user input until '#'
        while message != "#":
            self.send_command(message) #send the accepted input as messages to the server
            message = input("Client: ")
        self.send_command("#")
        response = self.receive_response()
        print("Server:", response)

    #GET Command
    def get_messages(self):
        self.send_command("GET")
        response = self.receive_response()
        #continue to display each line of the server's response until '#'
        while response != "#":
            print("Server:", response)
            response = self.receive_response()
        print("Server: #" )

    #DELETE Command
    def delete_messages(self):
        self.send_command("DELETE")
        #continue to accept the message IDs as input for deletion '#'
        message = input("Client: ")
        while message != "#":
            self.send_command(message) #send the accepted input as messages to the server
            message = input("Client: ")
        self.send_command("#")
        response = self.receive_response()
        print("Server:", response)
        
    #QUIT Command
    def quit(self):
        self.send_command("QUIT") #Send the QUIT message to the server to indicate the need to close connection
        response = self.receive_response()
        print("Server:", response)
        time.sleep(0.5) #wait for server response
        if (response == "OK"):
            self.sock.close() #close the socket and disconnect from the server

#==================================================================================================================#

#Main code to utlise the Client class and it's functions
if __name__ == "__main__":

    if len(sys.argv) != 3: #Initial command should have exactly 3 arguments
        #if incorrect arguments then show the client the correct format and exit
        print("Usage: python MessageBoardClient.py <server_ip> <server_port>") 
        sys.exit(1)

    server_ip = sys.argv[1] #Use the second argument to initalise the serevr_ip variable
    server_port = int(sys.argv[2]) #Use the third argument to initalise the server_ip variable

    client = MessageBoardClient(server_ip, server_port) #use the initalised values of variables to construct the Client
    client.connect_to_server() #initiate a TCP connection to the indicated server

    while True: #keep taking command inputs until the client quits (or system exits on error)
        command = input("Client: ").upper()
        #check the primary command to see which client function to execute
        if command == "POST":
            client.post_message()
        elif command == "GET":
            client.get_messages()
        elif command == "DELETE":
            client.delete_messages()
        elif command == "QUIT":
            client.quit()
            break
        else:
            #OTHER Commands
            client.send_command(command)
            print("Server:",client.receive_response())
