# -*- coding: utf-8 -*-
#!/usr/bin/python3
import re
import json
import smtplib
from email.message import EmailMessage
#import numpy as np
#import pandas as pd
#import matplotlib as plt
import graphin

from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/upload")
def upload_file():
    return render_template("upload.html")

@app.route("/uploader", methods = ["POST"])
def uploader():
    if request.method == "POST":
        mysteryfile = request.files["file"]
        mysteryfile.save(secure_filename(mysteryfile.filename))
        if "cap" in mysteryfile.filename:
            return redirect(url_for("sip", filetoparse=mysteryfile.filename))
        elif "xls" in mysteryfile.filename:
            return redirect(url_for("excel", filetoparse=mysteryfile.filename))
        else:
            return "This format is not yet supported. Please check back soon."
@app.route("/excel/<filetoparse>")
def excel(filetoparse):
    return send_file(graphin.pygraph(filetoparse), mimetype='image/png')

@app.route("/sip/<filetoparse>")
def sip(filetoparse):
    sipjson = []
    with open(filetoparse) as capture:
        for line in capture:
            matchobj = re.search(r"sip:\+(\d+)@\[(.*)\]:?(\d+)", line)
            if matchobj:
                tinylist = []
                tinylist.append(matchobj.group())
                tinylist.append(matchobj.group(1))
                tinylist.append(matchobj.group(2))
                tinylist.append(matchobj.group(3))
                sipjson.append(tinylist)
        return json.dumps(sipjson)

@app.route("/emailsender")
def emailsender():
    msg = EmailMessage()
    msg['Subject'] = "this is my subject line, from Will"
    msg['From'] = "pythonstudent01@mail.com"
    msg['To'] = "rzfeeserspam@gmail.com"
    msg.preamble = "Hey you got a message from Will"

    with open("/home/student/emailpassword.txt") as emailpass:
        myemailpass = emailpass.read().rstrip('\n')
    mail = smtplib.SMTP("smtp.mail.com",587)
    mail.starttls()
    mail.login("pythonstudent01@mail.com", myemailpass)
    mail.sendmail("pythonstudent01@mail.com", "rzfeeserspam@gmail.com", msg.as_string())
    mail.quit()
    return "spammity spamcakes sent"
if __name__ == "__main__":
    app.run(port=5006)


