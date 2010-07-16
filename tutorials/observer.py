from dogtail.procedural import *

class Observer():
	def isFocussed(self, appName, trylimit = 30):
		attemptNum = 0
		while((not focus.application(appName))and(attemptNum<trylimit)):
			attemptNum += attemptNum
		if(attemptNum == trylimit): return False
		else: return True
		
