import glob, win32com.client, pythoncom
import os
import sys

# pptFiles = glob.glob(r'c:\tmp\pptx2pdf\*.ppt')
# pptFiles = [r'c:\tmp\pptx2pdf\1.ppt']
# print pptFiles

def convert(pptFiles):
    for pptFile in pptFiles:
        # print pptFile
        PPT=win32com.client.gencache.EnsureDispatch('powerpoint.application', 1)
        print 'Converting %s' % pptFile
        PPT.Visible = True
        #PPT.Activate()
        # presentation = PPT.Presentations.Open(pptFile, False, False, False)
        presentation = PPT.Presentations.Open(pptFile)
        # presentation.ExportAsFixedFormat(pptFile+'.pdf',
        #                                  win32com.client.constants.ppFixedFormatTypePDF,
        #                                  win32com.client.constants.ppFixedFormatIntentScreen,
        #                                  PrintRange=None)
        # presentation.ExportAsFixedFormat(pptFile+'.pdf',
        #                                 win32com.client.constants.ppFixedFormatTypePDF,
        #                                 win32com.client.constants.ppFixedFormatIntentScreen,
        #                                 PrintRange=None)
        presentation.ExportAsFixedFormat(pptFile + '.pdf', 2, 0, 0, 1, 1, False, 1, False, False, False,False)


files = glob.glob(os.path.join(sys.argv[1],"*.ppt"))
convert(files)