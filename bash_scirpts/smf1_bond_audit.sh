#! /bin/sh

rm  -f smf1_diff_hosts
rm  -f smf1_host_list

# check if CQL command is installed or not

x= 'which cql 2>/dev/null'
echo $x

if ["a$x"="a"]; then
        echo "CQL is installed"
else
        echo "CQL not found, Please install it from: http://confluence.smf1.twitter.com/display/OBSERVE/CQL"
fi



# Run the CQL Command to querry all the hosts in the fleet
# CQL can only be run from the CORPORATE BOX 

for line in `cat /home/aranjan/platform`;
	do
		for host in $(colony -z smf1 membersOf $line);

			 do
         			output= cql --dc smf1 -d 1 -T 360 "ts(SUM, system.network, $host, if/eth0/bonding/status)" ;
 			done

	done

cat output  | awk '/0.0$/{print $1}' | sort | uniq | sed -e 's,$,.prod.twitter.com,' >smf1_host_list


if [ "x$DEBUG" = "x" ]; then
	comm -2 -3 host_list smf1_bond_baseline.txt > smf1_diff_hosts     #baseline.txt is a masterfile of hosts from previous audits
	echo smf1_diff_hosts

