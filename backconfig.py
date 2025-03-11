from netmiko import ConnectHandler
import threading
import os 
from datetime import datetime
from queue import Queue
from tkinter import messagebox

queue = Queue()

unreachbleDevice =[]

def back(device) :

	try : 
		print(f'[ + ]  Connected to device {device}  [ + ]')

	
		sshCli = ConnectHandler(
			device_type = 'cisco_ios',
			host =device,
			port = 22,
			username =  'admin',
			password =  'admin', 
			auth_timeout=60,
			                    ) 
		  

	

		
		hostname = sshCli.send_command('sh run | in hostname'  ,read_timeout=200).split()[1]
		hostname = sshCli.send_command('wr'  ,read_timeout=200)
		
		 

		if (os.path.isdir(f'{hostname}')) : 
			pass 
		else : 
			os.mkdir(hostname)
	 	

		backupdate = datetime.now().strftime("%d-%m-%Y") 
		
		if (os.path.isdir(f'{hostname}\\{backupdate}')) : 
			pass 
		else : 
			os.mkdir(f'{hostname}\\{backupdate}')

		running_config= sshCli.send_command('sh run ')
		startup_config= sshCli.send_command('more nvram:startup-config')

		with open(f'{hostname}\\{backupdate}\\running_config.cfg','w') as f : 
			f.write(running_config) 

		with open(f'{hostname}\\{backupdate}\\startup_config.cfg','w') as f : 
			f.write(startup_config) 

	except Exception as e : 

		unreachbleDevice.append(device)
		print(e)
 

def fill_queue(ips): 
	for device in ips : 
		queue.put(device) 

 

def worker() :
	while not queue.empty() : 
		device = queue.get() 
		back(device)
	 	

 
def startbackup(devices) :

	# port_list = range(1,1024) 

	fill_queue(devices)

	thread_list =[]
	 
	for t in range(len(devices)*5) :
		thread = threading.Thread(target=worker)
		thread_list.append(thread)


	for thread in thread_list : 
		thread.start() 

	for thread in thread_list : 
		thread.join()

def ListDevices() :
	global breakLoop
	try : 
		file = open('devices.txt','r')
		Switches = file.readlines()
		devices = [] 
		for i in Switches : 
			i = i.replace("\n","")
			devices.append(i)
	except Exception as e : 
		breakLoop =False
		messagebox.showerror('No devices List','There No Device List Created.\n\nPlease create a device list and name it devices.txt')
		pass 

	return devices


 


 
# here you can define the list of you network devices 

allDevices =["150.1.1.1","150.1.2.2","150.1.3.3","150.1.4.4","150.1.5.5","150.1.6.6","192.168.100.129","150.1.8.8","150.1.9.9","150.1.10.10"]


 
startbackup(allDevices)


 

 
	
