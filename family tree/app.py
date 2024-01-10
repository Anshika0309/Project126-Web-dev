# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Anshika" # write your name
    age = "18" # write your age

    return render_template('index.html' , name = name , age = age)
@app.route("/father")
def father():
    name = "Pradeep" 
    age = "71"
    return render_template('father.html' , name = name , age = age)
@app.route("/mother")
def mother():
    name = "Sangeeta" 
    age = "50"
    return render_template('mother.html' , name = name , age = age)

@app.route("/friends")
def friends():
    name = "Aashi" 
    age = "16"
    return render_template('friends.html' , name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
