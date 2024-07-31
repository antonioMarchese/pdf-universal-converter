from document_converter.base_converter import Converter


base_file_path = './document_converter/uploads/teste'
extensions = ['xlsx', 'csv', 'docx', 'png', 'jpg']

converter = Converter()

for extension in extensions:
    file_path = "{0}.{1}".format(base_file_path, extension)
    content = converter.convert(file_path, serve=True)
