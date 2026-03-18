# Cuestionario de Evaluación: Comunicación por Sockets 📝

**Nombre del Estudiante:** Lissette Negrete
**Fecha:** 11-03-2026

*Instrucciones: Responde a las siguientes preguntas basándote en la teoría de redes y en el análisis del código de nuestro proyecto. Sube este archivo con tus respuestas a tu repositorio como evidencia de trabajo.*

1. **¿Qué es una Dirección IP y para qué sirve en nuestro proyecto?**
   Una dirección IP es un número único que identifica a un dispositivo dentro de una red. En nuestro proyecto sirve para que la computadora pueda encontrar y conectarse con la ESP32.

2. **¿Qué es un Puerto de red? (Menciona qué puerto estamos usando en el código de la ESP32).**
Permite que varios programas usen la misma dirección IP sin confundirse.
En el código de la ESP32 estamos usando el puerto 80.

3. **Define con tus propias palabras qué es un Servidor en informática.**
   Un servidor es un dispositivo o programa que espera conexiones de otros dispositivos y les proporciona información o servicios cuando se lo solicitan.

4. **¿Cuál es la diferencia entre un "Servidor" (Hardware/Software) y un "Servicio" (Service)?**
Un servidor es la computadora o programa que atiende solicitudes de otros dispositivos.
Un servicio es la función específica que ofrece ese servidor, por ejemplo: enviar datos, alojar una página web o manejar una base de datos.

5. **Investigación: ¿Cuál es la diferencia técnica entre un "Socket TCP" normal y un "WebSocket"?**
La diferencia es que WebSocket está diseñado para aplicaciones web y comienza con un "handshake" HTTP, mientras que el socket TCP es una conexión más básica y directa.

6. **Analizando nuestro código: ¿Quién actúa como Servidor y quién actúa como Cliente? (Justifica tu respuesta mencionando qué funciones del código lo demuestran, ej. `bind()`, `connect()`).**
En nuestro proyecto, la ESP32 actúa como servidor porque espera conexiones de otros dispositivos usando funciones.
La computadora con Python actúa como cliente porque inicia la conexión utilizando la función connect() para comunicarse con la ESP32.

7. **En el código de la computadora (Python), importamos la librería `threading` (Hilos). ¿Qué pasaría con la ventana de Tkinter si no usáramos hilos para recibir los datos de la red?**
Si no usáramos hilos, la ventana de Tkinter se quedaría congelada mientras espera datos de la red.
Esto pasaría porque el programa estaría ocupado esperando la información y no podría actualizar la interfaz gráfica.

8. **¿Por qué es necesario usar bloques `try...except` cuando trabajamos con conexiones de red e Internet?**
 Porque las conexiones de red pueden fallar, el bloque try...except evita que el programa se detenga y permite manejar los errores correctamente.

9. **En la función de encender el LED en Python, enviamos el comando así: `sock.send(b'ON')`. ¿Qué significa esa letra `b` antes de las comillas y por qué no enviamos un texto normal?**
   La letra b significa que el mensaje se envía en formato de bytes, no se envía texto normal porque los sockets trabajan con datos binarios, entonces es necesario convertir el texto a bytes para que pueda ser transmitido correctamente.

10. **Describe brevemente el flujo de datos: ¿Qué camino recorre la información desde que giras el potenciómetro físicamente hasta que la barra se mueve en la pantalla de la computadora?**
 Primero el potenciómetro envía una señal analógica a la ESP32, luego la ESP32 convierte esa señal en datos digitales y los envía por la red mediante el socket, después la computadora recibe esos datos con Python y finalmente la interfaz de Tkinter usa esa información para mover la barra en la pantalla.
