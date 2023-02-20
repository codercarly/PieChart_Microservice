import json
import matplotlib.pyplot as plt
import socket

'''
    CreatePieChart takes in labels and values from the client and returns a Pie Chart
    representation of those values
'''
def CreatePieChart(labels, values):
    # Plotting the pie chart
    plt.pie(
        values,
        labels=labels,
        startangle=90,
        shadow=True,
        radius=1.2,
        autopct='%1.1f%%'
    )

    # Plotting legend
    plt.legend()

    # Showing the plot
    plt.show()

'''
    Create a Socket Server to connect with the Client
'''
def server():
    labels = []
    values = []

    # Create a byte array to decode the json data sent by client
    tempData = bytearray()

    # Create a socket connection
    print("Creating socket connection...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 1234))
    s.listen(5) # Listen for data
    print("Listening for data...")
    conn, addr = s.accept()

    # If data is received...
    while True:
        dataReceived = conn.recv(4096)
        print("Data received...")

        tempData = tempData + dataReceived
        data = json.loads(tempData.decode("utf-8")) # Decode the json data sent by client

        # Get key/value pairs from the data
        for key in data.keys():
            labels.append(key)
        for value in data.values():
            values.append(value)

        print(labels)
        print(values)
        # Create the pie chart and display it for the user
        print("Creating pie chart...")
        CreatePieChart(labels, values)

        s.close()
        print("Closing connection...")

        # Restart the socket server
        server()

# Start up the socket server
server()