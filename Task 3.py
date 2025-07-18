import re

def check_password_strength(password):
    remarks = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("❌ Minimum 8 characters required.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        remarks.append("❌ Add uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        remarks.append("❌ Add lowercase letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        remarks.append("❌ Add numbers.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        remarks.append("❌ Add special characters.")

    # Strength Level
    if score <= 2:
        return "🔴 Weak", remarks
    elif score == 3 or score == 4:
        return "🟡 Moderate", remarks
    else:
        return "🟢 Strong", []

# Main
print("==== 🔐 Password Strength Checker ====")
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"\n✅ Strength Level: {strength}")
if feedback:
    print("Suggestions to improve:")
    for item in feedback:
        print("-", item)
