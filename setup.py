import os
import subprocess
import sys

def create_virtualenv():
    print("🔧 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "env"], check=True)

def install_dependencies():
    print("📦 Installing Flask...")
    subprocess.run(["env/bin/pip", "install", "Flask"], check=True)

    print("💥 Removing any preinstalled cadquery...")
    subprocess.run(["env/bin/pip", "uninstall", "-y", "cadquery"], check=False)

    print("📦 Installing CadQuery from GitHub source...")
    subprocess.run([
        "env/bin/pip", "install", "git+https://github.com/CadQuery/cadquery.git@master"
    ], check=True)

def main():
    python_version = sys.version_info
    if not (3, 10) <= python_version[:2] <= (3, 11):
        print(f"🚫 CadQuery currently only supports Python 3.10 or 3.11. You are using Python {python_version.major}.{python_version.minor}.")
        sys.exit(1)

    if not os.path.exists("env"):
        create_virtualenv()
    else:
        print("✅ Virtual environment already exists.")

    install_dependencies()
    print("\n✅ Setup complete!")
    print("To activate the environment:\n  source env/bin/activate")
    print("To run the app:\n  python app.py")

if __name__ == "__main__":
    main()