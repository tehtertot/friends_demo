from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, "flask_friends")

@app.route('/')
def index():
    get_all_friends_query = "SELECT * FROM friends"
    all_friends = mysql.query_db(get_all_friends_query)
    return render_template('index.html', friends = all_friends)

@app.route('/add_friend', methods=["post"])
def add_friend():
    add_friend_query = "INSERT INTO friends (name, age, friend_since)     VALUES (:qname, :qage, :qfriend_since)"
    data = { 'qname': request.form["n"],
             'qage': request.form["a"],
             'qfriend_since': request.form["f"] }
    mysql.query_db(add_friend_query, data)
    return redirect('/')


app.run(debug=True)