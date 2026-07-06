from analyzer import rate_password, recommendations, calculate_entropy

def analyze_password():
    password = input("Enter your password: ").strip()
    if not password:
        print("⚠️ Please enter a password!")
        return

    strength = rate_password(password)
    entropy = calculate_entropy(password)
    tips = recommendations(password)

    print("\n🔎 Password Analysis Result")
    print(f"Password Strength: {strength}")
    print(f"Entropy: {entropy} bits")

    if tips:
        print("\nRecommendations:")
        for tip in tips:
            print(f"- {tip}")
    else:
        print("\nYour password is strong! 👍")


if __name__ == "__main__":
    analyze_password()

    input("\nPress Enter to exit...")
    exit()  
    
    