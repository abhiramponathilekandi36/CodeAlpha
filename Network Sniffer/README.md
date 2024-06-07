A network sniffer allows you to intercept, log and analyze network traffic.

In this tutorial we will build one from scratch in python3, using only standard libraries.

If you are just looking for a good sniffer, then you should probably use tcpdump (terminal) or Wireshark (GUI). We are kind of reinventing the wheel here. The point of this tutorial is to take a (somewhat) deep dive into the network stack.

If you have fun building things yourself, or if you like to be able to turn every little knob, then this program-along tutorial is for you.

I expect you to have a basic understanding of the ISO/OSI (or TCP/IP) network model and beginner tier Python3 skills. We will write this application on Linux since it gives us greater freedom when it comes to sniffing low level traffic.
