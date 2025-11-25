"""
Lightweight setup guide for AI Personal Assistant.
This script helps with the initial setup and dependency installation.
"""

import subprocess
import sys
import os

def install_packages():
    """Install required packages using pip."""
    print("\n" + "="*60)
    print("Installing Dependencies...")
    print("="*60 + "\n")
    
    packages = [
        "Flask==2.3.3",
        "flask-cors==4.0.0",
        "SpeechRecognition==3.10.0",
        "pyttsx3==2.90",
        "wolframalpha==5.0.0",
        "requests==2.31.0",
        "python-dotenv==1.0.0"
    ]
    
    try:
        # First, upgrade pip
        print("Upgrading pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # Install each package
        print("\nInstalling packages...")
        for package in packages:
            print(f"  Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
        print("\n✅ All dependencies installed successfully!")
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error installing packages: {e}")
        return False

def verify_installation():
    """Verify that packages are installed."""
    print("\n" + "="*60)
    print("Verifying Installation...")
    print("="*60 + "\n")
    
    packages = [
        'flask',
        'flask_cors',
        'speech_recognition' if False else 'speech_recognition',  # Import as sr
        'pyttsx3',
        'wolframalpha',
        'requests',
        'dotenv'
    ]
    
    # Additional modules to check (with different import names)
    import_checks = {
        'flask': 'flask',
        'flask_cors': 'flask_cors',
        'speech_recognition': 'speech_recognition',
        'pyttsx3': 'pyttsx3',
        'wolframalpha': 'wolframalpha',
        'requests': 'requests',
        'dotenv': 'dotenv'
    }
    
    all_installed = True
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            all_installed = False
    
    return all_installed

def main():
    """Main setup function."""
    print("\n" + "="*60)
    print("🤖 AI Personal Assistant - Setup Helper")
    print("="*60)
    
    # Install packages
    if not install_packages():
        print("\n⚠️  Installation had issues. Please check the output above.")
        return False
    
    # Verify installation
    if not verify_installation():
        print("\n⚠️  Some packages may not be properly installed.")
        return False
    
    print("\n" + "="*60)
    print("✅ Setup Complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Open Terminal 1 and run:")
    print("   cd backend")
    print("   python app.py")
    print("\n2. Open Terminal 2 and run:")
    print("   cd frontend")
    print("   start index.html")
    print("\n3. Try voice or text commands in the web interface!")
    print("\n" + "="*60 + "\n")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
