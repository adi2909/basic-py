import urllib2
import json
import string
import socket
import string
import subprocess
from multiprocessing import Pool
import argparse
from optparse import OptionParser

'''
#if __name__ == "__main__":
parser = argparse.ArgumentParser(description='Bonding info: report hosts that are not bonded')
parser.add_argument("-D", "--dc", action="store",help="Choose datacenter. Default is set = smf1. Current optiosn are : smf1, smfd, smfc, smfv, atla")
args  = parser.parse_args()

if args.infile == 'smf1':
	obj= urllib2.urlopen('http://audubon.smf1.twitter.com/mdb/api/server.json?')
elif args.infile == 'atla':
	obj= urllib2.urlopen('http://audubon.atla.twitter.com/mdb/api/server.json?')	
else:
	exit
'''

parser = OptionParser()
parser.add_option("-D","--Datcenter",help="select the datacenter")
(options, args) = parser.parse_args()

if args == 'smf1':
	obj= urllib2.urlopen('http://audubon.smf1.twitter.com/mdb/api/server.json?')
elif args == 'atla':
	obj= urllib2.urlopen('http://audubon.atla.twitter.com/mdb/api/server.json?')
elif args == 'smfd':
	obj= urllib2.urlopen('http://audubon.smfd.twitter.com/mdb/api/server.json?')
else:
	print " You did not enter a valid Datacenter "
	exit


def get_bonding_status(machine):
        try:
                data = urllib2.urlopen('http://%s:30000/system/network/if/eth0/bonding/status'%machine,timeout=2).read()
                bond_status = data.split(' ')[1].strip(',')
                if bond_status == '0':
                        print machine, bond_status
        except:
                print machine, 'Vex Exception'

white_list = ['undefined', 'hbase-v2-worker', 'hadoop', 'hadoop-dw-worker','mesos','cassandra.prod.cuckoo-minutely','manhattan.test.greenbean','hadoop-tst-worker','manhattan.prod.spare-d', 'cuckoo-cassandra','hadoop-exp2','mesos.multi.slave','cassandra.prod.cuckoo-minutely','ads-memcache','ads.memcache.staging','cassandra.prod.chubbysnipe','cassandra.prod.reserve','cassandra.prod.spare','cassandra.prod.spiderduck','cassandra.prod.tweetdeck','hadoop','hadoop-dw-worker','hadoop-photo-worker','hadoop-tst-worker','manhattan.prod.revenue','manhattan.prod.spare-d']

'''
All the URL's for different datcenters
 
obj= urllib2.urlopen('http://audubon.smf1.twitter.com/mdb/api/server.json?')
obj= urllib2.urlopen('http://audubon.atla.twitter.com/mdb/api/server.json?') 
obj= urllib2.urlopen('http://audubon.smfd.twitter.com/mdb/api/server.json?')
'''

#obj= urllib2.urlopen('http://audubon.atla.twitter.com/mdb/api/server.json?')

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
