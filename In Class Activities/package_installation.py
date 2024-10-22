import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ['matplotlib', 'Crypto', 'package3']

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)
