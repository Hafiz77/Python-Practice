class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)

a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
            'user': person_b
        }
    }
}
    
def find_depth(dictionary):
    if not isinstance(dictionary, dict):
        raise ValueError("Invalid input")
    for key, val in dictionary.items():
        if isinstance(val, dict):
            dictionary[key] = find_depth(val)
        elif hasattr(val, '__dict__'):
            val_dict = find_depth(val.__dict__)
            dictionary[key] = val_dict
    return dictionary


def find_nested_depth(dic, depth=1):

    for key, val in dic.items():
        print key, depth
        if isinstance(val, dict):
            find_nested_depth(val, depth+1)

def print_depth(a):
    data_dict = find_depth(a)
    find_nested_depth(data_dict)

print_depth(a);
