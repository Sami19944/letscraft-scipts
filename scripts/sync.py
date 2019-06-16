import os
from shutil import copyfile

def sync(dev, plugins, name='server'):
	print("sync")

	plugin_folder = dev.config['paths']['plugin_folder']
	print("   plugin_folder: " + plugin_folder)
	
	for instance in dev.config['instances']:
		deploy = dev.config['instances'][instance]
		print("   " + instance + ": deploy=" + deploy)
		
	for instance in dev.config['instances']:
		deploy = dev.config['instances'][instance]
		print("   sync " + instance)

		instance_folder = dev.config['paths']['server_folder'] + instance + "/"
		print("      instance_folder: " + instance_folder)
		server_plugin_folder = instance_folder + "plugins/"
		print("      plugins: " + str(plugins).strip('[]'))

		if not os.path.exists(server_plugin_folder):
			os.makedirs(server_plugin_folder)

		for pl in plugins:
			src = plugin_folder + pl + ".jar"
			dst = server_plugin_folder + pl + ".jar"
			print("      copy " + src + " -> " + dst)
			copyfile(src, dst)