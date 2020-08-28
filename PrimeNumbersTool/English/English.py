#!/usr/bin/python
# -*- coding: UTF-8 -*-
# It is a tool of PrimeNumbers. 
# You can use them everywhere.
# It is using tkinter on python 3.7.8.
# My name is Fang Weiwei.
# version 1.2
# 作者:方尉玮
# python3.7.8   tkinter
# 版本：1.2
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter as tkFont
from tkinter.filedialog import askdirectory
newlist = []

class GUI():
	
	# 计算质数
	def go(x):
		global newlist
		newlist = []
		some = 0
		for some_maths in x:
			for inlist_number in x:
				if some_maths % inlist_number == 0:
					some += 1
			if some == 1:
				newlist.append(some_maths)
			some = 0
	
	# print Prime Numbers table 
	def printing(x):
		print('---Prime Numbers table---')
		GUI.go(x)
		for a in newlist:
			print(a, end = " ")

	# write file
	def go_file(x, y):
		file1 = open(x + y + ".txt", 'w')
		file1.write('---Prime Numbers table---\n')
		soming = 0
		for b in newlist:
			file1.write(str(b))
			file1.write('\000\000\000\000\000')  # 5 spaces
			soming += 1
			if soming == 5:
				file1.write("\n")
				soming = 0
		file1.write("\n" + '--There are ' + str(len(newlist)) + ' numbers--')
		file1.close()
		print("Generate!")
		print("\n", "There are " + str(len(newlist)) + " numbers") # 统计
	
	# GUI
	def gui():
		global entry1, oldlist
		root = tk.Tk()  # ico
		root.title("PrimeNumbersTool")
		root.iconbitmap('.\\ico\\ico.ico')
		root.resizable(0, 0)
		label1 = tk.Label(root, text = "PrimeNumbersTool", font = ("微软雅黑", 25, 'bold'))  
		label1.pack()
		label2 = tk.Label(root, text = "Most of large Numbers in the selected range：", font = ("微软雅黑", 14))
		label2.pack()
		entry1 = tk.Entry(root, font = ("微软雅黑", 14))
		entry1.pack()
		label2 = tk.Label(root, text = 'Prime save table location', font = ("微软雅黑", 14))     
		label2.pack()
		def selectPath():
			global path1
			path1 = str(askdirectory())
			if path1[-1] == "/":
			    pass
			if path1[-1] == " ":
				del path1[-1]
			if path1[-1] != "/" and path1[-1] != " ":
				path1 += "/"
		Button(root, text = "Path selection", command = selectPath, font = ("微软雅黑", 14)).pack()
		label3 = tk.Label(root, text = 'File name：', font = ("微软雅黑", 14))
		label3.pack()
		entry3 = tk.Entry(root)
		entry3.pack()
		label4 = tk.Label(root, text = ".txt", font = ("微软雅黑", 14))
		label4.pack()
		def button1_c():  
			global oldlist
			newlist = []
			if entry1.get() == "":
				box31 = tk.messagebox.showwarning(title = 'Warning', message = "Please select range maximum number!")
			elif path1 == "":
				box32 = tk.messagebox.showwarning(title = 'Warning', message = "Please enter the path!")
			elif entry3.get() == "":
				box33 = tk.messagebox.showwarning(title = 'Warning', message = "Please enter the file name!")
			else:
			    box36 = tk.messagebox.showinfo(title = 'Prompt', message = 'Prime Numbers table has been generated!\nThe file is stored in' + str(path1))
			try:
			    oldlist = range(2, int(entry1.get()) + 1)
			    GUI.printing(oldlist)
			except:
				box34 = tk.messagebox.showwarning(title = 'Warning', message = "Please confirm whether within the scope of maximum number to an integer!")
			entry1.select_clear()
			newlist = []
			try:
			    global x,y
			    x = str(path1)
			    y = str(entry3.get())
			    GUI.go_file(str(path1), str(entry3.get()))
			except:
			    box35 = tk.messagebox.showwarning(title = "Warning", message = "Please make sure the path is correct!")
		button1 = tk.Button(root, text = "Generate", command = button1_c, width = 30, height = 2, font = ("微软雅黑", 18, "bold"))
		button1.pack()
		root.mainloop()


GUI.gui()