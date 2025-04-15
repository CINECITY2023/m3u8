import subprocess
import sys

if len(sys.argv) < 2:
    print("Uso: python extraer_m3u8.py URL_DEL_VIDEO")
    sys.exit(1)

url = sys.argv[1]
archivo = "enlace_m3u8.txt"

try:
    resultado = subprocess.check_output(['yt-dlp', '-g', '-f', 'best', url], text=True)
    with open(archivo, 'w') as f:
        f.write(resultado.strip() + '\n')
    print(f"✅ Enlace M3U8 guardado en {archivo}")
except subprocess.CalledProcessError as e:
    print("❌ Error al ejecutar yt-dlp:", e)
