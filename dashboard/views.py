from django.shortcuts import render
from dashboard.models import Client
import plotly.graph_objects as go
import plotly.io as pio

def generate_bar_chart(ages, salaries):
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(x=ages, y=salaries, name='Salary', marker_color='blue'))
    bar_fig.update_layout(title='Salary by Age', xaxis_title='Age', yaxis_title='Salary')
    return pio.to_html(bar_fig, full_html=False)

def generate_pie_chart(cities):
    city_counts = {city: cities.count(city) for city in set(cities)}
    pie_fig = go.Figure(data=[go.Pie(labels=list(city_counts.keys()), values=list(city_counts.values()), hole=.3)])
    pie_fig.update_layout(title_text='Distribution of People by City')
    return pio.to_html(pie_fig, full_html=False)

def home(request):
    records = Client.objects.all()
    
    ages, salaries, cities = zip(*[(record.age, record.salary, record.city) for record in records])

    
    bar_graph = generate_bar_chart(ages, salaries)
    pie_chart = generate_pie_chart(cities)

    return render(request, 'home.html', {'bar_graph': bar_graph, 'pie_chart': pie_chart, 'records': records})
