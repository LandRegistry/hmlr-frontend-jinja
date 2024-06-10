import glob
import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

components = []
directories = glob.glob("hmlr_frontend_jinja/**/**/*.html", recursive=True)
for directory in directories:
    components.append(os.path.relpath(os.path.dirname(directory), "hmlr_frontend_jinja") + "/*.html")

setuptools.setup(
    name="hmlr-frontend-jinja",
    version="2.0.0",
    author="Matt Shaw",
    author_email="matthew.shaw@landregistry.gov.uk",
    description="HMLR Frontend Jinja Macros",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LandRegistry/hmlr-frontend-jinja",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={"hmlr_frontend_jinja": components},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    python_requires=">=3.8",
    install_requires=["jinja2!=3.0.0,!=3.0.1"],
)
