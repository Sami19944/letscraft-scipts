import os
import sys
import subprocess
import configparser
import threading

def start_wait(context, launch):
	
	p = subprocess.Popen(
		launch,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT
	)

	context.p = p
	print ("--- context set")

	config_file = "server.conf"
	config = configparser.ConfigParser()
	config.read(config_file)
	
	# edid config begin
	pid = p.pid
	config['server']['pid'] = str(pid)
	print ("--- server pid: " + str(pid) + " started")
	with open(config_file, 'w') as configfile:
		config.write(configfile)

	p.wait()

	#log end
	pid = 0
	config['server']['pid'] = str(pid)
	with open(config_file, 'w') as configfile:
		config.write(configfile)
	
	print ("--- server pid: " + str(pid) + " exited")



def server_start(context):
	print ("server_start")
	server_folder = context.main_config['paths']['server_folder']
	print ("   server_folder: " + server_folder)

	os.chdir(server_folder)
	path = os.getcwd()
	print ("   *path: " + path)

	jar_folder = context.main_config['paths']['jar_folder']
	print ("   jar_folder: " + jar_folder)

	config_file = "server.conf"
	print ("   *config_file: " + config_file)
	config = configparser.ConfigParser()
	config.read(config_file)

	if len(config.sections()) == 0:
		print("   error: config error")
		return
	
	pid = config['server']['pid']
	print ("   *pid: " + pid)
	if( pid != "0"):
		print("   error: server is already running")
		return
	server_jar = "../" + jar_folder + config['server']['server_jar']
	print ("   *server_jar: " + server_jar)

	launch = 'java -Xms1024M -Xmx1024M -jar -DIReallyKnowWhatIAmDoingISwear <server_jar> -o true'
	launch = launch.replace("<server_jar>", server_jar)
	print ("   *launch: " + launch)

	launch_external = 'start /wait cmd /c "<launch>"'
	launch_external = launch_external.replace("<launch>", launch)
	print ("   *launch_external: " + launch_external)
	
	print("   launching")
	thread = threading.Thread(target = start_wait, args = (config, launch_external))
	thread.start()

