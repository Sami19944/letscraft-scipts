import sys
import os
import subprocess
import logging
import configparser

from threading import Lock

from scripts import clean
from scripts import update
from scripts import sync	
from scripts import init	
from scripts import server_start
from scripts import start_all
from scripts import pipe
from scripts import status
from scripts import http_server

from scripts import http_server

class Dev:

	def __init__(self):
		self.config_file = 'main.conf'	
		self.servers_config_file = 'servers.conf'
		self.run_config_file = 'run.conf'
		self.config = configparser.ConfigParser()
		self.config.read(self.config_file)
		self.servers_config = configparser.ConfigParser()
		self.servers_config.read(self.servers_config_file)
		self.run_config = configparser.ConfigParser()
		self.run_config.read(self.run_config_file)
		self.instance_threads_size = 0
		self.instance_threads = {}
		self.run_config_mutex = Lock()

	def save_config(self):
		with open(self.config_file, 'w') as configfile:
			self.config.write(configfile)
	def save_servers_config(self):
		with open(self.servers_config_file, 'w') as configfile:
			self.servers_config.write(configfile)
	def save_run_config(self):
		with open(self.run_config_file, 'w') as configfile:
			self.run_config.write(configfile)

	# console stuff
	def command_handler(self, func):
		# reload config
		import configparser
		self.config = configparser.ConfigParser()
		self.config.read(self.config_file)

		if(func == "help"):
			help()
		elif func == "update":
			update.update(self)
		elif func == "clean":
			clean.clean(self)
		elif func == "init":
			init.init(self)
		elif func == "sync":
			sync.sync(self)
		elif func == "status":
			status.status(self)
		elif func == "start":
			start_all.start_all(self)
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
	print("waiting for threads to exit")
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


