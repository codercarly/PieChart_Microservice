import errno
import json
import socket
import subprocess
import time

# Sample dictionary being sent to microservice
catDict = {
    "Cat Toys": 1,
    "Cat Food": 2,
    "Cat Clothes": 3,
    "Cat Spa": 4,
    "Cat Vet": 5
}

dogDict = {
    "Dog Toys": 1,
    "Dog Food": 2,
    "Dog Clothes": 3,
    "Dog Spa": 4,
    "Dog Vet": 5
}

# Endcode the dictionary to json
catData = json.dumps(catDict).encode("utf-8")
dogData = json.dumps(dogDict).encode("utf-8")


keepGoing = True

while True:
    try:
        print("Creating socket connection...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect(("127.0.0.1", 1234))

        userInput = input("Dog or Cat? ")

        if userInput == "Dog":
            s.sendall(dogData)
            print("Sending dog data to microservice...")
            keepGoing = True
        elif userInput == "Cat":
            s.sendall(catData)
            print("Sending cat data to microservice...")
            keepGoing = True
        else:
            print("All done!")
            keepGoing = False

        time.sleep(5) # Pause before closing the connection
        s.close() # Close the socket when done
    except IOError as e:
        if e.errno == errno.EPIPE:
            pass