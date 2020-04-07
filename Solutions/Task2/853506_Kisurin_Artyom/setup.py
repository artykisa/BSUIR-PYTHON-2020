import setuptools

PACKAGE = "853506_Kisurin_lab2"
NAME = "853506_Kisurin_lab2"
DESCRIPTION = "my lab2"
with open("readme.md", "r") as f:
    LONGDESCRIPTION=f.read()
AUTHOR = "Artyom Kisurin"
AUTHOR_EMAIL = "crazypluton@gmail.com"
URL = "https://github.com/artykisa/BSUIR-PYTHON-2020/tree/master/Solutions/Task2/853506_Kisurin_Artyom"

setuptools.setup(
    name=NAME,
    version="1.0",
    description=DESCRIPTION,
    long_description=LONGDESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: Windows 10",
    ],
    python_requires='>=3.7',
)