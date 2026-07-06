import string
import itertools
import hashlib
import time

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_simulation(password, max_length=4, charset=string.ascii_lowercase):
    target_hash = hash_password(password)
    start_time = time.time()
    attempts = 0

    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            if guess_hash == target_hash:
                end_time = time.time()
                return {
                    "cracked": True,
                    "password": guess,
                    "attempts": attempts,
                    "time_taken": round(end_time - start_time, 2)
                }
    return {
        "cracked": False,
        "attempts": attempts,
        "time_taken": round(time.time() - start_time, 2)
    }

def analyze_password(password):
    print(f"\nAnalyzing password: {password}")

    # Strength analysis
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    print(f"Password length: {len(password)}")
    print(f"Strength score: {score}/4")

    # Run brute-force simulation
    print("\n[Brute-force Simulation]")
    result = brute_force_simulation(password, max_length=4, charset=string.ascii_lowercase + string.digits)

    if result["cracked"]:
        print(f"✅ Password cracked! It took {result['attempts']} attempts in {result['time_taken']}s")
    else:
        print(f"❌ Could not crack within {result['attempts']} attempts ({result['time_taken']}s).")
        print("This shows your password is stronger than the brute-force simulation range.")

# Example usage
if __name__ == "__main__":
    pw = input("Enter a password to analyze: ")
    analyze_password(pw)
