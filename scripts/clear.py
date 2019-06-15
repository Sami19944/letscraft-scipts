import os
import shutil

def clear(server_folder):
	print("clear")
	print("   server_folder: " + server_folder)
	if os.path.exists(server_folder):
		shutil.rmtree(server_folder) 
	os.makedirs(server_folder)