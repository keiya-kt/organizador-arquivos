"""
arquivo.name = foto.jpeg
arquivo.suffix = .jpeg
arquivo.stem = foto
"""


from pathlib import Path

import shutil

downloads = Path.home() / "Downloads"

sufixo_imagem = [".jpg", ".jpeg", ".png", ".gif"]
sufixo_video = [".mp4", ".mkv", ".avi"]
sufixo_audio = [".mp3", ".wav", ".flac"]
sufixo_documento = [".doc", ".docx", ".odt", ".txt", ".rtf"]
sufixo_compactado = [".zip", ".rar", ".7z", ".tar", ".gz"]
sufixo_programa = [".exe", ".msi"]

print(downloads)

for arquivo in downloads.iterdir():
    if not arquivo.is_file():
        continue

    if arquivo.suffix in sufixo_imagem:
        destino = downloads / "Imagens"
        destino.mkdir(exist_ok=True)
        shutil.move(arquivo, destino / arquivo.name)

    elif arquivo.suffix in sufixo_video:
        destino = downloads / "Video"
        destino.mkdir(exist_ok=True)
        shutil.move(arquivo, destino / arquivo.name)

    elif arquivo.suffix in sufixo_audio:
        destino = downloads / "Audio"
        destino.mkdir(exist_ok=True)
        shutil.move(arquivo, destino / arquivo.name)

    elif arquivo.suffix == ".pdf":
        destino = downloads / "PDFS"
        destino.mkdir(exist_ok=True)
        shutil.move(arquivo, destino / arquivo.name)

    elif arquivo.suffix in sufixo_documento:
        destino = downloads / "Documentos"
        destino.mkdir(exist_ok=True)
        shutil.move(arquivo, destino / arquivo.name)

    elif arquivo.suffix in sufixo_compactado:
        destino = downloads / "Compactados"
        destino.mkdir(exist_ok=True)
        shutil.move(arquivo, destino / arquivo.name)

    elif arquivo.suffix in sufixo_programa:
        destino = downloads / "Programas"
        destino.mkdir(exist_ok=True)
        shutil.move(arquivo, destino / arquivo.name)

    else:
        destino = downloads / "Outros"
        destino.mkdir(exist_ok=True)
        shutil.move(arquivo, destino / arquivo.name)

    print(f"{arquivo.name} vai para {destino}")