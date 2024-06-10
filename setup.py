from setuptools import setup
from setuptools import find_packages


with open('requirements.txt', 'r') as r:
    requerimento = r.read().splitlines()

with open('README.md', 'r') as rmd:
    descricao_pagina = rmd.read()


setup(
    name = 'Package_01',
    version = '0.0.1',
    author = 'Victor Acosta',
    author_email = 'victoracosta275@gmail.com',
    description = 'Meu primerio pacote',
    long_description = descricao_pagina,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Victor-Ribeiro-Acosta/image-processing-package.git',
    install_requires = requerimento,
    python_requires = ">=3.8",
)
