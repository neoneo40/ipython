import sys
import os
import glob
import win32com.client
 
def convert(files, formatType = 32):
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    powerpoint.Visible = 1
    for filename in files:

        # print filename
        newname = os.path.splitext(filename)[0] + ".pdf"
        deck = powerpoint.Presentations.Open(filename)
        deck.SaveAs(newname, formatType)
        # deck.SaveAs(newname, 18)
        deck.Close()
    powerpoint.Quit()
 
files = glob.glob(os.path.join(sys.argv[1],"*.ppt"))
# files = ['c:\\tmp\\pptx2pdf\\1.ppt']
print files
convert(files)