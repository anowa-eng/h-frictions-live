from flask import Blueprint, request
import csvfile
import json

class Endpoint:
    def __init__(self, file_name):
        self.file = f'db/{file_name}.csv'
        self.blueprint = Blueprint(file_name, file_name)
    def load_data(self):
        return csvfile.load(self.file)
    def rows(self):
        return len(self.load_data())
    # @self.blueprint.route(f'/api/{file_name}')
    def create(self, **kwargs):
        data = self.load_data()
        data.append({
            **kwargs,
            'ID': self.rows()
        })
        data.sync()
    def retrieve(self, ids):
        data = self.load_data()
        print(f'\n\ndata: {json.dumps(data)}\n\n')
        filtered_data = list(filter(
            lambda item: int(item.ID) in ids,
            data
        ))
        return filtered_data[0] if len(ids) == 1 else filtered_data
    def all(self):
        return self.load_data()
    def update(self, ids, new_data):
        data = self.load_data()
        for id in ids:
            data[id] = {**new_data, 'ID': id}
        data.sync()
    def delete(self, ids):
        data = self.load_data()
        for id in ids:
            del data[id]
        data.sync()
