import hashlib
import requests

def check_password_breach(password: str) -> bool:
    """
    Check if a password has appeared in known data breaches
    using Have I Been Pwned's k-Anonymity API.
    Returns True if found, False otherwise.
    """
    # Hash password with SHA-1
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    # Query HIBP API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError("API request failed")

    # Check if suffix exists in response
    hashes = (line.split(":") for line in res.text.splitlines())
    return any(h == suffix for h, _ in hashes)


# Breach check
print("\nChecking password against known data breaches...")
password = input("Enter a password to check: ")
try:
    if check_password_breach(password):
        print("❌ This password has been found in data breaches! Choose another one.")
    else:
        print("✅ This password was NOT found in known data breaches.")
except Exception as e:
    print(f"⚠ Could not check breach status: {e}")
