import os
from shutil import copyfile

def sync_jars(plugin_folder, plugins):
	print("sync_jars")
	print("   plugin_folder: " + plugin_folder)
	print("   plugins: " + str(plugins).strip('[]'))
	if not os.path.exists(plugin_folder):
	    os.makedirs(plugin_folder)
	# copy plugins
	for pl in plugins:
		src = "../letscraft-api/plugin_" + pl + "/target/" + pl + ".jar"
		dst = plugin_folder + pl + ".jar"
		print("   copy " + src + " -> " + dst)
		copyfile(src, dst)