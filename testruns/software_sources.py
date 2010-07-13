import sys

def openWindow():
	#!/usr/bin/python
	from dogtail.procedural import *
	from dogtail.rawinput import doTypingDelay
	
	focus.application('gnome-panel')
	focus.frame('Top Expanded Edge Panel')
	click('System', roleName='menu')
	click('Administration', roleName='menu')
	click('Software Sources', roleName='menu item')
	doTypingDelay()
	doTypingDelay()
	doTypingDelay()
	doTypingDelay()
	doTypingDelay()

def main():
	import subprocess
	openWindow()
	args = 'cnee --replay --no-synchronise --file ' + sys.argv[1]
	p = subprocess.Popen(args,shell= True)
	print 'hello'
    
if __name__=='__main__' :
    main()
