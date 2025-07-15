import os
from setuptools import setup

# Read README file if it exists
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return 'Helper functions for Google Cloud Storage operations'

setup(
    name='helpers_py',
    version='0.1.0',
    author='ToolProof',
    description='Helper functions for Google Cloud Storage operations',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/ToolProof/helpers_py',
    packages=['helpers_py'],
    package_dir={'helpers_py': 'src/helpers_py'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'google-cloud-storage',
        'python-dotenv',
    ],
)
