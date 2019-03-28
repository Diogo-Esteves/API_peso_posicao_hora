
import sqlite3
from flask_restful import Resource, reqparse


class EntradaDados(Resource):
    """ Classe para definir o metodo post para a entrada de dados no banco"""

    parser = reqparse.RequestParser()
    # parser.add_argument('peso',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be blank")
    parser.add_argument('posicaolat',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('posicaolon',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('hora',
                        type=str,
                        required=True,
                        help="This field cannot be blank")


    def post(self, peso):
        # if ListaDados.find_by_name():
            # return {'message': "An item with the time '{}' already exists.".format(hora)}, 400

        data = EntradaDados.parser.parse_args()
        item = {'peso': peso, 'hora': data['hora'],
               'posicao': data['posicaolat']+ " "+data['posicaolon']}
        
        try:
            self.insert(item)
        except:
            return {'message': 'An error occurred inserting item'}, 500  # Something went wrong
        
        return item, 201

    @classmethod
    def insert(self, item):
        connection = sqlite3.connect('data_wei_pos_tim.db')
        cursor = connection.cursor()

        query = "INSERT INTO dados VALUES (?, ?, ?)"
        cursor.execute(query, (item['peso'],item['hora'],item['posicao'],))

        connection.commit()
        connection.close()


class ListaDados(Resource):
    """ Classe para definir o metodo get para a coleta de dados no banco"""

    def get(self):
        item = self.find_by_name()
        # if item:
        #     return item
        return {'Entradas': item}, 201

    @classmethod
    def find_by_name(self):
        connection = sqlite3.connect('data_wei_pos_tim.db')
        cursor = connection.cursor()

        query = "SELECT * FROM dados"
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({'peso': row[0], 'hora': row[1], 'posicao': row[2]})

        if result:
            return items

        connection.commit()
        connection.close()
