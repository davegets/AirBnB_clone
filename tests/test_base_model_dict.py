from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)

print("--")
my_model = BaseModel(**my_model_json)
print(my_model.id)
print(my_model)
print(type(my_model.created_at))