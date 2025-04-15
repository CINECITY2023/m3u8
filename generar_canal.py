import subprocess 

def obtener_m3u8(url):
    try:
        result = subprocess.run(["yt-dlp", "-g", url], capture_output=True, text=True)
        m3u8_url = result.stdout.strip().split("\n")[-1]
        return m3u8_url
    except Exception as e:
        print(f"Error procesando {url}: {e}")
        return None

def main():
    # URL del canal específico de YouTube que deseas actualizar
    canal_url = "https://www.youtube.com/watch?v=OR9MH16MKrg"  # Reemplaza con el ID real

    m3u8 = obtener_m3u8(canal_url)
    if m3u8:
        # Guarda el enlace en un archivo .m3u8
        with open("canal.m3u8", "w", encoding="utf-8") as f:
            # En este caso, no se requiere encabezado de playlist, solo se guarda el enlace.
            # Si prefieres el formato de playlist, puedes agregar un encabezado #EXTM3U y
            # una línea EXTINF, por ejemplo:
            f.write("#EXTM3U\n")
            f.write(f"#EXTINF:-1, Canal Específico\n")
            f.write(m3u8 + "\n")
        print("Archivo canal.m3u8 generado exitosamente.")
    else:
        print("Error al generar el enlace m3u8.")

if __name__ == "__main__":
    main()
