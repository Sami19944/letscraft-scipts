import os
import sys
import subprocess
import threading
import configparser

def start_wait(dev, launch):
	#server_folder = dev.config['paths']['server_folder']
	#print ("   server_folder: " + server_folder)

	p = subprocess.Popen(
		launch,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT
	)

	#dev.instance_threads[instance] = None

	print ("--- context set")

	#import configparser
	#config_file = "server.conf"
	#config = configparser.ConfigParser()
	#config.read(config_file)
	
	# edid config begin
	pid = p.pid
	#config['server']['pid'] = str(pid)
	print ("--- server pid: " + str(pid) + " started")
	#with open(config_file, 'w') as configfile:
	#	config.write(configfile)
	#
	#dev.instance_threads_size = dev.instance_threads_size + 1
	p.wait()
	#dev.instance_threads_size = dev.instance_threads_size - 1

	#log end
	#pid = 0
	#config['server']['pid'] = str(pid)
	#with open(config_file, 'w') as configfile:
	#	config.write(configfile)
	
	print ("--- server pid: " + str(pid) + " exited")



def server_start(dev):
	print ("server_start")

	default_server = dev.config["default"]["start"]
	server = default_server

	server_folder = dev.config['paths']['server_folder'] + server + "/"
	jar_folder = dev.config['paths']['jar_folder']
	print ("   server_folder: " + server_folder)
	print ("   jar_folder: " + jar_folder)

	os.chdir(server_folder)
	path = os.getcwd()
	print ("   *path: " + path)


	server_config_file = "server.conf"
	print ("   *server_config_file: " + server_config_file)
	server_config = configparser.ConfigParser()
	server_config.read(server_config_file)
	
	server_jar = dev.config['default']['server_jar']
		#pid = config['server']['pid']
	#print ("   *pid: " + pid)
	#if( pid != "0"):
	#	print("   error: server is already running")
	#	return
	server_jar_path = "../../" + jar_folder + server_jar
	print ("   *server_jar: " + server_jar)
	print ("   *server_jar_path: " + server_jar_path)

	launch = 'java -Xms1024M -Xmx1024M -jar -DIReallyKnowWhatIAmDoingISwear <server_jar_path> -o true'
	launch = launch.replace("<server_jar_path>", server_jar_path)
	print ("   *launch: " + launch)

	launch_external = 'start /wait cmd /c "<launch>"'
	launch_external = launch_external.replace("<launch>", launch)
	print ("   *launch_external: " + launch_external)
	
	print("   launching")
	thread = threading.Thread(target = start_wait, args = (dev, launch_external))
	thread.start()

