import sys

def load_wordlist(wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_path}' not found.")
        sys.exit(1)

def try_login(username, password):
    # Placeholder for login attempt logic
    pass

def brute_force(username, wordlist):
    for password in wordlist:
        print(f"Trying {password}...")
        if try_login(username, password):
            print(f"Password found: {password}")
            break

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bruteforce.py <username> <wordlist>")
        sys.exit(1)

    username = sys.argv[1]
    wordlist = load_wordlist(sys.argv[2])

    brute_force(username, wordlist)
