from setuptools import setup, Command
import subprocess


class PostInstallCommand(Command):
    """Custom command to run post-install tasks."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Run the Miniconda installation and environment setup script
        subprocess.run(["python", "-m", "my_module.install_miniconda"], check=True)


setup(
    name="my_module",
    version="0.1.0",
    packages=["my_module"],
    install_requires=[],  # Conda manages all dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [],
    },
    cmdclass={
        "install": PostInstallCommand,
    },
)

