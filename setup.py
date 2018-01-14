from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='deathnote',
    version='0.1',
    description='Kill process on time.',
    long_description=readme,
    author='FUKUDA Yutaro',
    author_email='sktnkysh+dev@gmai.com',
    packages=find_packages(),
    url='https://github.com/sktnkysh/DeathNote',
    license=license,
    entry_points={'console_scripts': ["deathnote=deathnote.deathnote:main"]},)
