from utils import leetspeak_variants

def generate_wordlist(name=None, dob=None, pet=None):
    base_words = []

    if name:
        base_words.append(name.lower())
    if dob:
        base_words.append(dob)
        base_words.append(dob[-4:])  # Year only
    if pet:
        base_words.append(pet.lower())

    wordlist = set()

    for word in base_words:
        wordlist.add(word)
        wordlist.update(leetspeak_variants(word))
        for suffix in ["123", "1234", "1", "!", "@123"]:
            wordlist.add(word + suffix)

    with open("custom_wordlist.txt", "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print("\n📄 Wordlist generated: custom_wordlist.txt")
    print("🔑 Total words:", len(wordlist))  # ✅ ← keep this inside the function
