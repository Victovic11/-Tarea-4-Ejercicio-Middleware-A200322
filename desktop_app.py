import tkinter as tk
from tkinter import messagebox
import requests
from tkinter import ttk

# Función para conectarse a la API y obtener datos
def obtener_datos():
    url = "http://127.0.0.1:5000/solicitudes"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Imprimir la respuesta completa para verificar su estructura
        print("Respuesta de la API:", data)

        # Limpiar la lista antes de agregar nuevos datos
        lista.delete(0, tk.END)

        # Si data es una lista, recorrerla
        if isinstance(data, list):
            for solicitud in data:
                if isinstance(solicitud, dict):
                    lista.insert(tk.END, f"ID: {solicitud.get('id', 'N/A')} - Detalle: {solicitud.get('detalle', 'N/A')}")
                else:
                    lista.insert(tk.END, f"Solicitud: {solicitud}")
        else:
            lista.insert(tk.END, "Conexión a la API Problema: La API de Flask no está en ejecución o no se puede acceder por ejemplo, si hay un problema de red, el cliente Tkinter mostrará un mensaje de error. Solución: El uso de try-except en la función obtener_datos permite capturar excepciones de conexión y mostrar un mensaje de error a través de un cuadro de diálogo.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo conectar a la API: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Solicitudes API")
ventana.geometry("400x300")
ventana.config(bg="#f0f0f0")

# Estilo para los elementos
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.configure("TLabel", padding=6, background="#f0f0f0", font=("Arial", 12))
style.configure("TListbox", font=("Arial", 10))

# Etiqueta
etiqueta = ttk.Label(ventana, text="Solicitudes desde la API:")
etiqueta.pack(pady=10)

# Botón para obtener datos de la API
boton = ttk.Button(ventana, text="Obtener Solicitudes", command=obtener_datos)
boton.pack(pady=5)

# Lista para mostrar las solicitudes
lista = tk.Listbox(ventana, height=10, width=50, bd=2, relief="solid", font=("Arial", 10))
lista.pack(pady=10)

# Iniciar el loop de la ventana
ventana.mainloop()