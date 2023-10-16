from pathlib import Path
import os, sys

# Ler os arquivos que estão na pasta
folder_files = os.listdir('C:\\Users\\tr043272\\Desktop\\Laudos Arquivados')

# armazena os nomes em uma lista
archive_list = []
for archive in folder_files:
    archive_list.append(archive)
    print(archive_list)
archive_list.sort()

#Abre um documento de texto para armazenar essas informações
path = Path('C:\\Users\\tr043272\\Desktop\\Laudos Arquivados')
arquivo_de_texto = path / 'laudos.txt'

#Abre o documento e escreve os arquivos 
with open(arquivo_de_texto, 'w') as f:
    for archive in folder_files:
        f.write(archive + '\n')