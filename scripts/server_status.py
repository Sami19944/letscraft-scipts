import subprocess
import configparser
import os

def server_status(context):
	print ("server_status")
	server_folder = context.main_config['paths']['server_folder']
	print ("   server_folder: " + server_folder)

	os.chdir(server_folder)
	path = os.getcwd()
	print ("   *path: " + path)
	config_file = "server.conf"
	print ("   *config_file: " + config_file)

	config = configparser.ConfigParser()
	config.read(config_file)

	print ("   server_info")

	pid = int(config['server']['pid'])
	print ("   *pid: " + str(pid))

	server_jar = config['server']['server_jar']
	print ("   *server_jar: " + server_jar)

	