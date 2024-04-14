import shutil
import time
import os


while True:
	# check if there are USB drives mounted
	for usb in [f"/media/usb{i}/" for i in range(8)]:
		print("checking usb" + usb)
		# check if there is a file called "DIRECT.SSH" to flag the usb drive as a direct ssh prompt
		if not (os.path.isfile(usb + "DIRECT.SSH")):
			print("NO DIRECT SSH PROMPT")
			# if there is no file, continue with the next usb device
			continue
		# if there is such a file, continue
		# save netplan file name
		yaml_name = os.listdir("/etc/netplan")[0]
		# move current netplan .yaml to a safe copy
		print("moving netplans")
		os.rename("/etc/netplan/" + os.listdir("/etc/netplan")[0], os.listdir("/etc/netplan")[0] + ".temp")
		# copy direct ssh netplan .yaml to /etc/netplan/
		shutil.copy("direct_ssh.yaml", "/etc/netplan/" + yaml_name)
		# apply netplan
		print("applying netplan")
		os.system("netplan apply")
		# while the Direct SSH usb is still in, wait
		while (os.path.isfile(usb + "DIRECT.SSH")):
			print("waiting.............")
			time.sleep(2)
		# when the usb is disconnected, delete the direct SSH netplan conf
		print("removing direct ssh conf.....")
		os.remove("/etc/netplan/" + yaml_name)
		# move original yaml conf back
		os.rename(yaml_name + ".temp", "/etc/netplan/" + yaml_name)
		# apply netplan
		os.system("netplan apply")
	time.sleep(2)
