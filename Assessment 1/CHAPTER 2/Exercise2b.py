from tkinter import *

#Creating the main window
app = Tk()
app.title("Square Grid")

#With two frames—left and right—each with two labels, this code generates a Tkinter program
#The left frame contains the labels A and B, and the right frame contains the labels C and D
left_frame = Frame(app, relief=GROOVE, borderwidth=5)
left_frame.pack(side='left', expand=True, fill='both')

right_frame = Frame(app, relief=GROOVE, borderwidth=5)
right_frame.pack(side='right', expand=True, fill='both')

#Every label enlarges to occupy the available area inside its corresponding frame
label_a = Label(left_frame, text="A", width=12, bg='pink')
label_a.pack(side='top', expand=True, fill='both') #Aligning at the top, expand and fill available space

label_b = Label(left_frame, text="B", width=12, bg='white')
label_b.pack(side='bottom', expand=True, fill='both') #Aligning at the bottom, expand and fill available space

#Labels C and D inside the right frame
label_c = Label(right_frame, text="C", width=12, bg='white')
label_c.pack(side='top', expand=True, fill='both')  #Align at the top, expand and fill available space

label_d = Label(right_frame, text="D", width=12, bg='pink')
label_d.pack(side='bottom', expand=True, fill='both')  # Align at the bottom, expand and fill available space

app.geometry("300x200") #Setting the window size
app.mainloop() #The program is run by the main event loop (mainloop()), with the window size set to 300x200 pixels.