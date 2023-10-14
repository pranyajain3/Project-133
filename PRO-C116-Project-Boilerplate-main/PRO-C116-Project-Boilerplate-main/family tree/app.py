# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def me():

    name = "Pranya" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
def father():

    name = "Hemant"
    age = "46"
    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
def mother():
    name = "Priyanshu"
    age = "44"
    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
def sister():
    name = "Khushi"
    age = "19"
    return render_template('index.html' , name = name , age = age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
