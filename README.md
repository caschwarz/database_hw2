# database_hw2
The code can be compiled by simply running python my_ping.py or python my_traceroute.py, assuming you are in the correct directory that these programs are in

Each of these programs requires command line arguments to be run.
They both require the -d <destination> argument, which defines where the destination of the network traffic is
They optionally can take other flags:

my_ping can take:
-c int 
stops after receiving this number of packets
-i int
waits this amount of second in between each run
-s int
sets the packetsize
-t int
if set, the program will automatically exit after this many seconds

my_traceroute can take:
-n int (1 or 0)
if set to 1, prints both symbolically and numerically
-q int
number of probes in each TTL
-s int (1 or 0)
if set to 1, shows the summary of unvisited probes

PLEASE NOTE: the program must be run in the administrator command prompt with administrator privileges to run without error

Run examples:

python my_ping.py -d google.com -s 56 -i 5
python my_ping.py -d google.com -i 10 -c 5 -t 100
python my_traceroute -d google.com -n 1 -s 1
python my_traceroute -d google.com -n 1 -q 10

