# This is the model part of the Model-View-Controller
# The class holds the name of a text file and its contents.
# Both the name and the contents can be modified in the GUI
# and updated through methods of this model.
# 

class Model:
    def __init__( self ):
        self.fileName = None
        self.fileContent = ""

    def isValid( self, fileName ):
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False

    def setFileName( self, fileName ):
        #Sets the member fileName to the value of the argument if the file exists
        if self.isValid( fileName ):
            self.fileName = fileName
            self.fileContents = open( fileName, 'r').read()
        else:
            self.fileContents = ""
            self.fileName = ""
            
    def getFileName( self ):
        #Returns the name of the file name member.
        return self.fileName

    def getFileContents( self ):
        #Returns the contents of the file if it exists, otherwise returns an empty string.
        return self.fileContents
    
    def writeDoc( self, text ):
        #Writes the string with name equal to the name of the file that was read + the suffix ".bak"
        if self.isValid( self.fileName ):
            fileName = self.fileName + ".bak"
            file = open( fileName, 'w' )
            file.write( text )
            file.close()