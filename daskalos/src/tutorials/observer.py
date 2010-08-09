# ########################################################################################################################
# Date : 15th July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################
"""
		Here there are some functions which the tutorials of Daskalos use to run.Functions like focus.application,click etc
		are all part of dogtail.procedural module.
"""
import sys

try :
	from dogtail.procedural import *
except ImportError :
	print "dogtail doesn't seem to be installed.It is also important to have dogtail0.7.0 or above."
	sys.exit
	
import time

class Error(Exception):
	def __init__(self, errorMessage):
		print errorMessage
 

class Observer():
	def isFocussed(self, appName, trylimit = 30):
		attemptNum = 0
		while((not focus.application(appName))and(attemptNum<trylimit)):
			attemptNum +=  1
			time.sleep(1)
		if(attemptNum == trylimit): raise Error ("Could not focus the application " + appName)
		else: return True
		
	def frameFocussed(self, frameName, trylimit = 3):
		print "focussing ", frameName                   #debug statement
		attemptNum = 0
		while((not focus.frame(frameName))and(attemptNum<trylimit)):
			attemptNum += 1
			time.sleep(1)
		if(attemptNum == trylimit): raise Error ("Could not focus the frame " + frameName)
		else: return True
		 	
		
	def openWindowFromMenu(self,args):
		"""This functions should open the window of applications which are there in gnome panel
		"""
		if(not self.isFocussed('gnome-panel')): 
			raise Error("Could not focus gnome-panel")

		click(args[0], roleName='menu')
		click(args[1], roleName='menu')
		click(args[2], roleName='menu item')
	
	description = ["""Synaptic is a graphical package management tool which enables\n you to install, upgrade and remove software packages in a user\n friendly way.
				   """,
				   	'Software Sources',
				   	'Users and groups',
				   	'Time and Date' ,
				   	'Startup Manger',
				   	'Login Screen',
				   	'Network Tools',
				   	'Firefox Web Browser',
				   	'Gedit Text Editor',
				   	'Kate Text Editor',
				   	'Gnome Terminal']
				   
	dictionary = {'Synaptic Package Manager' : [('System', 'Administration', 'Synaptic Package Manager'), description[0]] ,
		 				'Software Sources' : [('System', 'Administration', 'Software Souces'), description[1]] ,
		 				'Users and groups' : [('System', 'Administration', 'Users and Groups'), description[2]] ,
		 				'Time and Date' : [('System', 'Administration', 'Time and Date'), description[3]] ,
		 				'Startup Manger' : [('System', 'Administration', 'StartUp-Manager'), description[4]] ,
		 				'Login Screen' : [('System', 'Administration', 'Login Screen'), description[5]] ,
		 				'Network Tools' : [('System', 'Administration', 'Network Tools'), description[6]] ,
		 				'Firefox Web Browser' : [('Applications', 'Internet' ,'Firefox Web Browser'), description[7]] ,
		 				'Gedit Text Editor' : [('Applications', 'Accessories', 'gedit Text Editor'), description[8]],
		 				'Kate Text Editor' : [('Applications', 'Accessories', 'Kate'), description[9]] ,
		 				'Gnome Terminal' : [('Applications', 'Accessories', 'Terminal'), description[10]] }
		 				
	
		
observer = Observer()	
