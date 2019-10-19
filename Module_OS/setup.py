import setuptools


with open('readme.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="count-files-with-optional-extension",
    version='0.0.1',
    author="Tran Viet Phuoc",
    author_email='phuoc.finn@gmail.com',
    description='A small tool to count how many files with optional extension',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tranvietphuoc/learn-python/Module_OS',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)