# ########################################################################################################################
# Date : 4th August 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################

"""
   		What the next few lines do : This code here is intended to use dogtail to press Alt+F2 and then tell how to run application.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

try :
	from tutorial import Tutorial
except ImportError :
	print 'Couldnot import tutorial.py'


class RunInstalledApp(Tutorial):
	
	header = 'How to run something which I just installed'
	
	Description = ''
	
	lines = ['To run something which you have just installed ',
			"\n- Press Alt + F2 keys together.",
			"\n- You will see a dialog box pop open with a searchbar in the center",
			"\n- Start typing the name of the application you have installed.",
			"\n- While you are typing,the name of the application might\n auto-complete on its own.",
			"\n- If it doesn't auto-complete then continue typing the\n whole name and then press enter or click run.",]
	
	for line in lines :
		Description = Description + line
	
	duration = '3-4 secs'
	
	DialogBox_label = ''
	
	tags = 'F2 alt search application '
	
	def __init__(self):
			self.part = self.run()
			
	def mainProgram(self):
		""" 
			dogtail modules are imported inside.
		"""
		
		from observer import Observer                             
		import dogtail.procedural
		import dogtail.rawinput
		
		observer = Observer()                              
		
		time.sleep(2)
		dogtail.procedural.keyCombo("<Alt>F2")

		
		
	def run(self):
		self.DialogBox_label = "Now enter your application's name and then\n press enter or click 'Run'"
		self.mainProgram()
		yield
		
tutorial = RunInstalledApp()

def main():
	import subprocess
	tutorial.mainProgram()
	
if __name__=='__main__' :
    main()
