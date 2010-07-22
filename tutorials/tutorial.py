class Tutorial:
    Name = ''
    Author = 'Devesh Yamparala <dev344@gmail.com>'
    Description = ''
    
    def __init__(self):
        pass

    def run(self):
        pass

    def cleanup(self):
        pass
        
class Error(Exception):
	def __init__(self, errorMessage):
		print errorMessage
 
