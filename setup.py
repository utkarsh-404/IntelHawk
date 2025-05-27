import os
import sys
import subprocess
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, init

REQUIRED_TOOLS = {
    'nmap': 'sudo apt install nmap',
    'sublist3r': 'pip install sublist3r',
    'theHarvester': 'pip install theharvester',
    'whatweb': 'sudo apt install whatweb',
    'bchecker': [
        'git clone https://github.com/yourusername/Breach-Checker.git',
        'cd Breach-Checker && pip install -r requirements.txt'
    ]
}

def show_banner():
    init(autoreset=True)
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText('IntelHawk'))
    print(Fore.YELLOW + " " * 5 + "Advanced OSINT Reconnaissance Platform\n")

def check_dependencies():
    missing = False
    print("\n[+] Checking system dependencies...")
    for tool, cmd in REQUIRED_TOOLS.items():
        if subprocess.call(['which', tool], stdout=subprocess.DEVNULL) != 0:
            print(f"{Fore.RED}✖ {tool} not installed!")
            print(f"{Fore.YELLOW}➔ Install with: {cmd}")
            missing = True
    return missing
    bchecker_installed = subprocess.call(
        ['python', '-m', 'bchecker', '--help'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ) == 0
    
    if not bchecker_installed:
        print(f"{Fore.RED}✖ Breach-Checker not installed!")
        print(f"{Fore.YELLOW}➔ Install with:")
        print("  git clone https://github.com/yourusername/Breach-Checker.git")
        print("  cd Breach-Checker && pip install -r requirements.txt")
        missing = True

if __name__ == '__main__':
    show_banner()
    if check_dependencies():
        print(f"\n{Fore.RED}❌ Please install missing dependencies first!")
        sys.exit(1)
    print(f"\n{Fore.GREEN}✅ All dependencies are satisfied!")