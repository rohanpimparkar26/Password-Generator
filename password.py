import string
import random

print("🔐 Welcome to the Customizable Password Generator!")

# Step 1: Ask the user what to include in the password
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

# Step 2: Validate at least one type is selected
if not any([include_lowercase, include_uppercase, include_digits, include_special]):
    print("⚠️ You must select at least one character type.")
    exit()

# Step 3: Combine character sets based on user input
selected_characters = []

if include_lowercase:
    selected_characters += list(string.ascii_lowercase)
if include_uppercase:
    selected_characters += list(string.ascii_uppercase)
if include_digits:
    selected_characters += list(string.digits)
if include_special:
    selected_characters += list(string.punctuation)

# Step 4: Get password length
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        raise ValueError("Length must be positive.")
except ValueError as e:
    print("❌ Invalid input:", e)
    exit()

# Step 5: Shuffle and generate password
random.shuffle(selected_characters)
password = [random.choice(selected_characters) for _ in range(length)]
random.shuffle(password)

# Step 6: Display final password
final_password = ''.join(password)
print("\n✅ Generated Password:", final_password)
