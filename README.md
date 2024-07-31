# PDF Universal Converter

**PDF Universal Converter** é uma biblioteca Python para a conversão de arquivos Excel, CSV, DOCX, JPG, JPEG e PNG em PDF. Ela oferece uma interface simples e flexível para converter documentos profissionais de maneira rápida e eficiente.
## Uso

Para gerar um documento PDF a partir de algum outro tipo de arquivo:

```python
from document_converter import Converter

pdf_converter = Converter(base_dir='./uploads')
pdf_converter.convert('file_path')
```

## Atenção

O documento gerado será armazenado no diretório passado em **base_dir** durante a inicialização do Conversor ou em 
**document_converter/uploads** por padrão.
