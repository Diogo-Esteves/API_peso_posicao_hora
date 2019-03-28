
from flask import Flask
from flask_restful import Api
from entradas import EntradaDados, ListaDados

app = Flask(__name__)
app.secret_key = 'desafio_bosch'
api = Api(app)

# api.add_resource(EntradaDados, '/entrada/<int:peso>/<float:posicaolat>//<float:posicaolon>/<float:horario>')
api.add_resource(EntradaDados, '/entrada/<int:peso>/')
api.add_resource(ListaDados, '/listadedados')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
