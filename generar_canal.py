import subprocess

# URL del canal o video en vivo de YouTube
url = "https://www.youtube.com/watch?v=OR9MH16MKrg/live"  # <-- Reemplaza con un enlace válido en vivo

try:
    # Ejecuta yt-dlp para obtener el enlace M3U8 directo
    result = subprocess.run(["yt-dlp", "-g", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0 or not result.stdout.strip():
        print("Error al generar el enlace m3u8.")
        print("stderr:", result.stderr)
    else:
        enlace = result.stdout.strip().split('\n')[-1]  # Obtener la última línea (video)
        
        with open("canal.m3u8", "w") as f:
            f.write("#EXTM3U\n")
            f.write("#EXTINF:-1, Canal En Vivo\n")
            f.write(enlace + "\n")
        
        print("Archivo canal.m3u8 generado con éxito.")
except Exception as e:
    print("Excepción:", e)
