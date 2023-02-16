from flask import Blueprint, request, jsonify
import csvfile
import json

convert_to_int = lambda int_list: list(map(lambda item: int(item), int_list))

class Endpoint:
    def __init__(self, file_name):
        self.file = f'db/{file_name}.csv'
        self.blueprint = Blueprint(file_name, file_name)
        self.route_init(file_name)
    def load_data(self):
        return csvfile.load(self.file)
    def rows(self):
        return len(self.load_data())
    def create(self, **kwargs):
        data = self.load_data()
        data.append({
            **kwargs,
            'ID': self.rows()
        })
        data.sync()
        return kwargs
    def retrieve(self, ids):
        data = self.load_data()
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
        return new_data
    def delete(self, ids):
        data = self.load_data()
        for id in ids:
            del data[id]
        data.sync()
    def route_init(self, file_name):
        @self.blueprint.route(f'/api/{file_name}')
        def api_all():
            try:
                return jsonify(self.all())
            except Exception as exception:
                return jsonify({
                    'error': str(exception)
                })
        @self.blueprint.route(f'/api/{file_name}/create')
        def api_create():
            return jsonify(self.create(**request.args))
        @self.blueprint.route(f'/api/{file_name}/get')
        def api_retrieve():
            querystring_ids = request.args.get('ids')
            if querystring_ids:
                ids = convert_to_int(querystring_ids.split(','))
                return jsonify(convert_to_int(ids))
            else:
                return jsonify({
                    'error': 'IDs must be provided in order for this endpoint to function.'
                })
        @self.blueprint.route(f'/api/{file_name}/update')
        def api_update():
            querystring_ids = request.args.get('where')
            new_data = json.loads(request.args.get('json'))
            if querystring_ids:
                ids = convert_to_int(querystring_ids.split(','))
                self.update(ids, new_data)
                return new_data
            else:
                return jsonify({
                    'error': 'IDs must be provided in order for this endpoint to function.'
                })
        @self.blueprint.route(f'/api/{file_name}/delete')
        def api_delete():
            querystring_ids = request.args.get('ids')
            if querystring_ids:
                ids = convert_to_int(querystring_ids.split(','))
                self.delete(ids)
                return jsonify(ids)
            else:
                return jsonify({
                    'error': 'IDs must be provided in order for this endpoint to function.'
                })
