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
import sys, os, subprocess, time

class DaskalosUI:

    tutorial_path = '/home/devesh/Desktop/Daskalos/tutorials/'
    images_path = '/home/devesh/Desktop/Daskalos/screenshots/'
    
    def main(self,args):
        gladeFile = args[0]
        builder = gtk.Builder()
        builder.add_from_file(gladeFile)
        signal_connections = { "on_start_tut_BTN_button_press_event" : self.func, 
                                'on_searchbar_changed' : self.searchbar_changed, 
                                "button-release-event" : self.run_tutorial,
                                'on_treeview1_cursor_changed' : self.cursor_changed, 
                                'on_stop_BTN_pressed' : self.on_stop_BTN_pressed,
                                'on_treeview_row_activated' : self.row_activated,
                                'on_back_BTN_clicked' : self.back_BTN_clicked,
                                'on_searchbar0_changed' : self.searchbar0_changed }
                                
        builder.connect_signals( signal_connections )
        
        self.window1 = builder.get_object("mainwindow1")
        self.window2 = builder.get_object("mainwindow2")
        self.window2.set_title("Daskalos")
        self.dialogbox = builder.get_object("dialogbox")
        try:
            self.window1.set_icon_from_file("Daskalos.jpg")
            self.window2.set_icon_from_file("Daskalos.jpg")
        except Exception, e:
            pass
        
        treeview = builder.get_object("treeview")
        treeview1 = builder.get_object("treeview1")
        self.liststore = self.init_treeview(treeview)
        self.liststore1 = self.init_treeview(treeview1)
        self.filenames = []
        self.get_list_items('', self.liststore)                    #initially lists all tutorials
        treeview1.set_reorderable(False)
        self.description_label = builder.get_object("description_label")
        self.tutorial_name_label = builder.get_object('tutorial_name_label')
        self.tutorial_name_label.set_label('Tutorial')
        self.author_name_label = builder.get_object('author_name_label')
        self.duration_label = builder.get_object('duration_label')
        
        self.start_tut_BTN = builder.get_object('start_tut_BTN')
        self.screenshot = builder.get_object('screenshot')
        
        searchbar = builder.get_object('searchbar')
        #window2 = filter( lambda o: isinstance(o,gtk.Window), builder.get_objects())[0]
        self.window1.show_all()

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
        
    def get_list_items(self, substring, liststore):
        """
            This function gets the list items every time someone searches.
            It searches the tutorials directory and checks if the searchword
            is there in the header or Description of tutorial file. 
        """
        sys.path.append(self.tutorial_path)
        for filename in os.listdir(self.tutorial_path):
            (shortname, extension) = os.path.splitext(filename)
            if (extension == '.py'):
                try:
                	module = __import__(shortname)
                except Exception, e:
                	print 'Error while importing ', shortname
                try:
                    if((substring in module.tutorial.header.lower()) or (substring in module.tutorial.tags.lower())):
                        liststore.append([module.tutorial.header])
                        if(liststore == self.liststore):
                            self.liststore1.append([module.tutorial.header])
                        self.filenames.append(shortname)
                except Exception, e:
                    pass
                #else :
                #    try:
                #       if(substring in module.tutorial.tags.lower()):
                #            liststore.append([module.tutorial.header])
                #            self.liststore1.append([module.tutorial.header])
                #            self.filenames.append(shortname)
                #    except Exception, e:
                #        pass
       
    def func(self, data1, data2):
        try:
    	    if self.selected_filename:
                self.window2.hide()
                self.dialogbox.show_all()
                time.sleep(5)
                self.dialogbox.set_keep_above(True)
        except Exception, e:
            pass
        print 'hello'
        time.sleep(3)
        print 'hello1'
        self.func1()
        #self.run_tutorial()
        #self.on_stop_BTN_pressed()
        
    	
    def row_activated(self, treeview, path, viewcolumn) :
        self.selected_filename = self.filenames[treeview.get_cursor()[0][0]]
        try :
            module = __import__(self.selected_filename)         
            self.description_label.set_label(module.tutorial.Description)
            self.tutorial_name_label.set_label(module.tutorial.header)
            self.author_name_label.set_label(module.tutorial.Author)
            self.duration_label.set_label(module.tutorial.duration)
        except Exception, e:
            print 'Unable to import ' + self.selected_filename
        try :
            screenshot_path = self.images_path + self.selected_filename + '_scaled.png'    
            self.screenshot.set_from_file(screenshot_path)
        except Exception, e:
            print 'Unable to get the screenshot ' + self.selected_filename + '_scaled.png'
        self.window1.hide()
        self.window2.show_all()
        #print 'a row has been activated', type(path)
        #print self.liststore[0].__str__()
        #print self.liststore[0].__getitem__(0)
   
    def func1(self):
        event = gtk.gdk.Event(gtk.gdk.BUTTON_RELEASE)
        event.button = 1
        self.start_tut_BTN.emit("button-release-event", event)
                
    def run_tutorial(self, data1, data2):
        time.sleep(2)
        print 'hello3'
        #args = 'python ' + self.tutorial_path + self.selected_filename + '.py'
        #p = subprocess.Popen(args,shell= True)               #will have to decide whether to remove this line of not
        #return_value = os.system(args)
        #time.sleep(2)
        #try :
        #    module = __import__(self.selected_filename)
        #    module.tutorial.run()
        #except Exception, e:
        #    pass
    
    def cursor_changed(self, treeview):
        """
            This function is called when one among the list is chosen.It then goes
            to the corresponding file and extracts the descripton from that file and 
            gets the respective screenshot also .
        """
        self.selected_filename = self.filenames[treeview.get_cursor()[0][0]]
        module = __import__(self.selected_filename)         #should include a try here
        self.description_label.set_label(module.tutorial.Description)
        self.tutorial_name_label.set_label(module.tutorial.header)
        try:
            self.author_name_label.set_label(module.tutorial.Author)
            self.duration_label.set_label(module.tutorial.duration)
        except Exception, e:
            pass
        screenshot_path = self.images_path + self.selected_filename + '_scaled.png'    # should include a try
        self.screenshot.set_from_file(screenshot_path)
        
    def searchbar_changed(self, data):
        """
            This function is called when searchbar is changed in window2.
            The function clears the list first and then calls a
            function to get list items.
        """
        self.liststore1.clear()
        self.filenames = []
        self.get_list_items(data.get_text().lower(), self.liststore1)
        
    def searchbar0_changed(self, data):
        """
            This function is called when searchbar is changed in window1.
            The function clears the list first and then calls a
            function to get list items.
        """
        self.liststore1.clear()
        self.liststore.clear()
        self.filenames = []
        self.get_list_items(data.get_text().lower(), self.liststore)
        
    def back_BTN_clicked(self, data):
        """
            This function is called when the back button in window2 is clicked.
            It hides window2 and shows window1
        """
        self.window2.hide()
        self.window1.show_all()
        
    def on_stop_BTN_pressed(self, data = None):
        self.dialogbox.hide()
        self.window2.show_all()
        
    def destroy(self,widget, data = None):
    	gtk.main_quit()


daskalosUI = DaskalosUI()
    	
if __name__ == "__main__":
    import sys
    daskalosUI.main(sys.argv[1:])

