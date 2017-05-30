# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='python-cnab',
    version='0.0.1',
    author='Marcio Ribeiro',
    author_email='marcio.ribeiro@bradootech.com',
    url='https://github.com/marciorpbradoo',
    keywords=['cnab', 'cnab240'],
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    package_data={
        'cnab240': [
            'bancos/bankofamerica/specs/*.json',
            'bancos/bradesco/specs/*.json',
            'bancos/bradesco_cobranca_retorno_400/specs/*.json',
        ],
    },
    install_requires=[
        'setuptools-git==1.1'
    ],
    license='MIT',
    description='Lib para gerar arquivo CNAB - Integração bancária',
    long_description=open('README.md', 'r').read(),
    download_url='https://github.com/marciorpbradoo/python-cnab-odoo',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock',
    ],
)
