#!/usr/bin/python

import sys
import os
import shutil
from shutil import copyfile

# paths
server_folder = "server/"
plugin_folder = "jars/plugins/"
template_folder = "template/"
jar_folder = "jars/"

# config
plugins = ['dev', 'network', 'clouddata']

# letscraft-dev
def sync_jars():
	print("sync_jars")
	if not os.path.exists(plugin_folder):
	    os.makedirs(plugin_folder)
	# copy plugins
	for pl in plugins:
		src = "../letscraft-api/plugin_" + pl + "/target/" + pl + ".jar"
		dst = plugin_folder + pl + ".jar"
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)
		
def sync_server():
	path = "server/plugins/"
	if not os.path.exists(path):
	    os.makedirs(path)
	for pl in plugins:
		src = "jars/plugins/" + pl + ".jar"
		dst = path + pl + ".jar"
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)

def clear():
	print("clearing: " + server_folder)
	if os.path.exists(server_folder):
		shutil.rmtree(server_folder) 
	os.makedirs(server_folder)
	
def copy_template():
	if not os.path.exists(server_folder):
		os.makedirs(server_folder)
	
	# copy jar
	jar = "spigot-1.14.2.jar"
	src = jar_folder + jar
	dst = server_folder + jar
	print("copying server jar: " + src + " -> " + dst)
	copyfile(src, dst)
	
	# copy template folder
	template_files = os.listdir(template_folder)
	for file in template_files:
		src = template_folder + file
		dst = server_folder + file
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)

def start():
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
	path = sys.argv[0]
	print("letscraft-dev")
	if(len(sys.argv) < 2):
		print("missing argument function")
		printHelp()
		sys.exit()
	
	func = sys.argv[1]
	# sync_jars
	if func == "sync_jars":
		sync_jars()
		sys.exit()
	# sync_server
	if func == "sync_server":
		sync_server()
		sys.exit()
	# clear
	if func == "clear":
		clear()
		sys.exit()
	# copy_template
	if func == "copy_template":
		copy_template()
		sys.exit()
	if func == "start":
		start()
		sys.exit()
	if func == "update":
		sync_jars()
		sync_server()
		sys.exit()
	# invalid
	print("invalid command")
	printHelp()
	sys.exit()
	