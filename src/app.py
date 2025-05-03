from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route("/articulos")
def articulos():
    return 'Pagina de articulos'

@app.route("/acerca_de")
def acerca_de():
    return 'Pagina acerca de...'

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return 'Pagina no encontrada', 404


if __name__ == '__main__':
    app.run(debug=True)