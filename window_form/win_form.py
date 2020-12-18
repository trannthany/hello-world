import clr #import the pythonnet library

# add reference for the 'System.Windows.Forms' namespace, the 'System.Reflection' namespace, and the 'System namespace
clr.AddReference('my-env/lib/python3.8/site-packages/clr/System.IO') # why it does not work?
clr.AddReference('System.Drawing')
clr.AddReference('System.Reflection')
clr.AddReference('System.Threading')
clr.AddReference('System.Windows.Forms')

#import all the namespaces.
import System
import System.IO
import System.Drawing
import System.Reflection
import System.Windows.Forms
from System.Threading import ApartmentState, Thread, ThreadStart

# Create our InteropExplorer Application Class Object
class InteropExplorer(System.Windows.Forms.Form):
    def __init__(self):
        #Define the caption text
        self.Text = "Interop Explorer"