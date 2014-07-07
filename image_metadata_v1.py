#-------------------------------------------------------------------------------
# Name:             Program for Collecting Image Metadata
# Purpose:          This program is designed to capture information about an
#                   image, including it's ID, filename, title, owner, and
#                   license type. It will then write this information to a csv
#                   file.
# Version History:  V1- Initial structuring of program.
#                   V2- Added write to csv functionality.
# Author:           Mika Smith
#
# Created:          07/07/2014
# Copyright:        (c) Mika Smith 2014
# Licence:          <Creative Commons>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

import csv

class Image:

    def __init__(self, image_ID, filename, title, owner, licence):
        #intialise instance variables
        self.image_ID = image_ID
        self.filename = filename
        self.title = title
        self.owner= owner
        self.licence = licence

    def get_image_ID(self):
        return self.image_ID

    def get_filename(self):
        return self.filename

    def get_title(self):
        return self.title

    def get_owner(self):
        return self.owner

    def get_licence(self):
        return self.licence

    def display_info(self):
        print("Image ID:", image_ID)
        print("Filename:", filename)
        print("Title:", title)
        print("Owner:", owner)
        print("Licence:", licence)

def get_info():
    global image_ID
    global filename
    global title
    global owner
    global licence
    image_ID=int(input("What is the ID of the image?"))
    filename=input("What is the filename?")
    title=input("What is the title?")
    owner=input("Who is the owner?")
    licence=input("What is the licence type?")

if __name__ == '__main__':
    images=[]
    num_images=int(input("How many images are there?"))
    for i in range(num_images):
        get_info()
        images.append(Image(image_ID, filename, title,owner,licence))
    for image in images:
        image.display_info()

file_name = 'imagedb.txt'

ofile = open(file_name, 'a') #open with write('w') or append('a') privelages
writer = csv.writer(ofile, delimiter=',')
#cycles through list of records created by gui

for i in range (0, len(images)):
# the following code is used for debugging purposes
##    print(schools[i].school_name)
##    print(schools[i].roll_size)
##    print(schools[i].num_classrooms)

#we write the object contents out as a list... refer
#http://stackoverflow.com/questions/348196/creating-a-list-of-objects-in-python
    writer.writerow([image.get_image_ID(),image.get_filename(),image.get_title(),image.get_owner(),image.get_licence()])

#explicitly closes the output file
ofile.close()
