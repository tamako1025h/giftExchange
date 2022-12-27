from setuptools import setup, find_packages

setup(
    name='giftExchange',
    version="0.0.1",
    packages=find_packages(),
    description='プレゼント交換プログラムです',
    url='https://github.com/tamako1025h/giftExchange',
    author='tamako',
    author_email='tamakoDev@gmail.com',
    include_package_data=True,
    entry_points={'console_scripts': [
        'giftExchange = giftExchange.main:main',
    ]},
)