from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Parallel processing package'
LONG_DESCRIPTION = 'A package that can create parallel processes and output progress of each process'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="myparproc", 
        version=VERSION,
        author="Thien-Minh Nguyen",
        author_email="<thienminh.npn@ieee.org>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],        
        keywords=['python', 'parproc'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Linux :: Ubuntu 20.04",
        ]
)