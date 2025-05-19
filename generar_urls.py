import os

# Ruta local donde están tus carpetas LOTE1 y lote2
carpeta_base = "imagenes"

# Subcarpetas que quieres recorrer
subcarpetas = ["LOTE1", "lote2"]

# URL base del repositorio en RAW
base_url = "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes"

# Lista final
urls = []

for sub in subcarpetas:
    ruta = os.path.join(carpeta_base, sub)
    for archivo in sorted(os.listdir(ruta)):
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            url = f"{base_url}/{sub}/{archivo}"
            urls.append(f'"{url}",')

# Mostrar el array completo
print("imagenes = [")
for url in urls:
    print("  " + url)
print("]")
