import re

# Example text
text = "My email is amira123@example.com and my phone number is 012-345-6789."

# 1. Find an email
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email = re.findall(email_pattern, text)
print("Email found:", email)

# 2. Find a phone number
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone = re.findall(phone_pattern, text)
print("Phone found:", phone)

# 3. Search for a word (case-insensitive)
word = re.search(r"amira", text, re.IGNORECASE)
if word:
    print("Found the word:", word.group())

# 4. Replace something
new_text = re.sub(r"\d", "X", text)
print("Replaced digits:", new_text)


