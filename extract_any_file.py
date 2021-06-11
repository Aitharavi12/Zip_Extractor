from zipfile import ZipFile
name = r'C:/Users/aitha/Downloads/demo.zip'
with ZipFile(name,'r') as zip:
	zip.printdir()
	print("extracting.........")
	zip.extractall()
	print("done and njoy.")
