'''
This is the main file of the peer-to-peer marketplace application.
'''
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import requests
import json
app = Flask(__name__)
app.secret_key = "secret_key"
# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'marketplace'
mysql = MySQL(app)
# CoinGecko API URL
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd"
# Routes
@app.route('/')
def index():
    # Fetch Monero rates from CoinGecko API
    response = requests.get(COINGECKO_API_URL)
    data = json.loads(response.text)
    monero_usd_rate = data['monero']['usd']
    # Fetch user's Monero account balance
    if 'user_id' in session:
        user_id = session['user_id']
        cur = mysql.connection.cursor()
        cur.execute("SELECT monero_balance FROM users WHERE id = %s", (user_id,))
        user_balance = cur.fetchone()[0]
        cur.close()
    else:
        user_balance = 0
    return render_template('index.html', monero_usd_rate=monero_usd_rate, user_balance=user_balance)
# Add registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        # Implement registration logic here
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('register.html')
# Add login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        # Implement login logic here
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    return render_template('login.html')
# Other routes and functions...
if __name__ == '__main__':
    app.run(debug=True)