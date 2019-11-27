=======================================================
Simulation: 
=======================================================

A gateway (GW) and a repeater (RP) are both access points (AP). Each AP should have a randomized
check-in time offset from 0.00 to 5.00 minutes (two digit precision).
In order to perform a complete firmware upgrade, each AP must check in a total of three times and run
two processes.

Upgrade cycle:

Check-in #1: AP should set its download_firmware flag to TRUE
Process #1: AP should “download” the firmware in a random amount of time from 0.00
to 5.00 minutes
Check-in #2: AP should set its download_complete flag to TRUE
Process #2: AP should “upgrade” its firmware in a random amount of time from 0.00 to
5.00 minutes
Check-in #3: AP should set its upgrade_complete flag to TRUE
AP rules:

Each AP checks in at precise 5.00 minute intervals beginning from its check-in offset time. If an
AP has not finished its download or upgrade within the 5 minute interval, it shall not proceed to
the next check-in state and must wait for the next 5 minute check-in.

GW rules:

Each GW must wait to begin its upgrade process until each of its RPs have set its
download_complete state to TRUE.


RP rules:
A RP can only check in if neither it nor its GW have begun Process #2 OR both the RP and its
GW have completed Process #2.





Requires Python 3.6. Install with (ideally using virtualenv):

$pip install simpy
$pip install numpy

====================================================================
Command Line Execution
====================================================================
change directory to src
$cd ./src
$python main.py
usage: main.py [-h] -d DURATION -s SEED -g NO_OF_GW -r NO_OF_RP

Network-Simulation tool

optional arguments:
  -h, --help            show this help message and exit
  -d DURATION, --duration DURATION
                        The duration of the simulation (simulates
                        milliseconds).
  -s SEED, --seed SEED  Random seed
  -g NO_OF_GW, --no of Gateways NO_OF_GW
                        No Of Gateway available in the network
  -r NO_OF_RP, --no of Repeater NO_OF_RP
                        No Of Repeater available in the network
 -i CHECKIN_INTERVAL, --interval CHECKIN_INTERVAL
                        check in mark


====================================================================
For Log	
====================================================================
Refer sim.log file under the src folder



==================================================================================
Sample run:
==================================================================================
No of Gateway:1
No of Repeater : 1
Checkin Interval : 5 (5mins)

$python main.py -d 100 -s 50 -g 1 -r 1 -i 5 -n 1
INFO:simulation.simulator:Starting simulation
INFO:simulation.simulator:0.00 Starting time
INFO:simulation.simulator:REPEATER 0 Initial checkin started:  0.00
INFO:simulation.simulator:GATEWAY 0 Initial checkin started:  0.00
INFO:simulation.simulator:GATEWAY 0 Initial checkin finished:  1.33
INFO:simulation.simulator:GATEWAY 0 says DOWNLOAD_FIRMWARE set to TRUE at 1.33
INFO:simulation.simulator:GATEWAY 0 download started:  1.33
INFO:simulation.simulator:REPEATER 0 Initial checkin finished:  1.72
INFO:simulation.simulator:REPEATER 0 says DOWNLOAD_FIRMWARE set to TRUE at 1.72
INFO:simulation.simulator:REPEATER 0 download started:  1.72
INFO:simulation.simulator:REPEATER 0 says DOWNLOAD_COMPLETE set to TRUE at 4.00
INFO:simulation.simulator:REPEATER 0 download finished: 4.00
INFO:simulation.simulator:REPEATER 0 Second Checkin started:  4.00
INFO:simulation.simulator:GATEWAY 0 download finished: 4.60
INFO:simulation.simulator:GATEWAY 0 says DOWNLOAD_COMPLETE set to TRUE at 4.60
INFO:simulation.simulator:GATEWAY 0 Second Checkin finished:  6.33
INFO:simulation.simulator:GATEWAY 0 says waiting for pipe at 6.33
INFO:simulation.simulator:REPEATER 0 Second Checkin finished:  6.72
INFO:simulation.simulator:REPEATER 0 upgrade started:  6.72
INFO:simulation.simulator:at time 6.72: GATEWAY 0 received message: REPEATER 0 says second_checkin set to TRUE at 6.72.
INFO:simulation.simulator:GATEWAY 0 says UPGRADE Starting at 6.72
INFO:simulation.simulator:GATEWAY 0 upgrade started:  6.72
INFO:simulation.simulator:REPEATER 0 upgrade finished: 7.95
INFO:simulation.simulator:REPEATER 0 Third Checkin started:  7.95
INFO:simulation.simulator:GATEWAY 0 upgrade finished: 10.83
INFO:simulation.simulator:GATEWAY 0 Third Checkin started:  10.83
INFO:simulation.simulator:GATEWAY 0 Third Checkin finished:  11.33
INFO:simulation.simulator:GATEWAY 0 says UPGRADE_COMPLETE set to TRUE at 11.33
INFO:simulation.simulator:GATEWAY 0 says waiting for pipe at 11.33
INFO:simulation.simulator:REPEATER 0 Third Checkin finished:  11.72
INFO:simulation.simulator:REPEATER 0 says UPGRADE_COMPLETE set to TRUE at 11.72
INFO:__main__:SIMULATION CYCLE :0 Total simulation Running_time :11.72


Total Simulation running time: 11.72

Gateway and Repeater checkin offset randomly generated here.
=======================================================================================


For Answers to the Questions. Kindly refer testcase.docx.

