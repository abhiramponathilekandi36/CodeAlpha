import socket
import struct
from ethernet_tools import EthernetFrame, IPV4, UDP, hexdump, TCP
from colors import *

ETH_P_ALL = 0x03 # Listen for everything
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))

while True:
    raw_data, addr = s.recvfrom(65565)

    # Ethernet
    frame = EthernetFrame(raw_data)
    print(str(frame))

    # IPV4
    if frame.EtherType == IPV4.ID:
        ipv4 = IPV4(frame.Payload)
        print(blue("└─ " + str(ipv4)))
        
        #UDP
        if ipv4.PROTOCOL == UDP.ID:
            udp = UDP(ipv4.PAYLOAD)
            print(yellow("   └─ " + str(udp)))
            print(yellow(hexdump(udp.PAYLOAD, 5)))
            
	# TCP
        elif ipv4.PROTOCOL == TCP.ID:
            tcp = TCP(ipv4.PAYLOAD)
            print(green("   └─ " + str(tcp)))
            print(green(hexdump(tcp.PAYLOAD, 5)))
