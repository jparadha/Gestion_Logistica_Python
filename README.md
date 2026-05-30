# Gestión Logística

Proyecto desarrollado en Python para la gestión de envíos de mercancías, utilizando una interfaz gráfica creada con Tkinter y una base de datos MySQL para el almacenamiento de información logística.

## Descripción

Este programa fue desarrollado como práctica de integración entre Python y bases de datos MySQL.

El sistema permite:

* Registrar nuevos envíos.
* Visualizar envíos almacenados en la base de datos.
* Actualizar información de envíos existentes.
* Eliminar registros de envíos.
* Gestionar información logística mediante una interfaz gráfica amigable.

---

## Funcionalidades

### 1. Registro de envíos

Permite ingresar:

* Número de seguimiento.
* Ciudad de origen.
* Ciudad de destino.
* Fecha de entrega prevista.
* Estado del envío.

La información es almacenada automáticamente en la base de datos MySQL.

---

### 2. Visualización de envíos

Los registros almacenados son recuperados desde MySQL y mostrados en una tabla interactiva utilizando el componente Treeview de Tkinter.

---

### 3. Actualización de envíos

Permite seleccionar un registro existente, modificar sus datos y actualizar la información almacenada en la base de datos.

---

### 4. Eliminación de envíos

Permite eliminar registros seleccionados mediante una confirmación previa para evitar eliminaciones accidentales.

---

## Tecnologías utilizadas

* Python 3
* Tkinter
* MySQL
* MySQL Connector/Python
* XAMPP (MySQL y phpMyAdmin)
* Visual Studio Code
* Git
* GitHub

---

## Conceptos aplicados

Durante el desarrollo del proyecto se utilizaron los siguientes conceptos:

* Funciones
* Interfaces gráficas con Tkinter
* Conexión a bases de datos MySQL
* Operaciones CRUD (Create, Read, Update, Delete)
* Consultas SQL
* Manejo de errores con try y except
* Eventos y componentes gráficos
* Control de versiones con Git y GitHub

---

## Estructura de la base de datos

Tabla: Envios

| Campo                | Tipo               |
| -------------------- | ------------------ |
| ID                   | INT AUTO_INCREMENT |
| NumeroSeguimiento    | VARCHAR(50)        |
| Origen               | VARCHAR(100)       |
| Destino              | VARCHAR(100)       |
| FechaEntregaPrevista | DATE               |
| Estado               | VARCHAR(50)        |

---

## Ejecución del programa

1. Iniciar Apache y MySQL desde XAMPP.
2. Verificar que la base de datos gestion_logistica exista en MySQL.
3. Abrir el proyecto en Visual Studio Code.
4. Ejecutar el archivo Python desde la terminal:

```bash
python gestion_logistica.py
```

5. Utilizar la interfaz gráfica para administrar los envíos.

---

## Funcionalidades CRUD implementadas

| Operación           | Estado |
| ------------------- | ------ |
| Create (Crear)      | ✔      |
| Read (Leer)         | ✔      |
| Update (Actualizar) | ✔      |
| Delete (Eliminar)   | ✔      |

---

## Autor

Proyecto desarrollado para fines educativos como actividad práctica de integración entre Python, Tkinter y MySQL.
