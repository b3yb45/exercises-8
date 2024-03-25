import json
IN_LIST = [("1", 2), ("2", 1), ("3", 3)]

encoded_array = json.dumps(IN_LIST)
decoded_list = json.loads(encoded_array)

out_list = sorted(decoded_list, key=lambda x: x[1], reverse=True)
print(out_list)
