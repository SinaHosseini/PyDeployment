from setuptools import setup
import os


def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="cow_face",
    version="1.0.1",
    author="Sina Hosseini",
    author_email="sshosseinivaez@gmail.com",
    description="Add a cow mask to the face",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/SinaHosseini/Cow-Face",
    requires=[],
    packages=["cow_face"]
)
