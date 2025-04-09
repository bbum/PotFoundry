import os
import shutil

def remove_venv():
    if os.path.isdir("env"):
        print("🧹 Removing existing virtual environment...")
        shutil.rmtree("env")
    else:
        print("✅ No virtual environment found to remove.")

def clean_pycache():
    print("🧼 Cleaning up __pycache__ directories...")
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                full_path = os.path.join(root, d)
                shutil.rmtree(full_path)
                print(f"  Removed: {full_path}")

def main():
    remove_venv()
    clean_pycache()
    print("\n💡 Environment reset.")
    print("To set up again, run:\n  python3 setup.py")

if __name__ == "__main__":
    main()