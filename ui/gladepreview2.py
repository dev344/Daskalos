# ########################################################################################################################
# Date : 23rd July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################
"""
            This is the second window for Daskalos.
"""

import gtk, gobject
import sys, os

class DaskalosUI:

    tutorial_path = '/home/devesh/Desktop/Daskalos/tutorials'
    
    def main(self,args):
        gladeFile = args[0]
        builder = gtk.Builder()
        builder.add_from_file(gladeFile)
        signal_connections = { "on_start_tut_BTN_button_press_event" : self.func, 'on_searchbar_changed' : self.changed}
        builder.connect_signals( signal_connections )
        
        window = builder.get_object("mainwindow2")
        window.set_title("Daskalos")
        try:
            window.set_icon_from_file("Daskalos.jpg")
        except Exception, e:
            pass
        
        treeview1 = builder.get_object("treeview1")
        self.liststore = self.init_treeview(treeview1)
        treeview1.set_reorderable(False)
    
        searchbar = builder.get_object('searchbar')
        #window = filter( lambda o: isinstance(o,gtk.Window), builder.get_objects())[0]
        window.show_all()

        raw_input("Press any key to quit")
        
    def init_treeview(self, treeview1):
        """
            This function initializes the treeview by defining the columns,
            etc and returns the liststore defined.
        """
        cell0 = gtk.CellRendererText()
        col0 = gtk.TreeViewColumn("   Tutorials", cell0, text = 0)
        treeview1.append_column(col0)
        
        liststore = gtk.ListStore( gobject.TYPE_STRING)
        treeview1.set_model(liststore)
        
        return liststore
        
    def get_list_items(self, substring):
        """
            This function gets the list items every time someone searches.
            It searches the tutorials directory and checks if the searchword
            is there in the header or Description of tutorial file. 
        """
        sys.path.append(self.tutorial_path)
        for filename in os.listdir(self.tutorial_path):
            (shortname, extension) = os.path.splitext(filename)
            if (extension == '.py'):
                module = __import__(shortname)
                try:
                    if(substring in module.tutorial.header.lower()):
                        self.liststore.append([module.tutorial.header])
                except Exception, e:
                    pass
       
    def func(self,*args):
    	print "U've just pressed Start tutorial button.Sorry there are no tutorials yet."
    
    def changed(self, data):
        """
            This function clears the list first and then call a
            function to get ilst items.
        """
        self.liststore.clear()
        if (data.get_text() is not ''):
            self.get_list_items(data.get_text().lower())
        
    def destroy(self,widget, data = None):
    	gtk.main_quit()


daskalosUI = DaskalosUI()
    	
if __name__ == "__main__":
    import sys
    daskalosUI.main(sys.argv[1:])

