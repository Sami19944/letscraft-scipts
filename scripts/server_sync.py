import os
from shutil import copyfile

def server_sync(context, plugins):
	print("sync_server")
	server_folder = context.main_config['paths']['server_folder']
	print("   server_folder: " + server_folder)
	server_plugin_folder = server_folder + "plugins/"
	print("   server_plugin_folder: " + server_plugin_folder)
	plugin_folder = context.main_config['paths']['plugin_folder']
	print("   plugin_folder: " + plugin_folder)
	print("   plugins: " + str(plugins).strip('[]'))
	path = os.getcwd()
	print ("   *path: " + path)

	if not os.path.exists(server_plugin_folder):
	    os.makedirs(server_plugin_folder)

	for pl in plugins:
		src = plugin_folder + pl + ".jar"
		dst = server_plugin_folder + pl + ".jar"
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)