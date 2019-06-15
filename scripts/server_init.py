import os
from shutil import copyfile
import configparser

def server_init(context):
	print("server_init")
	template_folder = context.main_config['paths']['template_folder']
	server_folder = context.main_config['paths']['server_folder']
	print("   template_folder: " + template_folder)
	print("   server_folder: " + server_folder)
	if not os.path.exists(server_folder):
		os.makedirs(server_folder)
	
	# copy template folder
	template_files = os.listdir(template_folder)
	for file in template_files:
		src = template_folder + file
		dst = server_folder + file
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)

	if not os.path.exists(server_folder):
		os.makedirs(server_folder)


	# set current workdir
	os.chdir(server_folder)
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
	