from setuptools import setup, find_packages

__version__ = '0.0.2'

setup(
    name='latex_renderer',
    version=__version__,
    packages=find_packages(),
    description="Latex table with image generator",
    author="Pavel Vyaznikov",
    author_email="sha.cehca@yandex.ru",
    license="MIT",
    python_requires='>=3.5',
    include_package_data=True
)
