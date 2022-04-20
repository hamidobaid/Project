from tkinter import *
root = Tk()
root.geometry("500x300") #Registration frame

def getvals():
    print("Accepted")

#Heading
Label(root, text="Python Registration form ", font="ar 15 bold").grid(row=0 , column=3)

#field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")


#packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)



#Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
checkvalue = IntVar

#creating entry field
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)

#packing Entry field
nameentry.grid(row=1 , column=3)
phoneentry.grid(row=2 , column=3)
genderentry.grid(row=3, column=3)


#Creating Check Box
checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

#Creating submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()