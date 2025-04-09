import os
import subprocess
import sys

def create_virtualenv():
    print("🔧 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "env"], check=True)

def install_dependencies():
    print("📦 Installing Flask...")
    subprocess.run(["env/bin/pip", "install", "Flask"], check=True)

    print("💥 Removing broken cadquery from PyPI (if installed)...")
    subprocess.run(["env/bin/pip", "uninstall", "-y", "cadquery"], check=False)

    print("📦 Installing CadQuery from GitHub wheel (v2.3.1)...")
    subprocess.run([
        "env/bin/pip", "install",
        "https://github.com/CadQuery/cadquery/releases/download/2.3.1/cadquery-2.3.1-py3-none-any.whl"
    ], check=True)

def main():
    if not os.path.exists("env"):
        create_virtualenv()
    else:
        print("✅ Virtual environment already exists.")

    install_dependencies()
    print("\\n✅ Setup complete!")
    print("To activate the environment:\\n  source env/bin/activate")
    print("To run the app:\\n  python app.py")

if __name__ == "__main__":
    main()