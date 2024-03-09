# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "M.RIDHAN BALAJI" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/")
def home():

    name = "M.MADHAN PANDIAN" # write your name
    age = "45" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/")
def home():

    name = "M.PRIYADHARSHINI MAHARANI" # write your name
    age = "43" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/")
def home():

    name = "M.DHANYASRI MADHAN" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
