import os
import sys
import configparser
import subprocess

def pipe(dev, command, instance="server"):
	print ("server_pipe")
	instance_folder = dev.config['paths']['server_folder'] + instance + "/"
	print ("   instance_folder: " + instance_folder)