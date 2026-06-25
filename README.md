# 🍷 Vinoteca Don Roberto

## Trabajo Práctico Evaluativo - Ingeniería de Software

## Integrantes

* Candela Picco
* Federico Ramirez
* Juan Ignacio Laporte
* Johnston Mateo.

---

# Descripción

**Vinoteca Don Roberto** es un sistema web desarrollado con **Django** para la administración de una vinoteca.

El sistema permite gestionar vinos, clientes y ventas mediante un panel de administración propio, además de ofrecer un catálogo público de vinos disponibles para los visitantes.
<img width="1853" height="989" alt="Captura desde 2026-06-24 23-10-31" src="https://github.com/user-attachments/assets/fc0d9848-baf5-4ade-bf31-4afd69f95e60" />

---

# Funcionalidades

## Usuarios

* Usuario personalizado utilizando `AbstractUser`.
* Registro de usuarios.
* Inicio de sesión.
* Cierre de sesión.
* Gestión de permisos mediante grupos.
<img width="1853" height="989" alt="Captura desde 2026-06-24 23-11-17" src="https://github.com/user-attachments/assets/a5357dca-d617-4af3-a4a5-f506058886c2" />
<img width="1853" height="989" alt="Captura desde 2026-06-24 23-11-23" src="https://github.com/user-attachments/assets/0e01c297-1d33-42b6-9343-dbf6a301b281" />

## Gestión de vinos

* Alta de vinos.
* Modificación de vinos.
* Eliminación de vinos.
* Activación y desactivación de vinos.
* Carga de imágenes.
* Visualización del stock.

<img width="1267" height="643" alt="Captura de pantalla 2026-06-24 230549" src="https://github.com/user-attachments/assets/82e0a36f-c0b8-4bea-bb71-a9842c21d37f" />


## Gestión de clientes

* Alta de clientes.
* Modificación de clientes.
* Eliminación de clientes.

<img width="1279" height="575" alt="Captura de pantalla 2026-06-24 231312" src="https://github.com/user-attachments/assets/ce317d3f-330f-46fb-8848-8524d486eb18" />


## Gestión de ventas

* Registro de ventas.
* Asociación con clientes.
* Asociación con el usuario que realiza la venta.
* Registro automático de fecha y hora.

<img width="1279" height="563" alt="Captura de pantalla 2026-06-24 230610" src="https://github.com/user-attachments/assets/f2f694e5-6524-431d-ac63-b3dbc53b08e0" />


## Catálogo público

Los usuarios no autenticados pueden visualizar el catálogo de vinos disponibles.

<img width="1265" height="644" alt="Captura de pantalla 2026-06-24 230537" src="https://github.com/user-attachments/assets/62d68be7-7209-40c8-ac54-26ff639eca63" />


---

# Base de datos

El sistema cuenta con los siguientes modelos:

* Usuario
* Bodega
* Categoría de vino
* Proveedor
* Cliente
* Vino
* Venta
* DetalleVenta

Se implementan relaciones mediante `ForeignKey` entre los diferentes modelos.

---

# Permisos

El sistema utiliza grupos y permisos propios de Django.

## Administrador

Puede administrar completamente el sistema.

* Crear
* Editar
* Eliminar
* Visualizar

todos los módulos del sistema.

## Vendedor

Puede:

* Visualizar vinos.
* Crear vinos.
* Editar vinos.
* Visualizar clientes.
* Crear clientes.
* Editar clientes.
* Registrar ventas.

No posee permisos para eliminar información.

---

# Panel de Administración

El panel de administración fue personalizado utilizando:

* `list_display`
* `search_fields`
* `list_filter`
* `ordering`

para facilitar la administración de la información.

---

# Context Processor

Se implementó un Context Processor para compartir información global del sistema con todos los templates.

Variables utilizadas:

* Nombre del sistema.
* Versión del sistema.

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/candePicco/vinoteca-don-roberto.git
```

Ingresar al proyecto:

```bash
cd vinoteca-don-roberto
```

Crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual.

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar las migraciones:

```bash
python manage.py migrate
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

Abrir el navegador:

```text
http://127.0.0.1:8000/
```

---

# Requisitos cumplidos

* ✔ Usuario personalizado (`AbstractUser`).
* ✔ Registro, inicio y cierre de sesión.
* ✔ CRUD completo para Vinos.
* ✔ CRUD completo para Clientes.
* ✔ Gestión de Ventas.
* ✔ Permisos mediante grupos.
* ✔ Protección de vistas con `login_required` y `permission_required`.
* ✔ Context Processor.
* ✔ Carga de imágenes mediante `ImageField`.
* ✔ Panel de administración personalizado.
* ✔ Estilos mediante archivos estáticos.

---

# Repositorio

https://github.com/candePicco/vinoteca-don-roberto

---

**Proyecto desarrollado para la materia Ingeniería de Software - 2026.**
