from distutils.core import setup
from setuptools import setup, find_packages
import py2exe

# setup(console=['Main.py'])  # For a console application
# OR
setup(
    windows=[{
        "script": "Main.py",
        "icon_resources": [(1, "icon.ico")],  # Specify your icon file
        }],  # For a GUI application
    name='Spari-Pogledom', 

    packages=['classes'],
    options={
        'py2exe': {
            'bundle_files': 1,  # Bundle everything into one file
            'compressed': True,  # Compress the output
        }
    },
    zipfile=None,  # Store files within the executable
)