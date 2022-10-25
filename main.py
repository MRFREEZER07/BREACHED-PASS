import argparse
import sys
from pwnedClass import Pwned
import colorama

parser = argparse.ArgumentParser(description='Tool to get breached password')   
parser.add_argument("--email", "-m", help="mail id to search password in db")
args = parser.parse_args()


if args.email:
    pwd=Pwned(args.email)
else:
    print(f"{colorama.Fore.LIGHTRED_EX}if u dont know how to use try \n python3 test.py --email<email> or -e<email>")