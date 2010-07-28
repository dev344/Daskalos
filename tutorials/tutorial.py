class Tutorial:
    """
    	This should be the general structure of the tutorial.
    	mainProgram() should be the function inside which dogtail modules are imported
    """
    
    
    header = ''
    Author = 'Devesh Yamparala <dev344@gmail.com>'
    Description = ''
    duration = ''
    
    def __init__(self):
        pass
        
	def mainProgram(self):
		pass
		
    def run(self):
        pass

    def cleanup(self):
        pass
        
class Error(Exception):
	def __init__(self, errorMessage):
		print errorMessage
 
