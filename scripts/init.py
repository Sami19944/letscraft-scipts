import os
from shutil import copyfile
import configparser

def init(dev, name = 'server'):
	print("init")
	template_folder = dev.config['paths']['template_folder']
	server_folder = dev.config['paths']['server_folder']
	print("   template_folder: " + template_folder)
	print("   server_folder: " + server_folder)
	instance_folder = server_folder + name + "/"
	print("   instance_folder: " + instance_folder)

	if not os.path.exists(instance_folder):
		os.makedirs(instance_folder)
	
	# copy template folder
	template_files = os.listdir(template_folder)
	for file in template_files:
		src = template_folder + file
		dst = instance_folder + file
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)

	if not os.path.exists(server_folder):
		os.makedirs(server_folder)


	# set current workdir
	os.chdir(instance_folder)
	path = os.getcwd()
	print("   *path: " + path)
	config_file = "server.conf"
	print("   *config_file: " + config_file)

	config = configparser.ConfigParser()
	config['server'] = {
		'server_folder' : server_folder,
		'pid': 0,
		'server_jar': 'spigot-1.14.2.jar'
	}
	with open(config_file, 'w') as configfile:
		config.write(configfile)
	