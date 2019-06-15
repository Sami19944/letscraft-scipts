import sys
import os
import configparser
import subprocess

from scripts import clean
from scripts import update
from scripts import server_sync	
from scripts import server_init	
from scripts import server_start
from scripts import server_status
from scripts import server_pipe

class Context():
	def __init__(self, main_config_file, main_config, p):
		self.main_config_file = main_config_file
		self.main_config = main_config
		self.p = p
		self.last_func = "n/a"

# console stuff
def command_handler(context, func):
	if(func == "help"):
		help()
	elif func == "context":
		print ("context")
		print ("   main_config_file: " + context.main_config_file)
		print ("   last_func: " + context.last_func)
		print ("   p is None: " + str(context.p is None))


	elif func == "start":
		server_start.server_start(context)
	elif func == "status":
		server_status.server_status(context)
	elif func == "pipe":
		if(len(sys.argv) < 3):
			print("usage: dev_py pipe <message>")
		else:
			server_pipe.server_pipe(context, sys.argv[2])
	elif func == "clean":
		clean.clean(context)
	elif func == "update":
		update.update(context, plugins)
	elif func == "sync":
		server_sync.server_sync(context, plugins)
	elif func == "init":
		server_init.server_init(context)
	# shortcuts
	elif func == "reload": # get the newest plugin jars
		command_handler("update")
		command_handler("sync")
		command_handler("start")
	elif func == "restart": # get the newest plugin jars and start server
		command_handler("clean")
		command_handler("update")
		command_handler("sync")
		command_handler("start")
	else:
		# invalid
		print("invalid command: " + func)
		help()
		
	context.last_func = func
	print("finished")

def console_loop():
	is_running = True
	start_path = os.getcwd()
	
	config_file = 'main.conf'
	main_config = configparser.ConfigParser()
	main_config.read(config_file)
	global context
	context = Context(config_file, main_config, None)

	while is_running:
		str = input(">> ")
		if(str == "exit"):
			is_running = False
		else:
			os.chdir(start_path)
			print("path: " + os.getcwd())
			command_handler(context, str)
	print("bye")

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
	
	plugins = ['dev', 'network', 'clouddata']
	shell = 'cmd'
	# config end

	path = sys.argv[0]
	if(len(sys.argv) < 2):
		print("   console")
		console_loop()
		sys.exit()
	func = sys.argv[1]


	config_file = 'main.conf'
	main_config = configparser.ConfigParser()
	main_config.read(config_file)
	context = Context(config_file, main_config, None)

	command_handler(context, func)
	