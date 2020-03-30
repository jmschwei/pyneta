from netmiko import ConnectHandler
from getpass import getpass

	device1 = {
		"host": 'cisco1.lasthop.io',
		"username": 'pyclass',
		"password": getpass(),
		"device_type": 'cisco_ios',
	}

	net_connect = ConnectHandler(**device1)
	print(net_connect.find_prompt())

	#cfg = [
	#    'no logging console',
	#    'logging buffered 10000',
	#    'clock timezone EST -5 0'
	#]
	#output = net_connect.send_config_set(cfg)
	output = net_connect.send_config_from_file(config_file='my_changes.txt')
	print(output)
