import os
import random

APPROVED_KEYS_FILE = "approved_keys.txt"

def generate_key():
    return "RDG-" + str(random.randint(10000, 99999))

def get_or_create_key():
    key_file = "user_key.txt"
    if os.path.exists(key_file):
        with open(key_file, "r") as f:
            return f.read().strip()
    else:
        new_key = generate_key()
        with open(key_file, "w") as f:
            f.write(new_key)
        return new_key

def check_approval(key):
    if not os.path.exists(APPROVED_KEYS_FILE):
        return False
    with open(APPROVED_KEYS_FILE, "r") as f:
        approved_keys = f.read().splitlines()
    return key in approved_keys

def banner():
    os.system("clear")
    print("\033[1;36m")
    print("██████╗ ██████╗  ██████╗     ████████╗ ██████╗  ██████╗ ██╗     ")
    print("██╔══██╗██╔══██╗██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔════╝ ██║     ")
    print("██████╔╝██████╔╝██║   ██║       ██║   ██║   ██║██║  ███╗██║     ")
    print("██╔═══╝ ██╔═══╝ ██║   ██║       ██║   ██║   ██║██║   ██║██║     ")
    print("██║     ██║     ╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗")
    print("╚═╝     ╚═╝      ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝")
    print("\033[0m")
    print("\033[1;33mAuthor: Malik Habib\033[0m")
    print("\033[1;34mWhatsApp: +923434571018\033[0m")
    print("="*60)

def main():
    banner()
    key = get_or_create_key()
    if check_approval(key):
        print("\033[1;32m[✓] Key Approved! Proceeding...\033[0m\n")
        print("[1] Poll Voting\n[2] Post Reactions\n[3] Comment Voting\n...etc")
        # Add actual options/functions here
    else:
        print("\033[1;31m[×] Your Key is Not Approved\033[0m")
        print("\033[1;33mKey : {}\033[0m".format(key))
        input("Press Enter to Request Approval...")
        os.system("xdg-open https://wa.me/923434571018")

if __name__ == "__main__":
    main()