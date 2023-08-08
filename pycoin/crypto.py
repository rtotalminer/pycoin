import hashlib, json
from json import JSONEncoder
from .transcation import Transaction


# subclass JSONEncoder
class model(JSONEncoder):
        def default(self, o):
            return o.__dict__


def hash_contents(contents):
    contents_model = json.dumps(contents, cls=model)
    h = hashlib.new('sha256')
    h.update(json.dumps(contents_model, sort_keys=True).encode('utf-8'))    
    return h.hexdigest()