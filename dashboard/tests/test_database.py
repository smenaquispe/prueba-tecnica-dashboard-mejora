from django.test import TestCase
from sqlalchemy import create_engine
from dashboard.models import Client

class DatabaseConnectionTest(TestCase):
    def test_connection(self):
        engine = create_engine('postgresql://postgres:admin@localhost/dashboard_db')
        self.assertIsNotNone(engine.connect())

class GetDataTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # This method is called once for the entire test class
        Client.objects.create(name="John", age=25, city="Arequipa", salary=1500.00)
        Client.objects.create(name="Maria", age=30, city="Lima", salary=2000.00)
        Client.objects.create(name="Peter", age=35, city="Cusco", salary=2500.00)

    def test_get_data(self):
        # Retrieve all records from the database
        records = Client.objects.all()
        self.assertEqual(records.count(), 3)  # Ensure 3 records are retrieved
        self.assertEqual(records[0].name, "John")  # Check the first record
        self.assertEqual(records[1].age, 30)  # Check the second record
        self.assertEqual(records[2].city, "Cusco")  # Check the third record