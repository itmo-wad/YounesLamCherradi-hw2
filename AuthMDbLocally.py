from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/auth"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Handles the login functionality.
    
    This function receives the login form data, checks if the provided username and password
    match a user in the database, and redirects to the profile page if the user is found.
    Otherwise, it returns an error message.
    """
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = mongo.db.forma.find_one({'username': username, 'password': password})
        
        if user:
            return redirect(url_for('profile'))  # Redirect to the profile page
        else:
            return 'Invalid username or password'  # Return an error message
    
    return render_template('login.html')  # Render the login page

@app.route('/profile')
def profile():
    return render_template('Profile.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
