import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_id_creation(self):
        """Test the id creation of a new instance."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))

    def test_save(self):
        """Test the save method updates `updated_at`."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict(self):
        """Test the method to_dict."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)

if __name__ == '__main__':
    unittest.main()