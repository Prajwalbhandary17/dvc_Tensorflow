from setuptools import setup

with open("README.md",'r',encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="prajwalbhandary17",
    description=" Dvc with Tensorflow  pipeline ",
    Long_description=long_description,
    Long_description_content_type="text/markdown",
    url= "https://github.com/Prajwalbhandary17/dvc_Tensorflow",
    author_email ="prajwalbhandary17@gmail.com",
    packages =["src"],
    License = "GNU",
    python_requires =">=3.7",
    install_requires =[
        "dvc",
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3"
    ]
)