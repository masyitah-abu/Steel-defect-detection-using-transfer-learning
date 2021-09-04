from tensorflow.keras.models import load_model
from tkinter import filedialog
import tkinter as tk
import cv2
from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
import numpy as np
import time
import os
import uuid

class SignApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (HomePage, MenuPage, SignToTextPage, InstructionPage):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("HomePage")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()


class HomePage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.controller.title('Classification of Steel Defect')
		self.controller.state('zoomed')

		center_frame = tk.Frame(self)
		center_frame.pack(fill='x', side='top')

		firstphoto = ImageTk.PhotoImage(Image.open("C:/Users/masyi/Desktop/PHD/erekadramiza/st.png"))
		firstphoto_label = tk.Label(center_frame, image=firstphoto)
		firstphoto_label.pack()
		firstphoto_label.image = firstphoto

		heading_label = tk.Label(self,
		                         text='INTELLIGENT STEEL DEFECT INSPECTION',
		                         font=('destain alternative', 30,'bold'),
                                 bg='#bca0dc'
		                         )
		heading_label.pack(pady=30)

		heading1_label = tk.Label(self,
		                          text='DO YOU WANT TO START NOW?',
		                          font=('destain alternative', 20, 'italic'),bg='#bca0dc'
		                          )
		heading1_label.pack(pady=10)

		def yes():
			controller.show_frame('MenuPage')

		def no():
			controller.destroy()

		button_frame = tk.Frame(self, )
		button_frame.pack(fill='both', expand=True)

		no_button = tk.Button(button_frame,
		                      text='QUIT',
                          command=no,
		                      relief='raised',
		                      font=('Arial', 14),
		                      bg='#551a8b',foreground='white'
		                      )

		no_button.place(relx=0.30, rely=0.3, relwidth=0.1, relheight=0.3)

		yes_button = tk.Button(button_frame,
		                       text='LETS START',
		                       command=yes,
		                       relief='raised',
		                       font=('Arial', 14),
		                       bg='#551a8b',foreground='white'
		                       )

		yes_button.place(relx=0.60, rely=0.3, relwidth=0.1, relheight=0.3)
		self.config(bg="#bca0dc")
		center_frame.config(bg="#bca0dc")
		button_frame.config(bg="#bca0dc")


class MenuPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		center_frame = tk.Frame(self)
		center_frame.pack(fill='x', side='top')

		firstphoto = ImageTk.PhotoImage(Image.open("C:/Users/masyi/Desktop/PHD/erekadramiza/st.png"))
		firstphoto_label = tk.Label(center_frame, image=firstphoto)
		firstphoto_label.pack(side='top')
		firstphoto_label.image = firstphoto
		#firstphoto_label.place(relx = 0.5,rely = 0.5,anchor = 'center')

		button_frame = tk.Frame(self)
		button_frame.pack(fill='both', expand=True)
		button_frame.place(relx = 0.5,rely = 0.6,anchor = 'center')

		def home():
			controller.show_frame('HomePage')

		home_button = tk.Button(button_frame,
		                        text='HOME',
		                        command=home,
		                        relief='raised',
		                        font=14,
		                        bg='#551a8b',foreground='white',
		                        width=25,
		                        height=4)
		home_button.grid(pady=10, padx=600)

		def SignToText():
			controller.show_frame('SignToTextPage')

		stt_button = tk.Button(button_frame,
		                       text='STEEL DETECTION',
		                       command=SignToText,
		                       relief='raised',
		                       font=14,
		                       bg='#551a8b',foreground='white',
		                       width=25,
		                       height=4)
		stt_button.grid(pady=10, padx=600)

		self.config(bg="#bca0dc")
		center_frame.config(bg="#bca0dc")
		button_frame.config(bg="#bca0dc")
		button_frame.place(relx = 0.5,rely = 0.6,anchor = 'center')

class SignToTextPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		canvas = tk.Canvas(self, width = 400, height =400, bg='#bca0dc',highlightbackground='#bca0dc')
		canvas.pack()

		def select_image():
			global panelA, panelB
			path2 = filedialog.askopenfilename()
			image = cv2.imread(path2)
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
			image = cv2.resize (image,(224,224))
			image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			image = Image.fromarray(image)
			image2 = Image.fromarray(image2)
			image = ImageTk.PhotoImage(image)
			image2 = ImageTk.PhotoImage(image2)
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(padx=10, pady=10)
			#panelA.place(relx = 0.4,rely = 0.55,anchor = 'center')
			canvas.create_window(200, 150, window=panelA)

			model = load_model('C:/Users/masyi/Desktop/PHD/erekadramiza/steelmodel2.h5')
			img = cv2.imread(path2,cv2.IMREAD_GRAYSCALE)
			img = cv2.resize(img,(32,32))
			img = np.asarray(img,dtype=np.float32)/255.0 
			img = np.reshape(img,[1,32,32,1])

			pred =np.argmax(model.predict(img)[0])
			if pred == 0:
				my_text.insert(tk.INSERT,"crazing",'tag-center')
			elif pred == 1:
				my_text.insert(tk.INSERT,"rolled in scale",'tag-center')
			elif pred == 2:
				my_text.insert(tk.INSERT,"pitted surface",'tag-center')
			elif pred == 3:
				my_text.insert(tk.INSERT,"patches",'tag-center')
			elif pred == 4:
				my_text.insert(tk.INSERT,"inclusion",'tag-center')
			elif pred == 5:
				my_text.insert(tk.INSERT,"scratches",'tag-center')
			elif pred == 6:
				my_text.insert(tk.INSERT,"no_defect",'tag-center')

		def clear(): 
			my_text.delete('1.0', END)
			panelA.config(image='')

		def back():
			controller.show_frame('MenuPage')
		
		label = tk.Label(self, text="INSPECTION RESULT",font=('Helvetica', 13),justify='center',bg='#bca0dc')
		canvas.create_window(200, 330, window=label)
		my_text =tk.Text(self, width=30,height=1,font=("Helvetica", 13))
		my_text.tag_configure('tag-center', justify='center',relief = SUNKEN)
		my_text.pack(side="bottom")
		canvas.create_window(200, 355, window=my_text)

		button_frame = tk.Frame(self)
		button_frame.pack(fill='both', expand=True)
		image_button = tk.Button(button_frame,
		                       text='SELECT AN IMAGE',
		                       command=select_image,
                           relief='raised',
		                       font=14,
		                       bg='#551a8b',foreground='white',
		                       width=20,
		                       height=2)
		image_button.grid(pady=10, padx=600)
		clear_button = tk.Button(button_frame,
		                       text='CLEAR',
		                       command=clear,
                           relief='raised',
		                       font=14,
		                       bg='#551a8b',foreground='white',
		                       width=20,
		                       height=2)
		clear_button.grid(pady=10, padx=600)
		back_button = tk.Button(button_frame,
		                       text='BACK',
		                       command=back,
                           relief='raised',
		                       font=14,
		                       bg='#551a8b',foreground='white',
		                       width=20,
		                       height=2)
		back_button.grid(pady=10, padx=600)
		self.config(bg="#bca0dc")
		button_frame.config(bg="#bca0dc")
		button_frame.place(relx = 0.5,rely = 0.7,anchor = 'center')

class InstructionPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		heading_label = tk.Label(self,
		                         text='PLEASE READ THE INSTRUCTION CAREFULLY',
		                         font=('Times New Roman', 20),
		                         foreground='#663300'
		                         )
		heading_label.pack(pady=60)

		lower_frame = tk.Frame(self, bg='#80c1ff', bd=10)
		lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

		label = tk.Label(lower_frame, text="This is a system to detect steel defect in industry\n\n 1) There are four page in this system (home page, menu page, detection page, and instruction page)\n 2) HOME PAGE >> consist two button\n\t a) QUIT = to quit interface\n\t b) LETS START = to enter menu page\n 3) MENU PAGE >> consist three button\n\t a) BACK = to back to home page\n\t b) STEEL DEFECT = to enter steel detection system\n\t c) INSTRUCTION = to enter instruction page\n 4) SYSTEM PAGE >> consist three button\n\t a) SELECT AN IMAGE = to select steel image for detection\n\t b) BACK = back to menu page\n\t c) CLEAR = to clear all input in system page\n",font=('Times New Roman', 13),justify='left')
		label.place(relwidth=1, relheight=1)

		def back():
			controller.show_frame('MenuPage')

		button_frame = tk.Frame(self)
		button_frame.place(relx=0.4, rely=0.86)
		#button_frame.pack(fill='both', expand=True)
		back_button = tk.Button(button_frame,
		                       text='BACK',
		                       command=back,
                           relief='raised',
		                       font=14,
		                       bg='#551a8b',foreground='white',
		                       width=15,
		                       height=2)
		back_button.grid(pady=10, padx=600)
		self.config(bg="#bca0dc")
		button_frame.config(bg="#bca0dc")

if __name__ == "__main__":
	app = SignApp()
	app.mainloop()
