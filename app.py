from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap5
from werkzeug.exceptions import BadRequest
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import DecimalField, SelectField, SubmitField, BooleanField
from wtforms.validators import NumberRange
from conversor import ConversorMoedas
from operator import itemgetter
import secrets


app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)
# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

# instancia conversor
conversor = ConversorMoedas()
# cache da lista de moedas ordenadas pelo nome
moedas = dict(sorted(conversor._code_names.items(), key=itemgetter(1)))


class MoedaForm(FlaskForm):
    # code = SelectField('Moeda Original', choices=sorted(conversor._codes_), default='USD')
    code = SelectField("Moeda Original", choices=moedas.items(), default="USD")
    codein = SelectField("Moeda Destino", choices=moedas.items(), default="BRL")
    value = DecimalField(
        "Valor a ser convertido",
        default=1,
        validators=[
            # Força valor mínimo
            NumberRange(min=0.01, message="O valor mínimo é %(min)s")
        ],
        places=2,
    )
    use_usd = BooleanField(
        "Permitir a conversão das moedas utilizando Dolar como intermediário",
        default=True,
    )
    submit = SubmitField("Submit")


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    """Função para lidar com erros 400 (Bad Request)

    Quando o servidor reinicia o token do usuário se tornará inválido,
    para evitar que o usuário receba um erro de Bad Request, é enviado
    para o usuário a página inicial
    """
    result = 0.00
    form = MoedaForm()
    return render_template("index.html", form=form, result=result)


@app.route("/", methods=["GET", "POST"])
def index():
    """index page"""
    result = 0.00
    form = MoedaForm()
    if form.validate_on_submit():
        code = form.code.data
        codein = form.codein.data
        value = float(form.value.data)
        use_usd = form.use_usd.data

        result = conversor.convert(code, codein, value, use_usd=use_usd)
        flash(result)

    return render_template("index.html", form=form, result=result)


if __name__ == "__main__":
    app.run(debug=True)
