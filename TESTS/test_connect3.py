{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf610
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0   1 from netmiko import ConnectHandler\
  2 from getpass import getpass\
  3\
  4 device1 = \{\
  5     "host": 'cisco1.lasthop.io',\
  6     "username": 'pyclass',\
  7     "password": getpass(),\
  8     "device_type": 'cisco_ios',\
  9     #"global_delay_factor": 2,\
 10 \}\
 11\
 12 net_connect = ConnectHandler(**device1)\
 13 print(net_connect.find_prompt())\
 14\
 15 output = net_connect.send_command("show ip int brief", delay_factor=4, max_loops=1000)\
 16 print(output)}