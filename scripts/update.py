import os
import hashlib
import configparser
from time import gmtime, strftime

from shutil import copyfile

def update(dev):
	print("update")
	print("path:        " + os.getcwd())
	target_folder =  dev.config['paths']['jar_folder']
	print("   target_folder: " + target_folder)
	if not os.path.exists(target_folder):
	    os.makedirs(target_folder)
	
	# read repo config
	
	repo_config_file = target_folder + "repo.conf"
	print("   repo_config_file: " + repo_config_file)
	repo_config = configparser.ConfigParser()
	repo_config.read(repo_config_file)
	print("   checking plugins")

	plugin_folder = dev.config['paths']['plugin_folder']
	if not os.path.exists(plugin_folder):
	    os.makedirs(plugin_folder)

	plugins = repo_config.sections()

	for pl in plugins:
		parent = os.path.abspath(os.path.join('.', os.pardir))
		src = parent + "/letscraft-api/" + pl + "/target/" + pl + ".jar"
		dst = plugin_folder + pl + ".jar"
		section = pl

		src_chksm = "src_not_found"
		if os.path.isfile(src):
			src_chksm = md5(src)
		else:
			print("   - error: file " + src + " not found")
			continue

		if os.path.isfile(dst):
			conf_chksm = repo_config.get(section,  'md5', fallback="config_fallback_md5")
		else:
			conf_chksm = "file_not_found"

		if(src_chksm != conf_chksm):
			print("   update " + pl  + " " + dst)
			print("      repo_md5: " + conf_chksm + " src_chksm: " + src_chksm)
			copyfile(src, dst)
			if (section in repo_config) == False:
				repo_config[section] = {}
			repo_config.set(section, 'md5', src_chksm)
			repo_config.set(section, 'last_update', strftime("%Y-%m-%d %H:%M:%S", gmtime()))
		else:
			repo_config.set(section, 'last_check', strftime("%Y-%m-%d %H:%M:%S", gmtime()))
			print("   - no need to update " + pl  + " " + dst)
	with open(repo_config_file, 'w') as configfile:
		repo_config.write(configfile)

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()