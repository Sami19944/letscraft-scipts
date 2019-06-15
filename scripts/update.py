import os
from shutil import copyfile

def update(context, plugins):
	print("update")
	target_folder =  context.main_config['paths']['plugin_folder']
	print("   target_folder: " + target_folder)
	print("   plugins: " + str(plugins).strip('[]'))
	if not os.path.exists(target_folder):
	    os.makedirs(target_folder)
	# copy plugins
	for pl in plugins:
		src = "../letscraft-api/plugin_" + pl + "/target/" + pl + ".jar"
		dst = target_folder + pl + ".jar"
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)