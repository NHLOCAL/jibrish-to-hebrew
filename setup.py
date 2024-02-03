from setuptools import setup

setup(
    name='jibrish_to_hebrew',
    version='1.4',
    py_modules=['jibrish_to_hebrew'],  # Specify the name of your Python module
    install_requires=[],  # Add any dependencies if needed
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        'Source': 'https://github.com/NHLOCAL/jibrish-to-hebrew/actions',
    },
)