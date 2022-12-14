import pymongo
from results import loglinkdata, monsterdata
import re
import zipfile
from tablebaber import tablebabmaker
from pymongo import MongoClient
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from filesetup import printer
import os
from shortlogana import bb2
from letssee import mate2
cluster = MongoClient("mongodb+srv://root:toor@cluster0.cx5wq.mongodb.net/?retryWrites=true&w=majority")
UPLOAD_FOLDER = r'Users\kizsa\Desktop\HTMLproject'
ALLOWED_EXTENSIONS = {'txt','zip','Task-1'}
app = Flask(__name__)
from flask import send_from_directory
filename=''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

from flask_pymongo import pymongo
db =cluster["HTML"]
collection = db["NAME/PHONENUMBER/EMAIL"]
from codecs import namereplace_errors
from flask import Flask, render_template, request
app = Flask(__name__)
#sfrom results import loglinkdata


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file.filename.endswith('zip'):
            filename=secure_filename(file.filename)
            file.save(os.path.join(r'/ws/viselvar-sjc/test/logfile22/NEWFLASK-MAIN',filename))
            with zipfile.ZipFile(filename,'r') as zipref:
                zipref.extractall(r'/ws/viselvar-sjc/test/logfile22/NEWFLASK-MAIN/UPLOAD_FOLDER')
            return redirect(url_for('download_file',name=filename))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(r'/ws/viselvar-sjc/test/logfile22/NEWFLASK-MAIN/UPLOAD_FOLDER' ,filename))
            return redirect(url_for('download_file', name=filename))
    return render_template('mainpage.html')
app.add_url_rule(
    "/UPLOAD_FOLDER/<name>", endpoint="download_file", build_only=True
)
       
    
@app.route('/UPLOAD_FOLDER/<name>')

def myfile(name):
    jobname=name.strip('.txt')
    if name.endswith('zip'):
        name=r'/ws/viselvar-sjc/test/logfile22/NEWFLASK-MAIN/UPLOAD_FOLDER/TaskLog.Task-1'
    with open(name,'r') as log:
        f=log.read()
    versionget=open('versiongit.txt','w')
    regularlog=open('regularlog.txt','w')
    regularlog.write(f)
    with open(name) as logfile:
        for line in logfile:
            if 'Switch Ports Model' in line:
                    
                    
                versionget.write(line)
                nextline=next(logfile)
                if '------ ' in nextline:
                    nextline=next(logfile)
                    
                versionget.write(nextline)
                nextline=next(logfile)
                versionget.write(nextline)
                break
        if 'Switch Ports Model' not in logfile:
            versionget.write('None')
            versionget.write('\n')
            versionget.write('NONE')   
                
        versionget.close()
    ShortenTextAeTestInfo='.%AETEST-6-INFO.+|.%AETEST-3-ERROR.+|%GENIE-6-INFO:.+pyATS.+|.%ASYNC_-3-ERROR.+|.%AETEST-4-WARNING.+|.%SCRIPT-3-ERROR.+|.%SCRIPT-6-INFO.+|.%aetest-5-NOTICE.+|.%autoeasy-5-NOTICE.+'
    ShortenTextAetError='.%AETEST-6-INFO.+|.%AETEST-3-ERROR..+|.%ASYNC_-3-ERROR.+'
    ShortenListOfText=re.findall(ShortenTextAeTestInfo,f)
    shortenlogpart2=']:.+'

    #write the shortened version to a file, Make this to a method, so it auto does this
    shortlog =open ('shortenedlog.txt','w+')
    for x in range (len(ShortenListOfText)):
        shortlog.write(ShortenListOfText[x])
        shortlog.write("\n")
    shortlog.close()
    with open('shortenedlog.txt','r') as log2:
        z=log2.read()
    shortenlistoftextpart2=re.findall(shortenlogpart2,z)


    results=open('new.txt','w')

    #this file is written simply because it makes the text easier to read, we took out anything that had cisco/time/etc
    for x in range(len(shortenlistoftextpart2)):
        results.write(shortenlistoftextpart2[x])
        results.write("\n")
    results.close()
    printer.poop()
    tablebabmaker.tablemaker(jobname,versionget)
    var=tablebabmaker.tablemaker(jobname,versionget)
    #dict1={}
    #dict1=loglinkdata.loglinkdatamethod()
    outputfile=r'/ws/viselvar-sjc/test/logfile22/NEWFLASK-MAIN/templates/momma.html'
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    fuk=open(r'/ws/viselvar-sjc/test/logfile22/NEWFLASK-MAIN/templates/momma.html','w+')
    fj=open('momma.html','r')
    for lines in fj:
        #print(lines)
        fuk.write(lines)
    fuk.close()
    fj.close()
    #db.collection.insert_one("hi")
    #print(dict1[1])
    list1=loglinkdata.loglinkdatamethod()
    name=var 
    allresults=mate2.bab5()
    return render_template('momma.html',name=name,allresults=allresults)
@app.route('/dict')
def index():

    #name = testcasename
    list1=bb2.hater()
    name=list1    
    return render_template('index.html', name=name)



if __name__ =='__main__':
    SECRET_KEY = "Your_secret_string"

    app.run(debug=True)
