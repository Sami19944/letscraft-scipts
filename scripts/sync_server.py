import os
from shutil import copyfile

def sync_server(plugin_folder, server_folder, plugins):
	print("sync_server")
	server_plugin_folder = server_folder + "plugins/"
	if not os.path.exists(server_plugin_folder):
	    os.makedirs(server_plugin_folder)
	for pl in plugins:
		src = plugin_folder + pl + ".jar"
		dst = server_plugin_folder + pl + ".jar"
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)