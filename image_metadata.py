#-------------------------------------------------------------------------------
# Name:             Program for Collecting Image Metadata
# Purpose:          This program is designed to capture information about an
#                   image, including it's ID, filename, title, owner, and
#                   license type. It will then write this information to a csv
#                   file.
# Version History:  V1- Initial structuring of program.
#                   V2- Added write to csv functionality.
#                   V3-Added GUI.
#                   V4-Added dropdown menus for file extension and licence type. Added validation for unique image ID.
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
from tkinter import *
import tkinter.messagebox

class Image:

    def __init__(self, image_ID, filename, extension, title, owner, licence):
        #intialise instance variables
        self.image_ID = image_ID
        self.filename = filename
        self.extension= extension
        self.title = title
        self.owner = owner
        self.licence = licence

    def get_image_ID(self):
        return self.image_ID

    def get_filename(self):
        return self.filename

    def get_extension(self):
        return self.extension

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

class GUI:

    def __init__(self):
        window = Tk()
        window.title("Image Metadata Entry")
        window.minsize(width=400, height=200)

        self.ready_to_write = False
        self.imagelist = []

        image_ID_label = Label(window, text='Enter Image ID:') #add to a list
        image_ID_label.pack()
        self.image_ID_field = Entry(window)
        self.image_ID_field.pack()

        filename_label = Label(window, text='Enter Filename:')
        filename_label.pack()
        self.filename_field = Entry(window)
        self.filename_field.pack()

        extension_label = Label(window, text='Enter File Extension:')
        extension_label.pack()
        self.extension_field = StringVar()
        extension_choices=['.jpg','.jpeg','.png','.gif']
        OptionMenu(window, self.extension_field, *extension_choices).pack()

        title_label = Label(window, text='Enter Title:')
        title_label.pack()
        self.title_field = Entry(window)
        self.title_field.pack()

        owner_label = Label(window, text='Enter Owner:')
        owner_label.pack()
        self.owner_field = Entry(window)
        self.owner_field.pack()

        licence_label = Label(window, text='Enter Licence Type:')
        licence_label.pack()
        self.licence_field = StringVar()
        licence_choices= ["BY", "BY-ND", "BY-SA","BY-NC","BY-NC-ND","BY-NC-SA"]
        OptionMenu(window, self.licence_field, *licence_choices).pack()

        button_validate_label = Label(window, text='Press to validate:')
        button_validate = Button(window, text='Submit', command=self.doSubmit)
        button_validate_label.pack()
        button_validate.pack()

        button_csv_label = Label(window, text='Convert Record to csv')
        button_csv = Button(window, text='write to csv', command=self.writetocsv)
        button_csv_label.pack()
        button_csv.pack()

        window.mainloop()

    def doSubmit(self):
        noduplicate = True;
        for image in self.imagelist:
            if self.image_ID_field.get() == image.get_image_ID():
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate Image ID');
                print('Please enter a unique Image ID');


        if noduplicate == True:
            if len(self.image_ID_field.get()) <1 or len(self.filename_field.get()) <1 or len(self.extension_field.get()) <1 or len(self.title_field.get()) <1 or len(self.owner_field.get()) <1  or len(self.licence_field.get()) <1 :
                    tkinter.messagebox.showwarning('Warning!','Please do not leave values empty.')
            else:
                try:
                    validated_image_ID = int(self.image_ID_field.get()) #not in ID_list

                    self.imagelist.append(Image(self.image_ID_field.get(),self.filename_field.get(), self.extension_field.get(), self.title_field.get(), self.owner_field.get(), self.licence_field.get()))
                    self.ready_to_write= True
                    tkinter.messagebox.showinfo('Success!','Your submission has been sucessful.')

                    #The following code clears the input boxes. Why did I choose to do this?
                    self.image_ID_field.delete(0, END)
                    self.filename_field.delete(0, END)
                    self.title_field.delete(0, END)
                    self.owner_field.delete(0, END)

                except:
                    tkinter.messagebox.showwarning('Warning!','Please enter a numeric value for Image ID.')
                    print('Please enter a numeric value for Image ID.')

    def writetocsv(self):
        csv_name = 'ITWORKED.txt'

        if self.ready_to_write:
            ofile = open(csv_name, 'w') #to overwrite the file use 'w' or to append to the file use 'a'
            writer = csv.writer(ofile, delimiter=',')
            for image in self.imagelist:
                writer.writerow([image.get_image_ID(),image.get_filename(), image.get_extension(), image.get_title(),image.get_owner(),image.get_licence()])
            ofile.close()
            tkinter.messagebox.showinfo('Success!',csv_name+' has been generated successfully.')
        else:
            tkinter.messagebox.showwarning('Error!', 'Please validate your data before writing it to a csv file.')

        self.ready_to_write= False

GUI()
