#necessary imports
import argparse
from scapy.all import *
import time
import datetime
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

"""

"""
def ping(destination,packets_to_receive, wait_time, data_to_send, timeout):
    start_time = datetime.datetime.now() #starts time for timing the execution
    print("Attempting to ping "+destination+"...")

    #this loop does the programs actual functionality
    while (datetime.datetime.now() - start_time).total_seconds() < timeout and packets_to_receive!=0:
        #reduce number of packets to receive
        packets_to_receive-=1
        #send the actual packet
        packet = IP(dst=destination) / ICMP()
        response = sr1(packet, verbose=True)
        #print the response
        if response:
            print("The ping to "+destination+" was successful")
            print("Summary: "+response.summary())
        else:
            print("The ping to "+destination+" has failed")
        #include the wait time
        time.sleep(wait_time)

    #print message when the program is over
    print("Execution time has ended")

"""
This function handles the command line argument parsing and then passes the data on to other functions
to do the computation for the programs output.
"""
def main():
    #this section parses command line arguments
    parser = argparse.ArgumentParser()
    # the c flag indicates the number of echo response packets to receive before exiting
    parser.add_argument("-c", type=int, help="number of echo response packets to receive before quitting")
    # the i flag is the number of seconds to wait between each packet being sent
    parser.add_argument("-i", type=int, help="the number of seconds to wait between sending packets")
    # the s flag is the number of data bytes that are sent
    parser.add_argument("-s", type=int, help="number of data (in bytes) to send")
    # if the t flag is provided, the program will exit after this many seconds regardless of packets received
    parser.add_argument("-t", type=int, help="number of seconds before the program exits")
    # the d flag is the server that the pings will be made to
    parser.add_argument("-d", type=str, help="the server the pings are made to")

    # save the arguments as variables
    args = parser.parse_args()
    destination=args.d
    if args.c is not None:
        packets_to_receive = args.c
    else:
        packets_to_receive = 999999999

    if args.i is not None:
        wait_time = args.i
    else:
        wait_time=1

    if args.s is not None:
        data_to_send = args.s
    else:
        data_to_send=56

    if args.t is not None:
        timeout = args.t
    else:
        timeout=999999999

    #call the function to operate ping
    ping(destination, packets_to_receive, wait_time, data_to_send, timeout)

#starts the program
if __name__=="__main__":
    main()