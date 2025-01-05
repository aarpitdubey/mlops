# Building URL Dynamically
# Variable Rule
# Jinja 2 Template Engine

'''
{{ }} expressions to print output in html.
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for

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

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return f'Hello, {name}!'
#     return render_template('form.html')


@app.route('/success/<int:score>')
def success(score):
    # return f"The marks you got is" + str(score)
    result=""
    if score >= 50:
        result = "P+assed."
    else:
        result = "Failed."
        
    return render_template('result.html', result=result)

@app.route('/successs/<int:score>')
def successs(score):
    # return f"The marks you got is" + str(score)
    result=""
    if score >= 50:
        result = "Passed."
    else:
        result = "Failed."
        
    exp={'score':score, 'result':result}
        
    return render_template('res.html', results=exp)

## if condition
@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result.html', result=score)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    
    total_score=0
    
    if request.method == 'POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
        
    return redirect(url_for('successs', score=total_score))


if __name__=="__main__":
    app.run(debug=True)