import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = [' ' + para.text for para in doc.paragraphs]
    return '\n\n'.join(fullText)