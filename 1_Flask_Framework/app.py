from flask import Flask

'''
 It creates an instance of he flask class,
 which will be your WSGI (Web Server Gateway Interface) application.
'''

### WSGI Application
app=Flask(__name__)


@app.route("/")
def home():
    return "Welcome to this best Flask Course"

@app.route("/about")
def about():
    return "This is the about page"

if __name__=="__main__":
    app.run(debug=True)