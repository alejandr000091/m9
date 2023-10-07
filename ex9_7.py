"""help"""

name = ["dan", "jane", "steve", "mike"]

def normal_name(names):
    return list(map(lambda x: x.capitalize(), names))

capitalized_names = normal_name(name)
print(capitalized_names)