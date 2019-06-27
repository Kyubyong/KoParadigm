import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'jamo',
    'xlrd',
]

setuptools.setup(
    name="KoParadigm",
    version="0.9",
    author="Kyubyong Park",
    author_email="kbpark.linguist@gmail.com",
    description="Korean Inflectional Paradigm Generator",
    install_requires=REQUIRED_PACKAGES,
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kyubyong/paradigm",
    packages=setuptools.find_packages(),
    package_data={'KoParadigm': ['koparadigm/paradigm.xlsx']},
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)