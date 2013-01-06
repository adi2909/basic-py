#!/usr/bin/env python
import json
import string
import subprocess
import argparse

allocatedll_hosts = {}


def load_allocated_hosts():
	#allocatedll_hosts = {}
	return true


def invalid_machine(node=None):
	#if allocatedll_hosts.has_key(node):
	# return true
	return None

	
parser = argparse.ArgumentParser(description='hostinfo: report hosts that are not fully used')
parser.add_argument('--infile', help='--input inputfile')
args = parser.parse_args()

load_allocated_hosts

if args.infile == None:
	exit

print '''
<html><head>
<title> HostInfo audit report </title>
<!-- READ UP ON CSS STYLING. -->
<style>
table {
  border: 1px;
  border-radius: 2px;
  padding: 25px;
  margin: 10px;
}
body {
    font: Verdana, Arial-Narrow;
    font-size: 11px;
}
th, td { margin: 2px; padding: 3px;}
th {
  background-color: #9aaaba;
  border-color: black;
}
tr:nth-child(even) { background: #dde; }
tr:nth-child(odd) { background: #ded; }
</style>
</head>
<body>
<h1> Host Info </h1>
<table border="1">
'''


#with open('allHostInfo.json', 'r') as file_handle:
with open(args.infile, 'r') as file_handle:
	all_hosts = json.load(file_handle)
  #
  # XXXXX: CHANGE THIS HEADER WHENEVER WE ADD/DROP FIELDS TO OUTPUT
  #
	print "<tr>\n<th>%s</th>\n<th>%s</th>\n<th>%s</th>\n<th>%s</th>\n<th>%s</th>\n" \
      %( 'Machine', 'IP', 'Burn_Status', 'BIOS start', 'BIOS end')
			
	for machine in all_hosts:
		if invalid_machine(machine):
			continue

		ip = all_hosts[machine]['facts']['ipaddress_prod']['server']
		#kernel_info=all_hosts[machine]['attributes']['kernel']['role']

		#every machine has this key. 
		burnstatus = all_hosts[machine]['attributes']['burnin_cpu']['server']
		#
		# some keys are not present for ALL machines in the json file.
		# make sure to check if the key exists. If not, don't store that value
		# 
		# optional value bios-start
		if all_hosts[machine]['attributes'].has_key('bios_update_start'):
			bios_start = all_hosts[machine]['attributes']['bios_update_start']['server']
		else:
			bios_start = 'undefined'

		if all_hosts[machine]['attributes'].has_key('bios_update_complete') :
			bios_end = all_hosts[machine]['attributes']['bios_update_complete']['server']
		else:
			bios_end = 'undefined'

		#My code here for HTML
		print "<tr>\n" + \
		"<td>" + machine + "</td>\n" + \
		"<td>" + ip + "</td>\n" + \
		"<td>" + burnstatus + "</td>\n" + \
		"<td>" + bios_start + "</td>\n" + \
		"<td>" + bios_end + "</td>\n" + "</tr>\n"
				
print '''
</table>
</body>
</html>
'''
