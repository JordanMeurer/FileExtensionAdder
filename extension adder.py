import os


dirPath = input("Enter a path: ")
extension = input("Enter extension: ")
if(os.path.isdir(dirPath) == False):
	print("Not a path")
	exit
else:
	os.chdir(dirPath)
	check = input("Is %s the correct path? (y\\n): " %dirPath)
	for x in os.listdir(os.getcwd()):
		if(os.path.isfile(x)):
			os.rename(x, x + "." + extension)