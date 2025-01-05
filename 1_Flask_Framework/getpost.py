from flask import Flask, render_template, request

'''
 It creates an instance of he flask class,
 which will be your WSGI (Web Server Gateway Interface) application.
'''

### WSGI Application
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}!'
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)