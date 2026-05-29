import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

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
            "Error de conexion  ",
            f"No se pudo conectar a la base de datos:\n{err}"
        )

        return None
    
#VENTANA PRINCIPAL

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Logística")
ventana.geometry("1050x650")
ventana.configure(bg="#f1f5f9")

#TITULO

titulo = tk.Label(
    ventana,
    text="Sistema de Gestión de Logística",
    font=("Arial", 22, "bold"),
    fg="#f1f5f9",
    bg="#0f172a",
)
titulo.pack(pady=15)

#FRAME USUARIO

frame_formulario = tk.LabelFrame(
    ventana,
    text="Informacion del Envio",
    bg="white",
    font=("Arial", 10, "bold"),
    padx=20,
    pady=15
)

frame_formulario.pack(
    padx=20,
    pady=10,
    fill=tk.X,
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

ventana = tk.Tk()

# EJECUTAR VENTANA

ventana.mainloop()