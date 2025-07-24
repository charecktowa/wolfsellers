# Proyecto: API de Productos con Django REST Framework

Este repositorio contiene un microservicio RESTful para gestionar **Productos** (CRUD) utilizando **Django REST Framework**, con soporte para **Docker**, **Swagger UI**, y pruebas automatizadas.

---

## 📁 Estructura del repositorio

```
wolfsellers/
├── app/                    # Proyecto Django (settings, urls, wsgi)
│   ├── app/
│   ├── productos/          # App Productos (models, views, serializers, tests)
│   ├── manage.py           # Script de gestión de Django
│   └── db.sqlite3          # Base de datos (local)
├── Dockerfile              # Imagen Docker para la aplicación
├── docker-compose.yml      # Definición de contenedores (app)
├── requirements.txt        # Dependencias Python
└── README.md               # Este archivo
```

---

## 🛠️ Requisitos previos

* Python 3.12+
* pip
---

## 🚀 Instalación local

   ```
1. Crea y activa un entorno virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Instala las dependencias:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Ejecuta migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```
6. Abre tu navegador en `http://localhost:8000/api/` para ver la API browsable.

---

## 🐳 Usando Docker

1. Desde la raíz del proyecto (`wolfsellers/`), construye y lanza los contenedores:

   ```bash
   docker-compose build
   docker-compose up -d
   ```
2. Las migraciones se ejecutan al inicial el contenedor
   
3. Accede a la aplicación en tu navegador:

   * API browsable: `http://localhost:8000/api/`
   * Swagger UI:  `http://localhost:8000/swagger/`
   * Redoc UI:    `http://localhost:8000/redoc/`

---

## 🗄️ Migraciones y pruebas

* Para generar y aplicar migraciones:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
* Para ejecutar el conjunto de pruebas automatizadas:

  ```bash
  python manage.py test
  ```

---

## 🔗 Endpoints disponibles

| Método | Ruta                   | Descripción                 |
| ------ | ---------------------- | --------------------------- |
| GET    | `/api/productos/`      | Listar todos los productos  |
| POST   | `/api/productos/`      | Crear un nuevo producto     |
| GET    | `/api/productos/{id}/` | Obtener detalle de producto |
| PUT    | `/api/productos/{id}/` | Actualizar un producto      |
| DELETE | `/api/productos/{id}/` | Eliminar un producto        |

---

## 📄 Documentación interactiva (Swagger / Redoc)

* **Swagger UI**:  `http://localhost:8000/swagger/`
* **Redoc UI**:    `http://localhost:8000/redoc/`

Ambas interfaces permiten explorar los endpoints, ver esquemas de datos y enviar peticiones directamente desde el navegador.

---

## 🔨 Ejemplos con cURL

* **Listar productos**:

  ```bash
  curl -X GET http://localhost:8000/api/productos/
  ```

* **Crear producto**:

  ```bash
  curl -X POST http://localhost:8000/api/productos/ \
       -H "Content-Type: application/json" \
       -d '{
             "nombre": "Mi Producto",
             "descripcion": "Descripción de ejemplo",
             "precio": "49.90",
             "disponible": true
           }'
  ```

* **Obtener producto**:

  ```bash
  curl -X GET http://localhost:8000/api/productos/1/
  ```

* **Actualizar producto**:

  ```bash
  curl -X PUT http://localhost:8000/api/productos/1/ \
       -H "Content-Type: application/json" \
       -d '{"precio": "59.90"}'
  ```

* **Eliminar producto**:

  ```bash
  curl -X DELETE http://localhost:8000/api/productos/1/
  ```

---