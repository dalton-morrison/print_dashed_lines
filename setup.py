import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="print_dashed_lines", # Replace with your own username
    version="0.0.1",
    author="Dalton Abraham",
    author_email="nojackie9@gmail.com",
    description="A single function that takes two parameters and prints dashed lines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
