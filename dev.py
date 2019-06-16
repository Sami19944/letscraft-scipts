import sys
import os
import configparser
import subprocess
import logging

from scripts import clean
from scripts import update
from scripts import server_sync	
from scripts import init	
from scripts import server_start
from scripts import server_pipe
from scripts import status

from scripts import http_server

class Dev:

	def __init__(self):
		self.config_file = 'main.conf'	
		self.config = configparser.ConfigParser()
		self.config.read(self.config_file)
		self.instance_threads_size = 0
		self.instance_threads = {}

	# console stuff
	def command_handler(self, func):
		plugins = ['dev', 'network', 'clouddata']
		if(func == "help"):
			help()
		#elif func == "test":
		#	http_server.test()
		#elif func == "context":
		#	print ("context")
		elif func == "start":
			server_start.server_start(self)
		#elif func == "pipe":
		#	if(len(sys.argv) < 3):
		#		print("usage: dev_py pipe <message>")
		#	else:
		#		server_pipe.server_pipe(context, sys.argv[2])
		elif func == "clean":
			clean.clean(self)
		elif func == "update":
			update.update(self, plugins)
		elif func == "sync":
			server_sync.server_sync(self, plugins)
		elif func == "init":
			init.init(self)
		elif func == "init":
			init.init(self)
		elif func == "status":
			status.status(self)
		# shortcuts
		#elif func == "reload": # get the newest plugin jars
		#	command_handler("update")
		#	command_handler("sync")
		#	command_handler("start")
		#elif func == "restart": # get the newest plugin jars and start server
		#	command_handler("clean")
		#	command_handler("update")
		#	command_handler("sync")
		#	command_handler("start")
		else:
			# invalid
			print("invalid command: " + func)
			help()
		print("finished")

def help():
	print("help")
	print("   start <server>")
	print("   status <server>")
	print("   update")
	print("   context")
	print("   init")
	print("   sync_server")
	print("   clean")
	print("   reload")
	print("   restart")
	print("   exit")

if __name__ == "__main__":
	print("letscraft-dev")
	dev = Dev()

	path = sys.argv[0]
	# single command
	if(len(sys.argv) > 1):
		func = sys.argv[1]
		dev.command_handler(func)
	# start env
	else:
		print("console")
		is_running = True
		start_path = os.getcwd()

		while is_running:
			str = input(">> ")
			if(str == "exit"):
				is_running = False
			else:
				os.chdir(start_path)
				print("path: " + os.getcwd())
				dev.command_handler(str)
		print("bye")
		sys.exit()
