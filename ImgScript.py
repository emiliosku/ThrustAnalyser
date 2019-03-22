import os

begining = "program_files +=  [('"
ending = ", 'DATA')]"
with open("imgScanSpec.txt", "w" ) as textFile:
	path = os.path.join(os.getcwd(), "img\\")
	pathForPrint = path.replace("\\", "\\\\")
	for file in os.listdir(path):
		if file.endswith(".png"):
			fullPath = pathForPrint + file
			textFile.write( begining + file + "', '" + fullPath + "'" + ending + "\n")
	
		