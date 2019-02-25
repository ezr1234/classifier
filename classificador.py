import usexif
import datetime
import os
import time
import exifread
import piexif
import shutil
from datetime import datetime




def getDataJPEG(file):
		#Get the metadata from FILE(photo)
		ret = usexif.fromfile(file)
		#Get the taken date from the photo
		result = ret['taken_date']
		#Get the year out of the date
		year = result.year
		#Return the year
		return year


def getDataJPG(file):
	#Load the file
	exif_dict = piexif.load(file)
	#Gets DateTimeOriginal from the Exif part
	taken_date = exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal]
	#Convertes de Byte result into a String one
	date = taken_date.decode("utf-8")
	#Convertes the string into a datetime
	date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
	#Gets the year out of the datetime
	return date.year
	




#Verify the extension of the file
def filterPath(pathitem):

	if pathitem == 'jpg' or pathitem == 'JPG':
		return 'jpg'
	else:
		if pathitem == 'jpeg' or pathitem == 'JPEG':
			return 'jpeg'

		else:
			return False


#Directory to work
diretorio = '.'

#Opens the directory and list the files
pathitens = os.listdir(diretorio)

#Get the number of files in the folder
amount = int(len(pathitens))

#Initiate variables for the whille loop
#Listitens is the variable that holds the verified itens
listitens = []
count = 0
year = []
#Loop that verifies the extension of the file
while count < amount:

	#Get the value in the pathitens list related to the count
	finfo = pathitens[count]
	# Explode o arquivo em cada ponto (.)
	explod_file = finfo.split('.')
	# Apenas o nome do arquivo
	only_name = '.'.join(explod_file[:-1])
	# Extensão do arquivo
	extension = explod_file[-1]

	#If the the extension is true then add it to the listitens list

	if filterPath(extension) == 'jpg':
		#Add File to an list
		listitens.append(finfo)
		#Gets the year of the photo
		yearphotoJPG = getDataJPG(finfo)
		#Appends the year to the list called YEAR
		year.append(yearphotoJPG)
		try:
			#Create de directory
			os.mkdir('./'+str(yearphotoJPG))
			#Moves the file to the directory
			shutil.move(finfo, './'+str(yearphotoJPG))
			#Adds 1 to the counter
			count += 1
		except Exception: 
			#Moves the file if the folder is already created
			shutil.move(finfo, './'+str(yearphotoJPG))
			#Adds 1 to the counter
			count += 1
			
	
	elif filterPath(extension) == 'jpeg':
		#Add File to an list
		listitens.append(finfo)
		#Gets the year of the photo
		yearphotoJPEG = getDataJPEG(finfo)
		#Appends the year to the list called YEAR
		year.append(yearphotoJPEG)
		try:
			#Create de directory
			os.mkdir('./'+str(yearphotoJPEG))
			#Moves the file )to the directory
			shutil.move(finfo, './'+str(yearphotoJPEG))
			#Adds 1 to the counter
			count += 1
		except Exception:
			#Moves the file if the folder is already created 
			shutil.move(finfo, './'+str(yearphotoJPEG))
			#Adds 1 to the counter
			count += 1
			
	else: 
		count += 1


print(listitens)
print(year)



	



