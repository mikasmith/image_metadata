#-------------------------------------------------------------------------------
# Name:             Program for Collecting Image Metadata
# Purpose:          This program is designed to capture information about an
#                   image, including it's ID, filename, title, owner, and
#                   licence type. It will then write this information to a csv
#                   file.
# Version History:  V1- Initial structuring of program.
#                   V2- Added write to csv functionality.
#                   V3-Added GUI.
#                   V4-Added dropdown menus for file extension and licence type. Added validation for unique image ID. Seperated owners first name and last name.
#                   V5- Changed design of GUI. Added a default value for the option menus and extra validation for them. Changed root window's colour and size.
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

import csv #imports the csv library
from tkinter import * #imports graphical user interface library
import tkinter.messagebox

class Image:

    def __init__(self, image_ID, filename, extension, title, fn_owner, ln_owner, licence):
        #intialise instance variables
        self.image_ID = image_ID #numeric and unique
        self.filename = filename
        self.extension= extension #file type
        self.title = title
        self.fn_owner = fn_owner #The first name of the owner of the image
        self.ln_owner= ln_owner #The last name. I chose to break these down to comply to 1NF.
        self.licence = licence #The type of licence the owner holds for the image.

    def get_image_ID(self): #defining a get function for each field allows me to get, or retrieve the data held within the variables later.
        return self.image_ID

    def get_filename(self):
        return self.filename

    def get_extension(self):
        return self.extension

    def get_title(self):
        return self.title

    def get_fn_owner(self):
        return self.fn_owner

    def get_ln_owner(self):
        return self.ln_owner

    def get_licence(self):
        return self.licence

class GUI: #This is the graphical user interface

    def __init__(self):
        window = Tk() #creating root window that everything is held in
        window.title("Image Metadata Entry") #Title for root window
        window.minsize(width=650, height=150) #setting size of root window
        window.configure(bg = "cornsilk")#configure overrides any of the previous construction options.
        label_font= ("Cambria", "11")

        self.ready_to_write = False #boolean logic.
        self.imagelist = [] #setting up a list to store records efficiently.

        button_help_label = Label(window, text='Press for help:', font =(label_font))
        button_help_label.pack() #.pack is the attribute needed to actually let the widget show on the GUI.
        button_help = Button(window, text="Help", command=self.doHelp) #Run the doHelp function
        button_help.pack()

        image_ID_label = Label(window, text='Enter Image ID:', font =(label_font), padx = 2, pady = 2)
        image_ID_label.pack()
        self.image_ID_field = Entry(window, bd=2)
        self.image_ID_field.pack()

        filename_label = Label(window, text='Enter Filename:', font =(label_font))
        filename_label.pack()
        self.filename_field = Entry(window, bd=2)
        self.filename_field.pack()

        extension_label = Label(window, text='Enter File Extension:', font =(label_font))
        extension_label.pack()
        self.extension_field = StringVar() #Declaring the variable class.
        extension_choices=['.jpg','.jpeg','.png','.gif'] #The options that will show in the menu.
        self.extension_field.set("Please select an option") #Sets the default.
        OptionMenu(window, self.extension_field, *extension_choices).pack() #I chose to use a drop down menu to ensure that the user inputs one of the options given and to make it impossible to enter anything different.

        title_label = Label(window, text='Enter Title:', font =(label_font))
        title_label.pack()
        self.title_field = Entry(window, bd=2)
        self.title_field.pack()

        owner_label = Label(window, text='Enter Owner:', font =(label_font))
        owner_label.pack()
        fn_owner_label = Label(window, text='First name:', font =(label_font))
        fn_owner_label.pack()
        self.fn_owner_field = Entry(window, bd=2)
        self.fn_owner_field.pack()
        ln_owner_label = Label(window, text='Surname:', font =(label_font))
        ln_owner_label.pack()
        self.ln_owner_field = Entry(window, bd=2)
        self.ln_owner_field.pack()

        licence_label = Label(window, text='Enter Licence Type:', font =(label_font))
        licence_label.pack()
        self.licence_field = StringVar()
        licence_choices= ["BY", "BY-ND", "BY-SA","BY-NC","BY-NC-ND","BY-NC-SA"]
        self.licence_field.set("Please select an option")
        OptionMenu(window, self.licence_field, *licence_choices).pack()

        button_validate_label = Label(window, text='Press to validate:', font =(label_font))
        button_validate = Button(window, text='Submit', command=self.doValidate) #Run the doValidate function
        button_validate_label.pack()
        button_validate.pack()

        button_csv_label = Label(window, text='Convert Record to csv', font =(label_font))
        button_csv = Button(window, text='Write to csv', command=self.doWrite) #Run the doWrite function
        button_csv_label.pack()
        button_csv.pack()

        window.mainloop() #This waits for user input before it does anything. Infinite loop.

    def doHelp(self): #This function will only be called if the user presses the help button.
        tkinter.messagebox.showinfo('Help','-The image ID must be a number and it must be unique. \n-Please enter your records one by one and validate each time. \n-Once you are finished adding records, click "Write to CSV". This will write the entered records to a text file. ')

    def doValidate(self):#callback method for submit button.
        #the following code ensures that the Image ID is unique.
        noduplicate = True;
        for image in self.imagelist:
            if self.image_ID_field.get() == image.get_image_ID(): #If image ID has already been entered, then the warning message will show.
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate Image ID. Please enter a unique integer.');
                print('Please enter a unique Image ID');


        if noduplicate == True:
            #validation to ensure that no fields are left empty
            if len(self.image_ID_field.get()) <1 or len(self.filename_field.get()) <1 or len(self.extension_field.get()) <1 or len(self.title_field.get()) <1 or len(self.fn_owner_field.get()) <1  or len(self.ln_owner_field.get()) <1 or len(self.licence_field.get()) <1 or self.licence_field.get() =="Please select an option" or self.extension_field.get() =="Please select an option":
                    tkinter.messagebox.showwarning('Warning!','Please do not leave values empty.')
            else:
                try:
                    validated_image_ID = int(self.image_ID_field.get())

                    self.imagelist.append(Image(self.image_ID_field.get(),self.filename_field.get(), self.extension_field.get(), self.title_field.get(), self.fn_owner_field.get(), self.ln_owner_field.get(),self.licence_field.get()))
                    self.ready_to_write= True
                    tkinter.messagebox.showinfo('Success!','Your submission has been sucessful.')

                    #The following code clears the input boxes to save time in clearing them manually.
                    self.image_ID_field.delete(0, END)
                    self.filename_field.delete(0, END)
                    self.title_field.delete(0, END)
                    self.fn_owner_field.delete(0, END)
                    self.ln_owner_field.delete(0, END)
                    self.licence_field.set("Please select an option")
                    self.extension_field.set("Please select an option")

                except:
                    tkinter.messagebox.showwarning('Warning!','Please enter a numeric value for Image ID.')
                    print('Please enter a numeric value for Image ID.')

    def doWrite(self):
        csv_name = 'imagedb.txt' #I chose to use a comma separated value file so that I could easily import it into a MySQL database.

        if self.ready_to_write: #This will only be true if the record has passed validation (numeric and unique Image ID, no empty values)
            ofile = open(csv_name, 'w') #Currently, I have my program set to overwrite the file with 'w'. I can choose to append the file with 'a'
            writer = csv.writer(ofile, delimiter=',')
            print("List of submitted images:")
            for image in self.imagelist: #runs through the list of records and writes them to a csv file.
                print("-"+str(image.get_filename())+str(image.get_extension()))
                writer.writerow([image.get_image_ID(),image.get_filename(), image.get_extension(), image.get_title(),image.get_fn_owner(), image.get_ln_owner(),image.get_licence()])
            ofile.close() #closes the csv file
            tkinter.messagebox.showinfo('Success!',csv_name+' has been generated successfully.')
        else:
            tkinter.messagebox.showwarning('Error!', 'Please validate your data before writing it to a csv file.')

        self.ready_to_write= False
GUI()
