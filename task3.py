import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r'[\W_]', password):  # \W means non-word characters
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%).")

    # Strength Levels
    strength = {
        5: "Very Strong 💪",
        4: "Strong 👍",
        3: "Moderate ⚠️",
        2: "Weak 🚫",
        1: "Very Weak ❌",
        0: "Extremely Weak 😵"
    }

    print(f"\nPassword: {password}")
    print(f"Strength Score: {score}/5 → {strength[score]}")
    if feedback:
        print("\nSuggestions to improve:")
        for f in feedback:
            print(f"- {f}")
    print("\n" + "-" * 40)


# Example usage
if __name__ == "__main__":
    while True:
        pwd = input("Enter a password to check (or type 'exit' to quit): ")
        if pwd.lower() == 'exit':
            break
        check_password_strength(pwd)
