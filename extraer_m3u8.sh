#!/bin/bash

# Script para extraer enlace M3U8 desde YouTube usando yt-dlp

if [ -z "$1" ]; then
  echo "Uso: $0 https://www.youtube.com/watch?v=OR9MH16MKrg"
  exit 1
fi

URL="$1"
ARCHIVO="enlace_m3u8.txt"

yt-dlp -g -f best "$URL" > "$ARCHIVO"

if [ $? -eq 0 ]; then
  echo "✅ Enlace M3U8 guardado en $ARCHIVO"
else
  echo "❌ Error al extraer el enlace"
fi
