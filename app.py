import subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password are valid
        if username == 'myuser' and password == 'mypassword':
            # Redirect to the next page if the login is successful
            return redirect(url_for('card'))
        else:
            # Render the login page with an error message if the login is unsuccessful
            return render_template('login.html', error='Invalid username or password')
    
    # Render the login page
    return render_template('login.html')

@app.route('/card', methods=['GET','POST'])
def card():
    # Render the next page
    if request.method == 'POST':
        if 'button1' in request.form:
            # Handle button1 click
            subprocess.call(['python', 'data_set.py'])
        elif 'button2' in request.form:
            # Handle button2 click
            subprocess.call(['python', 'trainer.py'])
        elif 'button3' in request.form:
            # Handle button3 click
            subprocess.call(['python', 'recog.py'])   
        else:
            username = request.form['username']
            password = request.form['password']
            
            # Check if the username and password are valid
            if username == 'myuser' and password == 'mypassword':
                # Redirect to the next page if the login is successful
                return redirect(url_for('next_page'))
            else:
                # Render the login page with an error message if the login is unsuccessful
                return render_template('card.html', error='Invalid username or password')
    return render_template('card.html')

@app.route('/next_page',methods=['GET','POST'])
def next_page():
    if request.method == 'POST':
    #subprocess.call(['python', 'live_cam_predict.py'])
        if 'button1' in request.form:
                # Handle button1 click
            subprocess.call(['python', 'face_d.py'])
        elif 'button2' in request.form:
                # Handle button2 click
            subprocess.call(['python', 'Attendance-system.py'])
    return render_template('next_page.html')


if __name__ == '__main__':
    app.run(debug=True)