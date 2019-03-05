#Created by Enzo Zanelato Rodrigues
#Leave yout coments on the project at the wiki on github 
# https://github.com/ezr1234/classifier/wiki
#Version = 1.0


import usexif
import datetime
import os
import time
import exifread
import piexif
import shutil
from datetime import datetime



#Get the year of the JPEG file 
def getDataJPEG(file):
	try:
		#Get the metadata from FILE(photo)
		ret = usexif.fromfile(file)
		#Get the taken date from the photo
		result = ret['taken_date']
		#Get the year out of the date
		year = result.year
		#Return the year
		return year
		
	#If the photo does not have a year it alerts the user and later moves it to a folder called No Year
	except Exception:
		print('Photo '+ file + ' does not have the date that it was taken')
		return 'No Year'



#Get the year of the JPG file
def getDataJPG(file):
	try:
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

	#If the photo does not have a year it alerts the user and later moves it to a folder called No Year
	except Exception:
		print('Photo ' + file +' does not have the date that it was taken')
		return 'No Year'
	


#Verify the extension of the file
def filterPath(pathitem):

	if pathitem == 'jpg' or pathitem == 'JPG':
		return 'jpg'
	else:
		if pathitem == 'jpeg' or pathitem == 'JPEG':
			return 'jpeg'

		else:
			return False



#List that holds the folders 
folders =[]

#Moves the photo to the correct folder 
def movePhoto():
	try:
		#Create de directory
		os.mkdir('./'+str(yearphoto))
		#Moves the file )to the directory
		shutil.move(finfo, './'+str(yearphoto))
	except Exception:
		#Moves the file if the folder is already created 
		shutil.move(finfo, './'+str(yearphoto))

    

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

#Main loop
#Splits the file to verify if it is valied
#Then calls movePhoto() to move the photo to the correct folder labeled with the year
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
		yearphoto = getDataJPG(finfo)
		#Appends the year to the list called YEAR
		year.append(yearphoto)

		movePhoto()

		count += 1
			
	
	elif filterPath(extension) == 'jpeg':
		#Add File to an list
		listitens.append(finfo)
		#Gets the year of the photo
		yearphoto = getDataJPEG(finfo)
		#Appends the year to the list called YEAR
		year.append(yearphoto)
		
		movePhoto()

		count += 1


	elif len(explod_file) == 1:
		count +=1
		folders.append(finfo)

	else: 
		count += 1







print(listitens)
print(year)
print(folders)

#Iniciate the counter of the loop
countfolders = 0

#Initiate the loop that verifies the existance of photos in the folders
while countfolders != len(folders):
	try:
		os.chdir(folders[countfolders])
		print(os.getcwd())
		countfolders +=1

	except Exception:
		print(folders[countfolders] + ' is not a directory')
		countfolders +=1



