from setuptools import setup, find_packages

DEPENDENCIES = [
    "pandas",
    "numpy"
]

setup(
    name='HealthApp',
    python_requires='>=2.7',
    entry_points={
    'console_scripts': ['Health=HealthApp.Main:Main'],
    },
    setup_requires=[],
    install_requires=DEPENDENCIES,
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
