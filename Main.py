import json
import socket

# Sample dictionary being sent to microservice
dataDict = {
    "Dining Out": 1,
    "Groceries": 2,
    "Fun Stuff": 3,
    "Rent": 4,
    "Utilities": 5
}

# Endcode the dictionary to json
dataToSend = json.dumps(dataDict).encode("utf-8")

# Send json over socket
print("Creating socket connection...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
s.sendall(dataToSend)
print("Sending data to microservice...")

s.close() # Close the socket when done
