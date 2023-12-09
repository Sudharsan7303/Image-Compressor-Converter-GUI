from flask import Flask,render_template,request,flash,redirect,send_file
from config import Config
import os
from functions import Convert,Compress
import tmp

app=Flask(__name__)
app.config.from_object(Config)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home',home=True)

@app.route("/compressor",methods=["GET","POST"])
def compressor():
    try:

        image=None
        if request.method == 'POST' and request.files["img"]!=None and request.form["quality"]!=None:
            image=request.files["img"]
            qual=request.form["quality"]
        
            path=Compress(image,qual)
            return send_file(path,as_attachment=True) 

        else:

            return render_template('compressor.html',title='Compress',compress=True)
    except:
        return render_template('compressor.html',title='Compress',compress=True)


@app.route("/converter",methods=["GET","POST"])
def converter():
    try:
        image=None
        if request.method == 'POST':
            image=request.files["img"]
            
        
            path=Convert(image)
            
            return  send_file(path,as_attachment=True) 
            


        else:

            return render_template('converter.html',title='Convert',convert=True)
    except:
        return render_template('converter.html',title='Convert',convert=True)

