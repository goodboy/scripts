#!/usr/bin/perl

$busapi = `curl -s "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=ttc&r=224&s=5815"`;

if ($busapi =~ /minutes="(.+?)"/) {

	#if theres a bus in less than 10 minutes, pop up an xserver window to notify
	if ($1 < 10) {
		#exec("xmessage -display :0.0 -timeout 60 -geometry 400x150 \"Found a bus!! $1 minutes\"");
	}

	#print the time until a bus will arrive to stdout
	print "Bus arriving in $1 minutes\n";

}
