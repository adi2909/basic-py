#!/usr/bin/python2.7
import json
import string
import subprocess
import urllib2 

print '''
<html><head>Report</head>
<body>
<h1> Host Info </h1>
<table border="1">
'''

obj= urllib2.urlopen('http://audubon.smf1.twitter.com/mdb/api/server.json?')
all_hosts= json.load(obj)

#allocatedll_hosts = {}
#with open('allHostInfo.json', 'r') as fh:
#all_hosts = json.load(fh)
for mc in all_hosts:
		ip = all_hosts[mc]['facts']['ipaddress_prod']['server']
		kernel_info=all_hosts[mc]['attributes']['kernel']['role']
		burnstatus = all_hosts[mc]['attributes']['burnin_cpu']['server']
		if all_hosts[mc]['attributes'].has_key('bios_update_start'):
			bios_start = all_hosts[mc]['attributes']['bios_update_start']['server']
			if all_hosts[mc]['attributes'].has_key('bios_update_complete') :
				bios_end = all_hosts[mc]['attributes']['bios_update_complete']['server']
				#print "%s\t%s\t%s\t%s\t%s"	% (mc, ip, burnstatus,bios_start, bios_end)

				#My code here for HTML
				print "<tr>\n" +\
				"<td" + mc + "</td>\n" +\
				"<td" + ip + "</td>\n" +\
				"<td" + burnstatus + "</td>\n" +\
				"<td" + bios_start + "</td>\n" +\
				"<td" + bios_end + "</td>\n" +\
				"</tr>\n"
				
			else:
				#print "%s\t%s\t%s\t%s"	% (mc, ip, burnstatus,	bios_start)
				 print "<tr>\n" +\
                                "<td" + mc + "</td>\n" +\
                                "<td" + ip + "</td>\n" +\
                                "<td" + burnstatus + "</td>\n" +\
                                "<td" + bios_start + "</td>\n" +\
                                "</tr>\n"
		else:
			#print "%s\t%s\t%s"	% (mc, ip, burnstatus)
			print "<tr>\n" +\
                                "<td" + mc + "</td>\n" +\
                                "<td" + ip + "</td>\n" +\
                                "<td" + burnstatus + "</td>\n" +\
                                "</tr>\n"

print "</table>\n"
print "</body>\n"
print "</html>\n"
