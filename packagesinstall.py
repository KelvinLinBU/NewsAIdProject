import subprocess

def install_package(package):
    try:
        # Check if the package is installed
        subprocess.check_output(["pip3", "show", package])
    except subprocess.CalledProcessError:
        # If not installed, install the package
        print(f"Installing {package}...")
        subprocess.run(["pip3", "install", package], check=True)
        print(f"{package} installed successfully.")
        return True  # Package was installed
    return False  # Package was already installed


##### NOTE YOU MAY NEED TO INSTALL NODE, SEE README IN FRONTEND####
def main():
    packages_to_install = [
        "google-auth",
        "cred",
        "pymongo",
        "google-auth-oauthlib",
        "flask",
        "textblob",
        "openai",
        "clean-text",
        "requests"
        # Add more packages if any are missed 
    ]

    packages_installed = False  # Flag to track if any packages were installed

    for package in packages_to_install:
        if install_package(package):
            packages_installed = True

    if packages_installed:
        print("All required packages installed successfully.")
    else:
        print("All required packages are already installed.")

if __name__ == "__main__":
    main()
