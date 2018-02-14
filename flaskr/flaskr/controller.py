from flask import render_template, request, url_for, session,flash, redirect
from flaskr import app
from .Models import Entries
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

@app.route('/')
def entires():
    #return 'Hello'
    return render_template('entries.html', entries=Entries.Entries.query.all())

@app.route('/test/<name>')
def test(name):
    return str(name)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        e = Entries.Entries(text= request.form['text'], title= request.form['title'])
        db.session.add(e)
        db.session.commit()
        return redirect(url_for('entires'))

    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    e = db.session.query(Entries.Entries).get(id)#Entries.Entries.query.get(id)
    if e is None:
        raise Exception('Record not exist')

    if request.method == 'GET':
        return render_template('edit.html', title=e.title, text = e.text, eId=e.id)

    #Entries.Entries.update() \
    #        .values(title=request.form['title'], text= request.form['text'])\
    #        .where()
    e.title = request.form['title']
    e.text = request.form['text']
    #e.update()
    db.session.commit()
    return redirect(url_for('entires'))

@app.route('/delete/<id>')
def delete(id):
    db.session.query(Entries.Entries).filter_by(id=id).delete()
    #e = db.session.query(Entries.Entries).get(id)
    #e.delete()
    db.session.commit()
    return redirect(url_for('entires'))

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid name'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect( url_for('entires') )
    return render_template('login.html', error=error)

