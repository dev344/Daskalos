# Preview a glade file

import gtk, gobject
import sys, os

def main(args):
    gladeFile = args[0]
    builder = gtk.Builder()
    builder.add_from_file(gladeFile)
    builder.connect_signals({ "on_start_tut_BTN_button_press_event" : func})
    window = builder.get_object("mainwindow2")
    try:
        window.set_icon_from_file("web.jpg")
    except Exception, e:
        pass
    treeview1 = builder.get_object("treeview1")
    # add columns:
    C_DATA_COLUMN_NUMBER_IN_MODEL = 0
    cell0 = gtk.CellRendererText()
    col0 = gtk.TreeViewColumn("   Tutorials", cell0, text=C_DATA_COLUMN_NUMBER_IN_MODEL)
    treeview1.append_column(col0)
    liststore = gtk.ListStore( gobject.TYPE_STRING)
    tutorial_path = '/home/devesh/Desktop/Daskalos/tutorials'
    sys.path.append(tutorial_path)
    for filename in os.listdir(tutorial_path):
    	(shortname, extension) = os.path.splitext(filename)
    	if (extension == '.py'):
    		module = __import__(shortname)
    		try:
    			liststore.append([module.tutorial.header])
    		except Exception, e:
    			pass
    treeview1.set_model(liststore)
    # set reorderable
    treeview1.set_reorderable(True)

    #window.set_size_request(700,600)
    #window = filter( lambda o: isinstance(o,gtk.Window), builder.get_objects())[0]
    window.show_all()

    raw_input("Press any key to quit")
    
def func(*args):
	print "U've just pressed Start tutorial button.Sorry there are no tutorials yet."

def destroy(widget, data = None):
	gtk.main_quit()
	
if __name__ == "__main__":
    import sys
    main(sys.argv[1:])

