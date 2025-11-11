from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.1",
    description="This contains the code in the ./src directory of the project",
    author="J. Wade Hudson",
    packages=find_packages(where="./src"),
    package_dir={"":"./src"},
    install_requires=["setuptools"],
    entry_points={
        "packages":[
            "main=dab_project.main:main"
        ]
    }
)

# python3 setup.py bdist_wheel is the command that builds the wheel