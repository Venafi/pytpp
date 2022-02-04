# All of these attributes are defined in _about.py, but it must be imported this way.
__project_name__ = None
__version__ = None
__author__ = None
__author_email__= None
__project_url__ = None
exec(open('pytpp/_about.py', 'r').read())

from setuptools import setup, find_packages
import os

PROD_REQUIREMENTS = [
    'isodate==0.6.0',
    'logboss~=0.1.8',
    'packaging==20.9',
    'python-dateutil==2.8.2',
    'requests==2.24.0',
]

DEV_REQUIREMENTS = [
    'pyodbc==4.0.30',
    'lxml==4.4.1',
    'pandas==1.3.3',
    'paramiko==2.7.1'
]

DOC_REQUIREMENTS = [
    'Sphinx>=4.3.2',
    'sphinxcontrib-napoleon~=0.7',
    'sphinx-rtd-theme~=1.0.0',
    'sphinx-rtd-dark-mode~=1.2.4',
]

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        long_description = f.read()

    setup(
        name=__project_name__,
        url=__project_url__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        packages=find_packages(include=('pytpp*',)),
        package_dir={
            '': '.'
        },
        description='Venafi TPP Features and WebSDK API In Python',
        long_description=long_description,
        long_description_content_type='text/markdown',
        keywords=['pytpp', 'venafi', 'tpp', 'trust protection platform'],
        install_requires=PROD_REQUIREMENTS,
        extras_require={
            'dev': DEV_REQUIREMENTS,
            'doc': DOC_REQUIREMENTS ,
            'all': DOC_REQUIREMENTS + DEV_REQUIREMENTS
        },
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
