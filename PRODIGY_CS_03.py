import re

def check_password_strength(password):
    feedback = []
    strength = 0

    if len(password) < 8:
        feedback.append("❌ Password is too short (minimum 8 characters).")
    else:
        strength += 1

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one special character (e.g., !@#$%).")

    # Overall rating
    if strength == 5:
        status = "✅ Strong Password!"
    elif strength >= 3:
        status = "⚠️ Moderate Password - Can Be Improved"
    else:
        status = "❌ Weak Password"

    return status, feedback

def main():
    print("✨ Password Complexity Checker - ProDigy Infotech")
    password = input("Enter a password to check: ")

    status, feedback = check_password_strength(password)
    
    print("\n🔍 Analysis Result:")
    print(status)
    if feedback:
        print("\n🔧 Suggestions:")
        for msg in feedback:
            print(f"- {msg}")

if __name__ == "__main__":
    main()
