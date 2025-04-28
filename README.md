# Tu Crédito - Sistema de Gestión de Créditos

Sistema web para la gestión de créditos, clientes y bancos desarrollado con Django.

## 🚀 Características

- Gestión de Clientes (CRUD)
- Gestión de Créditos
- Gestión de Bancos
- API REST
- Autenticación de usuarios
- Envío de emails automáticos
- Pruebas unitarias
- Documentación API (Swagger)

## 🛠️ Tecnologías

- Python 3.10+
- Django 5.0
- PostgreSQL
- Docker
- Django Rest Framework
- drf-spectacular (Swagger)

## 📋 Requisitos Previos

- Python 3.10 o superior
- PostgreSQL
- Docker y Docker Compose (opcional)

## 🔧 Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-credito.git
cd tu-credito
```

2. Crear y activar entorno virtual:

```bash
python -m venv venv
source venv/bin/activate # Linux/MacOS
source venv/Scripts/activate # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:

```bash
cp .env.example .env
```

5. Ejecutar migraciones:

```bash
python manage.py migrate
``` 

6. Crear superusuario:

```bash
python manage.py createsuperuser

Se configuro un usuario para pruebas:
    user: atp
    password: admin
```

7. Ejecutar servidor:

```bash
python manage.py runserver
```

## 📝 Documentación API

La documentación de la API se encuentra en:

```bash
http://localhost:8000/api/docs/
http://localhost:8000/api/schema/
```

## Pruebas

Para ejecutar las pruebas:

```bash
python manage.py test core.tests
```

## 📦 Estructura del Proyecto

```bash
core/
├── api_views.py
├── models.py
├── serializers.py
├── services.py
├── tests/
├── urls.py
├── views.py
└── __init__.py
```

## 🔐 Seguridad

- Content Security Policy (CSP) configurado
- Permission Policy implementado
- Autenticación requerida para todas las vistas
- Validación de datos en formularios y API

## 📧 Notificaciones por Email

- Envío de emails automáticos para notificaciones de créditos y clientes
- Este sistema se configuro para utilizar cualquier servicio de email SMTP
- Por defecto se utilizar el servicio de mailtrap para pruebas

## Variables de Entorno

Copia `.env.example` a `.env` y configura las siguientes variables:

### Básicas
- `DEBUG`: Modo debug (True/False)
- `SECRET_KEY`: Clave secreta de Django
- `ALLOWED_HOSTS`: Hosts permitidos

### Base de Datos
- `DB_NAME`: Nombre de la base de datos
- `DB_USER`: Usuario de PostgreSQL
- `DB_PASSWORD`: Contraseña de PostgreSQL
- `DB_HOST`: Host de la base de datos
- `DB_PORT`: Puerto de PostgreSQL

### Email
- `EMAIL_HOST`: Host de email
- `EMAIL_PORT`: Puerto de email
- `EMAIL_USE_TLS`: Usar TLS
- `EMAIL_HOST_USER`: Usuario de email
- `EMAIL_HOST_PASSWORD`: Contraseña de email
- `EMAIL_FROM_EMAIL`: Email de remitente


### Credenciales de Prueba
Usuario administrador por defecto:
- Username: atp
- Password: admin

## Diagramas del proyecto
- Clonando el proyecto, pueden abrir el diagrama abriendolo en un navegador, ya que es un archivo SVG, que contiene diagrama ER, diagrama de secuencias y diagrama de arquitectura.






