import setuptools

# change this long description!
long_description = "postia is a utility tools to " \
    + "1) combine posts and comments in MOOC discussion forums " \
    + "into a sequence that can be used to train / test a Machine Learning model " \
    + "and 2) label posts as either students' or instructor's posts " \
    + "based on various criteria."


setuptools.setup(
    name="postia",
    version="0.1.0",
    author="Calvin Tantio",
    author_email="calvin.tantio@outlook.com",
    description="Utility tools to label interventions in MOOC Discussion Forums",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CT15/postia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'pandas'],
    python_requires='>=3.6',
)