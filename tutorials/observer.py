# ########################################################################################################################
# Date : 15th July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################



from dogtail.procedural import *

class Observer():
	def isFocussed(self, appName, trylimit = 30):
		attemptNum = 0
		while((not focus.application(appName))and(attemptNum<trylimit)):
			attemptNum +=  1
		if(attemptNum == trylimit): raise NameError ("Could not focus the application " + appName)
		else: return True
		
	def frameFocussed(self, frameName, trylimit = 3):
		print "focussing ", frameName                   #debug statement
		attemptNum = 0
		while((not focus.frame(frameName))and(attemptNum<trylimit)):
			attemptNum += 1
		if(attemptNum == trylimit): raise NameError ("Could not focus the frame " + frameName)
		else: return True
		
	def searchApp(self):
		"""Just an idea.Have to see if something comes out of it.
		"""
		# Synaptic = ('Sytem', 'Administration', 'Synaptic Package Manager')
		# Software Sources = ('Sytem', 'Administration', 'Software Souces')
		# Users and groups = ('Sytem', 'Administration', 'Users and Groups')
		# Time and Date = ('Sytem', 'Administration', 'Time and Date')
		# Startup Manger = ('Sytem', 'Administration', 'StartUp-Manager')
		# Login Screen = ('Sytem', 'Administration', 'Login Screen')
		# Network Tools = ('Sytem', 'Administration', 'Network Tools')
		# Firefox Web Browser = ('Applications', 'Internet' ,'Firefox Web Browser')
		# Gedit Text Editor = ('Applications', 'Accessories', 'gedit Text Editor')
		# Gvim Text Editor = ('Applications', 'Accessories', 'Gvim Text Editor')
		# Kate Text Editor = ('Applications', 'Accessories', 'Kate')
		# Gnome Terminal = ('Applications', 'Accessories', 'Terminal')
		pass
		
	def openWindow(self,*args):
		"""This functions should open the window of applications which are there in gnome panel
		"""
		if(not self.isFocussed('gnome-panel')): 
			raise NameError("Could not focus gnome-panel")

		click(args[0], roleName='menu')
		click(args[1], roleName='menu')
		click(args[2], roleName='menu item')
		
		
		
