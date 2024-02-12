#!/bin/sh

string=$(ps -ef | grep 'newserv' | grep -v 'grep' | cut -f4 -d'/')



echo "Content-type: text/html"
echo


echo '<html> <head> <title> NEWSERV BB CONSOLE </title> <style> *{font-family: system-ui;color:#666666;margin:0px;padding:0px;text-align:center;user-select:none;} .online {color:green} .offline{color:#ff4500} </style> </head> <body>'

if [ "$string" = "newserv" ]; then
	echo "SHIP SERVER IS CURRENTLY: <span class='online'>ONLINE</span>"
else
	echo "SHIP SERVER IS CURRENTLY: <span class='offline'>OFFLINE</span>"
fi




