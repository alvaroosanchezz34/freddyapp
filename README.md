# Freddy Fazbear's Pizza - Aplicación Django

Aplicación Django para gestionar los animatrónicos de Freddy Fazbear's Pizza con autenticación, autorización y gestión de permisos.

## Características principales

- Gestión completa de animatrónicos (CRUD)
- Sistema de autenticación y registro de usuarios
- Roles de usuario: Client y Staff con permisos específicos
- Tema oscuro/claro con almacenamiento en cookies
- Validación de formularios en el servidor
- Admin panel integrado

## Estructura del proyecto

```
- freddyproject/: Configuración del proyecto Django
- freddyapp/: Aplicación principal
  - models.py: Modelos Animatronic y Party
  - forms.py: Formulario AnimatronicForm
  - views.py: Vistas y controladores
  - urls.py: Rutas
  - templates/: Plantillas HTML
  - management/commands/: Comandos personalizados
```

## Instalación

1. Instalar Django: `pip install django`
2. Ejecutar migraciones: `python manage.py migrate`
3. Crear grupos: `python manage.py create_groups`
4. Crear datos de ejemplo: `python manage.py create_sample_data`
5. Iniciar servidor: `python manage.py runserver`

## Rutas principales

- `/freddyapp/list/`: Lista de animatrónicos (público)
- `/freddyapp/new/`: Crear nuevo animatrónico (autenticado + permiso)
- `/freddyapp/<id>/view/`: Ver detalles (autenticado)
- `/freddyapp/<id>/edit/`: Editar (autenticado + permiso)
- `/freddyapp/<id>/delete/`: Eliminar (autenticado + permiso)
- `/freddyapp/login/`: Login
- `/freddyapp/newuser/`: Registro
- `/freddyapp/logout/`: Logout

## Grupos de permisos

- **Client**: Solo permiso de lectura
- **Staff**: Todos los permisos (crear, leer, editar, eliminar)

## Modelos

**Animatronic**
- name (max 50 caracteres)
- animal (Bear, Chicken, Bunny, Fox)
- build_date (DateField)
- decommissioned (BooleanField)
- parties (ManyToMany con Party)

**Party**
- name
- attendants
