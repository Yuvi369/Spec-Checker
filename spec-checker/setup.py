from setuptools import setup, find_packages

setup(
    name='spec-checker',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['pandas'],
    entry_points={
        'console_scripts': [
            'spec-checker=spec_checker.cli:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    author='Yuvaraj',
    author_email='yuvarajsithusankar@email.com',
    description='A CLI and Python tool to validate various specs from CSV/JSON input',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
)
