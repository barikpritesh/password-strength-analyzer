import argparse
from password_analyzer import analyze_password
from wordlist_generator import generate_wordlist  # 👈 add this
from wordlist_generator import generate_wordlist


def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer & Wordlist Generator")
    parser.add_argument('--password', type=str, help='Password to analyze')
    parser.add_argument('--name', type=str, help='Name to include in wordlist')
    parser.add_argument('--dob', type=str, help='Date of Birth (DDMMYYYY)')
    parser.add_argument('--pet', type=str, help='Pet name')

    args = parser.parse_args()

    if args.password:
        analyze_password(args.password)

    if args.name or args.dob or args.pet:
        generate_wordlist(args.name, args.dob, args.pet)

if __name__ == "__main__":
    main()
