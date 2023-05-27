from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from Forms import AboutForm




app = Flask(__name__)
app.secret_key = 'admin'





USER_DB = 'postgres'
PASS_DB = 'Admin'
URL_DB = 'localhost'
NAME_DB = 'Clinica'


FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate()
migrate = Migrate(app, db)
migrate.init_app(app,db)

class Persona(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 nombre = db.Column(db.String(250))
 apellido = db.Column(db.String(250))
 email = db.Column(db.String(250))
 telefono=db.Column(db.String(250))
 sintomas=db.Column(db.String(250))

 def __str__(self):
        return f'Id:{self.id}, Nombre:{self.nombre}, Apellido:{self.apellido}, Email:{self.email},Sintomas:{self.sintomas}'

class SignupForm(FlaskForm):
 nombre = StringField('Name', validators=[DataRequired()])
 apellido = StringField('Last Name', validators=[DataRequired()])
 email = StringField('Email', validators=[DataRequired(), Email()])
 telefono=StringField('Telefono',validators=[DataRequired()])
 sintomas= StringField('Sintomas',validators={DataRequired()})
 submit = SubmitField('Register')

#path inicio, función inicio randerizo a pagina index.html
@app.route('/')
def inicio():
    personas = Persona.query.all()
    return render_template('index.html', personas=personas)

#path ver, randerizo a pagina detalle.html
@app.route('/ver/<int:id>')
def ver_detalle(id):
    persona = Persona.query.get_or_404(id)
    return render_template('detalle.html', personas=[persona])


@app.route('/Form', methods=['GET', 'POST'])
def form():
    form = SignupForm()
    if form.validate_on_submit():

        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        telefono=form.telefono.data
        sintomas=form.sintomas.data

        persona = Persona(nombre=nombre, apellido=apellido, email=email,sintomas=sintomas,telefono=telefono)

        db.session.add(persona)
        db.session.commit()

        return redirect(url_for('success'))
    return render_template('form.html', form=form)


#función respuesta formuario registro exitoso
@app.route('/success')
def success():
    return 'Registro exitoso!'

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    migrate.init_app(app, db)
    app.run()