
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.secret_key = 'desafio_bosch'
api = Api(app)

api.add_resource(EntradaDados, '/entrada/<int:peso>/<float:posicao>/<datime:horario>')
api.add_resource(ListaDados, '/listadedados/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
