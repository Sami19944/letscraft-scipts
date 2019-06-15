import sys

from scripts import clear
from scripts import sync_jars
from scripts import sync_server	
from scripts import copy_template	

def start():
	start_file = server_folder + "start_server.py"
	print("starting: " + start_file)
	if len(sys.argv) < 3:
		print("missing argument server_folder")
		sys.exit()
	execfile(server_folder + "start_server.py")

# console stuff
def printHelp():
	print("avaible functions:")
	print("   sync_jars")
	print("   sync_server")
	print("   clear")
	print("   copy_template")
	print("   start <server>")
	print("   update")

if __name__ == "__main__":

	# paths
	server_folder = "server/"
	plugin_folder = "jars/plugins/"
	template_folder = "template/"
	jar_folder = "jars/"
	
	# config
	plugins = ['dev', 'network', 'clouddata']
	shell = 'cmd'
	
	path = sys.argv[0]
	print("letscraft-dev")
	if(len(sys.argv) < 2):
		print("missing argument function")
		printHelp()
		sys.exit()
	
	func = sys.argv[1]
	
	if func == "clear":
		clear.clear(server_folder)
		sys.exit()
		
	if func == "sync_jars":
		sync_jars.sync_jars(plugin_folder, plugins)
		sys.exit()
		
	if func == "sync_server":
		sync_server.sync_server(plugin_folder, server_folder, plugins)
		sys.exit()
	
	
	if func == "copy_template":
		copy_template.copy_template(template_folder, jar_folder, server_folder)
		sys.exit()
	
	#if func == "start":
	#	start()
	#	sys.exit()
	# shortcuts
	
	if func == "reload":
		sync_jars.sync_jars(plugin_folder, plugins)
		sync_server.sync_server(plugin_folder, server_folder, plugins)
		sys.exit()
	
	if func == "restart":
		clear.clear(server_folder)
		copy_template.copy_template(template_folder, jar_folder, server_folder)
		sync_server.sync_server(plugin_folder, server_folder, plugins)
		
		sys.exit()
	
	# invalid
	print("invalid command: " + func)
	printHelp()
	sys.exit()
	