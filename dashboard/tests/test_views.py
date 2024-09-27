from django.test import Client
from django.test import TestCase


class HomeViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_view_renders_template(self):
        print('Test if the view renders the template')
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')