#Created by Enzo Zanelato Rodrigues
#Leave yout coments on the project at the wiki on github 
# https://github.com/ezr1234/classifier/wiki
#Version = 2.0


import usexif
import datetime
import os
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
		date = [result.year,result.month]
		#Return the year
		return date
		
	#If the photo does not have a year it alerts the user and later moves it to a folder called No Year
	except Exception:
		print('Photo '+ file + ' does not have the date that it was taken')




#Gets the year and month of a JPG photo
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
		date = [date.year,date.month]
		return date

	#If the photo does not have a year it alerts the user and later moves it to a folder called No Year
	except Exception:
		print('Photo ' + file +' does not have the date that it was taken')




#Verifies the extension and sends the file to getDataJPG or getDataJPEG to get the year and month 
def filterPath(extension,file):
    if extension == "jpg" or extension == 'JPG':
        return getDataJPG(file)
    elif extension == "jpeg" or extension == "JPEG":
        return getDataJPEG(file)
    

#Function that moves the photos
def movePhoto(year,month):
    try:
		#Makes the directory year
        os.mkdir('./'+str(year))
		#Makes the subdirectory of year called month
        os.mkdir('./'+str(year)+'/'+str(month))
		#Moves the photo
        shutil.move(finfo, './'+str(year)+'/'+str(month))
    except Exception:
		#Moves the photo if the folder is already created 
        shutil.move(finfo, './'+str(year)+'/'+str(month))




diretorio = "."

#Opens the directory and list the files
pathitens = os.listdir(diretorio)

#Get the number of files in the folder
amount = int(len(pathitens))




for i in range(amount):

    finfo = pathitens[i]
    #Splits the file in the dots
    explod_file = finfo.split('.')
    #Only the extension of the file
    extension = explod_file[-1]
	
	#Sends the file to filterPath to verify if it is a JPG ou JPEG
    date = filterPath(extension,finfo)
	
	#Gets the results and then calls the function to move the photo
    if date != None: movePhoto(date[0],date[1])

    


print('Done')