from flask import Blueprint, request
import csvfile

class Endpoint:
    def __init__(self, file_name):
        self.file = f'db/{file_name}.csv'
        self.blueprint = Blueprint(file_name, file_name)
    # @self.blueprint.route(f'/api/{file_name}')
    def create(self, **kwargs):
        data = csvfile.load(self.file)
        data.append(kwargs)
        data.sync()
    def __compare(list, **kwargs):
        new_list = list
            

    def get_all(self, **kwargs):
        data = csvfile.load(self.file)
        return data

            
