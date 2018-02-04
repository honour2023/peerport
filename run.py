from flask import Flask,render_template,request,flash
import os
from models.pagemodel import SignUp,Contact
from models.basemodels import DBSingelton
from datetime import datetime


app=Flask(__name__)

@app.before_first_request
def initialize_tables():
    connect_db()
    if not SignUp.table_exists():
        SignUp.create_table()
    disconnect_db()

    connect_db()
    if not Contact.table_exists():
        Contact.create_table()
    disconnect_db()


@app.before_request
def connect_db():
	DBSingelton.getInstance().connect()

@app.teardown_request
def disconnect_db(err=None):
	DBSingelton.getInstance().close()


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name =request.form.get('name')
        email = request.form.get('email')
        phone_num = request.form.get('phone_num')
        member=request.form.get('member')

        new_signup = SignUp.create(name=name,email=email,phone_num=phone_num,member_tag=member)

        if new_signup is True:
            flash('You have successfully sign up', 'success')

    return render_template('index.html')

@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        name= request.form.get('name')
        email = request.form.get('email')
        phone_num = request.form.get('phone_num')
        question = request.form.get('question')

        new_contact= Contact.create(name=name, email=email, phone_num=phone_num, question=question)

    return render_template('index.html')

