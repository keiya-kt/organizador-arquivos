# Organizador de Arquivos

Um projeto desenvolvido em Python para organizar automaticamente os arquivos da pasta Downloads, separando-os em pastas de acordo com suas extensões.

## Funcionalidades

- Identifica arquivos pela extensão.
- Cria pastas automaticamente quando necessário.
- Move imagens, vídeos, áudios, PDFs, documentos, arquivos compactados e programas para suas respectivas pastas.
- Move arquivos de extensões não reconhecidas para a pasta 'Outros'.
- Evita sobrescrever arquivos com nomes duplicados, adicionando um número ao nome do arquivo quando necessário.

## Tecnologias utilizadas

- Python 3
- pathlib
- shutil

## Como executar

1. Instale o Python 3.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no VS Code.
4. Execute o arquivo `organizador.py` pelo terminal:

```bash
python organizador.py
```

## Exemplo de funcionamento

O organizador separa automaticamente os arquivos de acordo com suas extensões.

**Antes da execução:**

```text
Downloads/
├── gato.jpg
├── lofi.mp3
├── trabalho.pdf
├── planilha.xlsx
└── gato.jpg
```

**Depois da execução:**

```text
Downloads/
├── Imagens/
│   ├── gato.jpg
│   └── gato_1.jpg
├── Áudios/
│   └── lofi.mp3
├── PDFs/
│   └── trabalho.pdf
└── Planilhas/
    └── planilha.xlsx
```

*Arquivos com nomes duplicados recebem um número adicional para evitar que um arquivo sobrescreva o outro.*

## Observação

O programa move arquivos diretamente da pasta Downloads. Recomendo testar com arquivos de cópia antes de utilizá-lo com arquivos importantes.

## Objetivo

Este projeto foi criado para praticar conceitos de Python, como condicionais, laços de repetição, listas, manipulação de caminhos e movimentação de arquivos.