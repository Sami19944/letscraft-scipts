import os
import sys
import configparser
import subprocess

def server_pipe(config, message):
	print ("server_pipe")
	server_folder = config['paths']['server_folder']
	print ("   server_folder: " + server_folder)

	os.chdir(server_folder)
	path = os.getcwd()
	print ("   *path: " + path)
	config_file = "server.conf"
	print ("   *config_file: " + config_file)

	config = configparser.ConfigParser()
	config.read(config_file)

	pid = int(config['server']['pid'])
	print ("   *pid: " + str(pid))
	if (str(pid) == "0"):
		print("   error: server not started")
		sys.exit()
