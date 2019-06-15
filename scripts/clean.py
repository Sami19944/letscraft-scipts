import os
import shutil

def clean(context):
	print("clean")
	target_folder = context.main_config['paths']['server_folder']
	print("   target_folder: " + target_folder)
	if os.path.exists(target_folder):
		shutil.rmtree(target_folder) 
	os.makedirs(target_folder)