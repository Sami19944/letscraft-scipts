import os
import sys

def start():
	path = os.getcwd()
	print ("starting jar")
	print ("   path: " + path)
	launch = "java -Xms1024M -Xmx1024M -jar -DIReallyKnowWhatIAmDoingISwear ../jars/spigot-1.14.2.jar -o true"
	os.system(launch)
	
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print ("missing argument path")
		sys.exit()
	path = sys.argv[2]
	os.chdir(path)
	start()