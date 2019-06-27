import os
import sys
import subprocess
import threading
import configparser

from threading import Lock

def start_and_wait(dev, server_name, path, launch):
	server = server_name
	p = subprocess.Popen(
		launch,
		shell=True,
		stdin=subprocess.PIPE
	)
	pid = p.pid
	print ("[server_" + server_name + "] pid " + str(pid))
	print ("[server_" + server_name + "] server started ")

	# run config
	print ("[server_" + server_name + "] config start ")
	dev.run_config_mutex.acquire()
	if not server in dev.run_config:
		dev.run_config.add_section(server)
	dev.save_run_config()
	dev.run_config_mutex.release()
	print ("[server_" + server_name + "] config end ")


	p.wait()
	print ("[server_" + server_name + "] server exited ")


def start_all(dev):
	print ("start_all")

	# run config
	if not os.path.isfile('run.conf'):
		open('run.conf', "a+")

	servers_config = dev.servers_config
	
	for server in servers_config['servers']:
		# TODO if argument not working
		if servers_config['servers'][server]:
			print("- " + server)
			server_folder = dev.config['paths']['server_folder'] + server + "/"
			print("   server_folder: " + server_folder)
			jar_folder = dev.config['paths']['jar_folder']
			print("   jar_folder: " + jar_folder)

			server_jar = servers_config.get(server, 'server_jar')
			print("   server_jar: " + server_jar)
			launch = servers_config.get(server, 'launch')
			launch = launch.replace('<server_jar>', "../../" + jar_folder + server_jar)
			print("   launch: " + launch)
			launch_external = 'start /wait cmd /c "cd <server_folder> & <launch>"'
			launch_external = launch_external.replace("<launch>", launch)
			launch_external = launch_external.replace("<server_folder>", server_folder)
			print("   launch_external: " + launch_external)
			print("   launching")
			thread = threading.Thread(target = start_and_wait, args = (dev, server, server_folder, launch_external))
			thread.start()
		else:
			print("- " + server + "(turned off)")

	

