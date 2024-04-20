from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jibrish_to_hebrew',
    version='1.4.1',
    py_modules=['jibrish_to_hebrew'],
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'Source': 'https://github.com/NHLOCAL/jibrish-to-hebrew/actions',
    },
    description='A Python package for converting jibrish string to Hebrew.',
    author='nh.local',
    author_email='nh.local11@gmail.com',
    license='MIT',
    url='https://github.com/NHLOCAL/jibrish-to-hebrew',
)
