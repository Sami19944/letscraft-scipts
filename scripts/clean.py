import os
import shutil

def clean(dev):
	print("clean")
	target_folder = dev.config['paths']['server_folder']
	print("   target_folder: " + target_folder)
	if os.path.exists(target_folder):
		shutil.rmtree(target_folder) 
	os.makedirs(target_folder)