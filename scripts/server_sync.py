import os
from shutil import copyfile

def server_sync(dev, plugins, name='server'):
	print("sync_server")
	instance_folder = dev.config['paths']['server_folder'] + name + "/"
	print("   instance_folder: " + instance_folder)
	server_plugin_folder = instance_folder + "plugins/"
	plugin_folder = dev.config['paths']['plugin_folder']
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