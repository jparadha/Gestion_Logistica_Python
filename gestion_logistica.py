import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
id_seleccionado = None

# CONEXIÓN A LA BASE DE DATOS

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_logistica"
        )
        return conexion

    except mysql.connector.Error as err:
        messagebox.showerror(
            "Error de conexión",
            f"No se pudo conectar a la base de datos:\n{err}"
        )

        return None

# LIMPIAR CAMPOS

def limpiar_campos():

    entry_seguimiento.delete(0, tk.END)
    entry_origen.delete(0, tk.END)
    entry_destino.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)

    combo_estado.set("En tránsito")

# MOSTRAR ENVÍOS

def mostrar_envios():

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute("""
            SELECT *
            FROM Envios
            ORDER BY ID ASC
        """)

        registros = cursor.fetchall()

        # Limpiar tabla antes de cargar datos nuevos
        for fila in tabla.get_children():
            tabla.delete(fila)

        # Insertar registros
        for registro in registros:

            tabla.insert(
                "",
                tk.END,
                values=registro
            )

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudieron mostrar los envíos:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()

# AGREGAR ENVÍO

def agregar_envio():

    seguimiento = entry_seguimiento.get()
    origen = entry_origen.get()
    destino = entry_destino.get()
    fecha = entry_fecha.get()
    estado = combo_estado.get()

    if not (
        seguimiento and
        origen and
        destino and
        fecha
    ):

        messagebox.showwarning(
            "Campos vacíos",
            "Debe completar todos los campos."
        )

        return

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute("""
            INSERT INTO Envios
            (
                NumeroSeguimiento,
                Origen,
                Destino,
                FechaEntregaPrevista,
                Estado
            )
            VALUES (%s, %s, %s, %s, %s)
        """,
        (
            seguimiento,
            origen,
            destino,
            fecha,
            estado
        ))

        conexion.commit()

        messagebox.showinfo(
            "Éxito",
            "Envío agregado correctamente."
        )

        mostrar_envios()
        limpiar_campos()

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudo agregar el envío:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()

def seleccionar_registro(event):

    global id_seleccionado

    seleccionado = tabla.focus()

    if not seleccionado:
        return

    datos = tabla.item(
        seleccionado,
        "values"
    )

    id_seleccionado = datos[0]

    limpiar_campos()

    entry_seguimiento.insert(0, datos[1])
    entry_origen.insert(0, datos[2])
    entry_destino.insert(0, datos[3])
    entry_fecha.insert(0, datos[4])

    combo_estado.set(datos[5])

def actualizar_envio():

    global id_seleccionado

    if id_seleccionado is None:

        messagebox.showwarning(
            "Selección requerida",
            "Debe seleccionar un envío."
        )

        return

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute("""
            UPDATE Envios
            SET
                NumeroSeguimiento=%s,
                Origen=%s,
                Destino=%s,
                FechaEntregaPrevista=%s,
                Estado=%s
            WHERE ID=%s
        """,
        (
            entry_seguimiento.get(),
            entry_origen.get(),
            entry_destino.get(),
            entry_fecha.get(),
            combo_estado.get(),
            id_seleccionado
        ))

        conexion.commit()

        messagebox.showinfo(
            "Éxito",
            "Envío actualizado correctamente."
        )

        mostrar_envios()
        limpiar_campos()

        id_seleccionado = None

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudo actualizar el envío:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()

def eliminar_envio():

    global id_seleccionado

    if id_seleccionado is None:

        messagebox.showwarning(
            "Selección requerida",
            "Debe seleccionar un envío."
        )

        return

    respuesta = messagebox.askyesno(
        "Confirmar eliminación",
        "¿Desea eliminar el envío seleccionado?"
    )

    if not respuesta:
        return

    conexion = conectar_bd()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:

        cursor.execute("""
            DELETE FROM Envios
            WHERE ID = %s
        """,
        (id_seleccionado,)
        )

        conexion.commit()

        messagebox.showinfo(
            "Éxito",
            "Envío eliminado correctamente."
        )

        mostrar_envios()
        limpiar_campos()

        id_seleccionado = None

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Error",
            f"No se pudo eliminar el envío:\n{err}"
        )

    finally:

        cursor.close()
        conexion.close()

# INTERFAZ GRÁFICA

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Logística")
ventana.geometry("1050x650")
ventana.configure(bg="#f1f5f9")


# TÍTULO

titulo = tk.Label(
    ventana,
    text="Sistema de Gestión de Logística",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#0f172a"
)

titulo.pack(
    pady=15,
    fill=tk.X
)


# FRAME FORMULARIO

frame_formulario = tk.LabelFrame(
    ventana,
    text="Información del Envío",
    bg="white",
    font=("Arial", 10, "bold"),
    padx=20,
    pady=15
)

frame_formulario.pack(
    padx=20,
    pady=10,
    fill=tk.X
)


# CAMPOS DEL FORMULARIO

campos = [
    ("Número de Seguimiento:", 0),
    ("Origen:", 1),
    ("Destino:", 2),
    ("Fecha Entrega:", 3),
    ("Estado:", 4)
]

for texto, fila in campos:

    tk.Label(
        frame_formulario,
        text=texto,
        bg="white",
        font=("Arial", 10)
    ).grid(
        row=fila,
        column=0,
        sticky="w",
        pady=5
    )


# ENTRADAS

entry_seguimiento = tk.Entry(
    frame_formulario,
    width=40
)

entry_seguimiento.grid(
    row=0,
    column=1,
    padx=10
)


entry_origen = tk.Entry(
    frame_formulario,
    width=40
)

entry_origen.grid(
    row=1,
    column=1,
    padx=10
)


entry_destino = tk.Entry(
    frame_formulario,
    width=40
)

entry_destino.grid(
    row=2,
    column=1,
    padx=10
)


entry_fecha = tk.Entry(
    frame_formulario,
    width=40
)

entry_fecha.grid(
    row=3,
    column=1,
    padx=10
)


# COMBOBOX ESTADO

combo_estado = ttk.Combobox(
    frame_formulario,
    values=[
        "Pendiente",
        "En tránsito",
        "Entregado"
    ],
    width=37,
    state="readonly"
)

combo_estado.grid(
    row=4,
    column=1,
    padx=10
)

combo_estado.set("En tránsito")


# FRAME BOTONES

frame_botones = tk.Frame(
    ventana,
    bg="#f1f5f9"
)

frame_botones.pack(
    pady=15
)


# BOTÓN AGREGAR

btn_agregar = tk.Button(
    frame_botones,
    text="Agregar",
    command=agregar_envio,
    bg="#15803d",
    fg="white",
    width=15,
    font=("Arial", 10, "bold")
)

btn_agregar.pack(
    side="left",
    padx=5
)


# BOTÓN ACTUALIZAR

btn_actualizar = tk.Button(
    frame_botones,
    text="Actualizar",
    command=actualizar_envio,
    bg="#2563eb",
    fg="white",
    width=15,
    font=("Arial", 10, "bold")
)

btn_actualizar.pack(
    side="left",
    padx=5
)


# BOTÓN ELIMINAR

btn_eliminar = tk.Button(
    frame_botones,
    text="Eliminar",
    command=eliminar_envio,
    bg="#dc2626",
    fg="white",
    width=15,
    font=("Arial", 10, "bold")
)

btn_eliminar.pack(
    side="left",
    padx=5
)


# BOTÓN LIMPIAR

btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar_campos,
    bg="#6b7280",
    fg="white",
    width=15,
    font=("Arial", 10, "bold")
)

btn_limpiar.pack(
    side="left",
    padx=5
)

# FRAME TABLA

frame_tabla = tk.LabelFrame(
    ventana,
    text="Envíos Registrados",
    bg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=10
)

frame_tabla.pack(
    padx=20,
    pady=15,
    fill="both",
    expand=True
)


# TREEVIEW

columnas = (
    "ID",
    "Seguimiento",
    "Origen",
    "Destino",
    "Fecha",
    "Estado"
)

tabla = ttk.Treeview(
    frame_tabla,
    columns=columnas,
    show="headings"
)


# ENCABEZADOS

tabla.heading("ID", text="ID")
tabla.heading("Seguimiento", text="N° Seguimiento")
tabla.heading("Origen", text="Origen")
tabla.heading("Destino", text="Destino")
tabla.heading("Fecha", text="Fecha Entrega")
tabla.heading("Estado", text="Estado")


# ANCHO COLUMNAS

tabla.column("ID", width=50, anchor="center")
tabla.column("Seguimiento", width=150, anchor="center")
tabla.column("Origen", width=150, anchor="center")
tabla.column("Destino", width=150, anchor="center")
tabla.column("Fecha", width=120, anchor="center")
tabla.column("Estado", width=120, anchor="center")


tabla.pack(
    side="left",
    fill="both",
    expand=True
)


# SCROLLBAR

scroll = tk.Scrollbar(
    frame_tabla,
    orient="vertical"
)

scroll.pack(
    side="right",
    fill="y"
)

tabla.config(
    yscrollcommand=scroll.set
)

scroll.config(
    command=tabla.yview
)

tabla.bind(
    "<<TreeviewSelect>>",
    seleccionar_registro
)

mostrar_envios()

# EJECUTAR VENTANA

ventana.mainloop()