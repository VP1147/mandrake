import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mandrake",
    version="2.2",
    author="Vinicius Pavão",
    author_email="pavao364@gmail.com",
    description="Jogo sobre Teorema de Pitágoras",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Education :: Testing"
    ],
    data_files=[()
)
