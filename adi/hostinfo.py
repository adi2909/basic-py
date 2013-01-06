#!/usr/bin/env python
import json
import string
import subprocess


print '''
<html><head>Report</head>
<body>
<h1> Host Info </h1>
<table border="1">
'''

allocatedll_hosts = {}
with open('allHostInfo.json', 'r') as fh:
	all_hosts = json.load(fh)
	for mc in all_hosts:
		ip = all_hosts[mc]['facts']['ipaddress_prod']['server']
		kernel_info=all_hosts[mc]['attributes']['kernel']['role']
		burnstatus = all_hosts[mc]['attributes']['burnin_cpu']['server']
		if all_hosts[mc]['attributes'].has_key('bios_update_start'):
			bios_start = all_hosts[mc]['attributes']['bios_update_start']['server']
			if all_hosts[mc]['attributes'].has_key('bios_update_complete') :
				bios_end = all_hosts[mc]['attributes']['bios_update_complete']['server']
				print "%s\t%s\t%s\t%s\t%s\t%s"	% (mc, ip, burnstatus,bios_start, bios_end, kernel_info)
			else:
				print "%s\t%s\t%s\t%s\t%s"	% (mc, ip, burnstatus,	bios_start,kernel_info)
		else:
			print "%s\t%s\t%s\t%s"	% (mc, ip, burnstatus,kernel_info)
