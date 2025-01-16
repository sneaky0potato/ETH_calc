import os
import platform
import subprocess
import sys

def install_miniconda():
    print("Checking for Miniconda installation...")
    # Detect OS and architecture
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Determine the correct installer
    if system == "linux":
        if machine == "x86_64":
            url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
        elif machine == "aarch64":
            url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh"
        else:
            raise Exception(f"Unsupported Linux architecture: {machine}")
    elif system == "darwin":  # macOS
        if machine == "arm64":
            url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh"
        elif machine == "x86_64":
            url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
        else:
            raise Exception(f"Unsupported macOS architecture: {machine}")
    elif system == "windows":
        if machine == "amd64":
            url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
        else:
            raise Exception(f"Unsupported Windows architecture: {machine}")
    else:
        raise Exception(f"Unsupported operating system: {system}")

    # Installer paths
    miniconda_dir = os.path.expanduser("~/miniconda3")
    installer_path = os.path.join(miniconda_dir, "miniconda.sh" if system != "windows" else "miniconda.exe")

    # Create directory and download installer
    os.makedirs(miniconda_dir, exist_ok=True)
    if system == "windows":
        subprocess.run(["curl", "-o", installer_path, url], check=True)
    else:
        subprocess.run(["wget", url, "-O", installer_path], check=True)

    # Run the installer
    if system == "windows":
        subprocess.run(["Start-Process", "-FilePath", installer_path, "-ArgumentList", "/S", "-Wait"], shell=True)
    else:
        subprocess.run(["bash", installer_path, "-b", "-u", "-p", miniconda_dir], check=True)

    # Cleanup
    os.remove(installer_path)
    print("Miniconda installation completed.")

def create_environment():
    env_name = "eh_notebook_env"
    dependencies = [
        "python=3.9",
        "ipywidgets",
        "ipython",
        "scipy",
        "numpy",
        "matplotlib",
        "notebook"
    ]
    
    # Activate Conda and create the environment
    try:
        subprocess.run(["~/miniconda3/bin/conda", "create", "-n", env_name, "-y"] + dependencies, check=True)
        print(f"Environment '{env_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating environment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_miniconda()
    create_environment()

