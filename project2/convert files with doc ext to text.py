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
from sklearn.cross_validation import cross_val_score
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
text = []
for path, dirs, files in os.walk(".", topdown=True):
        for filename in files:
            if not fnmatch.fnmatch(filename, '*.txt'): continue
            print "processing file: " + os.path.join(path, filename)            
            with open (os.path.join(path, filename), "r") as f:
                text.append(f.read())
                
df = pd.DataFrame(text)


#Create a list that has only the document names, remove extension e.g. ".txt"
rowid= []

for path, dirs, files in os.walk(".", topdown=True):
        for filename in files:
            if not fnmatch.fnmatch(filename, '*.txt'): continue
            print "processing file: " + os.path.join(path, filename)
            rowid.append(os.path.join(filename[:-4]))
            
#very list contains only file names and not the textention e.g. ".txt"            
print(rowid)


'''
convert the list of file names into a dataframe with a column called "rowid" and 
the filenames as the row ids
'''
dfrowid2 = pd.DataFrame({'ID': rowid})

#concatenate the two dataframes into a single dataframe 
frames = [dfrowid2, df]
id_resume = pd.concat(frames, axis=1)

#id_resume.to_excel('C:/ds_sandbox/project2/data/id_resumes.xlsx')

#change column names 
id_resume.columns = ['ID', 'resume_text']
id_resume.columns

#check data types, ID should be an integer
id_resume.dtypes

#convert ID to integer 
resume = id_resume.convert_objects(convert_numeric=True)

#check to make sure the type converted to a numeric type, in this case a float
resume.dtypes

#convert to clean text to remove unicode characters 
def clean_text(row):
    # return the list of decoded cell in the Series instead 
    return [r.decode('unicode_escape').encode('ascii', 'ignore') for r in row]
resume['resume_text'] = df.apply(clean_text)

resume

'''
read in the csv of the survey data
'''
#read in csv of survey data 
survey = pd.read_csv('C:/ds_sandbox/project2/data/survey_data_16May16a.csv', sep=',')

#check shape 
survey.shape

#notice that the data type for ID is an numeric type, this means we can join the survey data
survey.dtypes

#check that ID column is in the survey dataframe 
"ID" in survey

#join the survey data to the text data
text = pd.merge(resume, survey, how='inner', left_on='ID', right_on='ID')

text.shape
text.columns
type(text.resume_text)

'''
The join worked. This ties out my dissertation work within +/- 3 rows. 
Note for this analysis we aren't controlling for gender, although from prior work we know that
individuals identifying as females tend to report higher job performance behaviors. 
We are taking a purely text analytic approach. Also I didn't have time to figure out how to
control for gender in Python :D

Now we need to create our X and y 
'''

#define X and y. We will use cross-validation here so no need to split into test-train-split
X = text.resume_text

y = text.task_performance_dichotomous3

#create 3 different vectorizors using english stop words, and ngrams of 1, 2, and 3
vectTFidf1 = TfidfVectorizer(analyzer='word', lowercase=True, min_df=3, 
                             stop_words='english',max_features=5000, ngram_range=(1, 1))

vectTFidf2 = TfidfVectorizer(analyzer='word', lowercase=True, min_df=3, 
                             stop_words='english',max_features=1000, ngram_range=(2, 2))

vectTFidf3 = TfidfVectorizer(analyzer='word', lowercase=True, min_df=3, 
                             stop_words='english',max_features=1000, ngram_range=(3, 3))


#create 3 tf-idf dtms 
X_dtm1 = vectTFidf1.fit_transform(X)

X_dtm2 = vectTFidf2.fit_transform(X)

X_dtm3 = vectTFidf3.fit_transform(X)


from sklearn.svm import LinearSVC #nice
from sklearn import cross_validation
svm = LinearSVC(C=1, penalty='l2', loss='hinge')



from sklearn.naive_bayes import MultinomialNB #nice
from sklearn.linear_model import LogisticRegression
#unigrams
scores = cross_validation.cross_val_score(svm, X_dtm1, y, scoring='recall', cv=10)
print(scores.mean())
print vectTFidf1.get_feature_names()[-50:]

#bigrams
scores = cross_validation.cross_val_score(svm, X_dtm2, y, scoring='recall', cv=10)
print(scores.mean())
print vectTFidf2.get_feature_names()[-50:]

#trigrams
scores = cross_validation.cross_val_score(svm, X_dtm3, y, scoring='recall', cv=10)
print(scores.mean())
print vectTFidf3.get_feature_names()[-50:]


nb = MultinomialNB()
log = LogisticRegression()
scores = cross_validation.cross_val_score(nb, X_dtm3, y, scoring='recall', cv=10)
print(scores.mean())

scores = cross_validation.cross_val_score(log, X_dtm3, y, scoring='recall', cv=10)
print(scores.mean())

from sklearn.linear_model import LogisticRegression
log = LogisticRegression()

scores = cross_validation.cross_val_score(log, X_dtm3, y, scoring='recall', cv=10)
print(scores.mean())




# Set the parameters by cross-validation
#tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
#                     'C': [1, 10, 100, 1000]},
#                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
#
#clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=10)
#
#scores = cross_val_score(clf,X_dtm1, y, scoring='recall', cv=10)
#
#print("Recall: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


###############################################################################

#http://scikit-learn.org/stable/auto_examples/model_selection/grid_search_text_feature_extraction.html#example-model-selection-grid-search-text-feature-extraction-py
from __future__ import print_function

from pprint import pprint
from time import time
import logging

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import RandomizedSearchCV
from sklearn.pipeline import Pipeline

print(__doc__)

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

###############################################################################
# define a pipeline combining a text feature extractor with a simple
# classifier
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier()),
])

# uncommenting more parameters will give better exploring power but will
# increase processing time in a combinatorial way
parameters = {
    'vect__max_df': (0.5, 0.75, 1.0),
    'vect__max_features': (None, 5000, 10000, 50000),
    'vect__ngram_range': ((2, 2), (3, 3)),  # unigrams or bigrams
    'tfidf__use_idf': (True, False),
    'tfidf__norm': ('l1', 'l2'),
    'clf__alpha': (0.00001, 0.000001),
    'clf__penalty': ('l2', 'elasticnet'),
    'clf__n_iter': (10, 50, 80),
}

if __name__ == "__main__":
    # multiprocessing requires the fork to happen in a __main__ protected
    # block

    # find the best parameters for both the feature extraction and the
    # classifier
    grid_search = RandomizedSearchCV(pipeline, parameters, n_jobs=-1, verbose=1)

    print("Performing grid search...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    print("parameters:")
    pprint(parameters)
    t0 = time()
    grid_search.fit(X, y)
    print("done in %0.3fs" % (time() - t0))
    print()

    print("Best score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))


