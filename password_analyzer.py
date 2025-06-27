from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)

    print("\n🔐 Password Analysis")
    print("--------------------")
    print(f"Password: {password}")
    print(f"Score (0-4): {result['score']}")
    print("Feedback:", result['feedback']['warning'] or "Looks good!")
    
    suggestions = result['feedback']['suggestions']
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f"  - {s}")
    else:
        print("No suggestions, password looks strong.")
