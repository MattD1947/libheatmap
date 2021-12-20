from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def create_rectangle(x1, y1, x2, y2, **kwargs):
	if 'alpha' in kwargs:
		alpha = int(kwargs.pop('alpha') * 255)
		fill = kwargs.pop('fill')
		fill = root.winfo_rgb(fill) + (alpha,)
		image = Image.new('RGBA', (x2-x1, y2-y1), fill)
		images.append(ImageTk.PhotoImage(image))
		canvas.create_image(x1, y1, image=images[-1], anchor='nw')
	canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

def displayMap():
#garbage collection deletes the actual image so it has to be global
	global convertedImage
#change the path later to make it universal
	loadImage = Image.open(r"C:\Users\mikel\Desktop\Library Calculator\Library Floor 1.png")
	loadImage = loadImage.resize((round(loadImage.size[0]*0.25), round(loadImage.size[1]*0.21)))
	convertedImage = ImageTk.PhotoImage(loadImage)
	canvas.create_image(0,0, image = convertedImage, anchor ='nw')

#create transparent rectangles
def yellow_rectangle():
	create_rectangle(50, 50, 250, 150, fill='yellow', alpha=.5)

def orange_rectangle():
	create_rectangle(50, 50, 250, 150, fill='orange', alpha=.5)

def red_rectangle():
	create_rectangle(50, 50, 250, 150, fill='red', alpha=.5)
#end of making rectangle

def newWindow():
	global canvas
	mapWindow = Toplevel()
	canvas = Canvas(mapWindow, width=1075, height= 800)
	canvas.pack()
	displayMap()
	
floor1dict = {
	"c1"    : 0, "c2"    : 0, "c3"   : 0, "c4"   : 0, "c5"   : 0,
	"c6"    : 0, "c7"    : 0, "c8"   : 0, "c9"   : 0, "c10"  : 0,
	"c11"   : 0, "c12"   : 0, "c13"  : 0,
	"t101"  : 0, "t102"  : 0, "t103" : 0, "t104" : 0, "t105" : 0,
	"t106"  : 0, "t107"  : 0, "t108" : 0, "t109" : 0, "t110" : 0,
	"t111"  : 0, "t112"  : 0, "t113" : 0, "t114" : 0, "t115" : 0,
	"t116"  : 0, "t117"  : 0, "t118" : 0, 
	"sr101" : 0, "sr102" : 0 }

floor2dict = {
	"t201"  : 0, "t202"  : 0, "t203"  : 0, "t204"  : 0, "t205"  : 0,
	"t206"  : 0, "t207"  : 0, "t208"  : 0, "t209"  : 0, "t210"  : 0,
	"t211"  : 0, "t212"  : 0, "t213"  : 0, "t214"  : 0, "t215"  : 0,
	"t216"  : 0, "t217"  : 0, "t218"  : 0, "t219"  : 0, "t220"  : 0,
	"t221"  : 0, "t222"  : 0, "t223"  : 0, "t224"  : 0, "t225"  : 0,
	"t226"  : 0,
	"cte1"  : 0, "cte2"  : 0,
	"c219"  : 0, "c221"  : 0, "c222"  : 0, "c225"  : 0, "c227"  : 0,
	"c229"  : 0,
	"sr201" : 0, "sr202" : 0, "sr206" : 0, "sr207" : 0, "sr213" : 0,
	"sr214" : 0, "sr215" : 0, "sr216" : 0 }

def updateFloor1(event=None):
	floor1dict[variable.get()] = int(selectedValueEntry.get())


root = Tk()
images = []
x= ''

optionLabel = Label(root, text='Choose location on Floor 1')
optionLabel.pack()

variable = StringVar(root)
variable.set('')
dropdown = ttk.Combobox(root, values=list(floor1dict.keys()), textvariable=variable)
dropdown.bind('<<ComboboxSelected>>', lambda event: selectedLabel.config(text=floor1dict[variable.get()]))
dropdown.pack()

notifyLabel = Label(root, text='Current number of students on Floor 1 is: ')
notifyLabel.pack()

selectedLabel = Label(root, text='')
selectedLabel.pack()

notifyChangeLabel = Label(root, text='Enter new number to change the current value: ')
notifyChangeLabel.pack()

selectedValueEntry = Entry(root)
selectedValueEntry.insert(0, x)
selectedValueEntry.bind('<Return>', updateFloor1)
selectedValueEntry.pack()

submitButton = Button(root, text='Submit Data', command=newWindow)
submitButton.pack()

root.mainloop()