import os
from setuptools import setup, find_packages

requirements_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')

requirements = []
with open(requirements_path) as req_file:
    for req_line in req_file:
        req_line = req_line.strip()
        if req_line.count('==') == 1:
            requirements.append(req_line)

setup(
    name='pdfu_universal_converter',
    version='0.0.1',
    description='A library for generating PDF from all formats',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    author='GovOne',
    author_email='contato@digital',
    url='https://gitlab.govone.digital/govone/document_generator.git',
    keywords=['govone', 'document', 'generator', 'pdf', 'excel', 'csv'],
    packages=find_packages(where='document_generator'),
    package_dir={"": "pdf_converter"},
    setup_requires=['wheel'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest",
            "flake8"
        ]
    },
    dependency_links=[]
)
