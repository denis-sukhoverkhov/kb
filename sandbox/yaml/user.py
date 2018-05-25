import yaml


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print('Dump object')
with open('config.yaml', 'w') as f:
    user1 = User('Sergo', 14)
    yaml.dump(user1, f)


print('Load object')
with open('config.yaml', 'r') as f:
    result = yaml.load(f)

print(result)
