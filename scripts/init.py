import os
from shutil import copyfile
import configparser

def init(dev, name = 'server'):
	print("init")
	template_folder = dev.config['paths']['template_folder']
	server_folder = dev.config['paths']['server_folder']
	print("   template_folder: " + template_folder)
	print("   server_folder: " + server_folder)
	print("   instances: " + server_folder)
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
		template_files = os.listdir(template_folder)
		for file in template_files:
			src = template_folder + file
			dst = instance_folder + file
			print("      copy " + src + " -> " + dst)
			copyfile(src, dst)

		if not os.path.exists(server_folder):
			os.makedirs(server_folder)


		# set current workdir
		config_file = instance_folder + "server.conf"
		print("      *config_file: " + config_file)

		config = configparser.ConfigParser()
		config['server'] = {
			'instance_folder' : instance_folder,
			'pid': 0,
			'server_jar': 'spigot-1.14.2.jar'
		}
		with open(config_file, 'w') as configfile:
			config.write(configfile)
		