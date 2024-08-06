import os
import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pathlib import Path

def crear_factura(datos_cliente, detalles_transaccion, datos_empresa):
    # Ruta del escritorio
    desktop = Path.home() / "Desktop"
    pdf_path = desktop / "factura.pdf"

    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    width, height = letter

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Factura")

    # Datos del cliente
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, f"Cliente: {datos_cliente['nombre']}")
    c.drawString(100, height - 120, f"Dirección: {datos_cliente['direccion']}")

    # Datos de la empresa
    c.drawString(100, height - 160, f"Empresa: {datos_empresa['nombre']}")
    c.drawString(100, height - 180, f"Dirección: {datos_empresa['direccion']}")

    # Detalles de la transacción
    c.drawString(100, height - 220, "Detalles de la transacción:")
    y = height - 240
    for item in detalles_transaccion:
        c.drawString(100, y, f"{item['producto']} - {item['cantidad']} x {item['precio_unitario']}")
        y -= 20

    # Calcular y agregar totales
    subtotal = sum(item['cantidad'] * item['precio_unitario'] for item in detalles_transaccion)
    impuestos = subtotal * 0.15
    total = subtotal + impuestos

    c.drawString(100, y - 20, f"Subtotal: {subtotal}")
    c.drawString(100, y - 40, f"Impuestos: {impuestos}")
    c.drawString(100, y - 60, f"Total: {total}")

    c.save()

def generar_factura():
    datos_cliente = {
        'nombre': entry_cliente_nombre.get(),
        'direccion': entry_cliente_direccion.get()
    }

    detalles_transaccion = [
        {'producto': entry_producto.get(), 'cantidad': int(entry_cantidad.get()), 'precio_unitario': float(entry_precio.get())}
    ]

    datos_empresa = {
        'nombre': entry_empresa_nombre.get(),
        'direccion': entry_empresa_direccion.get()
    }

    crear_factura(datos_cliente, detalles_transaccion, datos_empresa)
    messagebox.showinfo("Éxito", "Factura generada correctamente en el escritorio.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Generador de Facturas")

# Entradas de datos del cliente
tk.Label(root, text="Nombre del Cliente").grid(row=0, column=0)
entry_cliente_nombre = tk.Entry(root)
entry_cliente_nombre.grid(row=0, column=1)

tk.Label(root, text="Dirección del Cliente").grid(row=1, column=0)
entry_cliente_direccion = tk.Entry(root)
entry_cliente_direccion.grid(row=1, column=1)

# Entradas de detalles de la transacción
tk.Label(root, text="Producto").grid(row=2, column=0)
entry_producto = tk.Entry(root)
entry_producto.grid(row=2, column=1)

tk.Label(root, text="Cantidad").grid(row=3, column=0)
entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=3, column=1)

tk.Label(root, text="Precio Unitario").grid(row=4, column=0)
entry_precio = tk.Entry(root)
entry_precio.grid(row=4, column=1)

# Entradas de datos de la empresa
tk.Label(root, text="Nombre de la Empresa").grid(row=5, column=0)
entry_empresa_nombre = tk.Entry(root)
entry_empresa_nombre.grid(row=5, column=1)

tk.Label(root, text="Dirección de la Empresa").grid(row=6, column=0)
entry_empresa_direccion = tk.Entry(root)
entry_empresa_direccion.grid(row=6, column=1)

# Botón para generar la factura
tk.Button(root, text="Generar Factura", command=generar_factura).grid(row=7, columnspan=2)

root.mainloop()
