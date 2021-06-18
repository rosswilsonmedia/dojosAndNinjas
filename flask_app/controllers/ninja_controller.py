from flask import render_template, request, redirect, session

from flask_app import app
from ..models.ninja import Ninja
from ..models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    results=Dojo.get_all()
    return render_template('new_ninja.html', all_dojos=results)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    dojo=Dojo.get_one({'id':request.form['dojo_id']})
    data={
        'dojo':dojo,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age']
    }
    Ninja.add_new(data)
    return redirect('/dojos/' + str(dojo.id))