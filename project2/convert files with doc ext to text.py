# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 11:32:25 2016

@author: jdweaver
"""
import pandas as pd
import numpy as np
import scipy as sp
import os
import hashlib
#import the packages we need to convert PDFs to text
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import fnmatch, os, pythoncom, sys, win32com.client
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
#fyi need to specifically install textblob via anaconda: 
#conda install -c https://conda.anaconda.org/sursma textblob
#don't use the most recent version due to conflicts
from textblob import TextBlob, Word
from nltk.stem.snowball import SnowballStemmer
%matplotlib inline    

for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

'''
Number of .doc texts = 290 
Number of .docx texts = 483
Number of .pdf texts = 80
''' 

count = 0
for (dirname, dirs, files) in os.walk(".", topdown=True):
   for filename in files:
       if filename.endswith('.pdf') :
           count = count + 1
print 'Files:', count


'''
convert all .doc files into .txt files
reference: https://www.safaribooksonline.com/library/view/python-cookbook-2nd/0596007973/ch02s28.html
1 file deleted due to security issues with the word doc
1 file deleted due to it not being english
'''
wordapp = win32com.client.gencache.EnsureDispatch("Word.Application")
try:
    for path, dirs, files in os.walk(".", topdown=True):
        for filename in files:
            if not fnmatch.fnmatch(filename, '*.doc'): continue
            doc = os.path.abspath(os.path.join(path, filename))
            print "processing %s" % doc
            wordapp.Documents.Open(doc)
            docastxt = doc[:-3] + 'txt'
            wordapp.ActiveDocument.SaveAs(docastxt,
                FileFormat=win32com.client.constants.wdFormatText)
            wordapp.ActiveDocument.Close( )
finally:
    # ensure Word is properly shut down even if we get an exception
    wordapp.Quit( )

'''
convert all .docx files into .txt files, change the -3 to -4 so file extension works
#10 files had to be deleted because it was corrupted
'''
wordapp = win32com.client.gencache.EnsureDispatch("Word.Application")
try:
    for path, dirs, files in os.walk(".", topdown=True):
        for filename in files:
            if not fnmatch.fnmatch(filename, '*.docx'): continue
            doc = os.path.abspath(os.path.join(path, filename))
            print "processing %s" % doc
            wordapp.Documents.Open(doc)
            docastxt = doc[:-4] + 'txt'
            wordapp.ActiveDocument.SaveAs(docastxt,
                FileFormat=win32com.client.constants.wdFormatText)
            wordapp.ActiveDocument.Close( )
finally:
    # ensure Word is properly shut down even if we get an exception
    wordapp.Quit( )
    
'''
remove any files that end in .doc or .docx since we created duplicate .txt
files 
'''
for root, dirs, files in os.walk(".", topdown=True):
    for currentFile in files:
        print "processing file: " + currentFile
        exts = ('.doc', '.docx')
        if any(currentFile.lower().endswith(ext) for ext in exts):
            os.remove(os.path.join(root, currentFile))    

'''
Now we need to convert the 80 pdf files into text. 
PDF files are notoriously difficult to work with, fortuantely since we only
need the text we don't need to spend hours figuring out which pieces of the
pdf we need
reference: http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
reference: http://davidmburke.com/2014/02/04/python-convert-documents-doc-docx-odt-pdf-to-plain-text-without-libreoffice
run this in terminal: conda install -c https://conda.anaconda.org/pejo pdfminer
original module github: https://github.com/euske/pdfminer
'''


#define a function to convert a pdf file into text
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

path = 'C:\\ds_sandbox\\project2\\testingfolder\\120685.pdf'
txt = convert_pdf_to_txt(path)
print(txt)

with open('test.txt', 'w') as f:
    f.write(txt)


'''
create a loop to loop through all 5 directories and convert files ending
#in .pdf to .txt 
'''

#the following loop works....don't fucking touch it! 
#for path, dirs, files in os.walk(".", topdown=True):
#        for filename in files:
#            if not fnmatch.fnmatch(filename, '*.pdf'): continue
#            print "processing file: " + os.path.join(path, filename)            
#            convert_pdf_to_txt(os.path.join(path, filename))
            

#http://stackoverflow.com/questions/1900956/write-variable-to-file-including-name
#http://stackoverflow.com/questions/1684194/saving-output-of-a-for-loop-to-file
for path, dirs, files in os.walk(".", topdown=True):
        for filename in files:
            if not fnmatch.fnmatch(filename, '*.pdf'): continue
            print "processing file: " + os.path.join(path, filename)            
            doc = convert_pdf_to_txt(os.path.join(path, filename))
            with open(os.path.join(path, filename.replace('.pdf', '.txt')), 'w') as f: 
                f.write(doc)
#delete all pdf files 
for root, dirs, files in os.walk(".", topdown=True):
    for currentFile in files:
        print "processing file: " + currentFile
        exts = ('.pdf')
        if any(currentFile.lower().endswith(ext) for ext in exts):
            os.remove(os.path.join(root, currentFile))  
            
           
#: read text files into dataframe http://stackoverflow.com/questions/33912773/python-read-txt-files-into-a-dataframe

