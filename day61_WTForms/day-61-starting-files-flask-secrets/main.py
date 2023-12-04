from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap4
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, Length
import email_validator



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)
bootstrap = Bootstrap4(app)

app.secret_key = "some secret string"
email = "admin@email.com"
password = "12345678"

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), InputRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), InputRequired(), Length(8)])
    submit = SubmitField(label='Log in')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        if login_form.email.data == email and login_form.password.data == password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
