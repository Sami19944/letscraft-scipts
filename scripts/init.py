import os
import configparser

from time import gmtime, strftime
from shutil import copyfile

def init(dev):
	print("init")
	server_folder = dev.config['paths']['server_folder']
	jar_folder = dev.config['paths']['jar_folder']
	print("   server_folder: " + server_folder)
	print("   jar_folder: " + server_folder)

	# instances
	print("   instances")
	for key in dev.servers_config['servers']:
		status = dev.servers_config.getboolean('servers', key, fallback=False)
		if status:
			server = key
			print("   - " + key)
			intance_folder = server_folder + server + "/"
			print("     intance_folder: " + intance_folder)
			# folder
			if not os.path.exists(intance_folder):
				os.makedirs(intance_folder)

			# config
			if not server in dev.servers_config:
				dev.servers_config.add_section(server)

			# server jar
			if 'server_jar' in dev.servers_config[server]:
				server_jar = dev.servers_config.get(server, 'server_jar')
				print("     server_jar: " + server_jar)
			else:
				server_jar = dev.config.get('default', 'server_jar')
				dev.servers_config.set(server, 'server_jar', server_jar)
				print("     server_jar (DEFAULT): " + server_jar)

			# group
			if 'group' in dev.servers_config[server]:
				group = dev.servers_config.get(server, 'group')
				print("     group: " + group)
			else:
				group = dev.config.get('default', 'group_server')
				dev.servers_config.set(server, 'group', group)
				print("     group (DEFAULT): " + group)

			# launch
			if 'launch' in dev.servers_config[server]:
				launch = dev.servers_config.get(server, 'launch')
				print("     launch: " + launch)
			else:
				launch = dev.config.get('default', 'launch')
				dev.servers_config.set(server, 'launch', launch)
				print("     launch (DEFAULT): " + launch)

			# template# copy template folder
			templates_folder = dev.config['paths']['templates_folder'] + group + "/"
			print("     templates_folder: " + templates_folder)
			if os.path.isdir(templates_folder):
				template_files = os.listdir(templates_folder)
				for file in template_files:
					src = templates_folder + file
					dst = intance_folder + file
					copyfile(src, dst)


			dev.servers_config.set('main', 'last_access', strftime("%Y-%m-%d %H:%M:%S", gmtime()))

		else:
			print("   - " + key + " DEAKTIVATED")

		with open(dev.servers_config_file, 'w') as configfile:
			dev.servers_config.write(configfile)
	return


	for instance in dev.config['instances']:
		deploy = dev.config['instances'][instance]
		print("      " + instance + ": deploy=" + deploy)

	for instance in dev.config['instances']:
		deploy = dev.config['instances'][instance]
		print("   init " + instance)
	
		instance_folder = server_folder + instance + "/"
		print("      instance_folder: " + instance_folder)

		if not os.path.exists(instance_folder):
			os.makedirs(instance_folder)
	
		# copy template folder
		template_files = os.listdir(templates_folder)
		for file in template_files:
			src = templates_folder + file
			dst = instance_folder + file
			print("      copy " + src + " -> " + dst)
			copyfile(src, dst)

		if not os.path.exists(server_folder):
			os.makedirs(server_folder)


		# set current workdir
		config_file = instance_folder + "server.conf"
		print("      *config_file: " + config_file)


		#import configparser
		#config = configparser.ConfigParser()
		#config['server'] = {
		#	'instance_folder' : instance_folder,
		#	'pid': 0,
		#	'server_jar': 'spigot-1.14.2.jar'
		#}
		with open(config_file, 'w') as configfile:
			config.write(configfile)
		