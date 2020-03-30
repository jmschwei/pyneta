from netmiko import ConnectHandler
from getpass import getpass

	device1 = {
		"host": 'cisco1.lasthop.io',
		"username": 'pyclass',
		"password": getpass(),
		"device_type": 'cisco_ios',
		#"global_delay_factor": 2,
		}

	net_connect = ConnectHandler(**device1)
	print(net_connect.find_prompt())

	output = net_connect.send_command("show ip int brief", delay_factor=4, max_loops=1000)
	print(output)}
