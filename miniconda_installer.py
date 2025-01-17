import os
import platform
import subprocess
import sys
import urllib.request

def is_conda_installed():
    """Check if Conda is installed by trying to get its version."""
    try:
        subprocess.run(["conda", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_miniconda():
    """Download and silently install Miniconda based on system architecture."""
    response = input("Miniconda not found. Would you like to install it? (yes/no): ").strip().lower()
    if response != "yes":
        print("Miniconda installation aborted.")
        sys.exit(0)

    system = platform.system().lower()
    machine = platform.machine().lower()

    installer_url = None
    installer_file = None
    install_prefix = os.path.expanduser("~/miniconda3")

    # Determine download URL and installer file path based on OS and architecture.
    if system == "windows":
        installer_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
        installer_file = os.path.abspath("miniconda.exe")
    elif system == "darwin":
        # macOS
        if machine == "arm64":
            installer_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh"
        elif machine == "x86_64":
            installer_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
        else:
            print(f"Unsupported macOS architecture: {machine}")
            sys.exit(1)
        installer_file = os.path.expanduser("~/miniconda3/miniconda.sh")
        os.makedirs(os.path.dirname(installer_file), exist_ok=True)
    elif system == "linux":
        # Linux
        if machine == "x86_64":
            installer_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
        elif machine == "aarch64":
            installer_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh"
        elif machine == "s390x":
            installer_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh"
        else:
            print(f"Unsupported Linux architecture: {machine}")
            sys.exit(1)
        installer_file = os.path.expanduser("~/miniconda3/miniconda.sh")
        os.makedirs(os.path.dirname(installer_file), exist_ok=True)
    else:
        print(f"Unsupported operating system: {system}")
        sys.exit(1)

    print(f"Downloading Miniconda installer for {system} {machine}...")
    urllib.request.urlretrieve(installer_url, installer_file)
    print("Download complete.")

    # Run the installer silently based on OS.
    if system == "windows":
        print("Running silent installer...")
        subprocess.run([installer_file, "/S"], check=True)
        os.remove(installer_file)
        print("Miniconda installation complete on Windows.")
    else:
        print("Running silent installer...")
        subprocess.run(["bash", installer_file, "-b", "-u", "-p", install_prefix], check=True)
        os.remove(installer_file)
        print("Miniconda installation complete on Unix-like OS.")

    print(f"\nTo activate conda in the current session, run:\nsource {install_prefix}/bin/activate")
    print("Then initialize conda on all shells by running:\nconda init --all")

def main():
    if is_conda_installed():
        print("Conda is already installed. Skipping installation.")
    else:
        install_miniconda()

if __name__ == "__main__":
    main()
