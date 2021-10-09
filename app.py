#idea: build an app to sign up for tests that takes 5 inputs: first name, last name, email,student ID, and a dropdown menu to select which test they are signing up for and when a button is pressed all of the information is stored in a table and all fields are wiped

#download pgAdmin? 

import tkinter as tk
from tkinter import messagebox
from tkinter import *

#create the window and set the size
win = tk.Tk() 
win.title("Student Registration Portal")
win.geometry("500x300")

#canvas = Canvas(win, width = 500, height =300)
#canvas.pack()
#create person class
class Person:
	def __init__(self,first,last):
		self._firstname = first
		self._lastname = last
	def getFirst(self):
		return self._firstname
	def getLast(self):
		return self._lastname
#create student class that inherits from person
class Student(Person):
	def __init__(self, first, last, email, ID, test):
		super().__init__(first, last)
		self.email = email
		self._ID = ID
		self.test = test
	def getID(self):
		return self._ID
#	def __str__(self):

#create all screens for which button you press
def screenACT():
	global x
	x = " the ACT!"
	destroyPage1()
	infoInput()
	global label2
	label2 = tk.Label(win, text = "Sign up for the ACT")
	label2.grid(row=1, column=1, padx = 10,pady=10)

def screenSAT():
	global x
	x = " the SAT!"
	destroyPage1()
	infoInput()
	global label2
	label2 = tk.Label(win, text = "Sign up for the SAT")
	label2.grid(row=1, column=1, padx=10,pady=10)

def screenRISE():
	global x
	x = " RISE testing!"
	destroyPage1()
	infoInput()
	global label2
	label2 = tk.Label(win, text = "Sign up for RISE testing")
	label2.grid(row=1,column = 1,padx=10,pady=10)

def destroyPage1():
	qTest.destroy()
	actBtn.destroy()
	satBtn.destroy() 
	riseBtn.destroy() 
	
def destroyPage2():
	label2.destroy()
	firstLabel.destroy()
	lastLabel.destroy()
	emailLabel.destroy()
	idLabel.destroy()
	firstText.destroy()
	lastText.destroy() 
	emailText.destroy() 
	idText.destroy() 
	saveBtn.destroy()
	backBtn.destroy()




#SCREEN NUMBER 1
def screenOne():
#label asking which test
	global qTest 
	qTest = tk.Label(win, text = "Which test would you like to take?")
	qTest.grid(row = 1, column = 2,padx = 10, pady = 10)
#buttons for each test
	global actBtn
	actBtn = tk.Button(win, text = "ACT", width =10, height = 2, command = screenACT)
	actBtn.grid(row = 2, column= 1, padx=10, pady=10 )

	global satBtn
	satBtn = tk.Button(win, text = "SAT", width =10, height = 2, command = screenSAT)
	satBtn.grid(row = 2, column= 2, padx=10, pady=10 )

	global riseBtn
	riseBtn = tk.Button(win, text = "RISE", width =10, height = 2, command = screenRISE)
	riseBtn.grid(row = 2, column= 3, padx=10, pady=10 )

def screenCongrats():
	#label saying thanks
	congratsLabel = tk.Label(win,text = "Thank you for signing up for" + x)
	congratsLabel.place(relx = .5, rely = .1, anchor = "center")
	#return home function and Button
	def returnHome():
		congratsLabel.destroy()
		rtnBtn.destroy() 
		endBtn.destroy()
		screenOne()
	rtnBtn = tk.Button(win, text = "Return Home",command=returnHome)
	rtnBtn.place(relx=.5,rely=.5,anchor="center")
	#end program button
	def endProgram():
		win.destroy()
	endBtn = tk.Button(win, text = "Exit",command=endProgram)
	endBtn.place(relx = .5, rely = .7, anchor = "center")	





def infoInput():
	global firstText, lastText, emailText,idText,firstLabel,lastLabel,emailLabel,idLabel,saveBtn, backBtn
	#create textboxes
	firstText = tk.Text(win,height=1,width=25,borderwidth = 3,relief = "groove")
	lastText = tk.Text(win,height=1,width=25,borderwidth = 3,relief = "groove")
	emailText = tk.Text(win,height=1,width=25,borderwidth = 3,relief = "groove")
	idText = tk.Text(win,height=1,width=25,borderwidth = 3,relief = "groove")
	##put textboxes on the grid
	firstText.grid(row=2,column=1,pady=10, padx = 5)
	lastText.grid(row=3,column=1,pady=10, padx = 5)
	emailText.grid(row=4,column=1,pady=10, padx = 5)
	idText.grid(row=5,column=1,pady=10, padx = 5)
	#create labels
	firstLabel = tk.Label(win,text="First Name")
	lastLabel = tk.Label(win,text="Last Name")
	emailLabel = tk.Label(win,text="Email")
	idLabel = tk.Label(win,text="ID")
	#place labels on the grid
	firstLabel.grid(row=2,column=0,pady=10,padx=0)
	lastLabel.grid(row=3,column=0,pady=10,padx=0)
	emailLabel.grid(row=4,column=0,pady=10,padx=0)
	idLabel.grid(row=5,column=0,pady=10,padx=0)

	def saveBtnClick():
	#this function will store all text boxes in a student class and wipe the text boxes
	
	#!!! create an if statement so that it shows an error if all boxes are not filled
	#create variables to store inputs
		fname = firstText.get('1.0',"end-1c")
		lname = lastText.get('1.0','end-1c')
		emailInput = emailText.get('1.0',"end-1c")
		idInput = idText.get('1.0','end-1c')

		if fname != "" and lname != "" and emailInput != "" and idInput != "":
		#create the student with the variables
			s = Student(fname, lname, emailInput, idInput, "bruh")

			#clear the textboxes
			firstText.delete("1.0","end-1c")
			lastText.delete("1.0","end-1c")
			emailText.delete("1.0","end-1c")
			idText.delete("1.0","end-1c")

			pushToTable(s)
			destroyPage2()
			screenCongrats()
		else:
			messagebox.showerror("Invalid Information","You need to enter all the required information.")

	#create the button that will clear all text boxes and store their values and push them to the table
	saveBtn = tk.Button(win,text="Submit",width=5,height=1,command=saveBtnClick)
	saveBtn.grid(row=5,column =3,padx=10,pady=10)
	def backBtnClick():
		destroyPage2()
		screenOne()
	#create a back button that will clear the screen and show screen 1
	backBtn = tk.Button (win,text = "Back",width=5,height=1,command=backBtnClick)
	backBtn.grid(row=6, column = 1, padx=10,pady=10)

s = Student("g","","","","")


#create button and put it on grid

def pushToTable(student):
	var = student.getFirst()
	car2 = student.getLast()
	print(car2)
	print(var)

screenOne()
win.mainloop()
