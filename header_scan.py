import sys
import requests
import colorama
from colorama import Fore
from colorama import init
init()




if len(sys.argv)==2:

    print(Fore.BLUE + "\nChecking Security Headers")
    x = requests.get(sys.argv[1])

    headers=x.headers

    if headers.get('X-Frame-Options',None) is None:
        print(Fore.RED + "\nX-Frame-Options Missing")
    else: 
        print(Fore.GREEN + "\nX-Frame-Options is Present")

    if headers.get('X-XSS-Protection',None) is None:
        print(Fore.RED + "X-XSS-Protection is Missing")
    else: 
        print(Fore.GREEN + "X-XSS-Protection is Present")

    if headers.get('X-Content-Type-Options',None) is None:
        print(Fore.RED + "X-Content-Type-Options is  Missing")
    else: 
        print(Fore.GREEN + "X-Content-Type-Options is Present")

    if headers.get('Strict-Transport-Security',None) is None:
        print(Fore.RED + "Strict-Transport-Security is  Missing")
    else: 
        print(Fore.GREEN + "Strict-Transport-Security is Present")

    if headers.get('Content-Security-Policy',None) is None:
        print(Fore.RED + "Content-Security-Policy is  Missing\n")
    else: 
        print(Fore.GREEN + "Content-Security-Policy is Present\n")

else:
    sys.stderr.write("Usage: python {0} <url>\n".format(sys.argv[0]))


