from setuptools import setup

classifiers = ["Development Status :: Beta",
               "Intended Audience :: Developers",
               "Operating System :: OS Independent",
               "Programming Language :: Python :: 2.7",
               "Programming Language :: Python :: 3.5",
               "Operating System :: OS Independent",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ""

setup(
    name='lazy-ai',
    version='1',
    packages=[],
    install_requires=['requests'],
    url='http://www.ahmetkotan.com.tr',
    license='MIT',
    author='Ahmet Kotan',
    author_email='ahmtkotan@gmail.com',
    description='Lazy AI Python Client',
    long_description=long_description,
    keywords="lazy ai",
    classifiers=["Intended Audience :: Developers",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.5",
                 "Operating System :: OS Independent",
                 'Topic :: Software Development :: Libraries :: Python Modules']
)