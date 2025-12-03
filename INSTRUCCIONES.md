# Freddy Fazbear's Pizza - Aplicación Django

Aplicación Django para gestionar los animatrónicos de Freddy Fazbear's Pizza.

## Características

- **Gestión de Animatrónicos**: Crear, editar, ver y eliminar animatrónicos
- **Relaciones con Fiestas**: Asociar fiestas a animatrónicos
- **Autenticación y Autorización**: Sistema de login/registro con roles (Client y Staff)
- **Tema Oscuro/Claro**: Cambiar tema mediante cookies
- **Permisos Granulares**: Control de acceso basado en permisos

## Estructura del Proyecto

```
freddyapp/
├── models.py              # Modelos Animatronic y Party
├── forms.py               # Formulario AnimatronicForm con validaciones
├── views.py               # Vistas y controladores
├── urls.py                # Rutas de la aplicación
├── admin.py               # Registro de modelos en admin
├── templates/
│   └── freddyapp/
│       ├── base.html                      # Plantilla base con header
│       ├── animatronic_list.html          # Lista de animatrónicos
│       ├── animatronic_form.html          # Formulario crear/editar
│       ├── animatronic_view.html          # Detalles del animatrónico
│       ├── animatronic_confirm_delete.html # Confirmación de eliminación
│       ├── login.html                     # Formulario de login
│       └── register.html                  # Formulario de registro
└── management/
    └── commands/
        ├── create_groups.py               # Comando para crear grupos y permisos
        └── create_sample_data.py          # Comando para crear datos de ejemplo
```

## Instalación y Configuración

1. **Crear y activar el entorno virtual**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalar dependencias**:
   ```bash
   pip install django
   ```

3. **Ejecutar migraciones**:
   ```bash
   python manage.py migrate
   ```

4. **Crear grupos y permisos**:
   ```bash
   python manage.py create_groups
   ```

5. **Crear datos de ejemplo (opcional)**:
   ```bash
   python manage.py create_sample_data
   ```

6. **Crear un superusuario (opcional)**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

## Acceso a la Aplicación

- **Página principal**: http://127.0.0.1:8000/freddyapp/list/
- **Admin Django**: http://127.0.0.1:8000/admin/

## Rutas Disponibles

| Ruta | Descripción | Controlador | Autenticación |
|------|-------------|------------|---------------|
| `/freddyapp/list/` | Lista de animatrónicos | `animatronic_list` | Público |
| `/freddyapp/new/` | Crear nuevo animatrónico | `animatronic_new` | Requerida + Permiso add_animatronic |
| `/freddyapp/<id>/view/` | Ver detalles | `animatronic_view` | Requerida |
| `/freddyapp/<id>/edit/` | Editar animatrónico | `AnimatronicUpdate` | Requerida + Permiso change_animatronic |
| `/freddyapp/<id>/delete/` | Eliminar animatrónico | `AnimatronicDelete` | Requerida + Permiso delete_animatronic |
| `/freddyapp/newuser/` | Registro de usuario | `register_user` | Público |
| `/freddyapp/login/` | Login | `LoginView` | Público |
| `/freddyapp/logout/` | Logout | `LogoutView` | Público |
| `/freddyapp/theme/` | Activar tema oscuro | `set_theme_dark` | Público |
| `/freddyapp/clearcookies/` | Limpiar cookies | `clear_cookies` | Público |

## Modelos

### Animatronic
```python
- name (CharField, max 50 caracteres)
- animal (CharField, opciones: Bear, Chicken, Bunny, Fox)
- build_date (DateField)
- decommissioned (BooleanField)
- parties (ManyToManyField con Party)
```

### Party
```python
- name (CharField)
- attendants (IntegerField)
```

## Grupos de Permisos

### Client
- Permiso: `view_animatronic`
- Los usuarios nuevos se asignan automáticamente a este grupo

### Staff
- Permisos: `view_animatronic`, `add_animatronic`, `change_animatronic`, `delete_animatronic`

## Validaciones del Formulario AnimatronicForm

- **name**: Obligatorio, máximo 50 caracteres
- **animal**: Obligatorio, máximo 2 caracteres
- **build_date**: Obligatorio, widget de calendario
- **decommissioned**: Obligatorio, checkbox booleano
- **parties**: Opcional, múltiples selecciones

## Características Especiales

### Tema Oscuro/Claro
- Botón "Dark theme" en el header activa el tema oscuro (almacenado en cookie)
- Botón "Light theme" en el header desactiva el tema oscuro (borra la cookie)

### Header
- Botones de tema (Dark/Light)
- Enlaces de "Register" y "Log in" (solo para usuarios no autenticados)
- Mensaje "Hi, <usuario>" y botón "Log out" (solo para usuarios autenticados)

## Notas de Desarrollo

- El formulario valida los datos del lado del cliente y del servidor
- Los mensajes de error personalizados se muestran en los campos
- Las plantillas usan Bootstrap-like styling con CSS personalizado
- Los decoradores de permiso aseguran que solo usuarios autorizados puedan acceder a ciertas vistas
- La cookie del tema se persiste durante 1 año
