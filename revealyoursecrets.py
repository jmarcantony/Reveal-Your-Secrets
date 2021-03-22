try:
    import validators
    import requests
    import sys
    import time
except ModuleNotFoundError:
    print("[-] Requirements not satisfied!\n    run 'pip install -r requirements.txt' to install requirements.")
    quit()

def rec_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"\n[*] Scan Completed in {round(end - start, 2)} seconds!\n")
    return wrapper

found = 0

@rec_time
def scan(wordlist_path, URL):
    global found
    try:
        with open(wordlist_path, "r") as wordlist:
            print(f"\n[*] Scanning {URL}\n")
            paths = wordlist.readlines()
            for init_path in paths:
                path = init_path.strip()
                if URL[-1] == "/":
                    new_url = f"{URL}{path}"
                else:
                    new_url = f"{URL}/{path}"
                req = requests.get(new_url)
                if req.status_code == 200:
                    found += 1
                    print(f"[+] Found Directory: {new_url}")
    except FileNotFoundError:
        print("[-] Invalid Wordlist Path!")
        quit()


def main():
    args = sys.argv

    if len(args) > 1:
        URL = args[1]

        if validators.url(URL):
            if "-w" in args:
                try:
                    wordlist_path = args[args.index("-w") + 1]
                except IndexError:
                    print(f"[-] Specify a valid Wordlist Path!\n    Try: 'python {args[0]}' for help")
            else:
                print(f"[-] Please Specify a Wordlist Path to use!\n    Try: 'python {args[0]}' for help")
                sys.exit()

            scan(wordlist_path, URL)
            print(f"[*] Found {found} Hidden Directories!")
        else:
            print(f"[-] Invalid URL!\n    Try: 'python {args[0]}' for help")
            quit()
    else:
        print(f"Basic Usage: python {args[0]} [URL] -w [WORDLIST PATH]")
        quit()


if __name__ == "__main__":
    print(r"""
 _____                      _  __     __                 _____                    _       
 |  __ \                    | | \ \   / /                / ____|                  | |      
 | |__) |_____   _____  __ _| |  \ \_/ /__  _   _ _ __  | (___   ___  ___ _ __ ___| |_ ___ 
 |  _  // _ \ \ / / _ \/ _` | |   \   / _ \| | | | '__|  \___ \ / _ \/ __| '__/ _ \ __/ __|
 | | \ \  __/\ V /  __/ (_| | |    | | (_) | |_| | |     ____) |  __/ (__| | |  __/ |_\__ \
 |_|  \_\___| \_/ \___|\__,_|_|    |_|\___/ \__,_|_|    |_____/ \___|\___|_|  \___|\__|___/
                                                                                    Author: ninjahacker123 
    """)
    main()
