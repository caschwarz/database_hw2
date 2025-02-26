#necessary imports
import argparse
from scapy.layers.inet import traceroute, ICMP, IP
from scapy.sendrecv import sr1

"""
This function defines lists for traceroute and fills those lists with the probes visited. Then,
the function prints out the list to standard output and optionally prints out the probes not
visited based on the users arguments.
"""
def trace_route(destination, hop_toggle, probe_number, summary):
    print("Tracing the route to "+destination+"...")

    unanswered = [] #stores the list of probes that weren't visited
    result = {} #stores the list of probes
    ttl=1 #time to live

    #this loop sends and receives the packet and prints out the route that it took
    while ttl <= 20:
        #sends packet
        icmp_request = IP(dst=destination, ttl=ttl) / ICMP() / b"X"
        reply = sr1(icmp_request, timeout=2, verbose=True)

        #display packet data
        if reply is None:
            unanswered.append(ttl)
            result[ttl] = []
            print("Hop "+str(ttl)+": Timed out")
        else:
            addresses = reply.src
            result[ttl] = [addresses]
            print("Hop "+str(ttl)+": "+addresses)

        ttl += 1

        # Control the number of probes per TTL by the probe number parameter
        if ttl > probe_number:
            break

    # prints the summary of the probes not visited
    if summary == 1:
        print("\nSummary of Unanswered Probes")
        for ttl in unanswered:
                print("Hop "+str(ttl)+": No response")

    print("Traceroute Complete")

"""
This function handles the command line argument parsing and then passes the data on to other functions
to do the computation for the programs output.
"""
def main():
    #this section parses command line arguments
    parser = argparse.ArgumentParser()
    # the n flag indicates that the hop addresses should be printed only numerically and not symbolically and numerically
    parser.add_argument("-n", type=int, help="0 to show only numerical hop addresses; 1 to show both")
    # the q flag sets the number of probes per TTL
    parser.add_argument("-q", type=int, help="sets the number of probes per TTL (time to live)")
    # the s flag optionally prints the number of probes that were not answered on each hop
    parser.add_argument("-s", type=int, help="0 to hide the summary; 1 to show the summary")
    # the d flag is the destination to trace the route to
    parser.add_argument("-d", type=str, help="the name to use trace route to")

    # save the arguments as variables
    args = parser.parse_args()
    if args.n is None:
        hop_toggle=0
    else:
        hop_toggle= args.n
    if args.q is None:
        probe_number=1
    else:
        probe_number=args.q
    if args.s is None:
        summary=1
    else:
        summary=args.s
    destination=args.d

    #call the function to operate the traceroute
    trace_route(destination, hop_toggle, probe_number, summary)

#starts the program
if __name__=="__main__":
    main()