print ('Enter path of the file')
path = input()

print ('Input initial connecion')
initial_connection = input()
initial_connection = initial_connection.upper()

print ('Path: ', path,)
print ('Initial connection: ', initial_connection)

message = ''

key = initial_connection

with open (path) as dat:
    triplets = dat.readlines()
    size = len(triplets) #number of triplets in total
    i = 0 #counter

while len(message)<86: 

    while i<size:

        string = triplets[i]
        lcon, msg, rcon = string.split('#') # splitting triplet into left connection, right connection and part of the message 

        if key == lcon: 
            message = message + msg
            print (message)
            a, b, c, d = rcon
            key = c+b+a # reversing right connection and making a key for a new search

        i += 1
    if len(message) == 0: # in case of a wrong input of the initial connection
        print('Try again with "QVH" as initial connection.')
        break
    i = 0





