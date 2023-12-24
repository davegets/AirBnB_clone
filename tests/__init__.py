import uuid
from datetime import datetime
# Adjust the __init__ method in the BaseModel class:

def __init__(self, *args, **kwargs):
    """
    Initialization of the base model.
    If kwargs is provided, an instance is created from the key-values.
    Otherwise, id and datetime fields are set to new.
    """
    if kwargs:
        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                setattr(self, key, datetime.fromisoformat(value))
            elif key != '__class__':
                setattr(self, key, value)
    else:
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()