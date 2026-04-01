import tkinter as tk
from tkinter import ttk
import socket
import threading

# --- CONFIGURACIÓN ---
IP_ESP32 = "192.168.1.XX" 
PUERTO = 80

# --- CLASE DE DATOS ---
class DatosSensor:
    def __init__(self, valor):
        self.valor = valor

# --- LÓGICA DE RED ---
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conectar():
    try:
        sock.connect((IP_ESP32, PUERTO))
        print("Conectado al ESP32")
        threading.Thread(target=recibir_datos, daemon=True).start()
    except Exception as e:
        print("Error al conectar:", e)

def recibir_datos():
    # Convertimos el flujo de red en un formato de lectura por líneas
    archivo_red = sock.makefile('r')
    while True:
        try:
            # Lee exactamente hasta el salto de línea (\n)
            linea = archivo_red.readline()
            if not linea: 
                break # Si está vacío, se desconectó
            
            # Limpiamos espacios y procesamos
            valor_limpio = linea.strip()
            if valor_limpio:
                sensor = DatosSensor(int(valor_limpio))
                # Actualizar la interfaz
                progress['value'] = sensor.valor
                lbl_valor.config(text=f"Potenciómetro: {sensor.valor}")
                
        except ValueError:
            # Si llega basura ocasional, la ignoramos y el ciclo continúa
            pass
        except Exception as e:
            print("Desconectado del servidor:", e)
            break

# Agregamos manejo de errores al enviar para evitar que la app colapse si se cae la red
def led_on(): 
    try: sock.send(b'ON')
    except: print("Error enviando ON")

def led_off(): 
    try: sock.send(b'OFF')
    except: print("Error enviando OFF")

# --- INTERFAZ GRÁFICA ---
root = tk.Tk()
root.title("Control ESP32 - Instituto Cordillera")
root.geometry("460x270")  # Ventana más grande
root.resizable(False, False)

# Estilo morado y con bordes suaves
style = ttk.Style()
style.theme_use('default')
style.configure("Purple.Horizontal.TProgressbar", troughcolor="#E8DAFF", background="#A020F0", thickness=24, bordercolor="#9B30FF", relief="flat")
style.configure("Purple.TButton", background="#8F4FCC", foreground="white", borderwidth=1, focusthickness=3, focuscolor="#8A2BE2")
style.map("Purple.TButton", background=[('active', '#9F5CE4')])

tk.Label(root, text="CONTROL DE DISPOSITIVO", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

lbl_valor = tk.Label(root, text="Potenciómetro: 0", font=("Arial", 10, "bold"))
lbl_valor.grid(row=1, column=0, columnspan=2)

progress = ttk.Progressbar(root, length=320, maximum=4095, style="Purple.Horizontal.TProgressbar")
progress.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

btn_on = ttk.Button(root, text="Encender LED", command=led_on, style="Purple.TButton")
btn_on.grid(row=3, column=0, padx=16, pady=12, ipadx=10, ipady=4)

btn_off = ttk.Button(root, text="Apagar LED", command=led_off, style="Purple.TButton")
btn_off.grid(row=3, column=1, padx=16, pady=12, ipadx=10, ipady=4)

threading.Thread(target=conectar, daemon=True).start()

root.mainloop()