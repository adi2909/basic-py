#! /bin/sh

for line in `cat /home/aranjan/platform`;
	do
		for host in $(colony -z smf1 membersOf $line);

			 do
         			cql --dc smf1 -d 1 -T 360 "ts(SUM, system.network, $host, if/eth0/bonding/status)" ;
 			done

	done
