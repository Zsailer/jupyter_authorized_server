from setuptools import setup, find_packages

setup(
    name="jupyter_authorized_server",
    version="0.0.1",
    author="Zach Sailer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'jupyter-authorized-server = jupyter_authorized_server.app:main'
        ]
    },
    python_requires='>=3.6',
)