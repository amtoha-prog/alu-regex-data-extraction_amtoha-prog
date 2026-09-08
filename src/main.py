import re

import json
from string import digits

# Defining regex patterns
patterns = {
    'email': r'\b[A-Za-z0-9.]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b',
    'phone': r'\+?\d{1,3}[\s.-]?\(?\d{2,3}\)?[\s.-]?\d{2,4}[\s.-]?\d{2,4}',
    'url': r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?',
    'hashtag': r'#[A-Za-z0-9_]+'  ,  
    'credit_card': r'\b(?:\d{4}[-\s.]?){3}\d{4}\b'
}
# Read the input file
with open ('input/raw-text.txt', 'r') as f:
    raw_text=f.read()

extracted_data = {
    'emails': [],
    'phones': [],
    'urls':[],
    'hashtags': [],
    'credit_cards': []

}
# Find all emails
print("Searching for emails...")
for match in re.finditer(patterns['email'], raw_text):
    email = match.group()  
    extracted_data['emails'].append(email)  
    print(f"  Found: {email}")

# Find all phone numbers
print("\n Searching for phone numbers...")
for match in re.finditer(patterns['phone'], raw_text):
    phone = match.group()

    # Remove non-digit characters from the phone number to check its length
    digits_only = ''.join(filter(str.isdigit, phone))

     # If it has a '+' it's probably a real phone
    if '+' in phone:
        extracted_data['phones'].append(phone)
        print(f"  Found: {phone}")
        
    # Otherwise, only keep if it's 7-11 digits
    elif len(digits_only) >= 7 and len(digits_only) <= 11:
        extracted_data['phones'].append(phone)
        print(f"  Found: {phone}")

 
# Find all URLs
print("\nSearching for URLs...")
for match in re.finditer(patterns['url'], raw_text):
    url = match.group()
    extracted_data['urls'].append(url)
    print(f"  Found: {url}")

# Find all hashtags
print("\nSearching for hashtags...")
for match in re.finditer(patterns['hashtag'], raw_text):
    hashtag = match.group()
    extracted_data['hashtags'].append(hashtag)
    print(f"  Found: {hashtag}")

# Find all credit cards
print("\nSearching for credit card numbers...")
for match in re.finditer(patterns['credit_card'], raw_text):
    card = match.group()
    # Get just the digits
    digits_only = ''.join(c for c in card if c.isdigit())
    
    # Credit card should be 13-19 digits
    if len(digits_only) >= 13 and len(digits_only) <= 19:
        # HIDE the card number for security and show only the last 4 digits
        redacted = '*' * (len(digits_only) - 4) + digits_only[-4:]
        
        extracted_data['credit_cards'].append(redacted)
        print(f"  Found: {redacted} (redacted for security)")


print("Results Summary:")

print("\n" + "=" * 50)

print (f'Emails found: {len(extracted_data["emails"])}')
print (f'Phone numbers found: {len(extracted_data["phones"])}')
print (f'URLs found: {len(extracted_data["urls"])}')
print (f'Hashtags found: {len(extracted_data["hashtags"])}')
print (f'Credit card numbers found: {len(extracted_data["credit_cards"])}')

print("\n" + "=" * 50)

print("Saving results to JSON file...")
# Convert the JSON dictionary and save it

with open('output/sample-output.json', 'w') as f:
    json.dump(extracted_data, f, indent=2)

print("Done! Results saved to: output/sample-output.json")