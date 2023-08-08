from .crypto import model
from .crypto import hash_contents
import json

def root_hash(data):
    if data == []:
        return []
    hash_map = []
    for i in data:
        i_model = json.loads(json.dumps(i, cls=model))
        hash_map.append(hash_contents(i_model))

    count = len(hash_map)

    while (count > 1):
        branch = []
        if not (count % 2 == 0):
            hash_map.append(hash_map[:-1])
        count = len(hash_map)
        for i in range(count//2):
            contents = hash_map[i] +  hash_map[i+1]
            contents_model = json.loads(json.dumps(contents, cls=model))
            leaf = hash_contents(contents_model)
            branch.append(leaf)
        hash_map = branch
        count = len(hash_map)
    return hash_map[0]



# data = [1, 2, 3, 4, 5, 6, 7, 8] # count = 8

# root_hash = root_hash(data)

# for i in range(len(root_hash)):
#     print(f"[{i+1}]\t{root_hash[i]}")