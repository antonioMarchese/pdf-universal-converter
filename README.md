
# Document Generator

** Document Generator** é uma biblioteca Python para a geração de documentos em formatos PDF, Excel e CSV. Ela oferece uma interface simples e flexível para criar documentos profissionais de maneira rápida e eficiente.

## Instalação

Para instalar a biblioteca, você pode usar o `pip`:

```bash
pip install document_generator
```

### Requisitos Adicionais
Para gerar documentos PDF a partir de HTML, é necessário instalar o wkhtmltopdf no seu sistema operacional. O wkhtmltopdf é uma ferramenta que converte HTML em PDF usando o Webkit.

Instalação do wkhtmltopdf

* No Ubuntu/Debian:
    ```bash
    sudo apt-get install wkhtmltopdf
    ```

* No Fedora:
    ```bash
    sudo dnf install wkhtmltopdf
    ```

* No macOS (usando Homebrew):
  ```bash
    brew install wkhtmltopdf
  ```

* No Windows:

    Baixe o instalador a partir da [página de lançamentos do wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) e siga as instruções de instalação.

Após a instalação do wkhtmltopdf, a biblioteca `document_generator` poderá utilizar a funcionalidade de geração de PDFs a partir de HTML.

## Funcionalidades

- **PDF**: Criação de PDFs com suporte a orientação retrato e paisagem, além de geração a partir de HTML.
- **Excel**: Criação de planilhas Excel com facilidade para adicionar dados em células específicas.
- **CSV**: Geração de arquivos CSV de forma simples e intuitiva.

## Uso

### PDF

Para gerar um documento PDF:

```python
from document_generator import PDFGenerator

pdf = PDFGenerator()
pdf.create_canvas("example.pdf", orientation='landscape')
pdf.add_text("Hello, world!", 100, 750)
pdf.save("example.pdf")
```

### Excel

Para gerar uma planilha Excel:

```python
from document_generator import XlsxGenerator

xlsx = XlsxGenerator()
xlsx.create_workbook("example.xlsx")
xlsx.add_data("Hello, world!", 0, 0)
xlsx.save("example.xlsx")
```

### CSV

Para gerar um arquivo CSV:

```python
from document_generator import CSVGenerator

csv = CSVGenerator()
csv.create_csv("example.csv")
csv.add_row(["Hello", "world"])
csv.save("example.csv")
```

## Estrutura da Biblioteca

A biblioteca é organizada da seguinte forma:

```
document_generator/
├── document_generator/
│   ├── csv/
│   │   ├── __init__.py
│   │   └── csv_generator.py
│   ├── pdf/
│   │   ├── __init__.py
│   │   └── pdf_generator.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── .py
│   ├── xlsx/
│   │   ├── __init__.py
│   │   └── xlsx_generator.py
│   ├── __init__.py
│   └── base_document.py
├── tests/
│   ├── __init__.py
│   ├── csv/
│   │   ├── __init__.py
│   │   └── test_csv_generator.py
│   ├── pdf/
│   │   ├── __init__.py
│   │   └── test_pdf_generator.py
│   ├── xlsx/
│   │   ├── __init__.py
│   │   └── test_xlsx_generator.py
│   └── conftest.py
├── requirements.txt
├── setup.py
└── README.md
```

## Contribuição

Contribuições são bem-vindas! Se você quiser contribuir com este projeto, siga as etapas abaixo:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`)
4. Envie para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### Como Gerar Tag de Versões no Git ( ⚠️ Somente após aprovação e merge da MR)

Para manter o controle das versões da sua biblioteca, você pode criar tags no Git. Siga os passos abaixo para gerar e subir uma tag de versão:

1. Commit de Todas as Alterações

    Certifique-se de que todas as suas alterações estão commitadas:

    ```bash
    git add .
    git commit -m "Descrição das alterações"
    ```

2. Criar uma Nova Tag

    Crie uma nova tag de versão. Substitua vX.X.X pela versão apropriada, seguindo as diretrizes do [Versionamento Semântico](https://semver.org/lang/pt-BR/):

    ```bash
    git tag vX.X.X
    ```

3. Subir a Tag para o Repositório Remoto

    Envie a tag criada para o repositório remoto:

    ```bash
    git push origin vX.X.X
    ```

4. Listar Todas as Tags (Opcional)

    Para ver todas as tags existentes no repositório, use o comando:

    ```bash
    git tag
    ```

### Como Gerar e Subir o Pacote
1. Configuração do Ambiente

   Crie e ative um ambiente virtual (opcional, mas recomendado):


2. Instalar Dependências de Build

    Instale as dependências necessárias para a criação do pacote:

    ```bash
    pip install setuptools wheel twine
    ```

3. Gerar o Pacote 

    Na raiz do projeto, execute os seguintes comandos para gerar os arquivos de distribuição:

    ```bash
    python setup.py sdist bdist_wheel
    ```
    Isso gerará os arquivos dentro do diretório dist/:

    ```bash
    dist/
        document_generator-X.X.X-py3-none-any.whl
        document_generator-X.X.X.tar.gz
    ```


4. Publicar o Pacote no Repositório ( ⚠️ Somente após a aprovação, merge da MR e atualização da tag de versão)

    Para publicar em um repositório privado, use o comando:

    ```bash
    twine upload --repository-url <URL_DO_REPOSITORIO> dist/*
    ```
   
5. Instalar o Pacote em Outro Projeto

    Para instalar o pacote em outro projeto, adicione o caminho para o arquivo .whl no requirements.txt:

    ```text
    # requirements.txt

    --extra-index-url <URL_DO_REPOSITORIO>
    document_generator==X.X.X
   ```
    Em seguida, execute:
    
    ```bash
    pip install -r requirements.txt
    ```

## Autor

Criado por GovOne. Para mais informações, entre em contato em [contato@govone.digital](mailto:contato@govone.digital).

## Referências

Para mais informações, consulte a [documentação oficial](https://gitlab.govone.digital/govone/document_generator.git).

