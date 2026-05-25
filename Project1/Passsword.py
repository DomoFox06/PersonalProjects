


def main():
    password = input("Enter password to check: ")
    print (f"You entered {password} ")

    score = score_password(password)
    issues = check_rules(password)
    label = verdict(score)

    print ("\n---Password Report----")
    print (f"Score: {score}/100")
    print(f"Verdict: {label}")

    if issues:
        print("\nSuggestions:")
        for tip in issues:
            print(f" - {tip}")
    else: print(" \nAll Rules Passed!")

    print("-------------------")
   



def check_rules(password):
    """Check password against basic security rules.
    Returns a list of feedback strings. Empty list = all rules passed."""
    feedback = []

    #rule 1
    if len(password) < 8:
        feedback.append("Passsword too short. Must be at least 8 charecters")

    #rule 2
    if not any(c.isupper() for c in password):
        feedback.append("Must have at least one uppercase letter")

    #rule 3
    if not any(c.islower() for c in password):
        feedback.append("Must have at least one lowercase letter")

    #rule4
    if not any(c.isdigit() for c in password):
        feedback.append("Must have at least one number")

    #rule 5
    special_chars = "!@#$%^&*()_+-=[]{}|;:,./?"
    if not any(c in special_chars for c in password):
        feedback.append("Must have at least one special character. Ex.!@#$%^&*()_+-=[]{}|;:,./?")

    return feedback

def score_password(password):
    """Score a password from 0 to 100 based on length and variety."""
    score = 0

    score += min(len(password) * 4, 40)

    if any(c.isupper() for c in password):
        score += 15
    if any(c.islower() for c in password):
        score += 15
    if any(c.isdigit() for c in password):
        score += 15

    special_chars = "!@#$%^&*()_+-=[]{}|;:,./?"
    if any(c in special_chars for c in password):
        score += 15

    # Never go above 100
    return min(score, 100)

def verdict(score):
    """Convert a numeric score to a readable verdict."""
    if score < 30:
        return "Weak"
    elif score < 60:
        return "Fair"
    elif score < 80:
        return "Strong"
    else:
        return "Very Strong"

if __name__ == "__main__":
    main()    