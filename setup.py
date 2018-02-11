"""Setup script for package"""
# pylint: disable-all

from setuptools import find_packages, setup

def long_description():
    with open('README.rst') as readme:
        return readme.read()

def requirements():
    with open('requirements.txt') as requirements:
        return [
            line.strip()
            for line in requirements.readlines()
            if line.strip() and not line.startswith(('#', '-'))
        ]

def fuse(lst):
    return ''.join(str(i) for i in lst)

numversion = [0, 0, 1]
lifecycle = ['dev', 0]
version = (
    '.'.join([str(i) for i in numversion] + [fuse(lifecycle)])
)

setup(
    name='cloudwatchiter',
    version=version,
    license='MIT License',
    description=(
        'cloudwatchiter provides tools for manipulating '
        'Cloudwatch Schedule Expressions'
    ),
    long_description=long_description(),
    author='Josiah Niedrauer',
    author_email='jniedrauer@gmail.com',
    url='https://github.com/jniedrauer/cloudwatchiter',
    keywords='datetime, cron, cloudwatch, schedule expression, aws',
    install_requires=requirements(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    packages=find_packages(),
    include_package_data=True,
)
