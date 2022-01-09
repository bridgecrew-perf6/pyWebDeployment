from flask import Flask, render_template
app = Flask(__name__) # create an instance of Flask class, __name__ is a special variable that gets as value the string "__main__" when you’re executing the script
@app.route('/')
def home():
    return render_template('home.html') # "Hello word" 
	#The flask framework has been written in a way so that it looks for HTML template files in a folder that should be named templates

@app.route('/about/')#this is houw you create another page http://localhost:5000/about/
def about():
    return render_template('about.html')
	
if __name__ == '__main__':#We are executing the script. Therefore, __name__ will be equal to "__main__",If the script is imported from another script, the script keeps it given name (e.g. hello.py)
    app.run(debug=True)