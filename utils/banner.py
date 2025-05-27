from pyfiglet import Figlet
from colorama import Fore, init

def show_banner():
    init(autoreset=True)
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText('IntelHawk'))
    print(Fore.YELLOW + " " * 5 + "Advanced OSINT Reconnaissance Platform\n")
    print(Fore.WHITE + " " * 10 + "https://github.com/utkarsh-404/IntelHawk\n")