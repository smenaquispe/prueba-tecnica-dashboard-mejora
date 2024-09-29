from django.test import Client as Cl
from django.test import TestCase
from dashboard.models import Client

class HomeViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Cl()
        Client.objects.create(name="Alice", age=30, city="New York", salary=50000)
        Client.objects.create(name="Bob", age=25, city="Los Angeles", salary=60000)
        Client.objects.create(name="Charlie", age=35, city="Chicago", salary=70000)
        Client.objects.create(name="David", age=28, city="New York", salary=65000)
        Client.objects.create(name="Eve", age=22, city="Los Angeles", salary=55000)
    
    def test_view_renders_template(self):
        print('Test if the view renders the template')
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')