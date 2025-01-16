# Installation Instructions for `my_module`

`my_module` automates the installation of Miniconda and the creation of a Conda environment tailored to your project. Follow these steps to install and use the module:

---

## Prerequisites
- Ensure you have `Python >= 3.6` and `pip` installed on your system.
- Ensure your system has internet access for downloading Miniconda and dependencies.

---

## Installation Steps

### 1. Build the Module
If you have downloaded the source code, navigate to the project directory and build the module:
Command:
```
python setup.py sdist bdist_wheel
```

This will create a distributable package in the `dist/` directory.

### 2. Install the Module
Use `pip` to install the module:
Command:
```
pip install dist/my_module-0.1.0.tar.gz
```

---

## What Happens During Installation?
1. Miniconda Installation:
   - The script detects your operating system and architecture.
   - It downloads and installs the appropriate Miniconda version.

2. Environment Creation:
   - A Conda environment named `eh_notebook_env` is created.
   - The following dependencies are installed in the environment:
     - `python=3.9`
     - `ipywidgets`
     - `ipython`
     - `scipy`
     - `numpy`
     - `matplotlib`
     - `notebook`

---

## Verifying the Installation

### Sourcing the Environment

#### Linux/macOS:
- To activate the environment:
  ```bash
  source ~/miniconda3/bin/activate eh_notebook_env
  ```
- To deactivate:
  ```bash
  conda deactivate
  ```

#### Windows:
- To activate the environment using Command Prompt:
  ```cmd
  %USERPROFILE%\miniconda3\Scripts\activate eh_notebook_env
  ```
- To deactivate:
  ```cmd
  conda deactivate
  ```

- If using PowerShell:
  ```powershell
  . %USERPROFILE%\miniconda3\Scripts\activate eh_notebook_env
  ```

### Check Installed Packages
- After activating the environment, list installed packages:
  ```bash
  conda list
  ```

- Run your project notebook or scripts to confirm everything works.

---

## Uninstalling

### Linux/macOS:
1. Remove the Conda environment:
   ```bash
   conda remove -n eh_notebook_env --all
   ```
2. Uninstall Miniconda by deleting its installation directory:
   ```bash
   rm -rf ~/miniconda3
   ```

### Windows:
1. Remove the Conda environment:
   ```cmd
   conda remove -n eh_notebook_env --all
   ```
2. Uninstall Miniconda:
   - Delete the `miniconda3` directory, usually located in `%USERPROFILE%\miniconda3`:
     ```cmd
     rmdir /S /Q %USERPROFILE%\miniconda3
     ```


