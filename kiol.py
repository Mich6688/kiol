from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

def file_write():
    with open('receive_file.txt', mode='a+') as my_file:
        name = request.form['name']
        gmail =request.form['email']
        msg = request.form['message']
        my_file.write(f'name of user:{name} , message from user {msg}, users gmail{gmail}')

@app.route("/find", methods=['POST', 'GET'])
def receive():
    if request.method == "POST":
        file_write()
        return 'Submitted Successfully'
       
    



