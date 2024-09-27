from django.test import TestCase
from django.urls import reverse
from dashboard.models import Client

class DashboardViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create test data in the database
        Client.objects.create(name="Alice", age=30, city="New York", salary=50000)
        Client.objects.create(name="Bob", age=25, city="Los Angeles", salary=60000)
        Client.objects.create(name="Charlie", age=35, city="Chicago", salary=70000)
        Client.objects.create(name="David", age=28, city="New York", salary=65000)
        Client.objects.create(name="Eve", age=22, city="Los Angeles", salary=55000)

    def test_dashboard_view_renders_graphs(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Salary by Age')
        self.assertContains(response, 'Distribution of People by City')
        self.assertContains(response, 'Client Records')

    def test_dashboard_graph_data(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        # Verificar que los datos correctos se están pasando al gráfico
        self.assertContains(response, '50000')
        self.assertContains(response, '60000')
        self.assertContains(response, '70000')
        self.assertContains(response, '65000')
        self.assertContains(response, '55000')

        self.assertContains(response, 'New York')
        self.assertContains(response, 'Los Angeles')
        self.assertContains(response, 'Chicago')
    
    def test_dashboard_pie_chart_city_distribution(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        # Verificar que el gráfico de pastel contiene las ciudades correctas
        self.assertContains(response, 'New York')
        self.assertContains(response, 'Los Angeles')
        self.assertContains(response, 'Chicago')
    
    def test_dashboard_table_contains_clients(self):
        response = self.client.get(reverse('home'))

        # Verificar que los nombres de los clientes están en la tabla
        self.assertContains(response, 'Alice')
        self.assertContains(response, 'Bob')
        self.assertContains(response, 'Charlie')
        self.assertContains(response, 'David')
        self.assertContains(response, 'Eve')
