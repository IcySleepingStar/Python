# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:23:15 2019

@author: adrie
"""

import tkinter as tk

root = tk.Tk()

text1 = tk.Label(root, text = "Tout corps à l'équilibre thermodynamique rayonne des ondes éléctromagnétiques.")

t1 = """A graphical user interface (GUI) is a type of user interface that allows users to interact 
with electronic devices in a graphical way, i.e. with images, 
rather than text commands. Originally interactive user interfaces 
to computers were not graphical, they were text oriented and usually 
consisted of commands, which had to be remembered. 
The DOS operating system from Microsoft and the Bourne shell 
under Linux are examples of such user-computer interfaces."""

text2 = tk.Label(root, justify = tk.LEFT, padx = 10, text = t1).pack(side = "left")

text1.pack(side = "right")

root.mainloop()