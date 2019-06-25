import os
import configparser
from shutil import copyfile

def sync(dev):
	print("sync")

	server_folder = dev.config['paths']['server_folder']
	plugin_folder = dev.config['paths']['plugin_folder']
	print("   server_folder: " + server_folder)
	print("   plugin_folder: " + plugin_folder)

	server_config = dev.servers_config

	repo_conf_file = "jars/repo.conf"
	print ("   repo_conf_file: " + repo_conf_file)
	repo_conf = configparser.ConfigParser()
	repo_conf.read(repo_conf_file)

	print("   servers")
	for server in server_config['servers']:
		print("      -" + server)
		if server_config.getboolean('servers', server, fallback=False):
			instance_folder = server_folder + server + "/"
			print("        instance_folder: " + instance_folder)
			server_group = server_config[server]['group']
			print("        server_group: " + server_group)
			# plugin folder
			server_plugin_folder = instance_folder + "plugins/"
			if not os.path.exists(server_plugin_folder):
				os.makedirs(server_plugin_folder)
			# plugins
			for file in os.listdir(plugin_folder):
				if file in repo_conf and 'group' in repo_conf[file]:
					jar_group = repo_conf.get(file, 'group')
				else:
					default_jar_group = dev.config['default']['group_plugin']
					jar_group = default_jar_group
				
				if server_group ==jar_group:
					print("      plugin: " + file)
					src = plugin_folder + file
					dst = server_plugin_folder + file
					copyfile(src, dst)