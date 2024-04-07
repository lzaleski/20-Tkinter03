###############################################################################
# TODO: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk


form = tk.Tk()
form.title("Form")
form.columnconfigure([0,1,2,3], weight = 1, minsize=75)
form.rowconfigure([0,1,2], weight = 1, minsize=100)

nameFrame = tk.Frame(
    master = form,
    relief = tk.RAISED,
    borderwidth = 5
    )
nameFrame.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = "nsew")
name = tk.Label(
    master = nameFrame,
    text = "Name: ",
    bg = "white",
    fg = "black",
    width = 8
)
name.pack()
name_e = tk.Entry(master = nameFrame)

ad1Frame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
ad1Frame.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = "nsew")
addressLine1 = tk.Label(
    master = ad1Frame,
    text = "Address Line 1: ",
    bg = "black",
    fg = "white",
    width = 17
)
addressLine1.pack()
addressLine1_e =tk.Entry(master = ad1Frame)

ad2Frame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
ad2Frame.grid(row = 2, column = 0, padx = 0, pady = 0, sticky = "nsew")
addressLine2 = tk.Label(
    master = ad2Frame,
    text = "Address Line 2: ",
    bg = "white",
    fg = "black",
    width = 17
)
addressLine2.pack()
addressLine2_e =tk.Entry(master=ad2Frame)

cityFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
cityFrame.grid(row = 3, column = 0, padx = 0, pady = 0, sticky = "nsew")
city = tk.Label(
    master=cityFrame,
    text = "City: ",
    bg = "black",
    fg = "white",
    width = 6
)
city.pack()
city_e =tk.Entry(master=cityFrame)

stateFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
stateFrame.grid(row = 0, column = 1, padx = 0, pady = 0, sticky = "nsew")
state = tk.Label(
    master=stateFrame,
    text = "State: ",
    bg = "white",
    fg = "black",
    width = 7
)
state.pack()
state_e =tk.Entry(master=stateFrame)

zipFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
zipFrame.grid(row = 1, column = 1, padx = 0, pady = 0, sticky = "nsew")
zipCode = tk.Label(
    master=zipFrame,
    text = "Zip Code: ",
    bg = "black",
    fg = "white",
    width = 7
)
zipCode.pack()
zipCode_e =tk.Entry(master=zipFrame)

phoneFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
phoneFrame.grid(row = 2, column = 1, padx = 0, pady = 0, sticky = "nsew")
phoneNumber = tk.Label(
    master=phoneFrame,
    text = "Phone Number: ",
    bg = "white",
    fg = "black",
    width = 14
)
phoneNumber.pack()
phoneNumber_e =tk.Entry(master=phoneFrame)

emailFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
emailFrame.grid(row = 3, column = 1, padx = 0, pady = 0, sticky = "nsew")
emailAddress = tk.Label(
    master=emailFrame,
    text = "Email Address: ",
    bg = "black",
    fg = "white",
    width = 17
)
emailAddress.pack()
emailAddress_e =tk.Entry(master=emailFrame)

submitFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
submitFrame.grid(row = 0, column = 2, padx = 0, pady = 0, sticky = "nsew")
submit =tk.Button(
    master=submitFrame,
    text = "Submit",
    bg = "white",
    fg = "black"
)
submit.pack()



form.mainloop()

