# Star Wars Project

Una API REST construida en Django + Django REST Framework que expone un catálogo de personajes del universo Star Wars. Incluye autenticación JWT, paginación, búsqueda avanzada y documentación Swagger.

---

## Instalación y configuración

### 1. Clona el repositorio

```bash
git https://github.com/gerard2120/StarWarsProject.git
cd starwars-project
```

### 2. Crea un entorno virtual e instala dependencias

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

pip install -r requirements.txt
```

### 3. Migraciones y carga de datos

```bash
python manage.py migrate
python manage.py loaddata static/fixtures/starwars_data.json
```

### 4. Crea un superusuario

```bash
python manage.py createsuperuser
```

---

## Documentación Swagger

Disponible en:

```
http://localhost:8000/api/schema/swagger/
```

Incluye definición de modelos, parámetros de búsqueda, ejemplos y autenticación con JWT.

---


## Autor

**Luis Gerardo Diaz Diaz**  
Desarrollador Backend  
luis.gerard2120@gmail.com

---

