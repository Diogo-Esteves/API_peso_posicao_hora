
import sqlite3
from flask_restful import Resource

class EntradaDados(Resource):
    """ Classe para definir o metodo post para a entrada de dados no banco"""
    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)},400
            
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        
        try:
            self.insert(item)
        except:
            return {'messa': 'An error occurred inserting item'},500 # Something went wrong
        
        return item, 201


class ListaDados(Resource):
    """ Classe para definir o metodo get para a coleta de dados no banco"""

    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message':'Item not found'},404
