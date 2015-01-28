import sys
import os
import win32com.client

import win32com.client, sys, os

app = win32com.client.Dispatch("PowerPoint.Application")
app.Visible = True

names = []
for name in os.listdir(r'c:\tmp\pptx2pdf'):
    if name.endswith(('.ppt')): #or name.endswith('.pptx'):
        names.append(os.path.abspath(name))

# print os.listdir(r'c:\tmp\pptx2pdf')
print names
# presentation = app.Presentations.Open(names[0])
presentation = app.Presentations.Open(r'c:\tmp\pptx2pdf\1.ppt')
presentation.ExportAsFixedFormat('1.pdf', 'PpFixedFormatType')
presentation.ExportAsFixedFormat()

# HKEY_LOCAL_MACHINE\Software\Microsoft\Office\12.0\Registratio