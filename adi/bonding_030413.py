import urllib2
import json
import string
import socket
import string
import subprocess
from multiprocessing import Pool
import argparse
from optparse import OptionParser

print '''
<html><head>Report</head>
<body>
<h1> Bonding Audit </h1>
<table border="1">
'''

# Specifying the Datacenter or the Zone withing a Particular DC

parser = argparse.ArgumentParser(description='Bonding info: report hosts that are not bonded')
parser.add_argument("-D", "--dc", action="store", help="Choose datacenter")
args  = parser.parse_args()

if args.dc == 'smf1':
	print " Host List "
	obj= urllib2.urlopen('http://audubon.smf1.twitter.com/mdb/api/server.json?')
elif args.dc == 'atla':
	print " Host List "
	obj= urllib2.urlopen('http://audubon.atla.twitter.com/mdb/api/server.json?')
elif args.dc == 'smfd':
	print " Host List "
	obj= urllib2.urlopen('http://audubon.smfd.twitter.com/mdb/api/server.json?')
elif args.dc == 'atlc':
	print " Host List "
	obj= urllib2.urlopen('http://audubon.atlc.twitter.com/mdb/api/server.json?')
elif args.dc == 'smfc':
	print " Host List "
	obj= urllib2.urlopen('http://audubon.smfc.twitter.com/mdb/api/server.json?')	
else:
	exit

#Function that gets the bond status:

def get_bonding_status(machine):
	try:
		data = urllib2.urlopen('http://%s:30000/system/network/if/eth0/bonding/status'%machine,timeout=2).read()
    		bond_status = data.split(' ')[1].strip(',')
    		if bond_status == '0':
    			#print machine, bond_status
			print "<tr>\n" + \
			"<td>" + machine + "</td>\n" + \
			"<td>" + "Unbonded" + "</td>\n"+ "</tr>\n"
  	except:
  		#print machine, 'Vex Exception'
		pass

# White-list roles that need to be excluded 

white_list = ['undefined', 'hbase-v2-worker', 'hadoop', 'hadoop-dw-worker','mesos','cassandra.prod.cuckoo-minutely','manhattan.test.greenbean','hadoop-tst-worker','manhattan.prod.spare-d', 'cuckoo-cassandra','hadoop-exp2','mesos.multi.slave','cassandra.prod.cuckoo-minutely','ads-memcache','ads.memcache.staging','cassandra.prod.chubbysnipe','cassandra.prod.reserve','cassandra.prod.spare','cassandra.prod.spiderduck','cassandra.prod.tweetdeck','hadoop','hadoop-dw-worker','hadoop-photo-worker','hadoop-tst-worker','manhattan.prod.revenue','manhattan.prod.spare-d']

# Parsing through Json

all_hosts= json.load(obj)
machines = []
for mc in all_hosts:
	if all_hosts[mc]['groups']['role'] not in white_list:
		try:
			if all_hosts[mc]['attributes']['unmonitored']['server'] !='9999999999':
 				machines.append(all_hosts[mc]['facts']['hostname']['server'])
		except:
			pass 			


pool = Pool(200)
 
pool.map(get_bonding_status, machines)

print "</table>\n"
print "</body>\n"
print "</html>\n"
