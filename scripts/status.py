def status(dev):
	print("status")
	print("   instances")
	for instance in dev.config['instances']:
		key = "instance." + instance
		pid = dev.config[key]['pid']
		print("      instance: " + instance)
		print("      pid: " + pid)
	print("   debug")
	