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