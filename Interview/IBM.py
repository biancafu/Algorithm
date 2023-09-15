
def sentTimes(numberOfPorts, transmissionTime, packetIds):
    # value of hash = packet_id % numberOfPorts (the port packets are sent to)
    # ports are numbered from 0 to 1
    # packet is initially sent to port that has portnumber == hash value of its packet id
    # t = time to send a packet (process time > curr time + t)
    
    #use index of ports to determine which port, record value of time available for each port
    ports = [0] * numberOfPorts #[0 0 0 0]
    currTime = 0
    i = 0 #packet index
    output = []
    while i < len(packetIds):
        packet = packetIds[i]
        port_index = packet % numberOfPorts #hash value
        currTime += 1
        while currTime < ports[port_index]:
             port_index = (port_index + 1) % numberOfPorts
        ports[port_index] = currTime + transmissionTime
        output.append(port_index)
        i+=1
        
    
    return output
    
    
a = sentTimes(4,2,[0, 2, 6])
print(a)