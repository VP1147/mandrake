# -*- encoding: utf-8 -*-
import codecs
from distutils.core import setup

def ReadDescription():
    f = codecs.open("README.md", encoding="utf-8")
    long_description = f.read()
    f.close()
    return long_description

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mandrake",
    author="Vinicius Pavão",
    author_email="pavao364@gmail.com",
    description="Jogo simples sobre matemática",
    license="MIT",
    long_description=ReadDescription(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Education :: Testing"
    ],
    include_package_data=True,
    install_requires=['termios', 'tty','sys','math','os','random','json'],
)
