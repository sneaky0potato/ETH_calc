Electronic Structure Workshop

This workshop requires a Conda environment with specific dependencies for Jupyter notebooks and scientific computing.

## Prerequisites

- Supported operating systems: Windows, macOS (Intel or Apple Silicon), or Linux.
- Internet access for downloading Miniconda.
- Python installed (to run the installer script).
- Appropriate permissions to install software on your machine.

## Overview

The setup process will:

1. Check if Conda (Miniconda or Anaconda) is already installed.
2. If not installed, prompt you to download and install Miniconda automatically.
3. Once Conda is installed, guide you to create a Conda environment with required dependencies.

## Installing Conda (Miniconda)

If you do not already have Conda installed:

1. Run the `miniconda_installer.py` script:
   ```bash
   python miniconda_installer.py
   ```
   
   - The script checks for an existing Conda installation.
   - If Conda is not found, it will ask if you want to install Miniconda.
   - Upon your confirmation, it detects your OS and architecture, downloads the appropriate installer, and installs Miniconda silently.

## Sourcing Conda

After installing Miniconda, activate Conda in your current session:

**macOS/Linux:**
```bash
source ~/miniconda3/bin/activate
```

**Windows (Command Prompt):**
```cmd
C:\> "C:\Users\<YourUsername>\miniconda3\Scripts\activate.bat"
```
*(Replace `<YourUsername>` with your actual username. Adjust the path if Miniconda was installed elsewhere.)*

**Windows (PowerShell):**
```powershell
& "C:\Users\<YourUsername>\miniconda3\Scripts\Activate.ps1"
```

> **Note:** Adjust paths if your Miniconda installation directory is different.

To initialize Conda on all available shells after activation:
```bash
conda init --all
```
Then close and reopen your terminal or run the suggested commands to refresh your environment.

## Creating the Conda Environment

After Conda is set up, create the environment with required dependencies.

### Using the YAML File

1. Ensure the `environment.yml` file is in your project directory.
2. Run:
   ```bash
   conda env create -f environment.yml
   ```
   
   This creates an environment named `eh_notebook_env` with:
   - python=3.9
   - ipywidgets
   - ipython
   - scipy
   - numpy
   - matplotlib
   - notebook

### Manual Creation

Alternatively, create the environment manually:
```bash
conda create -n eh_notebook_env -y python=3.9 ipywidgets ipython scipy numpy matplotlib notebook
```

Then activate it:
```bash
conda activate eh_notebook_env
```

## Next Steps

With the environment set up and activated, you can:

- Launch Jupyter Notebook:
  ```bash
  jupyter notebook <notebook_name>.ipynb
  ```


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


