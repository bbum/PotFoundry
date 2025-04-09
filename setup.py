import os
import subprocess
import sys

def create_virtualenv():
    print("🔧 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "env"], check=True)

def install_dependencies():
    print("📦 Installing dependencies...")
    subprocess.run(["env/bin/pip", "install", "-r", "requirements.txt"], check=True)

def main():
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