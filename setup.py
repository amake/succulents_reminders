from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SuccsRemindersNorthBot',
    version='1.0',
    description='A bot to post succulent care reminders',
    long_description=long_description,
    url='https://github.com/amake/succulents_reminders',
    author='Aaron Madlon-Kay',
    author_email='aaron@madlon-kay.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='kanji hanzi ring twitter bot',
    py_modules=['succs', 'bot'],
    install_requires=['Mastodon.py']
)
