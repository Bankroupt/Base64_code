# Base64_code
Herramienta simple para codificar y decodificar texto en Base64.
## Requisitos

- Python 3.6+
## Instalación

1. Guardar el script en un archivo, por ejemplo base64.py
2. Hacer ejecutable (opcional):

```bash
git clone 
chmod +x base64.py
``` 
  
3. Ejecutar con Python:
  
```bash
python3 base64.py [opciones]
``` 
## Uso básico

- Mostrar ayuda:

```bash
python3 base64.py -h
``` 

- Codificar texto a Base64:

```bash
python3 base64.py -c "hola mundo
``` 

- Decodificar Base64 a texto:

```bash
python3 base64.py -d "aG9sYSBtdW5kbw=="
``` 

- Leer y procesar la primera línea de un archivo:

```bash
python3 base64.py -f ruta/al/archivo
``` 

Si el contenido es Base64 válido se intenta decodificar; si no, se muestra la codificación Base64 de la primera línea leída.
- Entrada por stdin (útil en pipelines):

```bash
echo "texto" | python3 base64.py echo "aG9sYSBtdW5kbw==" | python3 base64.py
``` 
## Comportamiento y detalles de implementación

- **Texto_a_base64(text)**  codifica UTF-8 y devuelve Base64.
- **De_base64_a_texto(b64)**  decodifica Base64 y devuelve texto UTF-8.
- **Lee todo el archivo (modo binario)** y intenta decodificarlo; si falla, muestra la versión Base64 del contenido leído.
- **Modo stdin** el script intenta validar Base64 con base64.b64decode(..., validate=True) para distinguir decodificación de codificación.
- **Manejo de errores:** excepciones genéricas para detectar datos no válidos; en casos reales de producción se recomienda capturar errores específicos y devolver códigos de salida distintos.
## Buenas prácticas

- Evitar pasar datos binarios complejos por la línea de comandos; usar archivos y stdin.
- Controlar la salida si trabajas con datos sensibles (no redirigir a logs públicos).
- Validar entradas externas antes de decodificar si esperas formatos específicos.
- Añadir pruebas unitarias para codificación/decodificación y tratamiento de archivos.
## Ejemplos rápidos

- Codificar:

```bash
python3 base64.py -c "secreto" 
c2VjcmV0bw==
``` 
   
- Decodificar:

```bash
python3 base64.py -d "c2VjcmV0bw==" 
secreto
``` 
   
- Usar archivo:

```bash
python3 base64.py -f /directorio/mensaje.txt
``` 
   
