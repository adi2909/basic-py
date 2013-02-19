#! /usr/bin/python2.7

import urllib2
import json
import string
import socket
import string
import subprocess


obj= urllib2.urlopen('http://audubon.smf1.twitter.com/mdb/api/server.json?')

all_hosts= json.load(obj)


for mc in all_hosts:
	hostnames = all_hosts[mc]['facts']['hostname']['server']
	print hostnames
	try:
		bond_status= urllib2.urlopen('http://%s:30000/system/network/if/eth0/bonding/status'%hostnames,timeout=2).read()
		print bond_status
	except:
		print hostnames, 'FAIL'


