from netmiko import ConnectHandler
from getpass import getpass

	device1 = {
		"host": '',
		"username": '',
		"password": getpass(),
		"device_type": 'cisco_ios',
	#"session_log": 'my_session.txt' )
	}

	net_connect = ConnectHandler(**device1)
	print(net_connect.find_prompt())

	command = 'delete flash:/MATT_TEST_1.txt'
 	output = net_connect.send_command(command, expect_string=r'MATT_TEST_1.txt', strip_prompt=False, strip_command=False)
 	output += net_connect.send_command('\\n', expect_string=r'MATT_TEST_1.txt', strip_prompt=False, strip_command=False)
 	output += net_connect.send_command('\\n', strip_prompt=False, strip_command=False)
	print(output)}
