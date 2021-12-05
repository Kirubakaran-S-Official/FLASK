from flask import Flask , request, render_template 

app = Flask("KIRUBA")  #appname

#DIFFERENT METHODS TO CALL THE FN() ...use postman tool to call in different method
@app.route('/home' , methods = ['GET'])
def home1():
     return "Read the data"

app.route('/home' , methods = ['POST'])
def home1():
     return "create the data"

app.route('/home' , methods = ['DELETE'])
def home1():
     return "delete the data"     
     
app.route('/home' , methods = ['PUT'])
def home1():
     return "upload the data"


#call html from templates
@app.route('/basic')
def myform():
     return render_template("basic.html")


#DYNAMIC SBDIRECTORY
@app.route('/name/<y>')
def text(y):
     return y
  

#TRANSFER USING ONLY POST
@app.route('/data' , methods = ['post'])
def mydata():
     if request.method == "post" :
        ish = request.form.get('i')
        #print(ish)
     return ish


#run with specific port and turn developer mode to ON for auto updating the py file
app.run(port = 786 , debug = True) 
