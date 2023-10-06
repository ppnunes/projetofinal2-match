from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import DecimalField, SelectField, SubmitField, BooleanField
from conversor import ConversorMoedas
import secrets


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)


conversor = ConversorMoedas()

class MoedaForm(FlaskForm):
    # code = SelectField('Moeda Original', choices=sorted(conversor._codes_), default='USD')
    code = SelectField('Moeda Original', choices=conversor._code_names.items(), default='USD')
    codein = SelectField('Moeda Destino', choices=conversor._code_names.items(), default='BRL')
    value = DecimalField('Valor a ser convertido')
    use_usd = BooleanField('Permitir a conversão das moedas utilizando Dolar como intermediário', default= True)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = 0.00
    form = MoedaForm()
    if form.validate_on_submit():
        code = form.code.data
        codein = form.codein.data
        value = float(form.value.data)
        use_usd = form.use_usd.data

        result = conversor.convert(code, codein, value, use_usd=use_usd)
        flash(result)
        
    return render_template('index.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)