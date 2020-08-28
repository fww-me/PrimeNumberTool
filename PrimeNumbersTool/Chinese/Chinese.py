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
	
	# 打印质数表
	def printing(x):
		print('--------------质数表--------------')
		GUI.go(x)
		for a in newlist:
			print(a, end = " ")

	# 写入文件
	def go_file(x, y):
		file1 = open(x + y + ".txt", 'w')
		file1.write('--------------质数表--------------\n')
		soming = 0
		for b in newlist:
			file1.write(str(b))
			file1.write('\000\000\000\000\000')  # 用5个空格来区分
			soming += 1
			if soming == 5:
				file1.write("\n")
				soming = 0
		file1.write("\n" + '--------------共' + str(len(newlist)) + '个--------------')
		file1.close()
		print("已生成！")
		print("\n", "共" + str(len(newlist)) + "个") # 统计
	
	# GUI部分，开始建立图形化
	def gui():
		global entry1, oldlist
		root = tk.Tk()  # 设定图标，初始化
		root.title("质数生成器")
		root.iconbitmap('.\\ico\\ico.ico')
		root.resizable(0, 0)  # 限制窗口大小
		label1 = tk.Label(root, text = "质数生成器", font = ("微软雅黑", 25, 'bold'))  # 组件
		label1.pack()
		label2 = tk.Label(root, text = "选定范围内最大数：", font = ("微软雅黑", 14))
		label2.pack()
		entry1 = tk.Entry(root, font = ("微软雅黑", 14))
		entry1.pack()
		label2 = tk.Label(root, text = '质数表保存位置', font = ("微软雅黑", 14))     
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
		Button(root, text = "路径选择", command = selectPath, font = ("微软雅黑", 14)).pack()
		label3 = tk.Label(root, text = '文件名：', font = ("微软雅黑", 14))
		label3.pack()
		entry3 = tk.Entry(root)
		entry3.pack()
		label4 = tk.Label(root, text = ".txt", font = ("微软雅黑", 14))
		label4.pack()
		def button1_c():  # 按钮触发
			global oldlist
			newlist = []
			if entry1.get() == "":
				box31 = tk.messagebox.showwarning(title = '警告', message = "请选定范围内最大数！")
			elif path1 == "":
				box32 = tk.messagebox.showwarning(title = '警告', message = "请输入路径！")
			elif entry3.get() == "":
				box33 = tk.messagebox.showwarning(title = '警告', message = "请输入文件名！")
			else:
			    box36 = tk.messagebox.showinfo(title = '提示', message = '质数表已生成！\n文件存放在' + str(path1))
			try:
			    oldlist = range(2, int(entry1.get()) + 1)
			    GUI.printing(oldlist)
			except:
				box34 = tk.messagebox.showwarning(title = '警告', message = "请确认是否范围内最大数为整数！")
			entry1.select_clear()
			newlist = []
			try:
			    global x,y
			    x = str(path1)
			    y = str(entry3.get())
			    GUI.go_file(str(path1), str(entry3.get()))
			except:
			    box35 = tk.messagebox.showwarning(title = "警告", message = "请确认路径是否正确！")
		button1 = tk.Button(root, text = "生成", command = button1_c, width = 30, height = 2, font = ("微软雅黑", 18, "bold"))
		button1.pack()
		root.mainloop()


GUI.gui()