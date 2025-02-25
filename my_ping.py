#necessary imports
import argparse

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

    # save the arguments as variables
    args = parser.parse_args()
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


#starts the program
if __name__=="__main__":
    main()