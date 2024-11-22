# MessageBoardClientServer

## Overview
This repository contains a simple TCP client-server application that implements a message board. Users can connect to the server and perform operations such as posting messages, retrieving messages, deleting messages, and quitting the connection.

## Features
- **POST**: Send messages to the server.
- **GET**: Retrieve messages from the server.
- **DELETE**: Remove messages using their IDs.
- **QUIT**: Safely close the connection to the server.

## Technologies Used
- Python 3.12.4
- Socket Programming

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/muhammadmahad4/MessageBoardClientServer.git
   ```
2. Navigate to the project directory:
   cd MessageBoardClientServer

## Usage
1. Start the server:
   python MessageBoardServer.py
   The server will listen for incoming connections on port `16111`.

2. Run the client:
   python MessageBoardClient.py <server_ip> <server_port>
   Replace `<server_ip>` with your server's IP address (or `localhost` if running on the same machine) and `<server_port>` with `16111`.

3. Follow the prompts in the client to execute commands.

## Commands
- **POST**: Input messages to send to the server. End input with `#`.
- **GET**: Retrieve all messages from the server.
- **DELETE**: Specify message IDs to delete. End input with `#`.
- **QUIT**: Close the connection to the server.

## Example
To post messages:
```
Client: POST
Client: Hello, World!
Client: This is a message.
Client: #
Server: OK
```

To retrieve messages:
```
Client: GET
Server: MESSAGE ID: 0000, RECEIVED DATETIME: 22/11/2024 12:00:00
Server: Hello, World!
Server: This is a message.
Server: #
```
