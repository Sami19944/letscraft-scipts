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

def sync_jars():
	if not os.path.exists(plugin_folder):
	    os.makedirs(plugin_folder)
	# copy plugins
	for pl in plugins:
		src = "../letscraft-api/plugin_" + pl + "/target/" + pl + ".jar"
		dst = plugin_cache + pl + ".jar"
		copyfile(src, dst)
		
def sync_server():
	path = "server/plugins/"
	if not os.path.exists(path):
	    os.makedirs(path)
	for pl in plugins:
		src = "jars/plugins/" + pl + ".jar"
		dst = path + pl + ".jar"
		copyfile(src, dst)

def clear():
	if os.path.exists(server_folder):
		shutil.rmtree(server_folder) 
	os.makedirs(server_folder)
	print("cleared: " + server_folder)
	
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
		print("copying server jar: " + src + " -> " + dst)
		copyfile(src, dst)

if __name__ == "__main__":
	clear()
	copy_template()
	sync_server()
