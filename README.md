
# Proyecto Dashboard

Este proyecto utiliza Django y Faker para migrar la base de datos, generar datos ficticios y ejecutar pruebas. Sigue los pasos a continuación para configurarlo y ejecutarlo.

## Requisitos

- Python 3.x
- Django
- Faker
- Base de datos configurada (MySQL, PostgreSQL, etc.)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/unity-project.git
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configura tu base de datos en el archivo `settings.py` (o usando variables de entorno) según tu entorno.

## Migración de Base de Datos

Para migrar las tablas necesarias en tu base de datos, ejecuta:

```bash
python manage.py migrate
```

Para realizar las migraciones de dashboard
```bash
python manage.py makemigrations dashboard
python manage.py migrate dashboard
```


## Carga de Datos Ficticios

Puedes utilizar el comando personalizado `seed_data` para generar clientes de prueba con Faker. En este ejemplo, se generarán 5 clientes ficticios:

```bash
python manage.py seed_data client 5
```

## Ejecución de Tests

Para asegurarte de que todo funciona correctamente, ejecuta las pruebas unitarias:

```bash
python manage.py test
```

## Ejecución del Servidor

Finalmente, para iniciar el servidor local y probar la aplicación, usa el siguiente comando:

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`.
