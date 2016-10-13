from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname = 'phonebook')
app = Flask('MyApp')

@app.route('/')

def phonebook():
    allentries = db.query('select * from myphonebook')

    return render_template(
        'phonebook.html',
        title = 'phonebook',
        allentries_list = allentries.namedresult()
        )

@app.route('/add')

def add():
    allentries = db.query('select * from myphonebook')
    return render_template(
        'addentry.html',
        title = 'addentry',
        allentries_list = allentries.namedresult()

    )

@app.route('/submit_new_entry', methods= ['POST'])

def submit_new_entry():

    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    db.insert(
    'myphonebook',
    name = name,
    phone_number = phone_number,
    email = email
    )
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
