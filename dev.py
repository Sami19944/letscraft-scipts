import sys
import os
import configparser
import subprocess
import logging

from scripts import clean
from scripts import update
from scripts import sync	
from scripts import init	
from scripts import server_start
from scripts import pipe
from scripts import status
from scripts import http_server

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
		# reload config
		self.config = configparser.ConfigParser()
		self.config.read(self.config_file)

		plugins = ['dev', 'network', 'clouddata']
		if(func == "help"):
			help()
		elif func == "update":
			update.update(self, plugins)
		elif func == "clean":
			clean.clean(self)
		elif func == "init":
			init.init(self)
		elif func == "sync":
			sync.sync(self, plugins)
		elif func == "status":
			status.status(self)
		elif func == "start":
			server_start.server_start(self)
		elif func == "httpserver":
			http_server.run(self)
		elif func == "reload":
			print("update then sync")
			self.command_handler("update")
			self.command_handler("sync")
			pipe.pipe(self, "reload")
			
		else:
			# invalid
			print("invalid command: " + func)
			help()
		print("finished")

def help():
	print("help")
	print("   env    : starts the enviroment")
	print("   update : updates cached jars")
	print("   clean  : cleans instance directory")
	print("   init   : inits server instances")
	print("   sync   : syncs server isntances")
	print("   status : shows overall status")
	
	print("   httpserver")

	print("   exit")

	print("   status <server> ")
	print("   start <server>")



def env(dev):
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


if __name__ == "__main__":
	print("letscraft-dev")
	path = sys.argv[0]

	# no arg
	if(len(sys.argv) <= 1):
		print("usage: dev.py <func>, try help")
		sys.exit()

	dev = Dev()

	func = sys.argv[1]

	# pre funcs
	if func == "env":
		env(dev)
	elif func == "version":
		print("not implemented yet")
	else:
		dev.command_handler(func)


