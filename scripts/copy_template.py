import os
from shutil import copyfile

def copy_template(template_folder, jar_folder, server_folder):
	print("copy_template")
	print("   template_folder: " + template_folder)
	print("   jar_folder: " + jar_folder)
	print("   server_folder: " + server_folder
	)
	if not os.path.exists(server_folder):
		os.makedirs(server_folder)
	
	# copy jar
	jar = "spigot-1.14.2.jar"
	src = jar_folder + jar
	dst = server_folder + jar
	print("   copying server jar: " + src + " -> " + dst)
	copyfile(src, dst)
	
	# copy template folder
	template_files = os.listdir(template_folder)
	for file in template_files:
		src = template_folder + file
		dst = server_folder + file
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)