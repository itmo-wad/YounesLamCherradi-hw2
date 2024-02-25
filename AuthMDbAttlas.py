from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Set up MongoDB client and connect to your MongoDB Atlas cluster
client = MongoClient('mongodb+srv://younes:1234@cluster0.nqb3ixv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['auth']   #The DataBase in whcih we will work with
collection = db['forma']  #The Collection in whcih we will work with for checking the Login Username&Password

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match in the database
        user = collection.find_one({'username': username, 'password': password})
        
        if user:
            # Redirect to the profile page if authenticated
            return redirect(url_for('profile'))
        else:
            # Render the login page with an error message
            return render_template('login.html', error='Invalid username or password')
    
    # Render the login page if the request method is GET
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
